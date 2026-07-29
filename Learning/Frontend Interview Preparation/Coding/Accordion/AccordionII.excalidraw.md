---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
import { useState, useId } from "react";

export default function Accordion({ sections }) {
  const [openSections, setOpenSections] = useState(new Set());
  const id = useId();
  const getUniqueId = (id, label, type) => {
    return `${id}-${type}-${label}`;
  };
  return (
    <div className="accordion">
      {sections.map(({ value, title, contents }) => {
        const isExpanded = openSections.has(value);

        return (
          <div className="accordion-item" key={value}>
            <h3>
              <button
                id={getUniqueId(id, value, "button")}
                className="accordion-item-title"
                type="button"
                aria-expanded={isExpanded}
                aria-controls={getUniqueId(id, value, "panel")}
                onClick={() => {
                  const newOpenSections = new Set(openSections);
                  newOpenSections.has(value)
                    ? newOpenSections.delete(value)
                    : newOpenSections.add(value);
                  setOpenSections(newOpenSections);
                }}
              >
                {title}
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
            </h3>
            <div
              id={getUniqueId(id, value, "panel")}
              className="accordion-item-contents"
              role="region"
              hidden={!isExpanded}
              aria-labelledby={getUniqueId(id, value, "button")}
            >
              {contents}
            </div>
          </div>
        );
      })}
    </div>
  );
}
 ^GglYEQQl

Accordion.js ^rRAa8DVV

%%
## Drawing
```compressed-json
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
```
%%