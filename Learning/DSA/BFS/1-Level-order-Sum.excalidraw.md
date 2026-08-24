---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
[1, 3, 4, null, 2, 7, null, 8] ^jHKrGaGM

function levelOrderSum(root):
    if (!root) return []
    
    result = []
    queue = [root]
        
    while queue.length > 0:
        levelSize = queue.length
        levelSum = 0
        
        for i = 0 to levelSize - 1:
            curr = queue.shift()
            levelSum += curr.val
            
            if curr.left:
                queue.push(curr.left)
            if curr.right:
                queue.push(curr.right)
            
        result.push(levelSum)
    return result ^wvsxpT2t

// class TreeNode {
//     constructor(val, left, right) {
//         this.val = val;
//         this.left = left;
//         this.right = right;
//     }
// }

class Solution {
    level_order_sum(root) {
        // Your code goes here
    if (!root) return []
    
    const result = []
    const queue = [root]
        
    while (queue.length > 0){

        const levelSize = queue.length
        let levelSum = 0
        
        for ( let i = 0; i  < levelSize ; i++){
            const curr = queue.shift()
            levelSum += curr.val
            
            if (curr.left){
                queue.push(curr.left)
            }
            if (curr.right){
                queue.push(curr.right)
            }
            
        }
        result.push(levelSum)
    }
    return result
    }
} ^WrcJQTvp

Time Complexity
- one external loop and one internal but 
at most we visit each value once so
O(N)
Space complexity
- At worst whe lowest level contains most 
nodes so O(N/2) => O(N)   ^AzaqqYJR

Time Complexity: O(N) where N is the number of nodes in the tree. We visit each node exactly once, and each node, we perform a constant amount of work.

Space Complexity: O(N) In the worst case, each node is on its own level, so the output list will contain N elements. ^n7sJsvWS

%%
## Drawing
```compressed-json
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

jxWhsghB+3wB0iu185HRgAPIQAPIgA==
```
%%