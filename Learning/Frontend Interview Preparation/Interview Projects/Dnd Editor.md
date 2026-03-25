```table-of-contents
```
- draggable="true" → makes an element draggable
- onDragStart → fires when user starts dragging (store what's being dragged). 
- onDragOver → fires when dragging over a target (must preventDefault to allow drop)
- onDrop → fires when dropped (read what was dragged, update state)
  
  
# Problem
````css
## Now do this to feel the problem

1. Run the app, click **Stress Test**
2. Then try **dragging** a new item from the sidebar onto the canvas
3. Notice the **lag** — every drag event is re-rendering all 200 items

---

## Why is it slow? (The root cause)
```
You drag → onDragOver fires → App state untouched
BUT React still re-evaluates every CanvasItem
because Canvas re-renders → all children re-render by default
````

Every `CanvasItem` re-renders even though **nothing about them changed**. With 200 items that's 200 wasted renders per mouse-move event. `onDragOver` fires dozens of times per second.

## Going through with Components and Profiler
### Phase 3 — Profiling with React DevTools

Before fixing anything, we need to **see** the problem. This is what separates good engineers from great ones in interviews.

---

### Step 1 — Install React DevTools

Install the **React Developer Tools** browser extension:

- [Chrome](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi)
- [Firefox](https://addons.mozilla.org/en-US/firefox/addon/react-devtools/)

After install you'll see a **⚛️ Components** and **⚛️ Profiler** tab in DevTools (F12).

---

### Step 2 — Enable "Highlight updates"

This gives you a **visual flash** on every re-render without even recording.

```
F12 → React DevTools → Components tab
  → click the ⚙️ settings gear icon
    → check "Highlight updates when components render"
```

Now click **Stress Test** then drag a sidebar item slowly over the canvas.

**You'll see:** every single `CanvasItem` flashes on every `onDragOver` event — even though their data never changed.

---

### Step 3 — Record a Profiler session

```
F12 → Profiler tab
  → click ⏺ Record
    → click Stress Test button
      → drag one item slowly over canvas for 2 seconds
        → click ⏹ Stop
```

#### What to look for in the flame chart

```
App                          ← re-renders (state owner, expected)
  └── Canvas                 ← re-renders (receives items prop)
        ├── CanvasItem [0]   ← re-renders ❌ nothing changed
        ├── CanvasItem [1]   ← re-renders ❌ nothing changed
        ├── CanvasItem [2]   ← re-renders ❌ nothing changed
        ...×200
```

Each bar's **width = time spent**. You'll see 200 CanvasItem bars all lighting up for a drag event they don't care about.

---

### Step 4 — Check the "Why did this render?" reason

```
Profiler → click any CanvasItem bar
  → right panel shows: "Why did this render?"
    → it will say: "Parent component rendered"
```

That's the smoking gun. The item has **no new props**, but it re-rendered purely because its parent did.

---

### What you've just diagnosed

| Problem                                         | Root Cause                                  |
| ----------------------------------------------- | ------------------------------------------- |
| 200 re-renders per drag event                   | `CanvasItem` has no memoization             |
| `onDragOver` triggers state-adjacent re-renders | Canvas re-renders propagate to all children |
| Wasted render time ~ms × 200                    | Compounds fast with complex components      |

---

### The fix (Phase 4 preview)

```
React.memo(CanvasItem)   → skip re-render if props didn't change
useCallback(handlers)    → stop passing new function refs on every render
```

### How does Flamegraph works
- Here component which caused update is App ? why 
- because `canvasItems` changed when we added a new item to canvasItems array and thus new props was passed down to `Canvas` component thus component causing change is App.jsx
![[Screenshot 2026-03-16 at 1.47.50 AM.png]]
#### Reading Your Profiler Output

#### Image 1 — The Flamegraph

```
App (1ms of 21ms)
  └── Canvas (3ms of 18ms)
        ├── CanvasItem
        ├── CanvasItem
        ├── CanvasItem × 200...
```

- **21ms total** for one commit (one React update cycle)
- **18ms spent inside Canvas** — almost all of it is rendering children
- **"What caused this update? → App"** — App's state changed (you clicked Stress Test), which cascaded down to every child

#### Image 2 — The CanvasItem detail
![[Screenshot 2026-03-16 at 1.49.13 AM.png]]
```
Rendered at:
  5.9s  for 21ms   ← Stress Test click (initial render, expected)
  13.8s for 22ms   ← This is the problem ❌
```

That **second render at 13.8s** — that's when you dragged or interacted. The item's props **never changed** but it still spent 22ms re-rendering. Multiply that by 200 items.
- This shows component rendered first when we clicked `Stress Test` 
- and then we dropped another item from sidebar. Showing it re-rendered when a new item was dropped from sidebar.
![[Screenshot 2026-03-16 at 1.49.13 AM.png]]

## Initial Optimization 
- We will use the memo and useCallback combination for optimizing our canvas rendering large number of items.
- `memo` wraps the component and does a shallow comaprisons props before re-rendering.
- Off-course if props didn't changed since last render -> React skips the render entirely.
- useCallback on the other hand is used to make sure that functions passed to Canvas component do not change.
- When App re-renders it creates new `handleDrop` function which is then. passed to Canvas where CanvasItem does a shallow comparison of old hanldeDrop and new handleDrop since they have different references in memory thus it even though we applied memo it wont work.
- Thus we use useCallback() which makes sure that handleDrop is created once and then never changes.
### Result
- as last time we create recording, 
1. stress test click 
2. then pick a component and drop on canvas slowly
- we can see clearly that no new render took place in canvas items.
![[Screenshot 2026-03-20 at 3.14.04 AM.png]]
### Why Does Canvas and App re render
Great — very specific question. Let me trace it step by step.
#### What happens when you drop a new component

```
You drop → onDrop fires → handleDrop runs → setCanvasItems called
```

`setCanvasItems` is a **state update**. That's the trigger.
#### React's re-render rule

```
When state changes in a component
→ that component re-renders
→ ALL its children re-render by default
```

So:

```
setCanvasItems called inside App
→ App re-renders        ← owns the state, must re-render
  └── Sidebar re-renders
  └── Canvas re-renders ← child of App, re-renders by default
        ├── CanvasItem  ← memo'd → bails out ✅
        ├── CanvasItem  ← memo'd → bails out ✅
        ...×200
```
#### Why Canvas re-renders even though it "didn't do anything"

Because React doesn't know that. By default React re-renders **every child** when a parent's state changes. And Canvas `items` prop changes when we drop a new item onto Canvas. but only the new item added gets rendered not whole list of 200 items.
## Phase 5: Virutalization
- Why we need it ?
- For now all 200 items / nodes exists in the page even if only few ( 5 ) are visible on the screen.
### Problem with 200 nodes
```text
Canvas renders 200 items
→ browser creates 200 real DOM nodes
→ each has layout, paint, memory cost
→ user can only see ~5 at a time
→ we're paying for 195 invisible items
```
### Fix: virtualization
Only render what's **visible in the viewport**. As user scrolls, swap items in and out.
```text
Without virtualization:     With virtualization:
┌─────────────┐             ┌─────────────┐
│ item 1  ✅  │             │ item 1  ✅  │
│ item 2  ✅  │             │ item 2  ✅  │
│ item 3  ✅  │             │ item 3  ✅  │
│ item 4  ✅  │             └─────────────┘ ← viewport ends
│ item 5  ✅  │             (items 4-200 don't exist in DOM)
│ ...         │
│ item 200 ✅ │  ← DOM node exists, costs memory
└─────────────┘
```
We will build from scratch using `IntersectionObserver` : The browser API tells you when an an element enters/leave the viewport.