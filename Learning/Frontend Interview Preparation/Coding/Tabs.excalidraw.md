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

%%
## Drawing
```compressed-json
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
```
%%