---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
Important Concepts ^QKe3I79N

https://react.dev/reference/react/useRef ^CilCzugS

https://developer.mozilla.org/en-US/docs/Web/API/Window/setInterval ^IzZ1MDJt

https://developer.mozilla.org/en-US/docs/Web/API/Window/requestAnimationFrame ^XvoFpwBG

Approach 1 (naive/bad): setInterval(() => setElapsed(e => e + 10), 10) — increment a counter every 10ms.

Why it's bad: setInterval doesn't guarantee it fires exactly every 10ms (JS event loop, tab throttling, browser deprioritizing background tabs). Errors accumulate — your stopwatch silently drifts from wall-clock time.

Approach 2 (better): Store startTime = Date.now() when starting. On each tick, compute elapsed = Date.now() - startTime + previouslyAccumulated. You still use setInterval just to trigger re-renders, but the displayed value is always computed from the actual timestamp delta, not accumulated increments.

Self-correcting — even if a tick is late, the math is still accurate.

Approach 3: Same timestamp-delta idea but using requestAnimationFrame instead of setInterval for the re-render trigger.

Pros: syncs with browser paint cycles, pauses automatically in inactive tabs (saves battery/CPU).
Cons: fires ~60 times/sec regardless of your 10ms display granularity — wasteful renders unless you throttle, and pausing in background tabs might be undesirable if you want it to keep counting silently while user is away (product decision). ^SIJpT73K

Aproaches ^PvqGZAro

import { useState, useRef, useEffect } from "react";
export default function Stopwatch() {
  const [_, forceTick] = useState(0);
  const startTimestamp = useRef(0);
  const accumulatedTime = useRef(0);
  const [isRunning, setIsRunning] = useState(false);
  const tickMs = 10;
  useEffect(() => {
    if (!isRunning) return;
    const id = setInterval(() => forceTick((n) => n + 1), tickMs);
    return () => clearInterval(id);
  }, [isRunning]);
  let elapsedTime =
    accumulatedTime.current +
    (isRunning ? Date.now() - startTimestamp.current : 0);
  const handleClick = () => {
    if (!isRunning) {
      startTimestamp.current = Date.now();
    } else {
      accumulatedTime.current = elapsedTime;
    }
    setIsRunning(!isRunning);
  };
  const handleReset = () => {
    if (isRunning) {
      setIsRunning(false);
    }
    startTimestamp.current = 0;
    accumulatedTime.current = 0;
    forceTick((n) => n + 1);
  };
  const formatTime = (et) => {
    const totalSeconds = Math.floor(et / 1000);

    // 2. Extract hours, minutes, and remaining seconds
    const hours = String(Math.floor(totalSeconds / 3600));
    const minutes = String(Math.floor((totalSeconds % 3600) / 60));
    const seconds = String(totalSeconds % 60);
    const centiSeconds = String(Math.floor((et % 1000) / 10));
    return { hours, minutes, seconds, centiSeconds };
  };
  const time = formatTime(elapsedTime);
  return (
    <div>
      <button
        type="button"
        className="wrapper"
        onClick={handleClick}
        aria-label="Stopwatch. Click to start or stop."
        aria-live="off"
      >
        {time.hours > 0 ? (
          <>
            <span className="hour">{time.hours}h</span>
            <span className="min"> {time.minutes.padStart(2, "0")}m</span>
            <span className="sec">{time.seconds.padStart(2, "0")}s</span>
            {time.centiSeconds.padStart(2, "0")}
          </>
        ) : time.minutes > 0 ? (
          <>
            <span className="min">{time.minutes}m</span>
            <span className="sec">{time.seconds.padStart(2, "0")}s</span>
            {time.centiSeconds.padStart(2, "0")}
          </>
        ) : (
          <>
            {" "}
            <span className="sec">{time.seconds}s</span>
            {time.centiSeconds.padStart(2, "0")}
          </>
        )}
      </button>
      <div>
        <button
          aria-label={isRunning ? "Stop timer" : "Start timer"}
          onClick={handleClick}
        >
          {isRunning ? "Stop" : "Start"}
        </button>{" "}
        <button onClick={handleReset}>Reset</button>
      </div>
    </div>
  );
}

body {
  font-family: sans-serif;
  font-size: 18px;
}

.sec {
  font-size: 22px;
}

.min {
  font-size: 26px;
}

.hour {
  font-size: 30px;
}

.wrapper {
  display: flex;
  gap: 4px;
  align-items: baseline;
  cursor: pointer;
  border: none;
  background: transparent;
  margin-bottom: 10px;
}
 ^sbQtfEnn

## Element Links
CilCzugS: https://react.dev/reference/react/useRef

IzZ1MDJt: https://developer.mozilla.org/en-US/docs/Web/API/Window/setInterval

XvoFpwBG: https://developer.mozilla.org/en-US/docs/Web/API/Window/requestAnimationFrame

%%
## Drawing
```compressed-json
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
```
%%