---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
/**
 * @param {string} selector
 * @return {{toggleClass: Function, addClass: Function, removeClass: Function}}
 */
export default function $(selector) {
  const element = document.querySelector(selector);

  return {
    /**
     * @param {string} className
     * @param {boolean} [state]
     * @return {Object|void}
     */
    toggleClass: function (className, state) {
      let classStr = element.getAttribute("class");
      if (!classStr) return this;
      let classList = classStr.trim().split(" ");
      let classNameList = className.trim().split(" ");
      classNameList.forEach((value) => {
        if (classList.includes(value)) {
          // exists already
          // remove if no state is present
          if (state === undefined) {
            this.removeClass(value);
          } else {
            if (!state) {
              this.removeClass(value);
            }
          }
        } else {
          if (state === undefined) {
            this.addClass(value);
          } else {
            if (state) {
              this.addClass(value);
            }
          }
        }
      });

      return this;
    },
    /**
     * @param {string} className
     * @return {Object}
     */
    addClass: function (className) {
      let classStr = element.getAttribute("class");
      if (!classStr) return this;
      let classList = classStr.trim().split(" ");
      let classNameList = className.trim().split(" ");
      classNameList.forEach((value) => {
        if (!classList.includes(value)) {
          classList.push(value);
        }
      });
      // remoe whitespaces
      let resultClassList = classList.filter((value) => value !== "");
      let resultClassStr = resultClassList.join(" ");
      element.setAttribute("class", resultClassStr);
      return this;
    },
    /**
     * @param {string} className
     * @return {Object}
     */
    removeClass: function (className) {
      let classStr = element.getAttribute("class");
      if (!classStr) return this;
      let classList = classStr.trim().split(" ");
      let classNameList = className.trim().split(" ");
      let resultClassList = classList.filter(
        (value) => !classNameList.includes(value),
      );
      let result = resultClassList.join(" ").trim();
      element.setAttribute("class", result);
      return this;
    },
  };
}
 ^Zx4RknSs

First Attempt ^izqIPivy

Optimize and modularizze the. code next ^hmIbXNVL

- If we observe the addClass and removeClass are ideally the subset of ToggleClass method with particular value of 
`state` as boolean value. ^XU0fhfZN

toggleClass ^GrmaILf6

add ^WZlJ8rkX

remove ^joN177oR

function classNameTokenSet(className) {
    return new Set(className.trim().split(/\s+/))
} ^AkfffA8m

classNameTokenSet("foo bar baz")
// Set { "foo", "bar", "baz" }

classNameTokenSet("  foo   bar  ")
// Set { "foo", "bar" }  ← extra spaces handled by \s+

classNameTokenSet("foo foo bar")
// Set { "foo", "bar" }  ← duplicate removed automatically ^mWFOx67W

function classNameTokenSet(className) {
  return new Set(className.trim().split(/\s+/));
}

export default function $(selector) {
  const element = document.querySelector(selector);

  return {
    toggleClass: function (className, state) {
      if (element == null) return this;
      const classes = classNameTokenSet(className);
      const elementClasses = classNameTokenSet(element.className);
      classes.forEach((cls) => {
        const shouldRemove =
          state === undefined ? elementClasses.has(cls) : !state;
        shouldRemove ? elementClasses.delete(cls) : elementClasses.add(cls);
      });

      element.className = Array.from(elementClasses).join(" ");
      return this;
    },

    addClass: function (className) {
      this.toggleClass(className, true);
      return this;
    },

    removeClass: function (className) {
      this.toggleClass(className, false);
      return this;
    },
  };
}
 ^Ft9s382x

Things we improved 
1. modularity by using sets to remove duplicate code 
2. Handle whitespace in a better way. ^bfBm1ILV

%%
## Drawing
```compressed-json
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
```
%%