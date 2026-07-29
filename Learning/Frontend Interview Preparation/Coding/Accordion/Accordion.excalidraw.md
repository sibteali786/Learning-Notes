---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
Accordion ^sF5oglTt

My Attempt ^UVridq8I

import { useState, useId, useEffect } from "react";

export default function Accordion({ items }) {
  const [ids, setIds] = useState(new Set());
  const accordionId = useId();
  const getUniqueId = (id, label, type) => {
    return `${accordionId}-${type}-${label}`;
  };
  const hanldeClick = (id) => {
    setIds((prevSet) => {
      const newSet = new Set([...prevSet]);
      if (newSet.has(id)) {
        newSet.delete(id);
        return newSet;
      } else {
        newSet.add(id);
        return newSet;
      }
    });
  };
  return (
    <div className="wrapper">
      {items.map(({ label, content }) => {
        const isExpanded = ids.has(getUniqueId(accordionId, "trigger", label));
        const buttonId = getUniqueId(accordionId, "trigger", label);
        return (
          <div
            className="accordion"
            key={getUniqueId(accordionId, "accordion", label)}
          >
            <button
              type="button"
              id={buttonId}
              className="accordion-trigger"
              onClick={() => hanldeClick(buttonId)}
            >
              {label}
              <span aria-hidden={true} className="accordion-icon" />
            </button>
            <p
              className={
                isExpanded
                  ? "accordion-panel-active"
                  : "accordion-panel-inactive"
              }
            >
              {content}
            </p>
          </div>
        );
      })}
    </div>
  );
}
 ^PJu5AlxG

Official Solution ^4uuQdWIm

Accordion.js

export default function Accordion({ sections }) {
  const [openSections, setOpenSections] = useState(new Set());

  return (
    <div className="accordion">
      {sections.map(({ value, title, contents }) => {
        const isExpanded = openSections.has(value);

        return (
          <div className="accordion-item" key={value}>
            <button
              className="accordion-item-title"
              type="button"
              onClick={() => {
                const newOpenSections = new Set(openSections);
                newOpenSections.has(value)
                  ? newOpenSections.delete(value)
                  : newOpenSections.add(value);
                setOpenSections(newOpenSections);
              }}>
              {title}
              <span
                aria-hidden={true}
                className={[
                  'accordion-icon',
                  isExpanded && 'accordion-icon--rotated',
                ]
                  .filter(Boolean)
                  .join(' ')}
              />
            </button>
            <div className="accordion-item-contents" hidden={!isExpanded}>
              {contents}
            </div>
          </div>
        );
      })}
    </div>
  );
} ^cq9zsWUp

App.js

import Accordion from './Accordion';

export default function App() {
  return (
    <div className="wrapper">
      <Accordion
        sections={[
          {
            value: 'html',
            title: 'HTML',
            contents:
              'The HyperText Markup Language or HTML is the standard markup language for documents designed to be displayed in a web browser.',
          },
          {
            value: 'css',
            title: 'CSS',
            contents:
              'Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a markup language such as HTML or XML.',
          },
          {
            value: 'javascript',
            title: 'JavaScript',
            contents:
              'JavaScript, often abbreviated as JS, is a programming language that is one of the core technologies of the World Wide Web, alongside HTML and CSS.',
          },
        ]}
      />
    </div>
  );
} ^ozpZteZW

Styles.css
body {
  font-family: sans-serif;
}

.wrapper {
  align-items: center;
  display: flex;
}

.accordion {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.accordion-item {
  display: flex;
  flex-direction: column;
  row-gap: 4px;
  padding: 4px 0;
}

.accordion-item:not(:first-child) {
  border-top: 1px solid #eee;
}

.accordion-item-title {
  align-items: center;
  border: none;
  background: none;
  cursor: pointer;
  font-weight: 500;
  padding: 4px;
  justify-content: space-between;
  text-align: start;
  display: flex;
}

.accordion-item-title:hover {
  background-color: #eee;
}

.accordion-icon {
  border: solid currentcolor;
  border-width: 0 2px 2px 0;
  display: inline-block;
  height: 8px;
  pointer-events: none;
  transform: translateY(-2px) rotate(45deg);
  width: 8px;
}

.accordion-icon--rotated {
  transform: translateY(2px) rotate(-135deg);
}

.accordion-item-contents {
  font-size: 14px;
  line-height: 1.2em;
  padding: 4px;
} ^99MJ1g0Z

styles.css
body {
  font-family: sans-serif;
}

.accordion-icon {
  border: solid currentcolor;
  border-width: 0 2px 2px 0;
  display: inline-block;
  height: 8px;
  pointer-events: none;
  transform: translateY(-2px) rotate(45deg);
  width: 8px;
}

.accordion-icon--rotated {
  transform: translateY(2px) rotate(-135deg);
}

.accordion {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.accordion-item {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.accordion-trigger {
  display: flex;
  justify-content: space-between;
  align-content: center;
  border: none;
  cursor: pointer;
  gap: 6px;
}

.accordion-trigger:hover {
  background-color: #eee;
}

.accordion-item-content {
  font-size: 14px;
}

.accordion-panel-inactive {
  display: none;
}

.accordion-panel-active {
  display: block;
}
 ^GAvo89us

%%
## Drawing
```compressed-json
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
```
%%