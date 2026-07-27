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