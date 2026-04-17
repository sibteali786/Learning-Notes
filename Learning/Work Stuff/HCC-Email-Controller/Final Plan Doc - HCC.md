# Emailing Module — Complete Implementation Plan

> Last updated: April 2026  
> Repos: `hcc-admin-v2` · `HCC-adam-backend` · `emailControllerAuth2`

---

## 1. Current Architecture (What Exists Today)

### hcc-admin-v2

- Mailing page has 3 tabs driven by `picklistName` prop: **Inbox**, **Gmail**, **Email Templates**
- `MailingComp` (`mailingComp/index.jsx`) switches between these via prop
- Bulk email: `mailingTable.jsx` → "Email All" button → `bulkEmialDrawer.jsx` → `POST apiPath.prodPath3/api/bulkEmail/sendBulkEmail/:id`
- Single email: `mailingTable.jsx` → "Send Mail" per row → `mailingDrawer.jsx` → `POST apiPath.devPath/api/appGmail/send/:id`
- Templates: fetched from `GET apiPath.prodPath/api/appGmail/templates` (returns hardcoded 3 file-based templates)

### emailControllerAuth2

- Only 2 route modules: `authRoutes.js` and `bulkEmailRoutes.js`
- Bulk email queue: BullMQ + Redis, processes via `bulkEmailService.js`
- Gmail send: `gmailService.js` using OAuth credentials stored on User model
- Templates: file-based only (`professional.html`, `modern.html`, `minimal.html`) — no DB model
- No SendGrid, no webhook endpoint, no activity logging, no contact lists

### HCC-adam-backend

- `emailTemplateModel.js` exists (templateName, subject, body, createdBy) — used for CRUD UI only, never used for actual sending
- Single email send: `POST /api/appGmail/send/:userId` via Gmail API
- No activity model today

### URL Map (current)

|`apiPath` key|Value (dev)|Value (prod)|Points to|
|---|---|---|---|
|`prodPath`|`http://localhost:3001`|`https://hcc-adam-backend.vercel.app`|HCC-adam-backend|
|`prodPath3`|`https://api-hccbackendcrm.com`|same|emailControllerAuth2|
|`devPath`|`http://localhost:8080`|—|emailControllerAuth2 (legacy)|

---

## 2. Target Architecture

### New tab structure (hcc-admin-v2 Mailing page)

|Tab|Sub-tabs|Was|
|---|---|---|
|0 — Inbox|—|Inbox tab (no change)|
|1 — Clients|Clients / Contacts|Gmail tab (renamed, extended)|
|2 — Bulk Email|Contact Lists / Bulk Jobs|New|
|3 — Templates|Contact Lists mgmt / Templates & Newsletters|New|

### New capabilities

- **Twilio SendGrid** as alternate bulk email provider alongside Gmail
- **DB-backed templates** with Template Builder (HTML paste, merge tags, live preview)
- **Contact Lists** — save named lists of clients/contacts for bulk sends
- **Bulk Jobs monitoring** — live status dashboard with pause/retry
- **Application-wide activity logging** — every significant action logged to adam-backend
- **Email delivery telemetry** — per-recipient sent/delivered/bounced tracked in emailControllerAuth2
- **SendGrid webhooks** — delivery events processed automatically

---

## 3. Who Owns What (Service Responsibility Map)

|Concern|Service|Notes|
|---|---|---|
|Single email send|HCC-adam-backend|`POST /api/appGmail/send/:userId` unchanged|
|Bulk email queue|emailControllerAuth2|Existing, extended|
|Templates CRUD|emailControllerAuth2|New — replaces file-based|
|Contact Lists CRUD|emailControllerAuth2|New|
|Bulk Jobs status|emailControllerAuth2|Existing routes, bugs fixed|
|Gmail OAuth|emailControllerAuth2|Existing, unchanged|
|SendGrid sending|emailControllerAuth2|New `sendgridService.js`|
|SendGrid webhooks|emailControllerAuth2|New `webhookController.js`|
|Application activity feed|HCC-adam-backend|New `activityModel.js`|
|Email delivery telemetry|emailControllerAuth2|New `emailDeliveryLogModel.js`|
|Client/contact data|HCC-adam-backend|Existing, unchanged|

---

## 4. New Models

### 4.1 `activityModel.js` — HCC-adam-backend

