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

AA==
```
%%