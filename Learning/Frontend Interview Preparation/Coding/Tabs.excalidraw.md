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
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

GslwAc2WsUxDAhRNh4oIAA==
```
%%