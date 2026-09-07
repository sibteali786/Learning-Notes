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

function memoize(fn):
    cache = new Map()
    return function(...args):
        key = args.join(",")
        if (cache.has(key)):
            return cache.get(key)
        result = fn.apply(this, args)
        cache.set(key, result)
        return result ^uVqjbV90

%%
## Drawing
```compressed-json
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
```
%%