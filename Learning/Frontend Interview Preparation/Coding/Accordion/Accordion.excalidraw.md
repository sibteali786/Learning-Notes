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