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

style.css

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
 ^TqeeAXOc

%%
## Drawing
```compressed-json
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
```
%%