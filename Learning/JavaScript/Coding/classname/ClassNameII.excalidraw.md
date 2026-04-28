---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
export default function classNames(...args) {
    const arr = args
    const hasSeen = new Set()
    for (const value of arr) {
        if (typeof value === 'string' && value !== ''){
            hasSeen.add(value)
        }else if (value && Array.isArray(value)){
            hasSeen.add(classNames(...value))
        }else if (value typeof === 'object' ){
            for const [key, val] of Object.entries(value)) {
                if ( val ) {
                    hasSeen.add(key)
                }else {
                    if ( hasSeen.has(key) && !val ){
                        hasSeen.remove(key)
                    }  
                }
            }
        }
    }
    let [key, value] = hasSeen.entries()
    return str.join(" ")
} ^eq1YjNsv

Version 2 ^DgHpFQmW

/**
 * @typedef {Record<string, unknown>} ClassDictionary
 * @typedef {Array<ClassValue>} ClassArray
 * @typedef {string | number | null | boolean | undefined | (() => unknown) | ClassDictionary | ClassArray} ClassValue
 */

/**
 * @param {...ClassValue} args
 * @returns {string}
 */
export default function classNames(...args) {
  const arr = args;
  const hasSeen = new Set();
  for (const value of arr) {
    if (typeof value === "string" && value !== "") {
      hasSeen.add(value);
    } else if (typeof value === "number" && value) {
      hasSeen.add(String(value));
    } else if (value && Array.isArray(value)) {
      const newStrArr = classNames(...value);
      if (newStrArr !== "") {
        for (const value of newStrArr.split(" ")) {
          hasSeen.add(value);
        }
      }
    } else if (value && typeof value === "object") {
      for (const [key, val] of Object.entries(value)) {
        if (val) {
          hasSeen.add(key);
        } else {
          if (hasSeen.has(key) && !val) {
            hasSeen.delete(key);
          }
        }
      }
    } else if (value && typeof value === "function") {
      const returnValue = value();
      const newStrArr = classNames(...[returnValue]);
      if (newStrArr !== "") {
        for (const value of newStrArr.split(" ")) {
          hasSeen.add(value);
        }
      }
    }
  }

  return Array.from(hasSeen.values()).join(" ");
}
 ^vBYPqE67

Version 3
Deeply nested array with object can cause issues since each recursion has its own hasSeen set ^ZKjXCl8k

function flatten(arr) {
  const result = [];
  for (const val of arr) {
    if (Array.isArray(val)) {
      result.push(...flatten(val));
    } else {
      result.push(val);
    }
  }
  return result;
} ^ok1u9Jen

add flatten to flat everything at same level ^BfBAbDnz

/**
 * @typedef {Record<string, unknown>} ClassDictionary
 * @typedef {Array<ClassValue>} ClassArray
 * @typedef {string | number | null | boolean | undefined | (() => unknown) | ClassDictionary | ClassArray} ClassValue
 */

/**
 * @param {...ClassValue} args
 * @returns {string}
 */
export default function classNames(...args) {
  const arr = flatten(args);
  const hasSeen = new Set();
  for (const value of arr) {
    if (typeof value === "string" && value !== "") {
      hasSeen.add(value);
    } else if (typeof value === "number" && value) {
      hasSeen.add(String(value));
    } else if (value && typeof value === "object") {
      for (const [key, val] of Object.entries(value)) {
        if (val) {
          hasSeen.add(key);
        } else {
          if (hasSeen.has(key) && !val) {
            hasSeen.delete(key);
          }
        }
      }
    } else if (value && typeof value === "function") {
      const returnValue = value();
      const newStrArr = classNames(returnValue);
      if (newStrArr !== "") {
        for (const value of newStrArr.split(" ")) {
          hasSeen.add(value);
        }
      }
    }
  }

  return Array.from(hasSeen.values()).join(" ");
}

function flatten(arr) {
  const result = [];
  for (const val of arr) {
    if (Array.isArray(val)) {
      result.push(...flatten(val));
    } else {
      result.push(val);
    }
  }
  return result;
}
 ^lejOBZbS

- In this way we flatten items first and then only process them otherwise we fails some tests like

 classNames('foo', [{ foo: false }, 'foo', { foo: false }])

here since array has nested structure the hasSeen would be new for this recursive call which 
if we want to avoid we need to either not use recursion at all or faltten everything first and then 
use our current recursive logic. ^kSDtjuC2

GO Over solution in GreatFrontend for ClassName II
- Its gives perspective about recursive call without flatten array method ^5iYoteA7

Version 4 ( Much Cleaner and purely using Recursion with global object ) ^EgyXBaXo

export default function classNames(...args) {
  const classes = new Set();

  function classNamesImpl(...args) {
    args.forEach((arg) => {
      // ignore falsy values
      if (!arg) {
        return;
      }

      const argType = typeof arg;

      if (argType === "string" || argType === "number") {
        classes.add(String(arg));
        return;
      }

      if (argType === "function") {
        const result = arg();
        if (!result) return;
        classes.add(String(result));
      }

      if (Array.isArray(arg)) {
        for (const cls of arg) {
          classNamesImpl(cls);
        }
        return;
      }

      if (argType === "object") {
        for (const key in arg) {
          if (Object.hasOwn(arg, key)) {
            arg[key] ? classes.add(key) : classes.delete(key);
          }
        }
      }

      return;
    });
  }

  classNamesImpl(args);

  return Array.from(classes).join(" ");
}
 ^MT7YoWEI

%%
## Drawing
```compressed-json
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
```
%%