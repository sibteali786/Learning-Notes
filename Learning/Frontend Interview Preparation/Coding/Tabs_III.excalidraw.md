---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
import { useId, useState, useRef } from "react";

function getTabListItemId(tabsId, value) { 
  return tabsId + "-tab-" + value;
}

function getTabPanelId(tabsId, value) {
  return tabsId + "-tabpanel-" + value; 
}

export default function Tabs({ defaultValue, items }) {
  const tabsId = useId();
  const [value, setValue] = useState(defaultValue ?? items[0].value );
  const refs = useRef([]);
  const handleFocus = (event) => {
    if (event.target.type === "button") {
      const computedIndex = refs.current.findIndex(
        (ref) => ref === event.target,
      );
      setValue(items[computedIndex].value);
    }
  };
  const handleOnKeyDown = (event) => {
    const currentIndex = refs.current.findIndex((ref) => ref.tabIndex === 0);
    if (event.target.type === "button") {
      if (event.key === "ArrowLeft") {
        event.preventDefault();
        const computed = (currentIndex - 1 + items.length) % items.length;
        refs.current[computed].focus();
      } else if (event.key === "ArrowRight") {
        event.preventDefault();
        const computed = (currentIndex + 1) % items.length;
        refs.current[computed].focus();
      } else if (event.key === "Home") {
        event.preventDefault();
        refs.current[0].focus();
      } else if (event.key === "End") {
        event.preventDefault();
        refs.current[items.length - 1].focus();
      }
    }
  };
  return (
    <div className="tabs">
      <div
        className="tabs-list"
        role="tablist"
        onFocus={handleFocus}
        onKeyDown={handleOnKeyDown}
      >
        {items.map(({ label, value: itemValue }, index) => {
          const isActiveValue = itemValue === value;

          return (
            <button
              id={getTabListItemId(tabsId, itemValue)}
              key={itemValue}
              ref={(el) => (refs.current[index] = el)}
              tabIndex={isActiveValue ? 0 : -1}
              type="button"
              className={[
                "tabs-list-item",
                isActiveValue && "tabs-list-item--active",
              ]
                .filter(Boolean)
                .join(" ")}
              role="tab"
              aria-controls={getTabPanelId(tabsId, itemValue)}
              aria-selected={isActiveValue}
            >
              {label}
            </button>
          );
        })}
      </div>
      <div>
        {items.map(({ panel, value: itemValue }) => (
          <div
            key={itemValue}
            tabIndex={0}
            id={getTabPanelId(tabsId, itemValue)}
            aria-labelledby={getTabListItemId(tabsId, itemValue)}
            role="tabpanel"
            hidden={itemValue !== value}
          >
            {panel}
          </div>
        ))}
      </div>
    </div>
  );
}
 ^gzEMD3S7

%%
## Drawing
```compressed-json
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
```
%%