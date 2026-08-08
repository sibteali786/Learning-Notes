---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
function solve(board):
    m = board.length
    n = board[0].length
    visited = new Set()
    directions = [[1,0], [-1,0], [0,1],[0,-1]]
    function dfs(row, col):
        key = `{row}-{col}`
        if visited.has(key):
            return
        if row < 0 or row >= m or col < 0 or col >= n:
            return 
        if board[row][col] == "X":
            return
        visited.add(key)
        board[row][col] = "S"
        for [dr, dc] of directions:
            key = `{dr+row}-{dc+col}`
            if !visited.has(key) and board[dr+row][dc+col] == "O":
                dfs(dr+row, dc+col)
    for col = 0 to n-1:
        if board[0][col] == 'O':
            dfs(0, col)
        if board[m-1][col] == 'O':
            dfs(m-1, col)
    for row = 0 to m-1:
        if board[row][0] == 'O':
            dfs(row, 0)
        if board[row][n-1] == 'O':
            dfs(row, n-1)

    
    for row = 0 to m - 1:
        for col = 0 to n - 1:
            if board[row][col] == "O":
                board[row][col] = "X"
            else if board[row][col] == 'S':
                board[row][col] = 'O'
     ^PoBnRLfI

Time Complexity
Border scan goes over 0 to R and 0 to C so O(R) + O(C)
dfs for border at worst visits all values so O(RxC)
final sweep again visits all values so O(RxC)
total = O(R) + O(C) + 2O(RxC) = O(RxC) + O(R) + O(C)
where as compare to O(RxC) R and C are negligible so O(RxC)

Space Complexity

Visited takes at worst all values as visited so O(RxC)
call stack offcourse takes in O(RxC)
even then total space isO(RxC) ^hRUvzv7n

/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solve = function(board) {
    const r = board.length;
    const c = board[0].length;
    const visited = new Set();
    const directions = [[1,0],[-1,0], [0,1], [0,-1]];
    // covering top and bottoms rows 

    function dfs(row, col){
        let key = `${row}-${col}`;
        if (visited.has(key)){
            return
        }

        if (row < 0 || row >= r || col < 0 || col >= c) {
            return
        }
        if (board[row][col] === "X") return

        board[row][col] = "S";
        visited.add(key);
        for (const [dr, dc] of directions){
            key = `${dr+row}-${dc+col}`
            if (!visited.has(key)){
                dfs(dr+row, dc+col)
            }
        }
    }

    for (let col = 0; col < c; col++){
        if (board[0][col] === "O"){
            dfs(0, col)
        }

        if (board[r-1][col] === "O"){
            dfs(r-1, col)
        }
    }

    for (let row = 0; row < r; row++){
        if (board[row][0] === "O"){
            dfs(row,0)
        }

        if (board[row][c-1]){
            dfs(row, c-1)
        }
    }

    // final sweep phase
    for(let row = 0; row < r; row++){
        for (let col = 0; col < c; col++){
            if (board[row][col] === "O"){
                board[row][col] = "X"
            }else if(board[row][col] === "S"){
                board[row][col] = "O"
            }
        }
    }
}; ^irBtrJul

Stack ^tJjeUSWm

function solve(board):
    r = board.length;
    c = board[0].length;
    
    directions = [[1,0], [-1,0], [0,1],[0,-1]]
    visited = new Set()
    stack = []
    function dfsIterative(row, col):
        stack.push([row, col])
        while(stack.length != 0){
            [ir, ic] = stack.pop()
            key = `{ir}-{ic}`
            if visited.has(key): continue
            if ir < 0 or ir >= r or ic <0 or ic >= col: continue
            if board[ir][ic] == "X": continue
            visited.add(key)
            board[ir][ic] = "S"
            for [dr, dc] of directions:
                key = `{dr+ir}-{dc+ic}`
                if !visited.has(key):
                    stack.push([dr+ir, dc+ic])
        }

    for col = 0 to c-1:
        if board[0][col] == 'O':
            dfsIterative(0, col)
        if board[c-1][col] == 'O':
            dfsIterative(c-1, col)
    for row = 0 to m-1:
        if board[row][0] == 'O':
            dfsIterative(row, 0)
        if board[row][r-1] == 'O':
            dfsIterative(row, r-1)

    
    for row = 0 to r - 1:
        for col = 0 to c - 1:
            if board[row][col] == "O":
                board[row][col] = "X"
            else if board[row][col] == 'S':
                board[row][col] = 'O' ^GCtk8jJM

## Embedded Files
ae93426224d848854a0b1fdfd354105a14b23a02: [[Pasted Image 20260805153701_541.png]]

%%
## Drawing
```compressed-json
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
```
%%