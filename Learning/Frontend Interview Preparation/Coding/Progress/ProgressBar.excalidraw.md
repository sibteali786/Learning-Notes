---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
App.jsx
import { useState, useEffect } from "react";
export default function App() {
  const [bars, setBars] = useState([]);

  const handleClick = () => {
    const newBar = { id: crypto.randomUUID(), started: false };
    setBars((prevBars) => [...prevBars, newBar]);
  };
  return (
    <div className="container">
      <button onClick={handleClick}>Add</button>
      {bars.map((bar) => (
        <Progress key={bar.id} id={bar.id} />
      ))}
    </div>
  );
}

function Progress({ id }) {
  const [started, setStarted] = useState(false);
  useEffect(() => {
    requestAnimationFrame(() => {
      requestAnimationFrame(() => {
        if (!started) {
          setStarted(true);
        }
      });
    });
  }, []);
  return (
    <div className="progress-wrapper">
      <div className="progress" style={{ width: started ? "100%" : "0" }}></div>
    </div>
  );
}

styles.css

body {
  font-family: sans-serif;
}

.container {
  display: flex;
  flex-direction: column;
  gap: 5px;
  align-items: flex-start;
}

.progress-wrapper {
  width: 100%;
  height: 12px;
  border: 1px solid black;
}

.progress {
  height: 100%;
  background-color: orangered;
  transition: all 2s ease-in;
}
 ^UriFK4Om

Progress.jsx
import { useEffect, useState } from 'react';

function ProgressBar() {
  const [startTransition, setStartTransition] = useState(false);

  // Start transition after first render and never
  // apply this effect ever again.
  useEffect(() => {
    if (startTransition) {
      return;
    }

    setStartTransition(true);
  });

  return (
    <div className="bar">
      <div
        className={['bar-contents', startTransition && 'bar-contents--filled']
          .filter(Boolean)
          .join(' ')}
      />
    </div>
  );
}

export default function App() {
  const [bars, setBars] = useState(0);

  return (
    <div className="wrapper">
      <div>
        <button
          onClick={() => {
            setBars(bars + 1);
          }}>
          Add
        </button>
      </div>
      <div className="bars">
        {Array(bars)
          .fill(null)
          .map((_, index) => (
            <ProgressBar key={index} />
          ))}
      </div>
    </div>
  );
}


style.css
body {
  font-family: sans-serif;
}

.wrapper {
  display: flex;
  flex-direction: column;
  gap: 16px;
  justify-content: center;
}

.bars {
  display: flex;
  flex-direction: column;
  row-gap: 8px;
}

.bar {
  background-color: #ccc;
  height: 8px;
}

.bar-contents {
  background-color: green;
  height: 100%;
  transform: scaleX(0);
  transform-origin: left;
  transition-duration: 2000ms;
  transition-property: transform;
  transition-timing-function: linear;
}

.bar-contents--filled {
  transform: scaleX(1);
}
 ^GwfsYbAY

%%
## Drawing
```compressed-json
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
```
%%