---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
Event Emitter ^ktD9ymL0

export default class EventEmitter {
  constructor() {
    this.observers = {}
  }

  /**
   * @param {string} eventName
   * @param {Function} listener
   * @returns {EventEmitter}
   */
  on(eventName, listener) {
    if (Object.hasOwn(this.observers, eventName)) {
        this.observers[eventName].push(listener)
    }else{
        this.observers[eventName] = [listener]
    }
    
    return this
  }

  /**
   * @param {string} eventName
   * @param {Function} listener
   * @returns {EventEmitter}
   */
  off(eventName, listener) {
    if (Object.hasOwn(this.observers, eventName)) {
        indexOfListener = this.observers[eventName].findIndex((observer) => observer === listener)
        if ( indexOfListener !== -1 ) {
            this.observers[eventName].splice(indexOfListener, 1)
        }
    }
    return this
  }

  /**
   * @param {string} eventName
   * @param  {...any} args
   * @returns {boolean}
   */
  emit(eventName, ...args) {
    if (Object.hasOwn(this.observers, eventName)) {
        if (this.observers[eventName].length >= 1 ) {
            this.observers[eventName].forEach((observer) => {
                observer(...args)
            })
            return true
        }
    }
    return false
  }
} ^6XiCIj9R

An event-based interaction model is the most common way of building user interfaces. The DOM is also built around this model with the document.addEventListener() and document.removeEventListener() APIs to allow responding to events like click, hover, input, etc.
Clarification questions

The following are good questions to ask the interviewer to demonstrate your thoughtfulness. Depending on their response, you might need to adjust the implementation accordingly.

    Can emitter.emit() be called without any arguments besides the eventName?
        Yes, it can be.
    Can the same listener be added multiple times with the same eventName?
        Yes, it can be. It will be called once for each time it is added when eventName is emitted in the order they were added.
    Following up on the question above, what should happen if a listener is added multiple times and emitter.off() is being called once for that listener?
        The listener will only be removed once.
    Can non-existent events be emitted?
        Yes, but nothing should happen and the code should not error or crash.
    What should the this value of the listeners be?
        It can be null.
    Can listeners contain code that invokes methods on the emitter instance?
        Yes, but we can ignore that scenario for this question.
    What if the listener callbacks throw an error during emitter.emit()?
        The error should be caught and not halt the rest of the execution. However, we will not test for this case.
 ^64MX6cNX

Questions to ask to interviewer ^DQRfgOj8

Read the solution at  ^CegVwD7x

## Element Links
CegVwD7x: https://www.greatfrontend.com/questions/javascript/event-emitter?language=js&tab=coding

%%
## Drawing
```compressed-json
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

7cheQ4QdocZBADGQgAA=
```
%%