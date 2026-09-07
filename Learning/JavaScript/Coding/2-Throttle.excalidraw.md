---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
Throttle ^ucz44bHR

function throttle(func, wait) {
    let isFuncCalled = false
    return function (...args) {
        const context = this;
        // check if is Called was set
        if (!isFuncCalled) {
            isFuncCalled = true
            func.apply(context, args)
            setTimeout(() => {isFuncCalled = false}, wait)
        }
    }
} ^odlWmr1g

With Cancel ^MFaxs5JP

function throttle(func, wait) {
    let isFuncCalled = false
    let timeoutID = null
    const myFunction = function (...args) {
        const context = this;
        // check if is Called was set
        if (!isFuncCalled) {
            isFuncCalled = true
            func.apply(context, args)
            timeoutID = setTimeout(() => {isFuncCalled = false}, wait)
        }
    }

    const unlock = function () {
        if(timeoutID){
            clearTimeout(timeoutID);
            isFuncCalled = false;
            timeoutID = null
        }
    }

    myFunction.cancel = unlock;
    return myFunction;
} ^QsRxIhjm

Leading and Trailing ^Jtkn7Mjk

function throttle(func, wait, options) {
    let isLeadingFuncCalled = false
    let isTrailingFuncLocked = false
    let storedArgs = undefined
    let storedContext = undefined
    let hadCallDuringWindow = false
    const {trailing = false, leading = true} = options
    return function (...args) {
        storedContext = this;
        storedArgs = args
        if(leading === true) {
            // check if is isLeadingFuncCalled was set
            if (!isLeadingFuncCalled) {
                isLeadingFuncCalled = true
                func.apply(storedContext, storedArgs)
                setTimeout(() => {isLeadingFuncCalled = false}, wait)
            }
        }
        
        if (trailing === true){
            if (!isTrailingFuncLocked) {
                isTrailingFuncLocked = true
                if ( !leading ) {
                    hadCallDuringWindow = true
                }
                setTimeout(() => {
                    if ( hadCallDuringWindow) {
                        func.apply(storedContext, storedArgs);
                        hadCallDuringWindow = false
                    }
                    isTrailingFuncLocked = false 
                }, wait)
            }else {
                hadCallDuringWindow = true
            }
        }
    }
} ^Fqa93ijW

Debounce vs Throttle — Leading & Trailing

Core difference first:
Debounce:  resets timer on every call, fires after LAST call
Throttle:  fires immediately, locks for wait duration

Leading:
Debounce:  fires on FIRST call, ignores until wait expires after LAST call
Throttle:  fires on FIRST call, ignores until wait expires
Trailing:
Debounce:  fires after wait expires from LAST call (default behavior)
Throttle:  fires ONCE after wait if any calls were MISSED during window
 ^dyPBiERx

%%
## Drawing
```compressed-json
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
```
%%