Application-wide activity log. Powers client profile activity feed. Single source of truth for all user-facing events.

```
actorUserId     ObjectId ref User
subjectType     String enum (see below)
subjectId       String (_id of affected document)
eventType       String enum (see below)
metadata        Mixed (JSON — flexible per event, see spec below)
correlationId   String (ties UI action → API → webhook outcome)
timestamp       Date default now
```

**`subjectType` enum:**

```
'client' | 'note' | 'task' | 'research' | 'email' | 'file' | 'template' | 'system'
```

**`eventType` enum (full list):**

```
note.created, note.updated, note.deleted, note.viewed,
note.attachment.added, note.attachment.removed,

client.created, client.updated, client.deleted, client.viewed,
client.merged, client.archived,

research.added, research.removed, research.status_changed, research.assigned,

email.draft_created, email.scheduled, email.sent, email.cancelled,
email.queued, email.delivered, email.bounced, email.deferred,
email.failed, email.complaint, email.unsubscribed,

bulk.started, bulk.completed, bulk.failed,

file.uploaded, file.exported, file.deleted,

task.created, task.updated, task.completed, task.assigned,

template.created, template.updated, template.deleted,

auth.login, auth.logout, auth.failed, auth.session_expired,

system.config_changed
```

**`metadata` shape per event type:**

```js
// email.sent
{ service: 'gmail'|'sendgrid', subject, preview, recipientEmail,
  messageId, templateId?, jobId?, attachmentCount }

// email.delivered | email.bounced | email.failed
{ service, recipientEmail, messageId, providerEvent,
  errorCode?, errorMessage?, jobId?, correlationId }

// bulk.started
{ jobId, service, recipientCount, templateId?, contactListId? }

// bulk.completed
{ jobId, sentCount, failedCount, durationMs }

// note.created
{ noteId, title, category, hasAttachments }

// research.status_changed
{ from, to, assignedTo? }

// client.updated
{ changedFields: ['phone', 'email'] }  // summary only, not full payload

// auth.login
{ ip, userAgent }

// template.created | template.updated
{ templateId, name, kind, service }
```

**Activity tap points (where to write):**

|Event|Triggered from|
|---|---|
|`note.*`|adam-backend `noteController.js`|
|`client.*`|adam-backend `clientsControllers.js`|
|`research.*`|adam-backend research controller|
|`email.sent` (single)|adam-backend `emailControllers.js`|
|`email.sent` (bulk, per recipient)|emailControllerAuth2 `bulkEmailService.js` → POST to adam-backend|
|`email.delivered / bounced / failed`|emailControllerAuth2 SendGrid webhook handler|
|`bulk.started / completed`|emailControllerAuth2 `bulkEmailService.js`|
|`template.*`|emailControllerAuth2 `templateController.js` → POST to adam-backend|
|`task.*`|adam-backend `taskController.js`|
|`file.*`|adam-backend `fileController.js`|
|`auth.*`|emailControllerAuth2 `auth.js` Passport callbacks|

---

### 4.2 `emailDeliveryLogModel.js` — emailControllerAuth2

Per-recipient delivery telemetry. High-volume operational log. Replaces the `results[]` array embedded in `BulkJob`.

```
jobId           ObjectId ref BulkJob (indexed)
recipientEmail  String
service         String enum: 'gmail' | 'sendgrid'
status          String enum: 'queued' | 'sent' | 'delivered' | 'bounced' | 'failed' | 'deferred'
subject         String
bodyPreview     String (first 200 chars of rendered body)
messageId       String (provider message ID — used for webhook matching)
errorCode       String
errorMessage    String
attemptCount    Number default 1
correlationId   String
sentAt          Date
deliveredAt     Date
bouncedAt       Date
```

> **Why not embed in BulkJob:** The embedded `results[]` array grows unboundedly. 500 recipients = 500 subdocs on one document. Separate collection with index on `jobId` is correct at scale.

---

### 4.3 `templateModel.js` — emailControllerAuth2 (primary) + HCC-adam-backend (mirror)

Replaces file-based template lookup. Stores HTML body in DB so Template Builder can create/edit dynamically.

```
name            String required
description     String
kind            String enum: 'template' | 'newsletter'
format          String enum: 'html' | 'text'
subject         String (may contain {{mergeTags}})
body            String (raw HTML with {{mergeTags}} — stored uncompiled)
usageCount      Number default 0 (incremented at send time)
createdBy       ObjectId ref User
service         String enum: 'gmail' | 'sendgrid' | 'both'
createdAt       Date
updatedAt       Date
```

