```table-of-contents
```
## Integration of Chat Application Into External Application
First of all we need to get credentials from the chat application so that we can store them in our application backend for them to work.
### Making request to Chat Api to generate credentials for your Application
```js
const response = await fetch(
`${process.env.NEXT_PUBLIC_CHAT_API_URL}/api/admin/tenants/generate-credentials`,
{
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
	tenantId: registrationData.tenantId,
	name: registrationData.name,
	adminEmail: registrationData.adminEmail,
  }),
}
);
```
- here tenantId is a string like `whatsnextplease-staging` 
- I am using `-staging` to show it staging environment, since each tenantId is uniquely stored in mongodb for chat application
- `name` can be whatever you want it to be lets say 'WhatsNextplease Staging'
- `adminEmail` for now its only a placeholder purpose was or will be to send credentials on this email so that we can keep things secure.
- https://api.hillcountrycoders10.com
#### Example
```json
{
  
  "tenantId": "whatsnextpleasestaging",
  "name": "What's Next Please Staging",
  "domain": "staging.whatnextplease.com",
  "allowedOrigins": [],
}
```
the response from the chat application for hitting this backend endpoint 
```json
success: true,
credentials: {
  tenantId,
  sharedSecret,
  registrationToken,
  expiresAt: registrationExpiry.toISOString(),
},
instructions: {
  step1:
	"Send sharedSecret and registrationToken to client via secure channel",
  step2: "Client stores sharedSecret in their .env file",
  step3: "Client calls POST /api/tenants/register with all credentials",
  step4: "You verify domain and activate tenant",
},
clientCurlExample: `curl -X POST https://your-chat-api.com/api/tenants/register \\
-H "Content-Type: application/json" \\
-d '{
"tenantId": "${tenantId}",
"domain": "client-domain.com",
"allowedOrigins": ["https://client-domain.com", "https://app.client-domain.com"],
"sharedSecret": "${sharedSecret}",
"registrationToken": "${registrationToken}"
}'`,
})
```
- The `sharedSecret` and `registrationToken` are needed to be stored in external application's backend from where we will call next endpoint i.e register.
- Remember `sharedSecret` verifies identity while `registrationToken` makes sure registration is done within 24 hours and then it expires. 
### Registering the application
We need to register application now after getting credentials 
- To streamline things i created chat.routes and chat.controller files in my backend to deal with this systematically
```ts
import { Request, Response } from 'express';
import crypto from 'crypto';
import prisma from '../config/db';
import { env } from '../config/environment';
import { logger } from '../utils/logger';

const CHAT_APP_URL = env.CHAT_APP_API_URL || 'http://localhost:5002';
const CHAT_SHARED_SECRET = env.CHAT_SHARED_SECRET!;
const TENANT_ID = env.TENANT_ID || 'whatsnextplease';

interface AuthenticatedRequest extends Request {
  user?: {
    id: string;
    email: string;
    firstName: string;
    lastName: string;
    avatarUrl?: string;
    role?: string;
    contactName: string;
  };
}

