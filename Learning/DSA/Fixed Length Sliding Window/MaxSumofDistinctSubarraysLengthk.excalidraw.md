---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
Max Sum of Distinct Subarrays Length k ^J9zOi1sK

nums = [1,5,4,2,9,9,9], k = 3 ^HRUS24zu

function maxSum(nums, k){
    state = {}
    maxSum = 0
    start = 0
    currSum = 0
    for end = 0 to nums.length - 1 {
        currSum += nums[end]
        state[nums[end]] = (state[nums[end] || 0]) + 1
        if (end - start + 1 == k ) {
            // check if keys are distinct only then have maxSum re-calculated
            if (Object.keys(state).length === k){
                maxSum = Math.max(currSum, maxSum)
            }
            currSum -= nums[start]
            state[nums[start]] = state[nums[start]] - 1
            if (state[nums[start]] == 0) {
                delete state[nums[start]]
            }
            start++
        }
    }
    return maxSum
} ^VccmCwGf

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maximumSubarraySum = function(nums, k) {
    let state = {};
    let maxSum = 0;
    let currSum = 0;
    let start = 0;
    for (let end =0;end < nums.length; end++){
        currSum += nums[end];
        state[nums[end]] = (state[nums[end]] || 0) + 1;
        if (end - start + 1 === k) {
            if (Object.keys(state).length === k) {
                maxSum = Math.max(maxSum, currSum);
            }
            currSum -= nums[start];
            state[nums[start]]--;
            if (state[nums[start]] === 0) {
                delete state[nums[start]];
            }
            start++;
        }
    }
    return maxSum;
}; ^qo5QC90H

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maximumSubarraySum = function(nums, k) {
    let state = {};
    let maxSum = 0;
    let currSum = 0;
    let distinctCount = 0
    let start = 0;
    for (let end =0;end < nums.length; end++){
        currSum += nums[end];
        if(!state[nums[end]]){
            distinctCount++;
        }
        state[nums[end]] = (state[nums[end]] || 0) + 1;
        if (end - start + 1 === k) {
            if (distinctCount === k) {
                maxSum = Math.max(maxSum, currSum);
            }
            currSum -= nums[start];
            state[nums[start]]--;
            if (state[nums[start]] === 0) {
                delete state[nums[start]];
                distinctCount--;
            }
            start++;
        }
    }
    return maxSum;
};  ^vQau36Xr

Un Optimized Js Code ^tiJcQvL7

Optimized One ^6NBSKrRd

Using Object.keys has O(k) time Complexity since we have to traverse all keys in hash map to get its length thus caching it is better using distincCount ^fUrhTT1L

nums = [1,5,4,2,9,9,9], k = 3 ^SbqHYfpL

[1,5,4,2,9,9,9] ^9XM6HH4k

func maxSubarraySum(nums, k){
    maxSum = -Infinity
    hasSeenBefore = {}
    for i = 0 to nums.length - k {
        sum = nums[i]
        hasSeenBefore[nums[i]] = 1
        for j = i + 1 to i + k - 1 {
            if nums[j] not in hasSeenBefore {
                sum = sum + nums[j]
                hasSeenBefore[nums[j]] = 1
            }else{
                break
            }
        }
        maxSum = Math.max(maxSum, sum)
        hasSeenBefore = {}
    }
    return maxSum == -Infinity ? 0: maxSum
} ^sV5XlmN9

Idea is to find duplicate
- If we try comparing adjacent values like nums[j] !== nums[j-1]
- It wont work ? why becuase its not a surety that adajacent would be same always
in case of k window 3 , 9,2,9 we would ignore 9 here since we are comparing adjacent only
- Thus we need a hash map to track numbers in a given window maybe. ^ykL2Udu1

Time Complexity
- Outer loop runs O(N-k) times while inner runs O(k) times for each O(N-k) thus
O(N-k)*O(k) = O(N)
- Hash map costs us O(k) since we are not storing all values and only few of whole array ^8NWvhXWy

Frequency 0 = element is gone from the window. Delete the key so future lookups treat it as a fresh entry.

This is exactly why a plain Set wouldn't work here — a Set has no frequency concept, so you can't know if an element is truly gone or just has one fewer copy. ^t4546e4F

%%
## Drawing
```compressed-json
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
```
%%