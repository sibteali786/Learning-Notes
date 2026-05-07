---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
- the idea that emit.on returns an object with method off that unsubscribes the first entry in the eventName array we have
- This means off should have context about eventName array so it can find it and remove the event
- this is different from Event Emitter we did last time ^P7lyYeEB

export class EventEmitter {
    constructor(){
        this.observers = Object.create(null)
    }
    
    on(eventName, listener) {
        if (!Object.hasOwn(this.observers, eventName) ) {
            this.observers[eventName] = []
            
        }
        this.observers[eventName].push(listener)
        let context = this
        return {
            off: function(){
                if ( !Object.hasOwn(context.observers, eventName)) {
                    return 
                }

                const index = context.observers[eventName].findIndex((observer) => observer === listener )
                if ( index < 0 ) return
                
                context.observers[eventName].splice(index, 1)
            }
        }
    }

    emit(eventName, ...args){
        if ( !Object.hasOwn(this.observers, eventName) || this.observers[eventName].length === 0 ) {
            return false
        }
        
        const listeners = this.observers[eventName].slice() // create copies
        listeners.forEach((listener) => {
            listener.apply(null, args)
        })
        return true
    }
} ^gMVOITxz

## EventEmitter II — Key Learnings

### New concepts introduced

**1. Closure for context**
When a method is returned inside an object, `this` loses its reference to the class instance. Storing `let context = this` before returning gives the inner function access via closure.

**2. Subscription object pattern**
Instead of `emitter.off(eventName, fn)`, returning `{ off: fn }` from `on` encapsulates the unsubscribe logic — caller doesn't need to track event names or listener references.

**3. Snapshot pattern (`slice()`)**
```
listeners = this.observers[eventName].slice()
```
Iterating a copy protects against mutations (add/remove) that happen *during* emit — a real-world concurrency-style bug.

**4. `Object.create(null)` vs `{}`**
| | `{}` | `Object.create(null)` |
|---|---|---|
| Has prototype? | ✅ yes | ❌ no |
| Risk of key collision? | possible (`toString`, `constructor`) | none |
| Safer for dictionaries? | ✅ mostly | ✅ always |

---

### Pattern comparison
| | EventEmitter I | EventEmitter II |
|---|---|---|
| Unsubscribe via | `emitter.off(name, fn)` | `sub.off()` |
| Context | args passed explicitly | closed over |
| Snapshot | ❌ | ✅ |

---

### Interview angle
> *"Why return a subscription object instead of exposing `off` directly?"*

Encapsulation — the caller doesn't need to hold references to `eventName` or `listener`. The subscription object owns that responsibility. This is the same pattern used by **RxJS subscriptions** and **DOM's `addEventListener`** alternatives.

--- ^OYC5V8P3

Read Solution at EventEmitter II for better techniques ^3kXw4KSc

%%
## Drawing
```compressed-json
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=
```
%%