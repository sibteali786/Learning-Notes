---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'



# Code Block

## Visual Comparison

### Sorting Approach:
```
Auxiliary Memory:
┌──────────────────────────┐
│ Keys (sorted strings):   │  O(m × n)
│ "act", "opst", "aht"    │  ← NEW strings!
├──────────────────────────┤
│ Values (pointers):       │  O(m)
│ →, →, →, →, →, →        │  ← references
└──────────────────────────┘
Total Auxiliary: O(m × n)
```

### Frequency Approach:
```
Auxiliary Memory:
┌──────────────────────────┐
│ Keys (tuples):           │  O(m)
│ (1,0,1,...), (0,0,0,...) │  ← 26 ints each
├──────────────────────────┤
│ Values (pointers):       │  O(m)
│ →, →, →, →, →, →        │  ← references
└──────────────────────────┘
Total Auxiliary: O(m)

# Excalidraw Data

## Text Elements
m=no of strings i.e 6
n = len of longest string i.e 4 for stop  ^8y2RD7wr

["act","pots","tops","cat","stop","hat"] ^ZBTUPWqa

What we can do is group anagrams based on some common criteria
- The one remember or comes in my mind is only one i.e sort a given string. ^QSssWmis

act ^Hhbf6rJT

act ^LyAm2twT

sort ^DkQxnkBe

{"act": []} ^zn6jvB4l

- We will ignore pots, tops since they have lenght of 4, chose cat ^zTPhSS05

- sort cat -> act, check in dictionary act exists, so add cat to act key within array ^Q8RiSXms

{"act": ["act", "cat"], "opst": ["opst", "tops","stop"], "aht": ["hat"]} ^1pdBuPI8

def groupAnagrams(strs: List[str]) returns List[List[str]] {
    groups = {}
    for i = 0 to len(strs) {
        sortedStr = sort(strs[i])
        if sortedStr not in groups.keys() {
            groups[sortedStr] = [strs[i]]
        }else {
            groups[sortedStr].push(strs[i])
        }
    }

    return list(groups.values())
} ^kl4LrkXZ

Time Complexity Analysis
- For loop = O(N) worst case
- For each item in list we call sorted for which average time complexity is O(nlogn)
- it seems soemthing like O(n * nLogn)
- while space complexity is O(N) as we are using only a dictionary ^GxwLyXbw

## Space Complexity Breakdown

Let me clarify with an example:

### What Takes Space?

**Input:** `strs = ["act", "pots", "tops", "cat", "stop", "hat"]`

**Your dictionary looks like:**
```
{
    "act": ["act", "cat"],           # key + 2 strings
    "opst": ["pots", "tops", "stop"], # key + 3 strings  
    "aht": ["hat"]                    # key + 1 string
}
```

### Space Analysis

**1. Keys (sorted strings):**
- You create `m` unique keys (worst case: all strings different)
- Each key has length up to `n`
- Space for keys: **O(m * n)**

**2. Values (original strings):**
- You store all `m` original strings in the dictionary
- Each string has length up to `n`
- Space for values: **O(m * n)**

**3. Output list:**
- Same strings again: **O(m * n)**

**Total: O(m * n) + O(m * n) + O(m * n) = O(m * n)**

---

## Why Not Just O(m)?

You said O(m) thinking "m entries in dictionary"

But **each entry contains strings**, not just references!

**Think of it this way:**
- If m = 1000 strings
- Each string length n = 100
- Total characters stored ≈ 1000 × 100 = 100,000 characters

That's why it's **O(m * n)** not O(m)

---

## Simplified Way to Think

**"Am I storing the actual string characters or just pointers?"**

- In your solution: storing actual strings → count the characters → O(m * n)
- If you only stored indices/pointers → O(m)

---

**Does this clarify it?** The key insight: space complexity counts the **data size**, not just number of containers. ^cbPLA9Pj

The Key Difference
Integers (and other primitives):

Fixed size: 4 bytes (32-bit) or 8 bytes (64-bit)
Doesn't matter if it's 1 or 999999
Space: O(1) per integer

Strings (and other collections):

Variable size: depends on length
"hi" = 2 bytes, "hello" = 5 bytes, "a"*100 = 100 bytes
Space: O(length) per string ^hCBB81ou

Corrected Time and Space Complexity ^6a7WFl9x

def groupAnagrams(strs: List[str]) returns List[List[str]] {
    groups = {}
    for str in strs {
        count = [0] * 26
        for char in str {
            count[char - ord("a")] += 1
        }
        key = tuple(count)
        if key not in groups {
            groups[key] = [str] 
        }else {
            groups[key].append(str)
        }
        
    }
    
return groups.values()    
} ^HmyosZxw

Time and Space Complexity ^QVaet97B

- Time complexity for outer level since we have nested loop is O(M*N)
- where M = no of strs or len of Strs
- while inner loops runs for n times where n is value of length of longest string

The Space complexity is 
- Keys are tuples so i think they have fixed space that cannot be changed
- values are strings so i have a guess itd O(M*N). ^91xJaNWO

- In case of Sorting appraoch at each step we were creating a new string  ^Rnf3bWY6

- While in case of frequency counting we are just storing tuples as keys which is constant size and wont change sine tuple length is always 26 so its constant  ^XaYccVrU

## Visual Comparison

### Sorting Approach:
```
Auxiliary Memory:
┌──────────────────────────┐
│ Keys (sorted strings):   │  O(m × n)
│ "act", "opst", "aht"    │  ← NEW strings!
├──────────────────────────┤
│ Values (pointers):       │  O(m)
│ →, →, →, →, →, →        │  ← references
└──────────────────────────┘
Total Auxiliary: O(m × n)
```

### Frequency Approach:
```
Auxiliary Memory:
┌──────────────────────────┐
│ Keys (tuples):           │  O(m)
│ (1,0,1,...), (0,0,0,...) │  ← 26 ints each
├──────────────────────────┤
│ Values (pointers):       │  O(m)
│ →, →, →, →, →, →        │  ← references
└──────────────────────────┘
Total Auxiliary: O(m) ^96APTNk6

This is a crucial concept in space complexity analysis. References/pointers are constant space, regardless of what they point to. ^Xfr3MRjk

Group Anagrams
Solved

Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:

Input: strs = ["x"]

Output: [["x"]]

Example 3:

Input: strs = [""]

Output: [[""]]

Constraints:

    1 <= strs.length <= 1000.
    0 <= strs[i].length <= 100
    strs[i] is made up of lowercase English letters.



Recommended Time & Space Complexity

You should aim for a solution with O(m * n) time and O(m) space, where m is the number of strings and n is the length of the longest string.
 ^YfBLvdDP

Group Anagrams ^cdTfF8wL

%%
## Drawing
```compressed-json
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

ADiggAA=
```
%%