---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
ImageCarousel.jsx

import { useState, useRef, useLayoutEffect, useEffect } from "react";

export default function ImageCarousel({
  images,
}: Readonly<{
  images: ReadonlyArray<{ src: string; alt: string }>;
}>) {
  const [imgIdx, setImgIdx] = useState(0);
  const [isTransitioning, setIsTransitioning] = useState(false);
  const [frameWidth, setFrameWidth] = useState(0);
  const [skipTransition, setSkipTransition] = useState(false);
  const frameDom = useRef<HTMLDivElement>(null);
  const stripDom = useRef<HTMLDivElement>(null);

  useLayoutEffect(() => {
    const frame = frameDom.current;
    if (!frame) return;

    const updateWidth = () =>
      setFrameWidth(frame.getBoundingClientRect().width);
    updateWidth();

    const observer = new ResizeObserver(updateWidth);
    observer.observe(frame);
    return () => observer.disconnect();
  }, []);

  useEffect(() => {
    const strip = stripDom.current;
    if (!strip) return;

    const handleTransitionEnd = () => {
      setIsTransitioning(false);
      setSkipTransition(false);
    };
    strip.addEventListener("transitionend", handleTransitionEnd);
    return () =>
      strip.removeEventListener("transitionend", handleTransitionEnd);
  }, []);

  function navigateTo(nextIndex: number, isWrapping: boolean) {
    if (isTransitioning || nextIndex === imgIdx) return;
    setIsTransitioning(true);
    setSkipTransition(isWrapping);
    setImgIdx(nextIndex);

    if (isWrapping) {
      requestAnimationFrame(() => {
        requestAnimationFrame(() => setIsTransitioning(false));
      });
    }
  }
  const goToNext = () => {
    const isWrapping = imgIdx === images.length - 1;
    navigateTo((imgIdx + 1) % images.length, isWrapping);
  };
  const goToPrev = () => {
    const isWrapping = imgIdx === 0;
    navigateTo((imgIdx - 1 + images.length) % images.length, isWrapping);
  };
  const goToIndex = (idx: number) => {
    navigateTo(idx, false);
  };
  return (
    <div
      className="frame"
      ref={frameDom}
      role="region"
      aria-roledescription="carousel"
      aria-label="Image carousel"
    >
      <div
        className="strip"
        ref={stripDom}
        style={{
          transform: `translateX(-${imgIdx * frameWidth}px)`,
          transition: skipTransition ? "none" : "transform 0.3s ease-in-out",
        }}
      >
        {images.map((image) => (
          <img
            key={image.src}
            alt={image.alt}
            src={image.src}
            className="carousel-image"
            style={{ width: frameWidth }}
          />
        ))}
      </div>
      <button
        onClick={goToNext}
        type="button"
        className="next-btn"
        aria-label="Next image"
      >
        &#10095;
      </button>
      <button
        onClick={goToPrev}
        type="button"
        className="prev-btn"
        aria-label="Prev image"
      >
        &#10094;
      </button>
      <div className="n-btn-wrapper">
        {Array(images.length)
          .fill(0)
          .map((_, idx) => (
            <button
              key={images[idx].src}
              onClick={() => goToIndex(idx)}
              className={idx === imgIdx ? "btn-noval--active" : "btn-noval"}
              aria-label={`Go to image ${idx + 1} of ${images.length}`}
              aria-current={idx === imgIdx ? true : false}
            ></button>
          ))}
      </div>

      <span
        aria-live="polite"
        className="sr-only"
        style={{
          whiteSpace: "nowrap",
        }}
      >
        {`Showing image ${imgIdx + 1} of ${images.length}: ${images[imgIdx].alt}`}
      </span>
    </div>
  );
}
 ^X4k2cEhq

body {
  font-family: sans-serif;
}

.frame {
  position: relative;
  margin: auto;
  background-color: black;
  height: 400px;
  overflow: hidden;
  width: min(600px, 100vw);
}

.strip {
  display: flex;
  height: 100%;
  will-change: transform;
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

.carousel-image {
  flex-shrink: 0;
  height: 100%;
  object-fit: contain;
}

.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
 ^TqeeAXOc

%%
## Drawing
```compressed-json
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
```
%%