export class ChatController {
  /**
   * Register WNP as tenant in Chat App
   * This now uses the credentials provided by Chat App admin
   */
  static async registerTenant(req: AuthenticatedRequest, res: Response) {
    try {
      const { tenantId, domain, adminEmail, name } = req.body;

      // Validate inputs
      if (!tenantId || !domain || !adminEmail || !name) {
        return res.status(400).json({
          success: false,
          error: 'Missing required fields: tenantId, domain, adminEmail, name',
        });
      }

      // Get credentials from environment
      const sharedSecret = env.CHAT_SHARED_SECRET;
      const registrationToken = env.CHAT_APP_REGISTRATION_TOKEN;

      if (!sharedSecret || !registrationToken) {
        return res.status(500).json({
          success: false,
          error:
            'Missing chat credentials in backend. Please update AWS Secrets Manager with CHAT_SHARED_SECRET and CHAT_APP_REGISTRATION_TOKEN, then redeploy.',
        });
      }

      // Parse allowed origins
      const raw = env.ALLOWED_ORIGINS || '[]';
      let allowedOrigins: string[] = [];
      try {
        const maybeValue = raw.includes('=') ? raw.split('=')[1] : raw;
        const normalized = maybeValue.trim().replace(/'/g, '"');
        allowedOrigins = JSON.parse(normalized);
        if (!Array.isArray(allowedOrigins)) {
          throw new Error('ALLOWED_ORIGINS parsed to non-array');
        }
      } catch (err) {
        logger.warn('Failed to parse ALLOWED_ORIGINS, falling back to empty array', { raw, err });
        allowedOrigins = [];
      }

      // Call Chat App registration endpoint
      const response = await fetch(`${CHAT_APP_URL}/api/tenants/register`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          tenantId,
          domain,
          allowedOrigins,
          sharedSecret,
          registrationToken,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        console.log('Chat app registration failed', data);
        logger.info('Chat app registration failed', { data });
        throw new Error(data.error || 'Registration failed');
      }

      logger.info('Tenant registered successfully', { tenantId, domain });

      res.json({
        success: true,
        message: 'Chat integration enabled successfully',
        tenant: data.tenant,
      });
    } catch (error) {
      logger.error('Tenant registration error', { error });
      res.status(500).json({
        success: false,
        error: error instanceof Error ? error.message : 'Failed to register tenant',
      });
    }
  }

  /**
   * Generate signed token for chat authentication
   */
  static async generateInitToken(req: AuthenticatedRequest, res: Response) {
    try {
      if (!req.user) {
        return res.status(401).json({ error: 'Not authenticated' });
      }
      // Sometimes when its a client we will have to fetch user details from DB for CLIENT entity
      let user;
      if (req.user?.role === 'CLIENT') {
        user = await prisma.client.findUnique({
          where: { id: req.user.id },
          select: {
            id: true,
            email: true,
            contactName: true,
            companyName: true,
            avatarUrl: true,
          },
        });
      } else {
        user = await prisma.user.findUnique({
          where: { id: req.user.id },
          select: {
            id: true,
            email: true,
            firstName: true,
            lastName: true,
            avatarUrl: true,
          },
        });
      }

      if (!user) {
        return res.status(404).json({ error: 'User not found' });
      }

      // Create token payload
      const payload = {
        tenantUserId: user.id,
        email: user.email,
        name:
          req.user?.role === 'CLIENT'
            ? `${(user as { contactName: string }).contactName}`.trim()
            : `${(user as { firstName: string; lastName: string }).firstName} ${(user as { firstName: string; lastName: string }).lastName}`.trim(),
        avatarUrl: user.avatarUrl || undefined,
        tenantId: TENANT_ID,
        externalSystem: 'wnp',
        timestamp: Date.now(),
        nonce: crypto.randomBytes(16).toString('hex'),
        iss: 'whatnextplease',
        aud: 'chat-app',
        exp: Math.floor(Date.now() / 1000) + 300, // 5 minutes
      };

      // Encode payload
      const token = Buffer.from(JSON.stringify(payload)).toString('base64');

      // Sign token
      const signature = crypto.createHmac('sha256', CHAT_SHARED_SECRET).update(token).digest('hex');

      res.json({
        success: true,
        token,
        signature,
        chatUrl: CHAT_APP_URL,
      });
    } catch (error) {
      console.error('Token generation error:', error);
      res.status(500).json({ error: 'Failed to generate token' });
    }
  }
}

```
#### Register Tenant
##### Frontend
frontend should make request like this 
```js
const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/chat/register-tenant`, {
	method: 'POST',
	headers: {
	  'Content-Type': 'application/json',
	  Authorization: `Bearer ${token}`,
	},
	body: JSON.stringify({
	  tenantId: credentials.tenantId,
	  domain: registrationData.domain,
	  adminEmail: registrationData.adminEmail,
	  name: registrationData.name,
	}),
  });
```
- We can store tenantId as state in react applicaton or persist it if we want so atfer generating credentials we can use it in next request to register tenant.
- Similar goes for domain, adminEmail and name
- `domain` is simply window.location.hostname
##### Backend
- As we can see this method receives request from frontend usually your own Frontend application which wants to integrate chat application
```js
static async registerTenant(req: AuthenticatedRequest, res: Response) {
    try {
      const { tenantId, domain, adminEmail, name } = req.body;

      // Validate inputs
      if (!tenantId || !domain || !adminEmail || !name) {
        return res.status(400).json({
          success: false,
          error: 'Missing required fields: tenantId, domain, adminEmail, name',
        });
      }

      // Get credentials from environment
      const sharedSecret = env.CHAT_SHARED_SECRET;
      const registrationToken = env.CHAT_APP_REGISTRATION_TOKEN;

      if (!sharedSecret || !registrationToken) {
        return res.status(500).json({
          success: false,
          error:
            'Missing chat credentials in backend. Please update AWS Secrets Manager with CHAT_SHARED_SECRET and CHAT_APP_REGISTRATION_TOKEN, then redeploy.',
        });
      }

      // Parse allowed origins
      const raw = env.ALLOWED_ORIGINS || '[]';
      let allowedOrigins: string[] = [];
      try {
        const maybeValue = raw.includes('=') ? raw.split('=')[1] : raw;
        const normalized = maybeValue.trim().replace(/'/g, '"');
        allowedOrigins = JSON.parse(normalized);
        if (!Array.isArray(allowedOrigins)) {
          throw new Error('ALLOWED_ORIGINS parsed to non-array');
        }
      } catch (err) {
        logger.warn('Failed to parse ALLOWED_ORIGINS, falling back to empty array', { raw, err });
        allowedOrigins = [];
      }

      // Call Chat App registration endpoint
      const response = await fetch(`${CHAT_APP_URL}/api/tenants/register`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          tenantId,
          domain,
          allowedOrigins,
          sharedSecret,
          registrationToken,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        console.log('Chat app registration failed', data);
        logger.info('Chat app registration failed', { data });
        throw new Error(data.error || 'Registration failed');
      }

      logger.info('Tenant registered successfully', { tenantId, domain });

      res.json({
        success: true,
        message: 'Chat integration enabled successfully',
        tenant: data.tenant,
      });
    } catch (error) {
      logger.error('Tenant registration error', { error });
      res.status(500).json({
        success: false,
        error: error instanceof Error ? error.message : 'Failed to register tenant',
      });
    }
  }
```
- Notice how we are using `sharedSecret` and `registrationToken` from .env file
- We also load `allowedOrigins` from .env these are urls that will be stored in the `tenant` document in mongodb chat app
- later we will verify if request was made from allowed origins only or not.
##### Example
```text
ALLOWED_ORIGINS=['https://api.whatnextplease.com','https://api-staging.whatnextplease.com','https://whatnextplease.com','staging.whatnextplease.com']
CHAT_SHARED_SECRET=2161c0bbb9b68ca6bdcd67e5f7d09c563a676c6e190c2db62e78788e36bade93
CHAT_APP_REGISTRATION_TOKEN=1067085c6985717b90e7bf0002719789598054fb8784f1b7162eef7fb0144cd0
```
### Verify the App
### Frontend 
Finally we make verify request 
```js
const response = await fetch(`${process.env.NEXT_PUBLIC_CHAT_API_URL}/api/tenants/verify`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          tenantId: credentials.tenantId,
          verificationCode: 'auto-verify',
        }),
      });
```

### Backend
This request is made directly to chat app backend thus its needed for chat app to have the frontend for your application as allowed origins other wise it wont work.
- Ask your admin to add your app frontend domain in chat app backend.
### Integrating Chat as Iframe in Your application
- We have a hook which we use to load the iframe and authenticate with chat backend using our own backend 
#### Frontend 
use-chat-auth.ts
```ts
'use client';

import { useState, useEffect, useRef } from 'react';
import { getCookie } from '@/utils/utils';
import { COOKIE_NAME } from '@/utils/constant';

const CHAT_BASE_URL = (process.env.NEXT_PUBLIC_CHAT_APP_URL || 'http://localhost:3000').replace(
  /\/embed\/?$/,
  ''
);

const CHAT_EMBED_URL = `${CHAT_BASE_URL}/embed`;

interface ChatAuthState {
  token: string | null;
  signature: string | null;
  iframeUrl: string | null;
  isLoading: boolean;
  error: string | null;
}

// Shared state across all hook instances
let sharedAuthState: ChatAuthState = {
  token: null,
  signature: null,
  iframeUrl: null,
  isLoading: false,
  error: null,
};

// Track active auth promise to prevent duplicate requests
let authPromise: Promise<void> | null = null;

// Listeners for state updates
const listeners = new Set<(state: ChatAuthState) => void>();

function notifyListeners() {
  listeners.forEach(listener => listener({ ...sharedAuthState }));
}

export function useChatAuth() {
  const [state, setState] = useState<ChatAuthState>(sharedAuthState);
  const token = getCookie(COOKIE_NAME);
  const isMounted = useRef(true);

  useEffect(() => {
    // Register // Register this component as a listener
    listeners.add(setState);

    // If already authenticated, return immediately
    if (sharedAuthState.iframeUrl && !sharedAuthState.error) {
      setState(sharedAuthState);
      return () => {
        listeners.delete(setState);
      };
    }

    // If auth is in progress, wait for it
    if (authPromise) {
      authPromise.then(() => {
        if (isMounted.current) {
          setState(sharedAuthState);
        }
      });
      return () => {
        listeners.delete(setState);
      };
    }

    // Start new auth
    fetchChatToken();

    return () => {
      isMounted.current = false;
      listeners.delete(setState);
    };
  }, [token]);

  const fetchChatToken = async () => {
    if (sharedAuthState.isLoading || !token) return;

    try {
      sharedAuthState = { ...sharedAuthState, isLoading: true, error: null };
      notifyListeners();

      console.log('[Chat Auth] Fetching token...');
      const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/chat/init-token`, {
        method: 'GET',
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      if (!response.ok) {
        throw new Error('Failed to get chat token');
      }

      const data = await response.json();

      // In fetchChatToken, after the fetch call
      if (!response.ok) {
        const data = await response.json();
        let errorMessage = 'Failed to get chat token';

        if (response.status === 403) {
          errorMessage =
            'Chat integration not activated. Please complete setup in Settings → Integrations.';
        } else if (data.error) {
          errorMessage = data.error;
        }

        throw new Error(errorMessage);
      }

      console.log('[Chat Auth] Token received, creating iframe URL');

      // Create iframe URL with token
      const url = new URL(CHAT_EMBED_URL);
      url.searchParams.set('ssoToken', data.token);
      url.searchParams.set('ssoSignature', data.signature);
      url.searchParams.set('t', Date.now().toString());

      sharedAuthState = {
        token: data.token,
        signature: data.signature,
        iframeUrl: url.toString(),
        isLoading: false,
        error: null,
      };

      notifyListeners();
      console.log('[Chat Auth] Authentication complete');
    } catch (error) {
      console.error('[Chat Auth] Failed:', error);
      sharedAuthState = {
        ...sharedAuthState,
        isLoading: false,
        error: error instanceof Error ? error.message : 'Failed to initialize chat',
      };
      notifyListeners();
    } finally {
      authPromise = null;
    }
  };
  // Set the auth promise
  if (!authPromise && sharedAuthState.isLoading) {
    authPromise = Promise.resolve();
  }

  return state;
}

