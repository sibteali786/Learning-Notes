---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
export default function promiseAllSettled(iterable) {
    return new Promise((resolve, reject) => {
        let results = new Array(iterable.length)
        let settled = iterable.length
        if (settled === 0 ) {
            resolve(results)
            return
        }
        
        iterable.forEach((item, index) => {
            Promise.resolve(item).then(
            (value) => {
                results[index] = {status: "fulfilled", value }
                settled -= 1    
                if (settled === 0 ) {
                    resolve(results)
                }
            },
            (reason)=> {
                results[index] = {status: "rejected", reason }
                settled -= 1
                if (settled === 0 ) {
                    resolve(results)
                }
            })
        })
    })
} ^Gzq95AHB

More clearner version ^jZ5gN1mu

export default function promiseAllSettled(iterable) {
    return new Promise((resolve, reject) => {
        let results = new Array(iterable.length)
        let settled = iterable.length
        if (settled === 0 ) {
            resolve(results)
            return
        }
        
        iterable.forEach((item, index) => {
            Promise.resolve(item).then(
            (value) => {
                results[index] = {status: "fulfilled", value }
                           },
            (reason)=> {
                results[index] = {status: "rejected", reason }
            }).finally(() => {
                settled -= 1    
                if (settled === 0 ) {
                    resolve(results)
                }

            })
        })
    })
} ^BuqqwqNZ

%%
## Drawing
```compressed-json
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
```
%%