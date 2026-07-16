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