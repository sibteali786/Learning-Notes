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
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=
```
%%