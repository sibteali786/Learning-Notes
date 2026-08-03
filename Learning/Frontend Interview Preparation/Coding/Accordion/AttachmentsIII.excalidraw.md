---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
import { useId, useState, useRef } from "react";

function getAccordionHeaderId(accordionId, value) {
  return accordionId + "-header-" + value;
}

function getAccordionPanelId(accordionId, value) {
  return accordionId + "-panel-" + value;
}

export default function Accordion({ sections }) {
  const accordionId = useId();
  const [openSections, setOpenSections] = useState(new Set());
  const refs = useRef([]);
  const handleFocus = (event) => {
    if (event.target.type === "button") {
      console.log("focus", event.target);
    }
  };
  const handleKeyDown = (event, value) => {
    if (event.target.type === "button") {
      const currentIndex = sections.findIndex(
        (section) => section.value === value,
      );
      let nextIndex = null;
      let e = null;
      switch (event.key) {
        case "ArrowDown":
          event.preventDefault();
          nextIndex = (currentIndex + 1) % sections.length;
          break;
        case "ArrowUp":
          event.preventDefault();
          nextIndex = (currentIndex - 1 + sections.length) % sections.length;
          break;
        case "Home":
          event.preventDefault();
          nextIndex = 0;
          break;
        case "End":
          event.preventDefault();
          nextIndex = sections.length - 1;
          break;
        default:
          break;
      }
      refs.current[nextIndex]?.focus()
    }
  };
  return (
    <div className="accordion">
      {sections.map(({ value, title, contents }, index) => {
        const isExpanded = openSections.has(value);
        const headerId = getAccordionHeaderId(accordionId, value);
        const panelId = getAccordionPanelId(accordionId, value);
        return (
          <div
            className="accordion-item"
            key={value}
            onFocus={handleFocus}
            onKeyDown={(e) => handleKeyDown(e, value)}
          >
            <button
              aria-controls={panelId}
              aria-expanded={isExpanded}
              id={headerId}
              className="accordion-item-title"
              type="button"
              ref={(el) => (refs.current[index] = el)}
              onClick={() => {
                const newOpenSections = new Set(openSections);
                newOpenSections.has(value)
                  ? newOpenSections.delete(value)
                  : newOpenSections.add(value);
                setOpenSections(newOpenSections);
              }}
            >
              {title}{" "}
              <span
                aria-hidden={true}
                className={[
                  "accordion-icon",
                  isExpanded && "accordion-icon--rotated",
                ]
                  .filter(Boolean)
                  .join(" ")}
              />
            </button>
            <div
              aria-labelledby={headerId}
              role="region"
              className="accordion-item-contents"
              id={panelId}
              hidden={!isExpanded}
            >
              {contents}
            </div>
          </div>
        );
      })}
    </div>
  );
}
 ^SMIaeodK

Improved Version ^CTY67QPT

import { useId, useState, useRef } from "react";

function getAccordionHeaderId(accordionId, value) {
  return accordionId + "-header-" + value;
}

function getAccordionPanelId(accordionId, value) {
  return accordionId + "-panel-" + value;
}

export default function Accordion({ sections }) {
  const accordionId = useId();
  const [openSections, setOpenSections] = useState(new Set());
  const refs = useRef([]);
  const handleFocus = (event) => {
    if (event.target.type === "button") {
      console.log("focus", event.target);
    }
  };
  const handleKeyDown = (event) => {
    if (event.target.type === "button") {
      const value = event.target.dataset.accordionValue
      const currentIndex = sections.findIndex(
        (section) => section.value === value,
      );
      let nextIndex = null;
      let e = null;
      switch (event.key) {
        case "ArrowDown":
          event.preventDefault();
          nextIndex = (currentIndex + 1) % sections.length;
          break;
        case "ArrowUp":
          event.preventDefault();
          nextIndex = (currentIndex - 1 + sections.length) % sections.length;
          break;
        case "Home":
          event.preventDefault();
          nextIndex = 0;
          break;
        case "End":
          event.preventDefault();
          nextIndex = sections.length - 1;
          break;
        default:
          break;
      }
      refs.current[nextIndex]?.focus();
    }
  };
  return (
    <div className="accordion" onKeyDown={(e) => handleKeyDown(e)}>
      {sections.map(({ value, title, contents }, index) => {
        const isExpanded = openSections.has(value);
        const headerId = getAccordionHeaderId(accordionId, value);
        const panelId = getAccordionPanelId(accordionId, value);
        return (
          <div className="accordion-item" key={value} onFocus={handleFocus}>
            <button
              aria-controls={panelId}
              aria-expanded={isExpanded}
              id={headerId}
              className="accordion-item-title"
              data-accordion-value ={value}
              type="button"
              ref={(el) => (refs.current[index] = el)}
              onClick={() => {
                const newOpenSections = new Set(openSections);
                newOpenSections.has(value)
                  ? newOpenSections.delete(value)
                  : newOpenSections.add(value);
                setOpenSections(newOpenSections);
              }}
            >
              {title}{" "}
              <span
                aria-hidden={true}
                className={[
                  "accordion-icon",
                  isExpanded && "accordion-icon--rotated",
                ]
                  .filter(Boolean)
                  .join(" ")}
              />
            </button>
            <div
              aria-labelledby={headerId}
              role="region"
              className="accordion-item-contents"
              id={panelId}
              hidden={!isExpanded}
            >
              {contents}
            </div>
          </div>
        );
      })}
    </div>
  );
}
 ^hE6iDOBa

%%
## Drawing
```compressed-json
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
```
%%