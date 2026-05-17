---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
Jquery.css ^uGWPYy7e

export default function $(selector) {
  let element = document.querySelector(selector);
  const response = {
    css: function () {
      if (!element) return arguments.length === 1 ? undefined : response;
      const property = arguments[0];
      const value = arguments[1];
      if (arguments.length === 1) {
        const val = element.style[property];

        return val === "" ? undefined : val;
      }
      element.style[property] = value;
      return response;
    },
  };
  return response;
} ^krKhSch8

Read solution at Jquery.css ^yVbMy9EJ

Approach 2 ( Official Solution )  ^vzhPyhU7

export default function $(selector) {
    const element = document.querySelector(selector)
    return {
        css: function(prop, value) {
            if ( value === undefined ) {
                if ( element === null ) {
                    return undefined
                }
                
                const value = element.style[prop]
                return value === '' ? undefined: value
            }
            // setter case
            if (element !== null ) {
                element.style[prop] = value
            }
            return this
        }
    }
} ^9HJmrubK

Approach 3 ( Class Based Solution )  ^INoNQSTs

export class jQuery {
    constructor (selector) {
        this.element = document.querySelector(selector)
    }

    css(prop, value) {
        // Getter case
        if ( value === undefined ) {
            if ( this.element === null ) {
                return undefined
            }
            const val = this.element.style[prop]
            return val === "" ? undefined : val
        }
        
        //setter
        if ( element !== null ) {
            this.element.style[prop] = value
        }
        return this    
    }
}

export default function $(selector) {
    return new jQuery(selector)
} ^8YcobuAb

## Element Links
yVbMy9EJ: https://www.greatfrontend.com/questions/javascript/jquery-css

%%
## Drawing
```compressed-json
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=
```
%%