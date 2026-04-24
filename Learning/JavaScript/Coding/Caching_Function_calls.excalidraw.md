---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
Cache Function calls ^FkBU92qG

export default function memoize(fn){
    cache = new Map()
    return function(...args) {
        key = args.join(",")
        if ( cache.has(key) ) {
            return cache.get(key)
        }
        
        result = fn.apply(this, args)
        cache.set(key, result)
        return result
    }
}  ^dOyBfieZ

Sure!

**Per single call (cache miss):**
- You store exactly **one** key-value pair
- That's O(1) space *per call*

**After N unique calls:**
- You've stored N entries in the cache
- Total space used = O(N) where N = number of unique argument combinations

---

So the correct way to say it:

| | Time | Space |
|---|---|---|
| Cache hit | O(1) | O(1) |
| Cache miss | O(1) | O(1) per call, O(N) total |

---

Your solution is correct! ✅ Here it is cleaned up as pseudocode:

```
function memoize(fn):
  cache = new Map()

  return function(...args):
    key = args.join(",")
    
    if cache.has(key):
      return cache.get(key)
    
    result = fn.apply(this, args)
    cache.set(key, result)
    return result
```

---

## Alternative approaches worth knowing:

**1. Plain object `{}` instead of Map**
- Works but `has` check needs care — use `key in cache` not `cache[key]` (falsy trap!)
- Map is cleaner for non-string keys

**2. `JSON.stringify(args)` instead of `join`**
- Handles nested objects as args
- But `JSON.stringify({a:1})` and `JSON.stringify({a:1})` — are these the same? ✅
- Slower than `join` for primitive args

**3. WeakMap for object arguments**
- Advanced — avoids memory leaks when object args get garbage collected

---

## Interview bonus points — mention these:
- **Cache eviction** — what if cache grows forever? LRU cache is the follow-up problem
- **Accessibility/Performance angle** — `useMemo` in React is memoize under the hood
- This pattern is called **memoization** — a form of **dynamic programming** ^vb2wpvro

%%
## Drawing
```compressed-json
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
```
%%