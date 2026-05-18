# AI-PMS — Multi-Tenancy & Scalability Analysis

> Generated: May 2026 | Internal Reference

---

## 1. What Is Multi-Tenancy (In Our Context)?

Multi-tenancy means multiple independent businesses (Hotel A, Hostel B, Restaurant C) all use the **same running application** without seeing each other's data.

**Real-world analogy:**

> Gmail is multi-tenant. You and 2 billion other users share the same servers, same code — but you only ever see your emails. That isolation is the whole game.

For AI-PMS, a "tenant" = **one hospitality business** (a hotel group, a hostel chain, a single guesthouse). They may have multiple properties, but they are one paying customer.

---

## 2. Current State of Multi-Tenancy in AI-PMS

### What's Actually There Right Now

The app uses **Row-Level Tenancy** (also called shared DB / shared schema). All tenants live in one MongoDB Atlas database, isolated only by ownership fields on each document.

```
MongoDB Atlas (single DB)
└── properties     → { owner: userId, managers: [userId] }
└── rooms          → { property: propertyId }
└── bookings       → { property: propertyId }
└── channelevents  → { propertyId: propertyId }
└── users          → { role: 'owner' | 'admin' | ... }
```

**Tenant boundary is enforced via:**

- `Property.owner` → ObjectId ref to User
- `propertyAccess.middleware.js` → checks `req.user._id` against `property.userId`
- GraphQL resolvers → filter queries by `owner: req.user.id`

### The Critical Gap — No `organizationId` / `tenantId`

The User model has **no concept of which organization/business it belongs to**. A user IS effectively a tenant, which creates problems:

```js
// Current — User IS the tenant boundary
Property.find({ owner: req.user.id })

// What's missing — an Organization layer
Property.find({ organizationId: req.user.organizationId })
```

**Scenario where this breaks:**

> "The Grand Lahore Hotel" has an owner + 3 staff members. Right now, each user is independent. There's no `Organization` model tying them together, so the owner can't properly delegate access across their own hotel chain to their team without the system confusing who "owns" what.

### Inconsistency in Auth Checks

Some resolvers use `req.user.sub` (Cognito JWT style), some use `req.user.id`, some use `req.user._id`. This means multi-tenant auth isn't applied consistently — some endpoints are likely leaking cross-tenant data.

```js
// Found in resolvers — 3 different patterns for the same thing:
owner: req.user.id        // propertyController
createdBy: req.user.sub   // bookingController  
userId: req.user._id      // monitoring middleware
```

---

## 3. Multi-Tenancy Models — Which to Pick?

There are 3 standard approaches. Here's how they map to AI-PMS:

### Model A — Shared DB, Shared Schema (Current)

```
Single MongoDB instance
All tenant data in same collections
Isolation via tenantId field on every document
```

|||
|---|---|
|✅ Pros|Cheapest to run, easiest to deploy, simple queries, one codebase|
|❌ Cons|One noisy tenant can slow everyone, data leak risk if filter forgotten, harder compliance (GDPR isolation)|
|🎯 Right for|**Startups, early stage, <500 tenants**|

### Model B — Shared DB, Separate Schema / Prefix (Middle ground)

```
Single MongoDB instance
Each tenant gets prefixed collections: tenant_abc_bookings, tenant_xyz_bookings
Or separate MongoDB databases on same Atlas cluster
```

|||
|---|---|
|✅ Pros|Better isolation, easy backup per tenant, compliance-friendly|
|❌ Cons|More complex connection management, cross-tenant queries impossible|
|🎯 Right for|**Mid-stage, compliance requirements, 10–500 tenants**|

### Model C — Separate DB per Tenant (Silo)

```
Each hotel chain gets their own MongoDB Atlas cluster
Separate backend instance or routing layer
```

|||
|---|---|
|✅ Pros|Maximum isolation, perfect for enterprise/GDPR, easy tenant offboarding|
|❌ Cons|Expensive, operationally complex, hard to run aggregated analytics across tenants|
|🎯 Right for|**Enterprise deals, regulated markets** — not now|

---

## 4. Scaling — Vertical vs Horizontal

### What These Mean

```
Vertical Scaling               Horizontal Scaling
─────────────────              ──────────────────
Bigger machine                 More machines
4 CPU → 16 CPU                 1 server → 4 servers
More RAM                       Load balancer in front
Faster disk                    Stateless app required
```

### For AI-PMS Right Now

**You don't have a scaling problem yet.** But here's the baseline direction that doesn't trap you:

```
Today (correct starting point):
  
  User → Single Node.js Server → MongoDB Atlas

When traffic grows (horizontal is the right path):

  User
   ↓
  Load Balancer (nginx / AWS ALB)
   ↓          ↓          ↓
 Node #1   Node #2   Node #3   ← Stateless (JWT, no session)
   ↓          ↓          ↓
        MongoDB Atlas
        (handles its own scaling via replica sets)
```

