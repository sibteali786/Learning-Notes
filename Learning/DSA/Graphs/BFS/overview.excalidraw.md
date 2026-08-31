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
```
%%