> Template bodies are stored as raw HTML. Merge tag substitution (`{{key}}`) happens at send time so edits to a template don't rewrite send history.

---

### 4.4 `contactListModel.js` — emailControllerAuth2 (primary) + HCC-adam-backend (mirror)

```
name            String required
description     String
ownerId         ObjectId ref User
members         Array of { email: String, name: String, clientRefId?: String }
filters         Mixed (optional saved filter query for dynamic lists)
createdAt       Date
updatedAt       Date
```

> `clientRefId` is optional — stores the adam-backend client `_id` for cross-reference. No cross-DB join required. Frontend passes email arrays at send time.

---

### 4.5 `bulkJob.js` — emailControllerAuth2 (modify existing)

**Add these fields to existing schema:**

```
templateId      ObjectId ref Template (new)
contactListId   ObjectId ref ContactList (new)
service         String enum: 'gmail' | 'sendgrid', default: 'gmail' (new)
scheduledAt     Date optional (new)
```

**Remove this field:**

```
results         [{ email, status, error }]  ← REMOVE, replaced by EmailDeliveryLog
```

---

## 5. New Services and Utilities

### 5.1 `src/utils/templateUtils.js` — emailControllerAuth2 (new)

Extracts `processTemplate()` currently duplicated in `gmailService.js` and `emailController.js`. Both services import from here.

```js
// Replaces {{key}} with data[key] throughout template HTML
function processTemplate(template, data) { ... }
module.exports = { processTemplate };
```

---

### 5.2 `src/services/sendgridService.js` — emailControllerAuth2 (new)

Mirrors the interface of `gmailService.js` exactly. Provider adapter — frontend never knows which service sent.

```js
// Same signature as gmailService.sendEmail
async function sendEmail(to, subject, body, templateId, templateData, userId, files) { ... }
module.exports = { sendEmail };
```

- Uses `@sendgrid/mail` package
- Reads `SENDGRID_API_KEY` and `SENDGRID_FROM_EMAIL` from env
- Imports `processTemplate` from `templateUtils.js`
- Reads template body from DB (`templateModel`) by `templateId` instead of filesystem

---

### 5.3 `src/utils/activityLogger.js` — emailControllerAuth2 (new)

Posts activity events back to adam-backend. Keeps adam-backend as single source of truth for activity feed.

```js
async function logActivity(eventType, subjectType, subjectId, actorUserId, metadata) {
  await axios.post(`${process.env.ADAM_BACKEND_URL}/api/activity`, {
    actorUserId, subjectType, subjectId, eventType, metadata,
    correlationId: generateId()
  });
}
module.exports = { logActivity };
```

---

## 6. New Controllers and Routes

### 6.1 emailControllerAuth2

#### `src/controllers/templateController.js` (new)

- `createTemplate` — POST `/api/templates`
- `getAllTemplates` — GET `/api/templates` (replaces hardcoded array in `emailController.js`)
- `getTemplate` — GET `/api/templates/:id`
- `updateTemplate` — PATCH `/api/templates/:id`
- `deleteTemplate` — DELETE `/api/templates/:id`
- Each mutation calls `activityLogger` to post `template.*` event to adam-backend

#### `src/routes/templateRoutes.js` (new)

Mounted in `index.js` as `app.use('/api/templates', templateRouter)`

#### `src/controllers/contactListController.js` (new)

- `createList` — POST `/api/contact-lists`
- `getAllLists` — GET `/api/contact-lists`
- `getList` — GET `/api/contact-lists/:id`
- `updateList` — PATCH `/api/contact-lists/:id`
- `deleteList` — DELETE `/api/contact-lists/:id`

#### `src/routes/contactListRoutes.js` (new)

Mounted as `app.use('/api/contact-lists', contactListRouter)`

#### `src/controllers/webhookController.js` (new)

- `handleSendgridWebhook` — POST `/api/webhooks/sendgrid`
    1. Verify `X-Twilio-Email-Event-Webhook-Signature` header → 403 if invalid
    2. Parse events array from SendGrid
    3. Update matching `EmailDeliveryLog` by `messageId`
    4. Call `activityLogger` for `email.delivered`, `email.bounced`, `email.failed` events

