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
```
%%