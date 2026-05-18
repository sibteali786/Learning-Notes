
## 🕐 Timezone Handling — Current State

### The Core Problem Visualized

```
Pakistani guest books Lisbon hostel
─────────────────────────────────────────────────────
Guest's browser (PKT = UTC+5)        Hostel server/DB (Lisbon = UTC+1 in winter)
                                     
User picks: "Check-in Dec 1"         
→ frontend does:
  new Date("2024-12-01T00:00:00")    ← ⚠️ NO timezone specified
  .toISOString()                     
  = "2024-11-30T19:00:00.000Z"       ← Stored as Nov 30, not Dec 1!
                                     
Hostel receptionist sees: Nov 30     ← Wrong day entirely
```

### What the code actually does right now

**Frontend (`toISOString` in `utilis/index.js`):**

```js
export const toISOString = (dateStr) => {
  return new Date(dateStr).toISOString(); // ← uses browser's local timezone
}
```

When a user picks a date from an `<input type="date">`, it's a string like `"2024-12-01"`. `new Date("2024-12-01")` is parsed as **midnight UTC** by browsers — but this is actually inconsistent across browsers and environments.

**Gantt chart (`gantt/page.jsx`) — this one is actually a bug:**

```js
startDate: new Date(startDate + "T00:00:00").toISOString(), // uses LOCAL time
endDate:   new Date(endDate   + "T23:59:59").toISOString(), // uses LOCAL time
```

This appends local midnight, then converts to UTC — so the Gantt range shifts by your timezone offset.

**Backend (conflict check in `roomAssignmentEngine.js`):**

```js
checkIn: { $lt: new Date(checkOut) },  // raw JS Date — UTC only
checkOut: { $gt: new Date(checkIn) }
```

The DB stores and compares pure UTC. This is actually the **right approach** — but it only works correctly if the frontend sends proper UTC-normalized dates, which it currently doesn't guarantee.

**OTA adapters (`BaseChannelAdapter.parseDate`):**

```js
parseDate(dateStr) {
  const d = new Date(dateStr); // ← no timezone awareness
  return isNaN(d) ? null : d;
}
```

Booking.com sends `"2024-12-01"` (date only, no time). `new Date("2024-12-01")` = **midnight UTC** in Node.js — which is actually fine for server-side, but means check-in is midnight UTC, not midnight Lisbon time.

---

## 🎯 What This Means Practically for MVP (Lisbon-first)

```
Scenario                    Risk Level    Why
──────────────────────────────────────────────────────
Staff books from Lisbon     🟡 LOW        Browser in UTC+1, offset is 1hr
                                          Dec 1 midnight Lisbon → Nov 30 23:00 UTC
                                          Could show wrong day in edge cases

OTA booking (Booking.com)   🟢 OK        OTAs send date strings, backend handles UTC
                                          conflict check works correctly
                                          
Pakistani booking Lisbon    🔴 HIGH       UTC+5 offset = 5hr shift
                                          Could book "Dec 1" but store as "Nov 30 19:00 UTC"
                                          Conflict check would use wrong date range

Gantt calendar view         🟡 MEDIUM     Ranges shift slightly per viewer timezone
                                          Not dangerous, just visually confusing
```

**For Lisbon MVP only** — the risk is low because UTC+1 only causes a 1-hour drift at midnight edge cases. The bigger risk is when you expand to Pakistan (UTC+5).

---

## ✅ The Fix — Minimal & MVP-Safe

The correct rule, borrowed from how every major booking system works:

> **Store `checkIn` and `checkOut` as date-only at midnight UTC (`T00:00:00.000Z`). The date is the date at the property's location. Forget time-of-day for booking purposes.**

A booking for Dec 1–3 in Lisbon means Dec 1–3 **at the property**. It should never shift regardless of where the guest booked from.

### Fix 1 — Frontend `toISOString` in `utilis/index.js`

```js
// REPLACE current toISOString:
export const toISOString = (dateStr) => {
  try {
    // Force midnight UTC — treat input as a property-local date, not browser-local
    if (/^\d{4}-\d{2}-\d{2}$/.test(dateStr)) {
      return dateStr + "T00:00:00.000Z"; // date-only string → midnight UTC directly
    }
    return new Date(dateStr).toISOString();
  } catch {
    return new Date().toISOString();
  }
};
```

### Fix 2 — Gantt page date construction

```js
// REPLACE in gantt/page.jsx:
// FROM:
startDate: new Date(startDate + "T00:00:00").toISOString(),
endDate:   new Date(endDate   + "T23:59:59").toISOString(),

// TO:
startDate: startDate + "T00:00:00.000Z",
endDate:   endDate   + "T23:59:59.999Z",
```

### Fix 3 — OTA adapter `parseDate` in `BaseChannelAdapter.js`

```js
// REPLACE:
parseDate(dateStr) {
  if (!dateStr) return null;
  const d = new Date(dateStr);
  return isNaN(d) ? null : d;
}

// WITH:
parseDate(dateStr) {
  if (!dateStr) return null;
  // Date-only strings (YYYY-MM-DD) should be midnight UTC, not local
  if (/^\d{4}-\d{2}-\d{2}$/.test(dateStr)) {
    const d = new Date(dateStr + "T00:00:00.000Z");
    return isNaN(d) ? null : d;
  }
  const d = new Date(dateStr);
  return isNaN(d) ? null : d;
}
```

The conflict detection in `roomAssignmentEngine.js` is **already correct** — it does pure UTC Date comparisons in MongoDB. Once the dates coming in are normalized to midnight UTC, it works perfectly.

---

## 📋 Priority for MVP

|Fix|Effort|Risk if skipped|
|---|---|---|
|`toISOString` in utils|5 min|🔴 Bookings land on wrong day for non-UTC users|
|Gantt date range|5 min|🟡 Gantt shows wrong week boundary|
|`parseDate` in BaseChannelAdapter|10 min|🟢 Low — OTAs usually send full ISO timestamps|
