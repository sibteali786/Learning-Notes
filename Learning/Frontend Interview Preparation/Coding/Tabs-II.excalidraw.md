---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
My Attempt ^Swoqhh9Z

import { useState, useId } from "react";

export default function Tabs({ defaultValue, items }) {
  const [value, setValue] = useState(defaultValue ?? items[0].value);
  const id = useId()
  return (
    <div className="tabs">
      <div className="tabs-list" role="tablist">
        {items.map(({ label, value: itemValue }, index) => {
          const isActiveValue = itemValue === value;

          return (
            <button
              id={`tab-${index}-${itemValue}-${id}`}
              key={itemValue}
              role="tab"
              aria-controls={`panel-${index}-${itemValue}-${id}`}
              type="button"
              aria-selected={isActiveValue ? true : false}
              className={[
                "tabs-list-item",
                isActiveValue && "tabs-list-item--active",
              ]
                .filter(Boolean)
                .join(" ")}
              onClick={() => {
                setValue(itemValue);
              }}
            >
              {label}
            </button>
          );
        })}
      </div>
      <div>
        {items.map(({ panel, value: itemValue }, index) => (
          <div
            id={`panel-${index}-${itemValue}-${id}`}
            aria-labelledby={`tab-${index}-${itemValue}-${id}`}
            key={itemValue}
            hidden={itemValue !== value}
            role="tabpanel"
          >
            {panel}
          </div>
        ))}
      </div>
    </div>
  );
}
 ^RamdJtdM

Tabs.js ^6Q9MeA8e

Official Solution ^07tXKhrZ

import { useId, useState } from 'react';

function getTabListItemId(tabsId, value) {
  return tabsId + '-tab-' + value;
}

function getTabPanelId(tabsId, value) {
  return tabsId + '-tabpanel-' + value;
}

export default function Tabs({ defaultValue, items }) {
  const tabsId = useId();
  const [value, setValue] = useState(defaultValue ?? items[0].value);

  return (
    <div className="tabs">
      <div className="tabs-list" role="tablist">
        {items.map(({ label, value: itemValue }) => {
          const isActiveValue = itemValue === value;

          return (
            <button
              id={getTabListItemId(tabsId, itemValue)}
              key={itemValue}
              type="button"
              className={[
                'tabs-list-item',
                isActiveValue && 'tabs-list-item--active',
              ]
                .filter(Boolean)
                .join(' ')}
              onClick={() => {
                setValue(itemValue);
              }}
              role="tab"
              aria-controls={getTabPanelId(tabsId, itemValue)}
              aria-selected={isActiveValue}>
              {label}
            </button>
          );
        })}
      </div>
      <div>
        {items.map(({ panel, value: itemValue }) => (
          <div
            key={itemValue}
            id={getTabPanelId(tabsId, itemValue)}
            aria-labelledby={getTabListItemId(tabsId, itemValue)}
            role="tabpanel"
            hidden={itemValue !== value}>
            {panel}
          </div>
        ))}
      </div>
    </div>
  );
} ^yjXtbfLF

%%
## Drawing
```compressed-json
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
```
%%