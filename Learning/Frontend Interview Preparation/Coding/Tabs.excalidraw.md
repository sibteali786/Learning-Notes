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

%%
## Drawing
```compressed-json
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
```
%%