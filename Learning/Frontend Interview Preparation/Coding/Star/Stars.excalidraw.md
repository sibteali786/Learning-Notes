---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
import { useState } from "react";
export default function StarRating({ maxStars, filledCount, onRatingChange }) {
  const [hoverIndex, setHoverIndex] = useState(null);
  const handleHover = (e) => {
    if (e.target.closest("[data-star-value]")) {
      const hoveredIndex = Number(e.target.dataset.starValue);
      setHoverIndex(hoveredIndex);
    }
  };
  const handleMouseLeave = () => {
    setHoverIndex(null);
  };
  const handleClick = (e) => {
    if (e.target.closest("[data-star-value]")) {
      onRatingChange(hoverIndex);
    }
  };
  let filled = hoverIndex === null ? filledCount : hoverIndex + 1;
  return (
    <div
      onMouseOver={handleHover}
      onMouseLeave={handleMouseLeave}
      onClick={handleClick}
    >
      {Array(maxStars)
        .fill(null)
        .map((value, index) => {
          if (filled > 0) {
            filled--;
            return (
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="star-icon star-icon-filled"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                strokeWidth="2"
                data-star-value={index}
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"
                />
              </svg>
            );
          }
          return (
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="star-icon"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              strokeWidth="2"
              data-star-value={index}
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"
              />
            </svg>
          );
        })}
    </div>
  );
}

body {
  font-family: sans-serif;
}
.star-icon {
  --icon-size: 32px;

  cursor: pointer;
  height: var(--icon-size);
  width: var(--icon-size);
}

.star-icon path {
  pointer-events: none;
}
.star-icon-filled {
  fill: yellow;
}


import StarRating from "./StarRating";
import { useState } from "react";

export default function App() {
  const [filled, setFilled] = useState(1);
  const handleRateChange = (index) => {
    console.log("Clicked", index);
    setFilled(index + 1);
  };
  return (
    <div>
      <StarRating
        maxStars={5}
        filledCount={filled}
        onRatingChange={handleRateChange}
      />
    </div>
  );
}
 ^qPExd995

My Attempt ^AcWRXVDM

Offocial and it works consistently ^T7I6kr8t

import { useState } from 'react';

function Star({ filled }) {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      className={['star-icon', filled ? 'star-icon-filled' : ''].join(' ')}
      fill="none"
      viewBox="0 0 24 24"
      stroke="currentColor"
      strokeWidth="2">
      <path
        strokeLinecap="round"
        strokeLinejoin="round"
        d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"
      />
    </svg>
  );
}

export default function StarRating({ value, max, onChange }) {
  const [hoveredIndex, setHoveredIndex] = useState(null);

  return (
    <div>
      {Array.from({ length: max }).map((_, index) => (
        <span
          key={index}
          tabIndex={0}
          onMouseEnter={() => setHoveredIndex(index)}
          onMouseLeave={() => setHoveredIndex(null)}
          onClick={() => onChange(index + 1)}>
          <Star
            filled={
              hoveredIndex != null ? index <= hoveredIndex : index < value
            }
          />
        </span>
      ))}
    </div>
  );
}
 ^E6GWF4Js

import { useState } from 'react';

import StarRating from './StarRating';

export default function App() {
  const [rating, setRating] = useState(3);

  return (
    <div>
      <StarRating max={5} value={rating} onChange={setRating} />
    </div>
  );
}
 ^c5XMJVOh

%%
## Drawing
```compressed-json
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

bwS0bIEIBI7gByOkAYOOEBOU/gQAP4IAA===
```
%%