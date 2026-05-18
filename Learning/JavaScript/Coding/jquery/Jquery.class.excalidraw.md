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

%%
## Drawing
```compressed-json
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=
```
%%