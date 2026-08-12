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
```
%%