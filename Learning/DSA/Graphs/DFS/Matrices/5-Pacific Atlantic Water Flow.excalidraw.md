---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
Pacific Atlantic Water Flow ^yhnoS4N3

function pacificAtlantic(grid):
    directions = [[1,0], [-1,0], [0,1],[0,-1]]
    pacificVisited = new Set()
    atlanticVisited = new Set()
    r = grid.length
    c = grid[0].length
    function dfs(row, col, visited, prevHeight):
        key = `{row}-{col}`
        if visited.has(key): return
        if row < 0 or row >= r or col < 0 or col >= c: return
        if grid[row][col] < prevHeight: return
        visited.add(key)
        for [dr, dc] of directions:
            key = `{dr+row}-{dc+col}`
            if !visited.has(key):
                dfs(dr+row, dc+col, visited, grid[row][col])
                
    // loop for topRow and left Column
    for col = 0 to c - 1:
        // pacific
        dfs(0, col, pacificVisited, grid[0][col])
        // atlantic
        dfs(r-1,col, atlanticVisited, grid[r-1][col])
    for row = 0 to r - 1:
        // pacific
        dfs(row, 0, pacificVisited, grid[row][0])
        // atlantic
        dfs(row,c - 1, atlanticVisited, grid[row][c-1])        
        
    // find cells present in both -> return as result
    result = []
    for row = 0 to r-1:
        for col = 0 to c-1:
            key = `{row}-{col}`
            if pacificVisited.has(key) and atlanticVisited.has(key):
               result.push([row,col])
    return result 
             ^NKc6vhAM

[1, 2, 3],
[4, 5, 6],
[7, 8, 9] ^BR0wtyUV

class Solution {
    pacific_atlantic_flow(grid) {
        const directions = [[1,0],[-1,0],[0,1],[0,-1]];
        const pacificSet = new Set();
        const atlanticSet = new Set();
        const r = grid.length;
        const c = grid[0].length;
        function dfs(row, col, visited, prevHeight){
            let key = `${row}-${col}`;
            if (visited.has(key)) return;
            if (row < 0 || row >= r || col < 0 || col >= c) return;
            if (grid[row][col] < prevHeight) return;
            visited.add(key)
            for (const [dr, dc] of directions){
                key = `${dr+row}-${dc+col}`
                if (!visited.has(key)){
                    dfs(dr+row, dc+col, visited, grid[row][col])
                }
            }
        }
        for (let col = 0; col < c ; col++){
            // pacific
            dfs(0, col, pacificSet, grid[0][col])
            // atlantic
            dfs(r-1,col, atlanticSet, grid[r-1][col])
        }
        for (let row = 0; row < r; row++){
            dfs(row, 0, pacificSet, grid[row][0])
            dfs(row, c -1, atlanticSet, grid[row][c-1])
        }
        const result = []
        for (let row = 0; row < r; row++){
            for (let col = 0; col < c; col++){
                const key = `${row}-${col}`
                if (pacificSet.has(key) && atlanticSet.has(key)){
                    result.push([row,col])
                }
            }
        }
        return result;
    }
} ^aoKeDwwe

function pacificAtlantic(grid):
    directions = [[1,0], [-1,0], [0,1],[0,-1]]
    pacificVisited = new Set()
    atlanticVisited = new Set()
    r = grid.length
    c = grid[0].length
    stack = []
    function dfs(row, col, visited, prevHeight):
        stack.push([row, col, prevHeight])
        while(stack.length !== 0){
            [ir, ic, prevHeight] = stack.pop()
            key = `{ir}-{ic}`
            if visited.has(key): continue
            if ir < 0 or ir >= r or ic < 0 or ic >= c: continue
            if grid[ir][ic] < prevHeight: continue
            visited.add(key)
            for [dr, dc] of directions:
                key = `{dr+ir}-{dc+ic}`
                if !visited.has(key):
                    stack.push([dr+ir,dc+ic, grid[ir][ic]])
        }
                
    // loop for topRow and left Column
    for col = 0 to c - 1:
        // pacific
        dfs(0, col, pacificVisited, grid[0][col])
        // atlantic
        dfs(r-1,col, atlanticVisited, grid[r-1][col])
    for row = 0 to r - 1:
        // pacific
        dfs(row, 0, pacificVisited, grid[row][0])
        // atlantic
        dfs(row,c - 1, atlanticVisited, grid[row][c-1])        
        
    // find cells present in both -> return as result
    result = []
    for row = 0 to r-1:
        for col = 0 to c-1:
            key = `{row}-{col}`
            if pacificVisited.has(key) and atlanticVisited.has(key):
               result.push([row,col])
    return result 
             ^oaRj0sdg

%%
## Drawing
```compressed-json
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
```
%%