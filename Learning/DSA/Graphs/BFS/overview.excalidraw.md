---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
BFS traverse Using Adjacency List ^oEGyAQxO

function bfs(start):
    visited  = new Set([start])
    queue = [start]
    
    while queue.length != 0:
        node = queue.shift()
        for neighbor in adjList[node]:
            if !visited.has(neighbor):
                visited.add(neighbor)
                queue.push(neighbor)
             ^eXrbg34i

BFS traverse for Matrix  ^7RrjMprh

INPUT
adjList = {
    "1": ["2", "4"],
    "2": ["1", "3"],
    "3": ["2", "4"],
    "4": ["1", "3", "5"],
    "5": ["4"]
}; ^h4g9RCvK

INPUT
matrix = [
    [0, 0, 0],
    [0, 1, 1],
    [0, 1, 0]
]; ^7mgfcmMX

function bfs(grid):
    visited = new Set()
    directions = [[-1,0],[1,0],[0,-1],[0,1]]
    
    queue = [[0,0]]
    
    while queue.length != 0:
        [row, col] = queue.shift()
        
        for [dr,dc] of directions:
            nRow = row+dr
            mCol = col+dc
            key = `{nRow}-{mCol}`
            if nRow >= 0 && nRow < grid.length && mCol >= 0 && mRow < grid[0].length:
                if !visited.has(key):
                    queue.push([nRow, mCol])
                    visited.add(`{nRow}-{mCol}`)                   ^eEk1qTXp

BFS Traversal of ADJ list by Level ^jCc9fwy4

function bfsLevel(graph, start):
    queue = [start]
    visited = new Set()
    visited.add(start)
    levels = []
    while queue.length != 0:
        levelSize = queue.length
        currentLevel = []
        for i = 0 to levelSize - 1:
            node = queue.shift()
            currentLevel.push(node)
            for neighbor of graph[node]:
                if !visited.has(neighbor):
                    visited.add(neighbor)
                    queue.push(neighbor)
        
        levels.push(currentLevel)
    return levels ^EmzMLjnL

INPUT
adjList = {
    "1": ["2", "4"],
    "2": ["1", "3"],
    "3": ["2", "4"],
    "4": ["1", "3", "5"],
    "5": ["4"]
}; ^d6bMCT6n

BFS level traverse for Matrix  ^siqLWjWe

function bfsLevelByLevel(matrix):
    rows = matrix.length
    cols = matrix[0].length
    
    directions = [[0,1], [1,0], [0,-1], [-1,0]]
    visited = new Set()
    queue = [[0,0]]
    visited.add("0-0")
    
    levels = []
    while queue.length != 0:
        levelSize = queue.length
        currentLevel = []
        
        for i = 0 to levelSize - 1:
            [row, col] = queue.shift() 
            currentLevel.push([row, col])
            for [dr, dc] of directons:
                r = dr+row
                c = dc+col
                key = `{r}-{c}`
                if r >= 0 && r < rows && c >= 0 && c < cols:
                    if !visited.has(key):
                        queue.push([r,c])
                        visited.add(key)
        levels.push(currentLevel)
    return levels ^XhqMejte

INPUT
matrix = [
    [0, 0, 0],
    [0, 1, 1],
    [0, 1, 0]
]; ^RxOG7egl

%%
## Drawing
```compressed-json
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

CAD8hAA=
```
%%