**Why horizontal is the right baseline direction:**

- Node.js is stateless by design (JWT auth ✅ already in place)
- MongoDB Atlas handles replication natively
- You can go from 1 → N servers behind a load balancer without touching the codebase — IF you keep the app stateless

**One thing that breaks horizontal scaling today:** The Socket.io monitoring server (`socketServer.js`) uses **in-memory state**. If you run 2 Node instances, a socket connected to Instance A won't receive events emitted on Instance B. Fix: use Redis as a Socket.io adapter when you scale.

---

## 5. Recommended Baseline Architecture

This is the direction to build toward — not to implement all at once.

```
┌────────────────────────────────────────────────────────┐
│                    PHASE 1 (Now)                        │
│                                                         │
│  Add Organization model as tenant root                  │
│  Fix tenantId consistently across all models            │
│  Fix auth field inconsistency (sub vs id vs _id)        │
│  Single server, single DB — that's fine                 │
└────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────┐
│                   PHASE 2 (Growth)                      │
│                                                         │
│  Add load balancer (nginx or AWS ALB)                   │
│  Deploy 2-3 stateless Node instances                    │
│  Add Redis for Socket.io adapter                        │
│  MongoDB Atlas auto-scales reads via replica reads      │
└────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────┐
│              PHASE 3 (Scale / Enterprise)               │
│                                                         │
│  Per-tenant DB option for enterprise customers          │
│  Caching layer (Redis) for property/room reads          │
│  DB indexes audit (already partially done)              │
│  Consider sharding only if >10M booking documents       │
└────────────────────────────────────────────────────────┘
```

> **Sharding and caching are not your problem.** MongoDB Atlas handles sharding internally if needed. Caching matters when you have repeated expensive reads — you don't have that volume yet. Solve multi-tenancy data model first.

---

## 6. What Needs to Change in Code (Phase 1)

### 6.1 Add Organization Model

```js
// NEW: models/Organization.js
const organizationSchema = new mongoose.Schema({
  name: { type: String, required: true },
  slug: { type: String, unique: true },  // used in routing
  plan: { type: String, enum: ['free', 'starter', 'pro'], default: 'free' },
  owner: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true },
  isActive: { type: Boolean, default: true },
  settings: { currency: String, timezone: String },
}, { timestamps: true });

organizationSchema.index({ owner: 1 });
organizationSchema.index({ slug: 1 });
```

### 6.2 Add organizationId to User

```js
// CHANGE in models/User.js — add to UserSchema fields:
organization: { 
  type: mongoose.Schema.Types.ObjectId, 
  ref: 'Organization' 
},
```

### 6.3 Add organizationId to Property (and cascade)

```js
// CHANGE in models/Property.js — add to propertySchema fields:
organization: { 
  type: mongoose.Schema.Types.ObjectId, 
  ref: 'Organization', 
  required: true 
},
// Add index:
propertySchema.index({ organization: 1 });
```

### 6.4 Standardize Auth Field

```js
// CHANGE in middleware/authMiddleware.js
// After JWT decode, normalize to one shape:
req.user = {
  id: decoded.sub || decoded.id || decoded._id,  // always 'id'
  role: decoded.role,
  organizationId: decoded.organizationId,
};
// Then every resolver uses req.user.id — no more sub/_id confusion
```

### 6.5 Update Base Query Pattern

```js
// CHANGE in all service files — from:
Property.find({ owner: req.user.id })

// To:
Property.find({ organization: req.user.organizationId })
```

---

## 7. Things NOT Worth Doing Yet

|Concept|Why Skip For Now|
|---|---|
|**Sharding**|MongoDB Atlas handles this internally; you'd need 10M+ documents to feel it|
|**Separate DB per tenant**|Operational overhead not justified until you have enterprise contracts|
|**Caching (Redis)**|Add when you see slow repeated reads; premature optimization now|
|**Horizontal scaling**|One well-sized server handles thousands of hotels; add LB when CPU > 70% consistently|
|**Message queues (Kafka)**|EventBus already handles async; Kafka is for millions of events/sec|

---

## 8. Summary Decision

```
DECISION: Stay on Shared DB / Shared Schema (Model A)
          but add Organization as the tenant root entity

SCALING:  Horizontal is the right direction — app is already 
          stateless (JWT). Just fix Socket.io when you scale.

PRIORITY ORDER:
  1. Add Organization model  ← unblocks everything else
  2. Fix auth field inconsistency  ← security / data leak risk
  3. Add organizationId to Property, Booking, Room  ← real isolation
  4. Only then think about load balancers / Redis
```