---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
s = "AABABBA", k = 1 ^StZ91Kuw

424. Longest Repeating Character Replacement ^IlRLNJ3j

One guiding question before you start:

For any substring you pick — how do you know if it's valid (achievable with at most k replacements)?
Think about it this way: if the window has length L and the most frequent character appears maxF times — how many replacements do you need? ^7XA3OiAZ

s = "AABABBA", k = 1 ^xYxjXcq2

## Breaking It Down

Take the window `"AABBB"`:
- Length = 5
- Characters: A appears 2 times, B appears 3 times

**Goal:** make all characters the same with minimum replacements.

**Option 1** — replace everyone to 'B' (most frequent): change the 2 A's → **2 replacements needed**

**Option 2** — replace everyone to 'A': change the 3 B's → **3 replacements needed**

So smartest move = **keep the most frequent character, replace everything else**.

---

### The Formula

```
replacements needed = windowLength - mostFrequentCount
                    = 5 - 3 = 2
```

So a window is **valid** if:
```
windowLength - mostFrequentCount <= k
```

---

### Concrete Examples with k=2

| Window | Length | maxFreq | Replacements needed | Valid? |
|--------|--------|---------|-------------------|--------|
| "AABBB" | 5 | 3 (B) | 5-3=2 | ✅ |
| "AABBB" | 5 | 3 (B) | 5-3=2 | ✅ k=2|
| "AABBC" | 5 | 2 (A/B) | 5-2=3 | ❌ k=2|
| "AABB" | 4 | 2 (A/B) | 4-2=2 | ✅ |

---

So the whole problem reduces to:
> *Find the longest window where `windowLength - maxFrequency <= k`* ^a5Wha2Wm

s = "AABABBA", k = 1 ^y9QiLav5

- I think for brute force i need to divide in two phases
1. Find what is maxFrequency value but in each window ? 
2. Then we can start with window size 1 and increase it until the widow is valid. ^3mzmJmyT

function characterReplacement(s, k):
    maxCount = 0
    for i = 0 to s.length - 1:
        state = {}                    // reset per outer iteration
        maxFreqCount = 0
        for j = i to s.length - 1:   // start inner loop from i, not 0
            state[s[j]] = (state[s[j]] || 0) + 1
            maxFreqCount = max(maxFreqCount, state[s[j]])
            windowSize = j - i + 1    // correct window size
            if windowSize - maxFreqCount <= k:
                maxCount = max(maxCount, windowSize)
            else:
                break                 // only break inner loop
    return maxCount ^p3VaKc9l

- Time complexity
one external loop O(N) 
one internal loop O(N - k ) where k goes from lenght of string to zero
total complexity is O(N^2)
- Space Complexity
state stores only limited keys so its constant O(1) while all others are variables as well
so O(1) ^lvrKPnYi

s = "AABABBA", k = 1 ^3QhPiNLr

function characterReplacement(s, k) {
    freqCount = {}
    start = 0
    maxCount = 0
    maxFreqCount = 0
    for end = 0 to s.length - 1 {
        freqCount[s[end]] =  ( freqCount[s[end]] || 0 ) + 1
        maxFreqCount = Math.max(maxFreqCount, freqCount[s[end]])
        while ( end - start + 1 - maxFreqCount > k ) {
            freqCount[s[start]]--
            start++
        }
        maxCount = Math.max(maxCount,end-start+1)
    }
    return maxCount
} ^LJTrAJm0

After shrinking, maxFreqCount is never updated downward. Does that concern you?
For example if maxFreqCount was 3 but after shrinking the actual max frequency drops to 2 — you're using a stale value.

maxFreqCount only ever increases — and that's intentional.

Here's why:
We're looking for a longer window than the best we've seen so far. If maxFreqCount drops after shrinking, the new window would only be same size or smaller than our current maxCount — so it's not worth tracking.
window valid when: windowSize - maxFreqCount <= k
→ windowSize <= maxFreqCount + k

// maxFreqCount only grows when we find a BETTER dominant character
// if it drops, best possible window = same size → no improvement
// so we just slide the window maintaining same size
In one sentence:

We only care about windows larger than what we've seen — and that only happens when maxFreqCount grows.

Your instinct was correct, just needed tightening. ^3xCZXzde

%%
## Drawing
```compressed-json
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
```
%%