```table-of-contents
```
# Zen
## fix:sidebar flickering during drag operations in compact mode #11015
Today i contributed to zen browser desktop feature
At first i tried with claude and resolved issue using timers and debouncer 
- What i did was that onEnter method i added a condition that if it was a `dragleave` event i ll mark a property `isDragging` as true and call clearTimeout
- Then in `onLeave` i ll check if its a `dragleave`  and `isDragging` is true then we set dragDebouncer to setTimeout with a hardcoded value of 150ms so that it does run just now but with a delay 
### Question why did we use timer here i.e `dragDebouncer` ?
We use `clearTimeout()` to implement **debouncing** - a technique to prevent rapid, flickering state changes.

**The problem:** When dragging near the sidebar edge, `dragleave` and `dragover` events fire rapidly (every few milliseconds), causing the sidebar to flicker.

**The solution:** Instead of immediately acting on `dragleave`, we wait 150ms. If another `dragover` event fires during that wait (meaning the drag is still active), we **cancel the wait** using `clearTimeout()` and start a new one.

This ensures the sidebar only hides after the drag has **truly ended** (no dragover events for 150ms), not just when crossing internal element boundaries.

**Think of it like a snooze button:** Each `dragover` "snoozes" the hide action for another 150ms. Only when you stop "snoozing" (stop dragging) does the action actually execute.

```js
// Time 0ms: dragleave fires
const onLeave = (event) => {
  if (event.type === 'dragleave' && this._isDragging) {
    clearTimeout(this._dragDebounceTimer);  // Clear any existing timer
    this._dragDebounceTimer = setTimeout(() => {
      this._isDragging = false;  // This will run in 150ms
    }, 150);
    return;  // Don't hide sidebar yet
  }
};

// Time 30ms: dragover fires (user still dragging)
const onEnter = (event) => {
  if (event.type === 'dragover') {
    this._isDragging = true;
    clearTimeout(this._dragDebounceTimer);  // ← CANCEL the 150ms timer!
    // Sidebar stays visible
  }
};

// Time 150ms: Nothing happens (timer was canceled)
// Sidebar stays visible ✓

// Time 200ms: dragleave fires again
// (same logic - start new 150ms timer)

// Time 250ms: dragover fires
// (cancel timer again)

// ... continues until drag really ends

// When drag ACTUALLY ends:
// Final dragleave → starts timer → 150ms passes with no dragover
// → Timer executes → _isDragging = false → Sidebar can hide
// Visual 
Event:     dragleave  dragover  dragleave  dragover  [actual end]  dragleave
Time:      0ms        30ms      80ms       120ms     200ms         250ms
           
Timer:     Start      Cancel    Start      Cancel                  Start
           (150ms)    ✗         (150ms)    ✗                       (150ms)
           
_isDragging: true → true → true → true → true → [wait] → false (at 400ms)
                                                  
Sidebar:   VISIBLE throughout dragging → Hides 150ms after last dragover
```

### The better solution and why my solution was'nt perfect 
- After several feedbacks from maintainer, he actually came with a much more elegant solution.
#### Problem with my solution 
The problem with my solution that it was being fired out for every child component of the sidebar we pass over as we are dragging which was resource consuming 
- The better approach was to not hide sidebar if it was fired from a child of parent ( a sub area of sidebar itself ) as he stated in the comment
![[Pasted image 20251029234403.png]]

### ELEGANCE at its peak 
So mr cheffy came up with a simple one liner solution that is just ignore dragleave when its caused by the childs of the parent ( sidebar area itself )
```js
(event.type === 'dragleave' &&
              event.explicitOriginalTarget !== target &&
              target.contains(event.explicitOriginalTarget))
```
whole code becomes 
```js
if (

event.explicitOriginalTarget?.closest?.('#urlbar[zen-floating-urlbar]') ||

(document.documentElement.getAttribute('supress-primary-adjustment') === 'true' &&

gZenVerticalTabsManager._hasSetSingleToolbar) ||

this._hasHoveredUrlbar ||

this._ignoreNextHover ||

(event.type === 'dragleave' &&

event.explicitOriginalTarget !== target &&

target.contains?.(event.explicitOriginalTarget))

) {

return;

}
```
- here `explicitOriginalTarget` is our the one we are over while dragging, `event.target`  is our sidebar and using condition `event.target.contains(event.explicitOriginalTarget)` we are making sure that its child of sidebar 

