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

- Some problems in my solution i observed.
Cloning protects the current emission from listeners that add or remove handlers while emit() is running.

- Storing in plain Javascript objects can cause issue if event stored is similar to inherited methods like toString()
If you store listeners in a plain JavaScript object, user-provided names such as valueOf or toString can collide with inherited properties. ^vRbKbwVP

export default class EventEmitter {
  constructor() {
    // Avoid creating objects via `{}` to exclude unwanted properties
    // on the prototype (such as `.toString`).
    this._events = Object.create(null);
  }

  on(eventName, listener) {
    // Group listeners by event name so emit/off only touch one bucket.
    if (!Object.hasOwn(this._events, eventName)) {
      this._events[eventName] = [];
    }
    this._events[eventName].push(listener);
    return this;
  }

  off(eventName, listener) {
    if (!Object.hasOwn(this._events, eventName)) {
      return this;
    }

    const listeners = this._events[eventName];

    const index = listeners.findIndex(
      (listenerItem) => listenerItem === listener,
    );

    if (index < 0) {
      return this;
    }

    this._events[eventName].splice(index, 1);
    return this;
  }

  emit(eventName, ...args) {
    if (
      !Object.hasOwn(this._events, eventName) ||
      this._events[eventName].length === 0
    ) {
      return false;
    }

    const listeners = this._events[eventName].slice();
    listeners.forEach((listener) => {
      listener.apply(null, args);
    });

    return true;
  }
} ^nB0m0Udd

## Element Links
CegVwD7x: https://www.greatfrontend.com/questions/javascript/event-emitter?language=js&tab=coding

%%
## Drawing
```compressed-json
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

BjnQiqEAOZCAA===
```
%%