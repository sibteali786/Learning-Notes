---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
First Attempt ( Probably Worst )  ^vTW11NLk

export default function Tabs() {
  const handleTabToggle = (event) => {
    const paras = document.querySelector(".paragraphs")
    const paragraphGrp = paras.querySelectorAll("[id^=tab-]");
    paragraphGrp.forEach((p) => {
      if (event.target.id === p.id){
        p.classList.remove("inactive")
      }else{
        p.classList.add("inactive")
      }
    });
    const btnGrp = document.querySelector("#btn-grp")
    const btns = btnGrp.querySelectorAll("button")
    btns.forEach(btn => {
      if (event.target.id === btn.id){
        btn.classList.add("active-btn")
      }else{
        btn.classList.remove("active-btn")
      }
    })
  };
  return (
    <div>
      <div id="btn-grp">
        <button className="active-btn" onClick={handleTabToggle} id="tab-1">
          HTML
        </button>
        <button onClick={handleTabToggle} id="tab-2">
          CSS
        </button>
        <button onClick={handleTabToggle} id="tab-3">
          {" "}
          JavaScript
        </button>
      </div>
      <div className="paragraphs">
        <p id="tab-1">
          The HyperText Markup Language or HTML is the standard markup language
          for documents designed to be displayed in a web browser.
        </p>
        <p className="inactive" id="tab-2">
          Cascading Style Sheets is a style sheet language used for describing
          the presentation of a document written in a markup language such as
          HTML or XML.
        </p>
        <p className="inactive" id="tab-3">
          JavaScript, often abbreviated as JS, is a programming language that is
          one of the core technologies of the World Wide Web, alongside HTML and
          CSS.
        </p>
      </div>
    </div>
  );
}
 ^Bp1oNdoD

Issues
- Direct DOM manipulation not through react ^E0RVo1B9

Second Attempt ^afp3BIKt

- Using react to manage state ( Virtual DOM ) ^NR4nmuIM

import { useState } from "react";
export default function Tabs() {
  const [activeTab, setActiveTab] = useState("tab-1")
  const btnNames = ["HTML", "CSS", "Javascript"]
  const tabIds = ["tab-1", "tab-2", "tab-3"]
  return (
    <div>
      <div id="btn-grp">
        {tabIds.map((id, idx) => (
          <button
            key={idx}
            className={activeTab === id ? "active-btn" : ""}
            onClick={() => setActiveTab(id)}
          >
            {btnNames[idx]}
          </button>
        ))}
      </div>
      <div className="paragraphs">
        {activeTab === "tab-1" && <p id="tab-1">
          The HyperText Markup Language or HTML is the standard markup language
          for documents designed to be displayed in a web browser.
        </p>}

        {activeTab === "tab-2" && <p id="tab-2">
          Cascading Style Sheets is a style sheet language used for describing
          the presentation of a document written in a markup language such as
          HTML or XML.
        </p>}
        {activeTab === "tab-3" && <p id="tab-3">
          JavaScript, often abbreviated as JS, is a programming language that is
          one of the core technologies of the World Wide Web, alongside HTML and
          CSS.
        </p>}
      </div>
    </div>
  );
}
 ^JsInlRJD

body {
  font-family: sans-serif;
}

.active-btn {
  padding: 4px 6px;
  background-color: blueviolet;
  color: white;
  border: none;
  border-radius: 4px;
}

#btn-grp {
  display: flex;
  gap: 4px
} ^ZH5UQusQ

Essential UX/a11y improvements (bonus-credit territory)

- ARIA roles — this is the big one interviewers look for: role="tablist" on the button group, role="tab" + aria-selected on buttons, role="tabpanel" on content, aria-controls/id linking tab↔panel.

-Keyboard navigation — Arrow keys to move between tabs (not just Tab+Enter), per WAI-ARIA Tabs pattern.

- Panel tabIndex={0} so screen reader / keyboard users can focus panel content directly.

- aria-labelledby on panel pointing to its tab.

- Avoid conditionally unmounting content if it's expensive to reconstruct (forms, video) — consider hidden attribute instead of unmounting, to preserve state. ^zVheg4Br

Solution  ^MhpAGRlJ

App.js

import Tabs from "./Tabs";

export default function App() {
  return (
    <div className="wrapper">
      <Tabs
        items={[
          {
            value: "html",
            label: "HTML",
            panel:
              "The HyperText Markup Language or HTML is the standard markup language for documents designed to be displayed in a web browser.",
          },
          {
            value: "css",
            label: "CSS",
            panel:
              "Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML or XML",
          },
          {
            value: "javascript",
            label: "JavaScript",
            panel:
              "JavaScript, often abbreviated as JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.",
          },
        ]}
      />
    </div>
  );
}
 ^PcHVHvzX

Tabs.js

import { useState } from "react";
export default function Tabs({ defaultValue, items }) {
  const [value, setValue] = useState(defaultValue ?? items[0].value);
  return (
    <div className="tabs">
      <div className="tabs-list">
        {items.map(({ label, value: itemValue }) => {
          const isActive = itemValue === value;
          return (
            <button
              key={itemValue}
              type="button"
              className={[
                "tabs-list-item",
                isActive && "tabs-list-item--active",
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
        {items.map(({ panel, value: itemValue }) => (
          <div key={itemValue} hidden={itemValue !== value}>
            {panel}
          </div>
        ))}
      </div>
    </div>
  );
}
 ^TOE3bf1d

styles.css

body {
  font-family: sans-serif;
}

.wrapper {
  align-items: center;
  display: flex;
}

.tabs {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.tabs-list {
  display: flex;
  gap: 6px;
}

.tabs-list-item {
  --active-color: blueviolet;
  background: none;
  border: 1px solid #000;
  border-radius: 4px;
  cursor: pointer;
  padding: 6px 10px;
}

.tabs-list-item:hover {
  border-color: var(--active-color);
  color: var(--acitve-color);
}

.tabs-list-item--active,
.tabs-list-item--active:hover {
  border-color: var(--active-color);
  background-color: var(--active-color);
  color: #fff;
}
 ^iWekNkn8

Why its better  ^PfxqlEIs

- Modular 
- Extendable easily
- follows dry principle
- consistent css classes name
- reusability in Css classes using variables
- better state management
- better class management ^fgURtLuY

%%
## Drawing
```compressed-json
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=
```
%%