#### `src/routes/webhookRoutes.js` (new)

Mounted as `app.use('/api/webhooks', webhookRouter)`

**SendGrid event → status mapping:**

|SendGrid event|`EmailDeliveryLog.status`|
|---|---|
|`delivered`|`delivered`|
|`bounce`|`bounced`|
|`dropped`|`failed`|
|`deferred`|`deferred`|
|`spamreport`|`failed`|
|`open` / `click`|skip (not tracked in v1)|

---

### 6.2 HCC-adam-backend

#### `controllers/activityController.js` (new)

- `createActivity` — POST `/api/activity`
- `getActivityFeed` — GET `/api/activity?subjectType=client&subjectId=:id`

#### `routes/activityRoutes.js` (new)

Mounted as `app.use('/api/activity', activityRouter)`

---

## 7. Modified Existing Files

### 7.1 emailControllerAuth2

#### `src/index.js`

```js
// Add BEFORE express.json() — webhook needs raw body
app.use('/api/webhooks/sendgrid', express.raw({ type: 'application/json' }));

// Existing
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true, limit: '10mb' }));

// Add new route mounts
const templateRouter = require('./routes/templateRoutes');
const contactListRouter = require('./routes/contactListRoutes');
const webhookRouter = require('./routes/webhookRoutes');
app.use('/api/templates', templateRouter);
app.use('/api/contact-lists', contactListRouter);
app.use('/api/webhooks', webhookRouter);
```

> **Critical:** `express.raw()` for the webhook path must come before `express.json()`. Webhook signature verification needs the raw request body.

#### `src/services/gmailService.js`

- Remove `processTemplate()` function — import from `templateUtils.js`
- Remove hardcoded `getEmailTemplates()` — replaced by DB query in `templateController.js`
- Update template lookup: query `templateModel` by `_id` instead of reading filesystem

#### `src/services/bulkEmailService.js`

- Add service dispatcher (Gmail vs SendGrid):

```js
const { sendEmail: gmailSend } = require('./gmailService');
const { sendEmail: sgSend } = require('./sendgridService');
const sender = job.data.service === 'sendgrid' ? sgSend : gmailSend;
```

- Replace `results.push(...)` with `EmailDeliveryLog.create(...)` per recipient
- Add `activityLogger` calls: `bulk.started` on job creation, `bulk.completed` on finish
- Fix: guard `templateData` parse — `if (typeof templateData === 'string') templateData = JSON.parse(templateData)`

#### `src/controllers/bulkEmailControllers.js`

- Extract `service` from `req.body` and pass to `addBulkEmailJob`
- **Bug fix:** `getBulkEmailStatus` uses `req.params.jobId` but route has `:id` — fix to `req.params.id`
- **Bug fix:** `getQueueStats` calls `bulkEmailService.getQueueStats()` but service not imported — add import

#### `src/controllers/emailController.js`

- Remove hardcoded `getEmailTemplates()` array — replaced by `templateController.getAllTemplates`
- Remove `processTemplate()` — import from `templateUtils.js`
- Add `activityLogger` call after successful single send: `email.sent`

---

### 7.2 HCC-adam-backend

#### `controllers/emailControllers.js`

- Add `activityLogger`-equivalent call after successful single send: `email.sent`
- Since activity model lives in same service, write directly: `Activity.create({ ... })`

#### `controllers/noteController.js`

- Add `Activity.create()` after note created, updated, deleted

#### `controllers/clientsControllers.js`

- Add `Activity.create()` after client created, updated, deleted

#### `controllers/taskController.js`

- Add `Activity.create()` after task created, updated, completed

---

### 7.3 hcc-admin-v2

#### `src/components/mailingComp/index.jsx`

Replace `picklistName` prop-driven switch with 4-tab layout using `useState`:

```js
const tabs = ['Inbox', 'Clients', 'Bulk Email', 'Templates'];
const [activeTab, setActiveTab] = useState(0);
```

- Tab 0 → existing `InboxTable` (unchanged)
- Tab 1 → existing `MailingTable` (was "Gmail" tab, no internal changes)
- Tab 2 → new `BulkEmailTab` component (sub-tabs: Contact Lists | Bulk Jobs)
- Tab 3 → new `TemplatesTab` component (sub-tabs: Contact Lists mgmt | Templates & Newsletters)
- Header actions become tab-contextual (Google auth button only on Tab 0/1, etc.)

