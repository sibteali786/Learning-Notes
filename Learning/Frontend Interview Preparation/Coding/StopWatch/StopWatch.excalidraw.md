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