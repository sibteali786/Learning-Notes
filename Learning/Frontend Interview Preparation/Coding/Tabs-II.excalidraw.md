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