#### `src/components/subcomponents/drawers/bulkEmialDrawer.jsx`

Add to existing drawer:

- `service` select at top: `Gmail` / `SendGrid`
- `contactListId` select: loads from `GET apiPath.prodPath3/api/contact-lists` — selecting pre-populates To field
- Pass `service` and `contactListId` in FormData on submit

---

## 8. New Frontend Components

### 8.1 New Tables

#### `src/components/subcomponents/tables/contactListsTable.jsx` (new)

- Calls `GET apiPath.prodPath3/api/contact-lists`
- Renders lists as **cards** (not table rows) — per handoff spec
- Each card: name, member count, description, select checkbox
- "Send bulk to selected" button opens upgraded `bulkEmialDrawer`
- "New list" button opens `newContactListDrawer`

#### `src/components/subcomponents/tables/bulkJobsTable.jsx` (new)

- Calls `GET apiPath.prodPath3/api/bulkEmail/getBulkEmailJobs/:userId`
- Polls every 5s while tab is open
- KPI cards at top: Sent (30d), Success rate, Failed count
- Table columns: status badge, subject, service (Gmail/SendGrid), sent/total progress, created date
- Running rows: Pause button
- Failed/partial rows: Retry button → `POST /api/bulkEmail/:jobId/retry`

#### `src/components/subcomponents/tables/templatesTable.jsx` (new)

- Calls `GET apiPath.prodPath3/api/templates`
- Grid of cards: name, kind badge (Template/Newsletter), subject preview, usageCount
- "Create new" button opens `templateBuilderDrawer`

---

### 8.2 New Drawers

#### `src/components/subcomponents/drawers/templateBuilderDrawer.jsx` (new)

- Fields: name, description, kind (Template/Newsletter), subject
- Body: textarea for HTML paste
- Merge tag chip buttons: `{{firstName}}`, `{{lastName}}`, `{{company}}`, `{{email}}`, `{{bookingLink}}`, `{{senderName}}`, `{{senderTitle}}` — clicking appends to body
- Live preview panel: renders `innerHTML` of body with sample values substituted
- Save → `POST apiPath.prodPath3/api/templates`

#### `src/components/subcomponents/drawers/newContactListDrawer.jsx` (new)

- Left side: searchable client table (`GET apiPath.prodPath/api/clients/allNewLeads`), checkboxes
- Right side: name + description fields + live selected count
- Save → `POST apiPath.prodPath3/api/contact-lists` with `members: [{ email, name, clientRefId }]`

---

## 9. Environment Variables

### emailControllerAuth2 — new vars needed

```
SENDGRID_API_KEY=
SENDGRID_WEBHOOK_PUBLIC_KEY=        # from SendGrid dashboard → Settings → Mail Settings
SENDGRID_FROM_EMAIL=                # verified sender in SendGrid
ADAM_BACKEND_URL=https://hcc-adam-backend.vercel.app
```

---

## 10. Build Order

Steps 1–6 are all backend. Steps 7–10 are independent frontend components (any order). Step 11 is final assembly.

|Step|What|Service|File(s)|
|---|---|---|---|
|1|Extract `processTemplate`, update imports|emailControllerAuth2|`templateUtils.js` (new), update `gmailService.js`, `emailController.js`|
|2|Template model + controller + routes|emailControllerAuth2|`templateModel.js`, `templateController.js`, `templateRoutes.js`|
|3|SendGrid service|emailControllerAuth2|`sendgridService.js`|
|4|Add service dispatcher to bulk worker|emailControllerAuth2|update `bulkEmailService.js`|
|5|Contact List model + controller + routes|emailControllerAuth2|`contactListModel.js`, `contactListController.js`, `contactListRoutes.js`|
|5a|Activity model + routes|HCC-adam-backend|`activityModel.js`, `activityController.js`, `activityRoutes.js`|
|5b|EmailDeliveryLog model, remove BulkJob.results[], activityLogger util|emailControllerAuth2|`emailDeliveryLogModel.js`, `activityLogger.js`, update `bulkEmailService.js`, `bulkJob.js`|
|5c|SendGrid webhook endpoint|emailControllerAuth2|`webhookController.js`, `webhookRoutes.js`, update `index.js`|
|6|Wire activity logging into existing controllers|HCC-adam-backend|update `emailControllers.js`, `noteController.js`, `clientsControllers.js`, `taskController.js`|
|7|Upgrade `bulkEmialDrawer.jsx` — service toggle + list picker|hcc-admin-v2|update `bulkEmialDrawer.jsx`|
|8|Contact Lists UI|hcc-admin-v2|`contactListsTable.jsx`, `newContactListDrawer.jsx`|
|9|Templates UI|hcc-admin-v2|`templatesTable.jsx`, `templateBuilderDrawer.jsx`|
|10|Bulk Jobs UI|hcc-admin-v2|`bulkJobsTable.jsx`|
|11|Restructure `MailingComp` — 4 tabs, assemble all components|hcc-admin-v2|update `mailingComp/index.jsx`|

