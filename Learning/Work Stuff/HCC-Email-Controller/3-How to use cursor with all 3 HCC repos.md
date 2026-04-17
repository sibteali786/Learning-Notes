This is solid advice from the previous chat. Let me expand it specifically for your 3-repo setup with concrete, copy-paste-ready content.

---

## The core idea

Cursor's AI only knows what's in its context window. In separate windows, it can't see the other repos. The fix is a **manually maintained contract document** that you paste into each window when working across repos — think of it as a shared brain you carry between windows.

---

## Step 1 — Create a `cross-repo-contract.md` file

Create this file outside all 3 repos (e.g. `~/Projects/emailing-module-contract.md`) and open it as a Notepad in each Cursor window.

Here's your starting contract, ready to copy:

```markdown
# Emailing module — cross-repo contract
Last updated: [date]

## Service URLs
- hcc-admin-v2 frontend: http://localhost:3000
- HCC-adam-backend: http://localhost:3001 (apiPath.prodPath)
- emailControllerAuth2: https://api-hccbackendcrm.com (apiPath.prodPath3)

## Who owns what
| Concern | Service |
|---|---|
| Single email send | HCC-adam-backend POST /api/appGmail/send/:userId |
| Bulk email queue | emailControllerAuth2 POST /api/bulkEmail/sendBulkEmail/:id |
| Templates CRUD (new) | emailControllerAuth2 POST/GET /api/templates |
| Contact Lists CRUD (new) | emailControllerAuth2 POST/GET /api/contact-lists |
| Bulk Jobs status | emailControllerAuth2 GET /api/bulkEmail/getBulkEmailJobs/:id |
| Client/contact data | HCC-adam-backend GET /api/clients/allNewLeads |
| Gmail OAuth | emailControllerAuth2 GET /auth/google |

## Models (emailControllerAuth2)

### Template
{ name, description, kind: 'template'|'newsletter', format: 'html'|'text',
  subject, body (raw HTML with {{mergeTags}}), usageCount, createdBy, service: 'gmail'|'sendgrid'|'both' }

### ContactList
{ name, description, ownerId, members: [{ email, name, clientRefId? }] }

### Activity
{ userId, jobId, clientRefId?, service, direction: 'outbound', type: 'email',
  subject, recipientEmail, status: 'sent'|'failed', error?, sentAt }

### BulkJob (extended)
Existing fields + templateId (ref Template), contactListId (ref ContactList),
service: 'gmail'|'sendgrid' (default 'gmail'), scheduledAt?

## API contracts (new endpoints)

### POST /api/templates
Body: { name, description, kind, format, subject, body, service }
Returns: { _id, name, ...template }

### GET /api/templates
Returns: [{ _id, name, kind, subject, usageCount }]

### POST /api/contact-lists
Body: { name, description, members: [{ email, name, clientRefId? }] }
Returns: { _id, name, members }

### GET /api/contact-lists
Returns: [{ _id, name, description, memberCount }]

### POST /api/bulkEmail/sendBulkEmail/:id (extended)
New fields added: service ('gmail'|'sendgrid'), contactListId (optional)
Existing fields unchanged: recipients, subject, body, templateId, templateData, attachments

## Template processing
- processTemplate() lives in emailControllerAuth2/src/utils/templateUtils.js
- Both gmailService.js and sendgridService.js import from there
- Templates use {{key}} syntax for merge tags
- Merge tag keys: firstName, lastName, company, email, bookingLink, senderName, senderTitle

## Frontend routes.js paths
- apiPath.prodPath  = localhost:3001 (prod: hcc-adam-backend.vercel.app)
- apiPath.prodPath3 = https://api-hccbackendcrm.com (emailControllerAuth2)
- apiPath.devPath   = localhost:8080 (single email send — legacy)

## Current known bugs (fix as you go)
- bulkEmailControllers.js getBulkEmailStatus: uses req.params.jobId but route has :id
- bulkEmailControllers.js getQueueStats: calls bulkEmailService.getQueueStats() but service not imported
- bulkEmailService.js: templateData JSON.parse assumes string — add guard: if (typeof templateData === 'string')

## Tab structure (hcc-admin-v2 MailingComp)
Tab 0: Inbox       → InboxTable (existing)
Tab 1: Clients     → MailingTable (existing, was 'Gmail' tab)
Tab 2: Bulk Email  → sub-tabs: Contact Lists | Bulk Jobs
Tab 3: Templates   → sub-tabs: Contact Lists mgmt | Templates & Newsletters

## Component map
mailingComp/index.jsx       → tab shell (restructure)
tables/mailingTable.jsx     → tab 1 (no change)
tables/inboxTable.jsx       → tab 0 (no change)
tables/contactListsTable.jsx → tab 2, sub-tab A (new)
tables/bulkJobsTable.jsx    → tab 2, sub-tab B (new)
tables/templatesTable.jsx   → tab 3, sub-tab B (new)
drawers/bulkEmialDrawer.jsx → add service toggle + list picker (modify)
drawers/templateBuilderDrawer.jsx → new
drawers/newContactListDrawer.jsx  → new
```