// Function to reset auth state (useful for logout)
export function resetChatAuth() {
  sharedAuthState = {
    token: null,
    signature: null,
    iframeUrl: null,
    isLoading: false,
    error: null,
  };
  authPromise = null;
  notifyListeners();
  console.log('[Chat Auth] State reset');
}

```
#### Backend 
```js
static async generateInitToken(req: AuthenticatedRequest, res: Response) {
    try {
      if (!req.user) {
        return res.status(401).json({ error: 'Not authenticated' });
      }
      // Sometimes when its a client we will have to fetch user details from DB for CLIENT entity
      let user;
      if (req.user?.role === 'CLIENT') {
        user = await prisma.client.findUnique({
          where: { id: req.user.id },
          select: {
            id: true,
            email: true,
            contactName: true,
            companyName: true,
            avatarUrl: true,
          },
        });
      } else {
        user = await prisma.user.findUnique({
          where: { id: req.user.id },
          select: {
            id: true,
            email: true,
            firstName: true,
            lastName: true,
            avatarUrl: true,
          },
        });
      }

      if (!user) {
        return res.status(404).json({ error: 'User not found' });
      }

      // Create token payload
      const payload = {
        tenantUserId: user.id,
        email: user.email,
        name:
          req.user?.role === 'CLIENT'
            ? `${(user as { contactName: string }).contactName}`.trim()
            : `${(user as { firstName: string; lastName: string }).firstName} ${(user as { firstName: string; lastName: string }).lastName}`.trim(),
        avatarUrl: user.avatarUrl || undefined,
        tenantId: TENANT_ID,
        externalSystem: 'wnp',
        timestamp: Date.now(),
        nonce: crypto.randomBytes(16).toString('hex'),
        iss: 'whatnextplease',
        aud: 'chat-app',
        exp: Math.floor(Date.now() / 1000) + 300, // 5 minutes
      };

      // Encode payload
      const token = Buffer.from(JSON.stringify(payload)).toString('base64');

      // Sign token
      const signature = crypto.createHmac('sha256', CHAT_SHARED_SECRET).update(token).digest('hex');

      res.json({
        success: true,
        token,
        signature,
        chatUrl: CHAT_APP_URL,
      });
    } catch (error) {
      console.error('Token generation error:', error);
      res.status(500).json({ error: 'Failed to generate token' });
    }
  }
