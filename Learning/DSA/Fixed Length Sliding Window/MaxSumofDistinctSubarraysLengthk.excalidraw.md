---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
Max Sum of Distinct Subarrays Length k ^J9zOi1sK

nums = [3, 2, 2, 3, 4, 6, 7, 7, -1]
k = 4 ^HRUS24zu

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

%%
## Drawing
```compressed-json
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
```
%%