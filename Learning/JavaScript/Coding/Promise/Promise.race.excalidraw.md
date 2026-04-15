---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
Promise.race() ^YZ4hGZsl

Questions ? 
1. How is this simpler than both Promise.all and Promise.any?
2. Empty array — what should happen? Re-read the requirement carefully.
3. Do you need a counter at all here? ^9JBKvW1v

export default function promiseRace(iterable) {
    return new Promise((resolve, reject) => {
        if (iterable.length === 0 ) {
            return
        }
        iterable.forEach((item) => {
            Promise.resolve(item).then((value) => {
                resolve(value)
            }, (reason) => {
                reject(value)
            })
        })
    })
} ^akASXQyY

/**
 * @param {Array} iterable
 * @return {Promise}
 */
export default function promiseRace(iterable) {
  return new Promise((resolve, reject) => {
    if (iterable.length === 0) {
      return;
    }
    iterable.forEach((item) => {
      Promise.resolve(item).then(
        (value) => {
          resolve(value);
        },
        (reason) => {
          reject(reason);
        },
      );
    });
  });
}
 ^IrQSDQ5s

%%
## Drawing
```compressed-json
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

aBC8Nq7IIQcm8ASHfkQUcIDMmyEAGyIAA===
```
%%