```
- This request returns a token which we use to form iframeUrl which is dealt by chat app frontend to make sure that the external app is properly authenticated.
#### External Application Iframe Modal Example
```tsx
'use client';

import { useEffect, useRef, useCallback, useState } from 'react';
import { MessageSquare, Maximize2, Minimize2, X } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from '@/components/ui/dialog';
import { useChatAuth } from '@/hooks/use-chat-auth';

interface ChatModalProps {
  /** Modal title */
  title?: string;
  /** Custom trigger button component */
  trigger?: React.ReactNode;
  /** Additional CSS classes for the modal */
  className?: string;
  /** Whether to show the modal in fullscreen initially */
  defaultFullscreen?: boolean;
  /** Callback when modal opens */
  onModalOpen?: () => void;
  /** Callback when modal closes */
  onModalClose?: () => void;
}

const DEFAULT_CONFIG = {
  title: 'Client Messages Chat',
};

export default function ChatModal({
  title = DEFAULT_CONFIG.title,
  trigger,
  className = '',
  defaultFullscreen = false,
  onModalOpen,
  onModalClose,
}: ChatModalProps) {
  const [isFullscreen, setIsFullscreen] = useState(defaultFullscreen);
  const [isChatLoaded, setIsChatLoaded] = useState(false);
  const [internalOpen, setInternalOpen] = useState(false);

  const iframeRef = useRef<HTMLIFrameElement>(null);
  const loadTimeoutRef = useRef<ReturnType<typeof window.setTimeout>>();
  const modalOpenTimeRef = useRef<number>(0);

  // Use shared auth hook
  const { iframeUrl, isLoading: isAuthenticating, error: authError } = useChatAuth();

  // Handle modal state changes
  const handleModalChange = useCallback(
    (open: boolean) => {
      setInternalOpen(open);

      if (open) {
        modalOpenTimeRef.current = Date.now();
        setIsChatLoaded(false);
        onModalOpen?.();

        // Set timeout for iframe load
        loadTimeoutRef.current = setTimeout(() => {
          if (!isChatLoaded) {
            console.warn('Chat iframe took too long to load');
            setIsChatLoaded(true);
          }
        }, 10000);
      } else {
        setIsFullscreen(false);
        onModalClose?.();

        if (loadTimeoutRef.current) {
          clearTimeout(loadTimeoutRef.current);
        }

        // Small delay before resetting loaded state
        setTimeout(() => {
          setIsChatLoaded(false);
        }, 300);
      }
    },
    [onModalOpen, onModalClose, isChatLoaded]
  );

  // Handle fullscreen toggle
  const toggleFullscreen = useCallback(() => {
    setIsFullscreen(prev => !prev);
  }, []);

  // Handle iframe load
  const handleIframeLoad = useCallback(() => {
    const loadTime = Date.now() - modalOpenTimeRef.current;

    if (loadTime > 500) {
      setIsChatLoaded(true);

      if (loadTimeoutRef.current) {
        clearTimeout(loadTimeoutRef.current);
      }

      console.log(`Chat iframe loaded in ${loadTime}ms`);
    } else {
      setTimeout(() => {
        setIsChatLoaded(true);
      }, 1000);
    }
  }, []);

  // Handle escape key to exit fullscreen
  useEffect(() => {
    const handleKeyDown = (event: KeyboardEvent) => {
      if (event.key === 'Escape' && isFullscreen && internalOpen) {
        setIsFullscreen(false);
      }
    };

    if (internalOpen) {
      document.addEventListener('keydown', handleKeyDown);
      return () => document.removeEventListener('keydown', handleKeyDown);
    }
  }, [isFullscreen, internalOpen]);

  // Cleanup timeouts on unmount
  useEffect(() => {
    return () => {
      if (loadTimeoutRef.current) {
        clearTimeout(loadTimeoutRef.current);
      }
    };
  }, []);

  // Default trigger button
  const defaultTrigger = (
    <Button className="flex items-center gap-2">
      <MessageSquare className="w-4 h-4" />
      Open Chat
    </Button>
  );

  return (
    <Dialog open={internalOpen} onOpenChange={handleModalChange}>
      <DialogTrigger asChild>{trigger || defaultTrigger}</DialogTrigger>

      <DialogContent
        showCloseButton={false}
        className={`${
          isFullscreen
            ? 'max-w-none max-h-none h-screen w-screen m-0 rounded-none'
            : 'max-w-6xl h-[85vh]'
        } p-0 transition-all duration-300 ${className}`}
      >
        <DialogHeader className="flex-row items-center justify-between p-4 border-b space-y-0">
          <DialogTitle className="flex items-center gap-2 text-lg">
            <MessageSquare className="w-5 h-5" />
            {title}
            {isChatLoaded && (
              <Badge variant="secondary" className="text-xs">
                Connected
              </Badge>
            )}
            {!isChatLoaded && (
              <Badge variant="outline" className="text-xs">
                Loading...
              </Badge>
            )}
          </DialogTitle>

          <div className="flex items-center gap-1">
            <Button
              onClick={toggleFullscreen}
              variant="ghost"
              size="sm"
              className="h-8 w-8 p-0"
              title={isFullscreen ? 'Exit fullscreen' : 'Enter fullscreen'}
            >
              {isFullscreen ? <Minimize2 className="w-4 h-4" /> : <Maximize2 className="w-4 h-4" />}
            </Button>

            <Button
              onClick={() => handleModalChange(false)}
              variant="ghost"
              size="sm"
              className="h-8 w-8 p-0"
              title="Close chat"
            >
              <X className="w-4 h-4" />
            </Button>
          </div>
        </DialogHeader>

        <div className="flex-1 relative">
          {/* Loading/Auth indicator */}
          {(!isChatLoaded || isAuthenticating) && (
            <div className="absolute inset-0 flex items-center justify-center bg-background/80 z-10">
              <div className="flex flex-col items-center gap-2 text-muted-foreground">
                <div className="w-4 h-4 animate-spin rounded-full border-2 border-current border-t-transparent" />
                <span>{isAuthenticating ? 'Authenticating...' : 'Loading chat...'}</span>
              </div>
            </div>
          )}

          {/* Auth Error */}
          {authError && (
            <div className="absolute inset-0 flex items-center justify-center bg-background/80 z-10">
              <div className="flex flex-col items-center gap-4 text-center p-6">
                <div className="text-destructive text-lg font-semibold">Authentication Failed</div>
                <p className="text-muted-foreground text-sm max-w-md">{authError}</p>
                <Button onClick={() => window.location.reload()} variant="outline">
                  Retry
                </Button>
              </div>
            </div>
          )}

          {/* Chat iframe - only render when modal is open and we have auth */}
          {internalOpen && iframeUrl && !authError && (
            <iframe
              ref={iframeRef}
              src={iframeUrl}
              title={title}
              className="w-full h-full border-0"
              onLoad={handleIframeLoad}
              style={{
                height: isFullscreen ? 'calc(100vh - 60px)' : 'calc(85vh - 60px)',
                minHeight: '400px',
              }}
              allow="camera; microphone; clipboard-write"
              sandbox="allow-same-origin allow-scripts allow-popups allow-forms allow-top-navigation-by-user-activation"
            />
          )}
        </div>
      </DialogContent>
    </Dialog>
  );
}

```