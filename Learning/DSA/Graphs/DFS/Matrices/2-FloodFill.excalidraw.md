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