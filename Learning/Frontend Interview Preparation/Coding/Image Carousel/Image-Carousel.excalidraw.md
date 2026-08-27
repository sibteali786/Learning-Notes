---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
import { useState } from "react";

export default function ImageCarousel({
  images,
}: Readonly<{
  images: ReadonlyArray<{ src: string; alt: string }>;
}>) {
  const [imgIdx, setImgIdx] = useState(0);
  const goToNext = () => {
    const nextIndex = (imgIdx + 1) % images.length;
    setImgIdx(nextIndex);
  };
  const goToPrev = () => {
    const nextIndex = (imgIdx - 1 + images.length) % images.length;
    setImgIdx(nextIndex);
  };
  return (
    <div
      className="wrapper"
      role="region"
      aria-aria-roledescription="carousel"
      aria-label="Image carousel"
    >
      <button
        onClick={goToNext}
        type="button"
        className="next-btn"
        aria-label="Next image"
      >
        Next
      </button>
      <img
        key={images[imgIdx].src}
        alt={images[imgIdx].alt}
        src={images[imgIdx].src}
        width="100%"
        aria-live="polite"
      />
      <button
        onClick={goToPrev}
        type="button"
        className="prev-btn"
        aria-label="Prev image"
      >
        Prev
      </button>
      <div className="n-btn-wrapper">
        {Array(images.length)
          .fill(0)
          .map((_, idx) => (
            <button
              key={idx}
              onClick={() => setImgIdx(idx)}
              className={idx === imgIdx ? "btn-noval--active" : "btn-noval"}
              aria-lable={`Go to image ${idx + 1} of ${images.length}`}
              aria-current={idx === imgIdx ? true : false}
            ></button>
          ))}
      </div>
      <span
        aria-live="polite"
        style={{
          whiteSpace: "nowrap",
        }}
      >
        {`Showing image ${imgIdx + 1} of ${images.length}: ${images[imgIdx].alt}`}
      </span>
    </div>
  );
}
 ^pCa57KsI

Styles.css

body {
  font-family: sans-serif;
}

.wrapper {
  position: relative;
  margin: auto;
  background-color: black;
  max-width: 600px;
  max-height: 400px;
  height: 400px;
}

.prev-btn {
  position: absolute;
  bottom: 50%;
  left: 4%;
}
.next-btn {
  position: absolute;
  bottom: 50%;
  right: 4%;
}

.btn-noval {
  height: 10px;
  width: 10px;
  border-radius: 50%;
  border: none;
  background-color: gray;
}

.btn-noval--active {
  height: 10px;
  width: 10px;
  border-radius: 50%;
  border: none;
  background-color: white;
}
.btn-noval,
.btn-noval:focus {
  cursor: pointer;
}

.n-btn-wrapper {
  position: absolute;
  bottom: 5%;
  left: 50%;
  background-color: rgba(133, 126, 126, 0.702);
  padding: 8px;
  display: flex;
  gap: 4px;
  width: fit-content;
  border-radius: 16px;
  transform: translate(-50%);
}

img {
  object-fit: contain;
  width: 100%;
  height: 100%;
}
 ^OVoHqnTi

Official Solution ^FGZ0zwg4

import { useState } from 'react';

function clsx(...classnames: Array<any>) {
  return classnames.filter(Boolean).join(' ');
}

export default function ImageCarousel({
  images,
}: Readonly<{
  images: ReadonlyArray<{ src: string; alt: string }>;
}>) {
  const [currIndex, setCurrIndex] = useState(0);
  const currImage = images[currIndex];

  return (
    <div className="image-carousel">
      <img
        alt={currImage.alt}
        src={currImage.src}
        key={currImage.src}
        className="image-carousel__image"
      />
      <button
        aria-label="Previous image"
        className="image-carousel__button image-carousel__button--prev"
        onClick={() => {
          const nextIndex = (currIndex - 1 + images.length) % images.length;
          setCurrIndex(nextIndex);
        }}>
        &#10094;
      </button>
      <div className="image-carousel__pages">
        {images.map(({ alt, src }, index) => (
          <button
            className={clsx(
              'image-carousel__pages__button',
              index === currIndex && 'image-carousel__pages__button--active',
            )}
            aria-label={`Navigate to ${alt}`}
            key={src}
            onClick={() => {
              setCurrIndex(index);
            }}
          />
        ))}
      </div>
      <button
        aria-label="Next image"
        className="image-carousel__button image-carousel__button--next"
        onClick={() => {
          const nextIndex = (currIndex + 1) % images.length;
          setCurrIndex(nextIndex);
        }}>
        &#10095;
      </button>
    </div>
  );
}
 ^uvcyeuTK

style.css

* {
  box-sizing: border-box;
  margin: 0;
}

body {
  font-family: sans-serif;
}

.wrapper {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  height: 100vh;
  width: 100vw;
}

.image-carousel {
  background-color: #000;
  height: 400px;
  overflow: hidden;
  width: min(600px, 100vw);
  position: relative;
}

.image-carousel__image {
  object-fit: contain;
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
}

.image-carousel__button {
  --size: 40px;
  height: var(--size);
  width: var(--size);

  background-color: #0008;
  border-radius: 100%;
  border: none;
  color: #fff;
  cursor: pointer;

  position: absolute;
  top: 50%;
  transform: translateY(-50%);
}

.image-carousel__button:hover {
  background-color: #000b;
}

.image-carousel__button--prev {
  left: 16px;
}

.image-carousel__button--next {
  right: 16px;
}

.image-carousel__pages {
  background-color: #0008;
  border-radius: 12px;
  display: inline-flex;
  gap: 8px;
  padding: 8px;

  position: absolute;
  bottom: 24px;
  left: 50%;
  transform: translateX(-50%);
}

.image-carousel__pages__button {
  --size: 8px;
  height: var(--size);
  width: var(--size);

  border: none;
  border-radius: 100%;
  background-color: #666;
  cursor: pointer;
  display: inline-block;
  flex-shrink: 0;
  padding: 0;
  transition: background-color 0.3s ease-in-out;
}

.image-carousel__pages__button:hover {
  background-color: #ccc;
}

.image-carousel__pages__button--active {
  background-color: #fff;
}
 ^g5KLfAdu

%%
## Drawing
```compressed-json
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
```
%%