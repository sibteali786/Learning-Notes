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

%%
## Drawing
```compressed-json
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
```
%%