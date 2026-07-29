---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
image = [[1,0,1],[1,0,0],[0,0,1]], sr = 1, sc = 1, color = 2 ^gwzaABXo

function floodFill(image, sr, sc, color):
    if image[sr][sc] == color:
        return image
    original_color = image[sr][sc]
    directions = [[-1,0], [1,0], [0,-1], [0,1]] 
    function dfs(row, col):
        if row < 0 or row >= image.length or col < 0 or col >= image[0].length:
            return
        if image[row][col] != original_color:
            return
        image[row][col] = color
        for [dr, dc] of directions:
            dfs(row+dr, col+dc)
    
    dfs(sr, sc)
    return image ^UnHu7fBu

/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} color
 * @return {number[][]}
 */
var floodFill = function(image, sr, sc, color) {
    if (image[sr][sc] === color){
            return image
        }
        const start_color = image[sr][sc]
        const directions = [[-1,0], [1,0], [0,-1], [0,1]]
        function dfs(row, col){
            if (row < 0 || row >= image.length || col < 0 || col >= image[0].length) {
                return
            }

            if (image[row][col] !== start_color) {
                return
            }
            image[row][col] = color
            for (const [dr, dc] of directions){
                dfs(row+dr, col+dc)
            }
        }
        dfs(sr, sc)
        return image
}; ^G6aDnKfC

Time Complexity
- we have a recursively running function which goes over 
a subset of MxN image matrices in worst case 
- O(RxC) as we go over each value in grid

Space Complexity 
- not saving anything so O(1) constant space 
- the stack depth goes as deep as RxC product so 
O(RxC)
- the input image RxC does not count since total space 
complexity counts auxiliary space  ^DEyafHRC

function floodFill(image, sr, sc, color):
    if image[sr][sc] == color:
        return image
    start_color = image[sr][sc]
    directions = [[-1,0],[1,0],[0,-1],[0,1]]
    stack = []
    function dfsIterative(ir, ic):
        stack.push([ir, ic])
        while stack.length != 0:
            [row, col] = stack.pop()
            image[row][col] = color
            for [dr, dc] in directions:
                if row+dr >= 0 and row+dr < image.length and col+dc >= 0 and col+dc < image[0].length:
                    if image[row+dr][col+dc] == start_color:
                        stack.push([row+dr, col+dc])
                    
    dfsIterative(sr,sc)
    return image ^nQ2tajjw

image = [[1,0,1],[1,0,0],[0,0,1]], sr = 1, sc = 1, color = 2 ^faKWExtd

stack = [] ^sFHE3cr2

stack = [[0,1],[2,1],[1,0],[1,2]] ^63YtlSyT

class Solution {
    flood_fill(image, sr, sc, color) {
        if (image[sr][sc] === color) {
            return image
        }
        const start_color = image[sr][sc]
        const directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        const stack = []
        function dfs(ir, ic) {
            stack.push([ir, ic])
            while (stack.length !== 0) {
                const [row, col] = stack.pop()
                image[row][col] = color
                for (const [dr, dc] of directions) {
                    if (row + dr >= 0 && row + dr < image.length && col + dc >= 0 && col + dc < image[0].length) {
                        if (image[row+dr][col+dc] === start_color) {
                            stack.push([row+dr, col+dc])
                        }
                    }
                }
            }
        }
        dfs(sr, sc)
        return image
    }
} ^pTrOm99K

%%
## Drawing
```compressed-json
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

Uc3uACa6l9ggdoYAEVBABFQgAA==
```
%%