---

## Step 2 — Cursor Notepad setup (per window)

In each Cursor window, create a Notepad via `Cmd+Shift+P > Notepad: New`. Name it `@contract`. Paste the full contract above. You reference it in prompts as `@contract`.

---

## Step 3 — Workflow per session

**When starting work in any window:**

```
@contract I'm about to implement [Step X — templateModel.js]. 
What does this file need to know about the other services?
```

**When you finish a step and it changes the contract** (new endpoint, field change, etc.):

1. Update `cross-repo-contract.md` on disk
2. Re-paste the updated section into each window's `@contract` notepad

**When switching to a different repo mid-feature:**

```
@contract I just finished templateModel.js and templateRoutes.js in emailControllerAuth2.
The GET /api/templates now returns [{ _id, name, kind, subject, usageCount, service }].
I'm now in hcc-admin-v2. What components need to call this endpoint?
```

---

## Step 4 — Cursor rules files (per repo)

Create a `.cursorrules` file at the root of each repo. This is loaded automatically into every chat in that window — no manual referencing needed.

**`emailControllerAuth2/.cursorrules`:**

```
This is a Node.js/Express bulk email service with BullMQ, Redis, MongoDB, Gmail API, and Twilio SendGrid.
It handles ONLY bulk email sending and related CRUD (templates, contact lists, activity logs).
Single email sending is NOT in this service — that lives in HCC-adam-backend.
Key files: src/services/gmailService.js, src/services/sendgridService.js, src/services/bulkEmailService.js
All template processing uses src/utils/templateUtils.js (processTemplate function).
Use require/module.exports (CommonJS). No TypeScript.
Auth: Passport + Google OAuth. Session-based via Redis.
Cross-repo contract is in @contract notepad — reference it before making API or model changes.
```

**`HCC-adam-backend/.cursorrules`:**

```
This is a Node.js/Express CRM backend. Handles clients, contacts, tasks, notes, single email send.
Single email: POST /api/appGmail/send/:userId uses Gmail API via emailCredentials on User model.
Bulk email is NOT here — it goes to emailControllerAuth2 (api-hccbackendcrm.com).
EmailTemplate model exists but is separate from emailControllerAuth2's Template model.
Use require/module.exports (CommonJS). No TypeScript.
Cross-repo contract is in @contract notepad — reference it before making API or model changes.
```

**`hcc-admin-v2/.cursorrules`:**

```
This is a Next.js 16 frontend CRM. JavaScript only, no TypeScript.
Calls TWO backends: apiPath.prodPath (HCC-adam-backend) and apiPath.prodPath3 (emailControllerAuth2).
apiPath.prodPath  = adam-backend (clients, contacts, single email, templates CRUD display)
apiPath.prodPath3 = emailControllerAuth2 (bulk send, contact lists, templates for sending, bulk jobs)
State: Zustand (store.js). No centralized route protection middleware.
UI: Tailwind + MUI + custom dark purple theme (#231C46, #2D245B, #452C95, #7F56D9, #B797FF, #E1C9FF).
Do not use HTML form tags — use onClick/onChange handlers.
Cross-repo contract is in @contract notepad — reference it before making API or model changes.
```

---

## Step 5 — Prompt templates for common situations

**Starting a new file:**

```
@contract @cursorrules
I'm creating [filename] in [service]. 
Based on the contract, this file needs to [what it does].
It will be called by [consumer] and will call [dependency].
```

**Debugging a cross-repo issue:**

```
@contract 
Frontend is calling POST /api/templates from hcc-admin-v2 and getting [error].
The endpoint is in emailControllerAuth2. Here's the frontend call: [paste code].
Here's the backend handler: [paste code].
What's the mismatch?
```

**Updating the contract after a change:**

```
I just changed the BulkJob model — added `service` and `contactListId` fields.
Update this section of the contract for me: [paste relevant section].
```

---

The `.cursorrules` file does the passive heavy lifting (always loaded), and `@contract` notepad handles the dynamic cross-repo state you update as you build. Together they give Cursor enough context to reason across all 3 repos without needing multi-root.