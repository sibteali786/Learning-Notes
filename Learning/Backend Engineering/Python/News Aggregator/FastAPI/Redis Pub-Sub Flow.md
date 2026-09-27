---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
request → attempts = 0
│
▼
[TOP] SET NX lock
├─ won → (existing) heartbeat + fetch
│        ├─ ok   → write cache → PUBLISH "done" → release lock → return data
│        └─ fail → PUBLISH "failed" → release lock → 500
│
└─ lost → ┌── cleanup guard (always unsubscribe + close) ──┐
          │ SUBSCRIBE channel                              │
          │ GET cache ── hit → return data                 │
          │    │ miss                                      │
          │    ▼                                           │
          │ [WAIT] message, up to 5s                       │
          │ ├─ "done"   → GET → return data                │
          │ ├─ "failed" → go to RETRY                      │
          │ └─ timeout                                     │
          │     ├─ elapsed > ~40s   → go to RETRY          │
          │     ├─ lock exists      → back to [WAIT]       │
          │     └─ lock gone → GET ─ hit  → return data    │
          │                         └ miss → go to RETRY   │
          └────────────────────────────────────────────────┘
          RETRY: attempts += 1
                 ├─ attempts > cap → 500
                 └─ sleep(backoff + jitter) → back to [TOP] ^8stBVWUw

%%
## Drawing
```compressed-json
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
```
%%