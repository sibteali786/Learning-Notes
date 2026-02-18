---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
3 Sum ^vIz9GYQe

nums = [-1,0,1,2,-1,-4] ^lUpil3uZ

right ^uVa9YxAJ

left ^wNPoscjw

complement  ^BwdQ7hJn

We can calculate complement at each step like in this case complement should be +5 or 5  ^WoycvDkD

function 3Sum(nums: Array[integer]) returns Array[Array[integer]] {
    // sort the array for better duplicate handling 
    nums.sort((a,b) => a-b)
    result = []
    for i = 0 to nums.length - 2 {
        if (i > 0 && nums[i] == nums[i-1]) continue
        
        left = i+1, right = nums.length - 1
        while (left < right){
            target = -nums[i]
            sum = nums[left] + nums[right]
            if (sum < target ) {
                left = left + 1
            }else if ( sum > target ) {
                right = right - 1
            }else {
                result.append([nums[i], nums[left], nums[right]])
                // skip duplicate left and right values 
                while (left < right && nums[left] == nums[left+1]) left = left + 1
                while (left < right && nums[right] == nums[right-1]) right = right - 1
                left = left + 1
                right = right - 1
            }
        }
    }
    return result
} ^6keimtCs

Time Complexity
1. Sorting the array so O(Nlogn)
1. We go over almost the entire array which accounts for O(N-2) but in large values of becomes O(N)
2. Then in each O(N) in worst case where all values are different we go over O(N-1) thus its becomes O(N^2) as total time complexity.

Space Coplexity
- We only use an array to store our results where each value is an anrray itself 
if O(N) is the space an array takes and each value of array which is array itself takes O(3) space i am not sure but it seems to be O(N)  ^o6GxpO6M

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    nums.sort((a,b) => a-b);
    const result = [];
    for(let i = 0; i < nums.length - 2; i++){
        if (nums[i] > 0) break;
        if (i > 0 && nums[i] === nums[i-1]) continue;
        
        let left = i + 1, right = nums.length - 1;
        while(left < right ) {
            const target = -nums[i];
            const sum = nums[left] + nums[right];
            if (sum < target) {
                left++;
            }else if(sum > target) {
                right--;
            }else {
                result.push([nums[i], nums[left], nums[right]]);

                // skip duplicate left and right
                while (left < right && nums[left] === nums[left+1]) left++;
                while (left < right && nums[right] === nums[right-1]) right--;
                left++;
                right--;
            }
        }
    }
    return result;
}; ^Stzf7Vzh

%%
## Drawing
```compressed-json
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
```
%%