## The History panel from custom history button never shows up
important ids 
- `PanelUI-menu-button` for panel from 3 dotted menu
```js
let appMenuHistoryBtn = document.getElementById("appMenu-history-button")
```
- The panel ui history for the history panel
  ```js
  let panelUIHistory = document.getElementById("PanelUI-history")
  ```
the menu we need to fix has id 
`PanelUI-history` and classes `PanelUI-subView cui-widget-panelview`
## Important File Details
- ZenUIManager.mjs had a problem that history tab was  being opening below screen so the maintainer modified a method
  ```js
  panelUIPosition(panel, anchor) {

void panel;

// The alignment position of the panel is determined during the "popuppositioned" event

// when the panel opens. The alignment positions help us determine in which orientation

// the panel is anchored to the screen space.

//

// * "after_start": The panel is anchored at the top-left corner in LTR locales, top-right in RTL locales.

// * "after_end": The panel is anchored at the top-right corner in LTR locales, top-left in RTL locales.

// * "before_start": The panel is anchored at the bottom-left corner in LTR locales, bottom-right in RTL locales.

// * "before_end": The panel is anchored at the bottom-right corner in LTR locales, bottom-left in RTL locales.

//

// ┌─Anchor(LTR) ┌─Anchor(RTL)

// │ Anchor(RTL)─┐ │ Anchor(LTR)─┐

// │ │ │ │

// x───────────────────x x───────────────────x

// │ │ │ │

// │ Panel │ │ Panel │

// │ "after_start" │ │ "after_end" │

// │ │ │ │

// └───────────────────┘ └───────────────────┘

//

// ┌───────────────────┐ ┌───────────────────┐

// │ │ │ │

// │ Panel │ │ Panel │

// │ "before_start" │ │ "before_end" │

// │ │ │ │

// x───────────────────x x───────────────────x

// │ │ │ │

// │ Anchor(RTL)─┘ │ Anchor(LTR)─┘

// └─Anchor(LTR) └─Anchor(RTL)

//

// The default choice for the panel is "after_start", to match the content context menu's alignment. However, it is

// possible to end up with any of the four combinations. Before the panel is opened, the XUL popup manager needs to

// make a determination about the size of the panel and whether or not it will fit within the visible screen area with

// the intended alignment. The manager may change the panel's alignment before opening to ensure the panel is fully visible.

//

// For example, if the panel is opened such that the bottom edge would be rendered off screen, then the XUL popup manager

// will change the alignment from "after_start" to "before_start", anchoring the panel's bottom corner to the target screen

// location instead of its top corner. This transformation ensures that the whole of the panel is visible on the screen.

//

// When the panel is anchored by one of its bottom corners (the "before_..." options), then it causes unintentionally odd

// behavior where dragging the text-area resizer downward with the mouse actually grows the panel's top edge upward, since

// the bottom of the panel is anchored in place. We want to disable the resizer if the panel was positioned to be anchored

// from one of its bottom corners.

let block = 'bottomleft';

let inline = 'topleft';

if (anchor?.closest('#zen-sidebar-top-buttons')) {

block = 'topleft';

}

if (gZenVerticalTabsManager._hasSetSingleToolbar && gZenVerticalTabsManager._prefsRightSide) {

block = 'bottomright';

inline = 'topright';

}

return `${block} ${inline}`;

},
  ``` 
### Last Tab not closing 
Relevant files found 
- ZenWorksapce.mjs
- drag_and_drop.js -> handle_drop
- tabBrowser.js -> adoptTab and swapBrowsersAndCloseOther and _beginRemoveTab_
	- checing fucntion #isLastTabInWindow 
	- asked MrCheffy to provide any pointer he can why isLasTabInWindow returns false.