---

## 11. Known Bugs to Fix Along the Way

|Bug|File|Fix|
|---|---|---|
|`getBulkEmailStatus` uses `req.params.jobId` but route registers `:id`|`bulkEmailControllers.js`|Change to `req.params.id`|
|`getQueueStats` calls `bulkEmailService.getQueueStats()` but service not imported|`bulkEmailControllers.js`|Add `const bulkEmailService = require('../services/bulkEmailService')`|
|`templateData = JSON.parse(templateData)` crashes if already object or null|`bulkEmailService.js`|Add guard: `if (typeof templateData === 'string') templateData = JSON.parse(templateData)`|

---

## 12. Cross-Repo Contract (for Cursor Notepads)

Copy this into a `cross-repo-contract.md` file and paste into each Cursor window's `@contract` notepad.

```markdown
# Emailing module — cross-repo contract

## Service URLs
- hcc-admin-v2: http://localhost:3000
- HCC-adam-backend: http://localhost:3001 (apiPath.prodPath)
- emailControllerAuth2: https://api-hccbackendcrm.com (apiPath.prodPath3)

## Who owns what
| Concern | Service |
|---|---|
| Single email send | HCC-adam-backend POST /api/appGmail/send/:userId |
| Bulk email queue | emailControllerAuth2 POST /api/bulkEmail/sendBulkEmail/:id |
| Templates CRUD | emailControllerAuth2 POST/GET /api/templates |
| Contact Lists CRUD | emailControllerAuth2 POST/GET /api/contact-lists |
| Bulk Jobs status | emailControllerAuth2 GET /api/bulkEmail/getBulkEmailJobs/:id |
| Gmail OAuth | emailControllerAuth2 GET /auth/google |
| Application activity feed | HCC-adam-backend POST/GET /api/activity |
| Email delivery telemetry | emailControllerAuth2 (EmailDeliveryLog collection) |
| SendGrid webhooks | emailControllerAuth2 POST /api/webhooks/sendgrid |

## New API endpoints

### emailControllerAuth2
POST   /api/templates              body: { name, description, kind, format, subject, body, service }
GET    /api/templates              returns: [{ _id, name, kind, subject, usageCount, service }]
PATCH  /api/templates/:id
DELETE /api/templates/:id
POST   /api/contact-lists          body: { name, description, members: [{ email, name, clientRefId? }] }
GET    /api/contact-lists          returns: [{ _id, name, description, memberCount }]
PATCH  /api/contact-lists/:id
POST   /api/bulkEmail/sendBulkEmail/:id  (extended: now accepts service, contactListId)
POST   /api/webhooks/sendgrid      (SendGrid delivery events)

### HCC-adam-backend
POST   /api/activity               body: { actorUserId, subjectType, subjectId, eventType, metadata }
GET    /api/activity?subjectType=client&subjectId=:id

## Models (emailControllerAuth2)
Template:        { name, description, kind, format, subject, body, usageCount, createdBy, service }
ContactList:     { name, description, ownerId, members: [{ email, name, clientRefId? }], filters }
EmailDeliveryLog:{ jobId, recipientEmail, service, status, subject, bodyPreview, messageId,
                   errorCode, errorMessage, attemptCount, correlationId, sentAt, deliveredAt, bouncedAt }
BulkJob (updated): added templateId, contactListId, service, scheduledAt — REMOVED results[]

## Models (HCC-adam-backend)
Activity: { actorUserId, subjectType, subjectId, eventType, metadata (Mixed), correlationId, timestamp }

## Template merge tags
Keys: firstName, lastName, company, email, bookingLink, senderName, senderTitle,
      companyName, companyAddress, companyWebsite
Syntax: {{key}} — substituted at send time, not at save time

## BulkJob sendBulkEmail extended payload
New fields: service ('gmail'|'sendgrid'), contactListId (optional)
Existing unchanged: recipients, subject, body, templateId, templateData, attachments

## Template processing
processTemplate() lives in emailControllerAuth2/src/utils/templateUtils.js
Both gmailService.js and sendgridService.js import from there

## Activity logging
emailControllerAuth2 posts events to adam-backend via activityLogger.js util
ADAM_BACKEND_URL env var in emailControllerAuth2 → adam-backend base URL

## SendGrid webhook
POST /api/webhooks/sendgrid — must receive raw body (not parsed JSON)
In index.js: register express.raw() for this path BEFORE express.json()
Env: SENDGRID_WEBHOOK_PUBLIC_KEY, SENDGRID_API_KEY, SENDGRID_FROM_EMAIL

## Frontend apiPath keys
apiPath.prodPath  = localhost:3001 (prod: hcc-adam-backend.vercel.app) → adam-backend
apiPath.prodPath3 = https://api-hccbackendcrm.com → emailControllerAuth2
apiPath.devPath   = localhost:8080 → emailControllerAuth2 (legacy single send)

## Tab structure (hcc-admin-v2 MailingComp)
Tab 0: Inbox       → InboxTable (existing, no change)
Tab 1: Clients     → MailingTable (existing, was 'Gmail' tab)
Tab 2: Bulk Email  → sub-tabs: Contact Lists | Bulk Jobs  (new)
Tab 3: Templates   → sub-tabs: Contact Lists mgmt | Templates & Newsletters  (new)

## Known bugs to fix
- bulkEmailControllers.js getBulkEmailStatus: req.params.jobId → req.params.id
- bulkEmailControllers.js getQueueStats: import bulkEmailService
- bulkEmailService.js: guard templateData parse before JSON.parse()

## New env vars (emailControllerAuth2)
SENDGRID_API_KEY=
SENDGRID_WEBHOOK_PUBLIC_KEY=
SENDGRID_FROM_EMAIL=
ADAM_BACKEND_URL=
```

