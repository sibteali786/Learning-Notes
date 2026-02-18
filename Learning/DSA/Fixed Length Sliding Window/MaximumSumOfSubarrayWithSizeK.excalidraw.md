---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
nums = [2, 1, 5, 1, 3, 2], k = 3  ^xhm1r0Bd

- first we extend window size to K 
- Compute sum of the window and update the max_sum if its larger than max_sum
- Then we contract the window by removing left most to preapre for next iteration. ^Q5iPfI4o

Maximum Sum of Subarray with Size K ^kBUNhcnI

function fixedLengthSlidingWindow(nums, k) {
    state = // require data structure
    start = 0
    max = 0
    for end = 0 to nums.length - 1 {
        // extend window 
        // add nums[end] to state  in O(1) time 
        if (end - start + 1 === k ){
            // size of window is k here 
            max = Math.max(max, contents of state);
            
            // contract window
            // remove nums[start] from state in O(1) time
            start++
        }
    }

    return max
} ^IcX0Q8YB

General Psedocode for Fixed Length Slidign Windows ^Q8eBl0nx

function maxSubarraySum(nums, k) {
    maxSum = -Infinity
    windowSum = 0
    start = 0
    for end  = 0 to nums.length - 1 {
        windowSum += nums[end]

        if(end - start + 1 == k) {
            maxSum = Math.max(windowSum, maxSum)
            windowSum -= nums[start]
            start++
        }
    }
    return maxSum
} ^Hd94SMbO

function maxSubarraySum(nums, k) {
    let windowSum = 0;
    let maxSum = -Infinity;
    let start = 0;
    for (let end = 0; end < nums.length - 1; ++end){
        windowSum += nums[end]
        if(end-start+1 ===k) {
            maxSum = Math.max(windowSum, maxSum);
            windowSum -= nums[start]
            start++;
        }    
    }
    return maxSum;
} ^49BapVIE

%%
## Drawing
```compressed-json
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
```
%%