---

## 13. Cursor IDE Setup

### `.cursorrules` — emailControllerAuth2

```
This is a Node.js/Express bulk email service with BullMQ, Redis, MongoDB, Gmail API, Twilio SendGrid.
Handles ONLY bulk email sending and related CRUD (templates, contact lists, activity logs).
Single email sending lives in HCC-adam-backend, not here.
Key files: src/services/gmailService.js, src/services/sendgridService.js, src/services/bulkEmailService.js
All template processing uses src/utils/templateUtils.js (processTemplate function).
Use require/module.exports (CommonJS). No TypeScript.
Auth: Passport + Google OAuth. Session-based via Redis.
Activity events are posted to adam-backend via src/utils/activityLogger.js.
Cross-repo contract: reference @contract notepad before making API or model changes.
```

### `.cursorrules` — HCC-adam-backend

```
This is a Node.js/Express CRM backend. Handles clients, contacts, tasks, notes, single email send.
Single email: POST /api/appGmail/send/:userId uses Gmail API via emailCredentials on User model.
Bulk email is NOT here — it goes to emailControllerAuth2 (api-hccbackendcrm.com).
Activity model lives here — it is the single source of truth for the application activity feed.
EmailTemplate model exists for CRUD display only — not used for actual email sending.
Use require/module.exports (CommonJS). No TypeScript.
Cross-repo contract: reference @contract notepad before making API or model changes.
```

### `.cursorrules` — hcc-admin-v2

```
This is a Next.js 16 frontend CRM. JavaScript only, no TypeScript.
Calls TWO backends separately:
  apiPath.prodPath  = HCC-adam-backend (clients, contacts, single email, activity feed)
  apiPath.prodPath3 = emailControllerAuth2 (bulk send, templates, contact lists, bulk jobs)
State: Zustand (store.js). No centralized route protection middleware.
UI: Tailwind + MUI + dark purple theme (#231C46, #2D245B, #452C95, #7F56D9, #B797FF, #E1C9FF).
Do NOT use HTML form tags — use onClick/onChange handlers instead.
Cross-repo contract: reference @contract notepad before making API or model changes.
```