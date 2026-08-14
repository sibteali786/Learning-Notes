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
N4KAkARALgngDgUwgLgAQQQDwMYEMA2AlgCYBOuA7hADTgQBuCpAzoQPYB2KqATLZMzYBXUtiRoIACyhQ4zZAHoFAc0JRJQgEYA6bGwC2CgF7N6hbEcK4OCtptbErHALRY8RMpWdx8Q1TdIEfARcZgRmBShcZQUebQBGAE5tHho6IIR9BA4oZm4AbXAwUDBSiBJuaAAJAHFlYmJ6ITTSyFhESsJ9aKR+MsxuZx5E+ISAZgA2AHZ4gA4pgFY+yBhB

ngAWAAZtRIWx+J4losgKEnVuKamx5akEQmVpbjHnm+tlYO5Nm+YoUjYAawQAGE2Pg2KRKr9rMw4LhAjkWmVNLhsP9lH8hBxiCCwRCJFCODC4dkoIjIAAzQj4fAAZVgHwkgg8ZIgPz+gIA6mdJNw+MdWb8AQg6TAGegmRUbhiHhxwnk0PEbmxYdg1KsFZsvvz0cI4ABJYjy1D5AC6N3J5CyBu4HCE1JuhCxWEquE2LIxWNlzCNtvt/LCCGI3Fm60S

mzGCx44ZujBY7C4aCjMaYrE4ADlOGJeXtNolZmNQw7mAARDJQQPcckEMI3TTCLEAUWCWRyRtNNyEcGIuHLQYVU1mC0SPAmPCjYyT/KIHH+Nrt+BuYNRFbQVfwNf9USgQiNEEQWMdyhZlOC1okuAQiQLI7H62IIdmg/Wrs08XJxHfEfW8U2C1w8XWTQeDGV1Um+dxxGNY4wEVaD4mOM1+WwP44DnP1WikUIABUsCgAAZR1Z1XasECKABfPoSjKCoJ

AWLD8AoBYADUJgAWVmfAsLwqYmIAQQWKomMkNhcBZdpIIgC0EEDcgqBuAY0CGPZtE2KZdnDaYJnWKZNgmG51VQIZwxUzYNgWBZNnieIJlzYcblOYhzkTHhRi03TDhuSQ7geUl+20CYknWQdhm/eIpgmSNXg4d5IK1DC2SFHFwUqABiBBw3ifYWWRVEdUxbFQWS/FyEJWF4VJc0qVpekJIlINvkFTluW4WD4sa4UasqOr3WEGU5RapUVTVFrNRuPL

9UNApEIwi1cCtPtUF9Bd+UdYhnXPMYevyr0fXnb5pIWkYJjDHgBymZM404bgFj0/lY1TDgMw4LNE1/MZf204Ci1LYJe0rEja3rYgm0yEk22mspO27P7+0HYdRwWGZ4iODDpyIxa9qnNhlwWtcNwwuA2EdXICmgwpWlKOKKc2aCIdKcmKbGFTH2AyNElC8LZl/ZZKe0QdLPzWZWeGMYRimWmeYZ1pZh2HSFhZiMQoA9YebAbZ+bmMYhcVq8xYlsno

Jg9Y+bZjmtJ0mzZlVuJTImCL1jN9ZjomfWKal0phm0B3gvZqzwqdxJbopsAmfWcyFdNqyh1mV3WndsAHYSCZZiSH2OfOw3Q/D7XI+RvNY/pw2bp2AspnWEdtN/R8VcNiYUhGSZTN9sKIp4AuwHj47tEWTWc6Vmvg7r4ZMpspWW8jdv4/zbR3ojsfLlVoeG9H5vwonim6Y7w2r20czgNmRI5YVq3a/rkem7N9fWk3+OrJtqYRx/efk8Xs/G+fq/Sh

vw2DmNy4gusi3SuAVX7D3fqvVuk8f4FhnlrYWECT6DzfivS+bcN6Sx/uXHYCxQwTAnDrb8A8KZL3Ph/NB18MHB2RnECcqkH5VxzkQ1oJDwGoKgVQxGKkRz20dosUBy8L5+0gegg2VDRw7FzJqK4kcxz8NIRAz+YBv5UIfjPKMlwozy0YXI1hQjFHKIpmFGW44Dgo2IcgwR49yFf0oYYkMzMcGXAgU7HRKC9HWKUbY1ocwZZqXkWbRB5iwFuKseww

xw41F0M0RHJhpQphe2mPmTYc9hwxxEW7H+O9QwP3LubBhsSwDxKdgOWefdUlhO8bsE2As4EENVkUxJpT4E8DSRQ0R4S655lzv7HSGdg4NJKckspLSKmlCSPE6YTt8EyL5P0hJgyUkjPSXHTJyQZibG0mpR2QcKYDKSYs1pNj2mtHHCkUWj5D4MOArMimMstLrHegBI+2sPEGJOb+XeqSmk62uIbO5DtHmVy0dc0ZYB1E7DDhoq5X5Vb/IeZZIFCt

XleI9lZGev4nnQpwbC/yAKEXPJBcswuwcXJMwilzFJhCcX3MBQSicoKXJ/yvKnXOQtqV4sxcC+lRKt4koAipUWkZonaMNvEzK8DtnrAZQcWWWyhHANfqpKJWLknSu2AjVWTMZgLOGYczxxzUXqo8obOIWkNh4IlVZF2PL44uSNWY7x3cALIwdvK46Q4GW5i9kFbp5sHW8z2JzWpbNRZhTVei54QyJWq22IG5OwaRZ6xtSamVmzTLCtZgU0YMxvw4

O2bsRI0qyXvQWJypF1s+YPw2BXZ5BxpXG2dsdeVFsK3zFvDWhhdbk18oWN3QcIZs6s0mK2qtuTEUp2RQasFcwEh33FQQgCqtjbhlDB2rlk6Ml8uSC0oNZSCm9pcplS5XKLJ6reR7FyuL3L+sKbvLSzw91WoZZetyGq/m7wHSexNG6VkkqjHzLYiR4aIsSKrZIWtvwjCAUfaV8T9jIwpWU35VDs1jBmNMse1q2mbopi5OumVS1PwQarGVAjn5Oyld

23DmU+14agz01SJHl1hlUguluZ6UXTtGOXYcp1nE7O8Qeu2ebm0bMo9h391HtiHFOojBdsif4TMCmndx4aZOLGkUrBTKj/LKd9fohCNw4CBG9CIcIU1vhdDtD2BAAAFEzzAzPcF+EIBAnlsK4QIjOf665SKlAokUKikAaLoAAJoTFC2mRIcAjCbAAPqSBpGmAAqmMfQAAhcEkXixiXgBJKSMlKAsgUoZf9obklhxPcO/kBlnBzAmbbLW+ZS2iwjP

ZZqCpkiPgxeO65nlvKPETM8euYnRPyyijFT4DV2TAkKnidAaUMpZVrCiNEHoCq4khCVIk5VjxVRFGKVkoJJSbhm1yRyPIFTTaFAd2qx36r8mlJIHaA1+TKhRMNDUVNIDjQNODc0loEBngxuhaiToSsQFwOsLanp+poCWvtFcqAn7WUDtMC6D0Lh9LKPdeMT0XrI6AyGHxICVoljLEjvGbn+R1nyiDFsJM0Dtn5FDGzC0jFDhvEOK4gTIBozQstVG

2NAS4wBvyQmxM2xTu+5TUFoxkYFmA0fEpBS4gAQCqLOlQU5cJD2KuvJ8sVdLq9kB5JUadZLIk8S3DaigMWoXQ7ApMtTIhiV52n91uTm28Dhh32juSNxCuA8xYoKmYWXvQm3WYUSN3Osg/OVQCtKh93rpB5kfQ3Y5Ob2xYQt6FVaw0cnDrQw+p4ffAjPmrY2/lLb1gsHGp0l4j0hsWmqZZE8AQxrR4nC+SeLynpv5eW+GyduMY9KSbrJ/D2n5v0ei

5MxvLMTS474JUb71PsvPyh+DzrlzGydtoNV0n6X9PW/dnLvepGlJBf9VF9KI36fg/Z/ByFnzJfdLS1H4H5vp/tz4kbIspMJ3o+J/g/t/pnmMpqCkOmlisMNfueiHP3qASGqft4sknzLmGXGuo+CvlbryozIgRvsgT/t4tZFwgAgFEASAYQYmsQWMsBMzJMJrlilQSfrQTBO9AkOXFMpah7ngWvsfjPuAewXXKZOQQfvLCwYIUxtsFcLpF0mPPXrf

ggevqwUIU8jsGOAngxt3jfr3nfgQaoSRspAfOar7t+LwfHPftQVHmocXC0m/swavvoSoVIT/EOHzB3gbizHAZxlYYYT/BFOgeXHxpfJIY/moTMP5IvvLObmzD4Q3gYa4SogennG7lomEWASRpcHegfNYeXBkUQWodPGHAcIvkAYoXocoQIeETHjLMjDME2gfjofAX4UkeEnEIviWmWkLPEUoa0TUZknXKLKYTwQUTQUIVGHEKdGIZQU4VUV/oUdb

MZCUfYeUWMTYUsXUYjKjqJs0b4YkQMXyrGj+FZJYmvOsRXimufrsGOI4bgZYQcZkSmr4mHFsK6tBhYZnI8YsSapermPmJVnPBUZ7s4dUU8X+g2qdBpvJhcSgRelsQ0fRnknsQkS4Ycbhp7FgWUr0ZUf0eCRickEBjgqNh8bCWwcBKMLmGhhZJqLSZqGMGSRMcNsMCSbMfcT/F7HkVZELDehSSkPOvpqCtJnJr6lMqBiahwRpOUazEKSkCKeRnguK

X+vEjMEOGkcAXMcKZpvxqLNbCON3CEWNsCXwbzIcNqdsrqb8b2uzFGLsF+safHFqWxv7IqXqcbCOJZERqEXMc4NsCMEiYikbr8TIe9MdCpnMKCkMCpHaZSsrKrjOmhpcPKb7J8cHFGbmIOg7g7NbGFOivvGPjnJGfPs6Xkg/DmfhtMIaaST6cWaKb0jcicsjCZGHDGX3A6YbFGcUvsrqjmdnpMvbjIpGXEF2d8mzC0jmfEvMPGo+qmRTHVhYs/Fz

LyWOB+qdBmorO2WmaMMEmccnNzL8VqkOEkEaZGdsFZEFAfHSkkMufhgcAKVpjrrpAhrEcMKdLzvCQkhZOadyQylAV+imdZAJheskDZFeIsHSbSQyXMVMTAQBXbNbBwTnmuXcT3iCQnPXMnHwr8fEpGNCayqCr2jSf6aJmWVaZwe/iFLOagSkDMV4TdHqaMDEbGVRWMtxiMfJuSTOj1hRZuYYqap6buRRuWZWjSRBZBXLlqkmd+XMMaj2v5PIc4g/

HLsbI+IRrue+dOsbEOJmYOXMaQVpEKjAdpDmWHqceRkpXpVpaUQ4YbvmCZbvGZYpSxUbA5asV4SUvZWpeZa8oZuLg5mZv9v6FZvgDZvZnKE5mgC5tThhJIB5pgPhIRD5mEORJRCtAtBAAWAgDAMlkYLMByLgKxGYPQAANLYBjB6gNhwC2b6C5YdASAFaeByT8glbOCJxWQRiOUcytRlAGQwLbGqQOyaguoLz8gOROSE69ohi2RYFKllBeT3CDa8A

l69wSpDITZijfYCgzZJTzYQCLb7DLY06rZ5RYg7VbbQhlQkh7bUi3ZdT3YsgJRNQXavZtQza3WMj3VSi9TPZw7I6DQfawAjSbW/aTRM50ySSA7A4I4rTg4ugLAw7EAvbw6YzxQHTcCAaYEOwOoMApjxgXACY42XSPSZiQS7CAaWSIzfQU6i6+aAx07NhgwWYs5dhs4tQDic6jijgDizV86JXI2g587C6U5i4ExEytikxKEy5qxDkJAbJOK8K4Uxq

RlDwPyHxaERQDhK0+loq6QUFeFCwHxa3slbnZ5hjvEMbCZG2oUmlgB1bgYspkJW26FoVDBDEDg2Usw82y41l4mmw3o0w+lbDyWtaR5hxO3wHOClq7zm1eFe3S0+mcIjkvldLh2cbOA2Q7CHzVqx2qxRklnALJJQXG1zmBE6T7CHBiW6S500J1m6SF2RmRHyyOLq2RQdk13mV135gN0sIhKczV0zy12WxF3W3xzOAv5hRob3k2n9350Wz10+mL6Vo

Fo6XVZpnt2KWd3D3O023ODswqTTAZn54z2D3z3F2tC72EmhjeysoNmlB50n1d3a0fL5hzD4pXJx330d1D2RmnG7xobTkSo3qf0b3f3a25lDgRSsYzLH1f2n0j0dl3kJCHDEXQaZQwMgNwPb2j2/z+TmSX5lIaXAO8Kb0/0cFxqCyAPoPEOgNn132ZTLoH2tlDpAW23r3UOYMR2ZQ4WBxfnya32sMD2wOP20O23OpINHkBnoZUOiY0PwNbmJwRR7C

jnDCENsMyMcNp0AR1EhiYE51t2CMYPCNyNznIzZrOoibQZANqMH6yNYMIPmQ0URj74W1CFEPqNGN2Mm2+Kq3y3uLSM2MaNTp1YBTiMoM9JoP6Oz0kPa2BEv1czdHIZznWMW2BNKF1Y6R/27qUORMP1b2cNlz706RMMRir1JMGPsMeP5PcOQPfnaZlNRO2OcMpyhPHmoOJPn3JN5KNOaPFEDiL7qX+MpOVM9MNp4PKN5iDNdOpOVF1aDj+SLDmQJO

TMF3DNBP1bdx4WLnLNz2rNpPHnoo150osNuMBO7MzNJDDmNLJ2qPlPuN5OaM7zIX/lh05NCP3NrOPN56UpWN8wL4e3mQ4ku1JDz5fN7pAOmVeluqBw/2fPrl+250NpOxHpXm7A/0HzdxjpHO511ELOHPQrOWzMTK17wsdnbqH0pLDFot1yEbszhlsoIPcY9wUOb4EtzDGzEPAoPK52poDnPwbBouhwThm0K3cuhzlzks5zvQol7Mv484FnMPcvGz

+JQuAs70yXdxazyslPHM0Y2SLCAF0WqvYPTx4JeXEYMseGRjJmhRGsINzN5hLlLOksJIUl60rNotirItYqlPn0yzPCKnv6TBovO5OzzCiV0nHNFIrrqkhgwvbDPDN0KL8Pp1ylhNTO8Xn37NItMFcrHO9qZQTigvMMws0IOtavHPun0ke2xva07w4L7AKWhT0tbkSKIkkVjgwuTWAbqkf0yHyxPMRyTA4HGOZtVJTVAYzUxopAHyGX57DueMmN70

HDtp6NUKcHwrdGEoiN21My0lpvaQRNrvKy0r4tosqXB7hsRvG7TCT1mHKxoujC6JtOqyTWMFat7C2tblcwJDMs304pzBXih33va3ZHdk8H8PgbkrJ2Usgcyz9PmWHu3IzzdtYnSvnNqTzNgcEI3o4UrVsafsmMYdXPfP1IOW/uYa0y+UEz+UmZM3xTBWhU0eQRRXubMA4TxVeboxU4pWBZpWVAABWtmAAGg2A2JoA2EYNgAAPLKAABaQgMAeoeV6

WHINQVQtV+WgQhWTVGELVFdcpA4pi+kawDlQGMlAcGych7TEAY1l2hOgj0BR9/I81PkbN8uglR861sU12gIZ1Eg+1mU8Q2Ux162fn6ABIO2V1lUN1nUH1zIPnCA52413VAg7U714on1j231SNf1b2Q0gNX2Y0GIE0gVM0kNC00NGEq0606AuAEwCNOXlXZQAY7O+YZcQU/+GOeNaAL8d0uN6YJN10SSBwmuVNv0wttNNOQM9OjNYNHYLNMMyO7N8

MI4N0uwi4fNIOguZQS4IuSV0VZQEu4tTO0uqdp3CD3qJ7XK15QpudWqy9/5luI7lM3L6sib+aBHrQUt6TOwyrieaHaF33Gwss2dtezl8uQG19WzHZE407WwUDFHelCQkPPq0PaZWsSceCvdo4APNtNCiw+79ZCLHRo6WBA4k++r1bWwybFkAqdGomyMoKf8pa5H7MyS4UudnC5jMdlcjPcxzPeHps7PxzITOjmL0KBFGhWHyByb0wBpatilkvXy0

HdkHZqiDyN0brR8n3cSstmy/Ggcud2R3PxDzlYqct6tAcxzzTYvWJwEoK5v+vH32Lva/9rPgGDvevvjiehvHZj4EiCMnvP4TvKrudO8AUpKlq1kQfFvBvxzVSPDCPq84scxfrgJe6a1CDpks6Obc8CwoKafOlIUmfW5Gyf9piBfyHRfbPj4r3zue+WvVcOvYAyQOCPuUfOr/Kpk1rQizlrfuCd71k3L4DuecLhwcuMhj8glWk3Ll6c6g/zfP4BpA

U0/BSdWhwHh8TYPE/y/kL/3orowW/PFO/D8K/Cpa/I8Ke0lLpJ/U/5/ir25U9Zs4Pk/Z//GF/icujxLt/b/kqirxiRbAhD/z34ukL+UdI/jAQzYQFd+q/blg43wYd9gBsA+xhMnd5+xcet8V/iAK0gz8EGGdTUIT0Px6UsByArciEzmCa9xCi+JAffzwEQsPONA9/tyzl6WceeMGYgTANoFkC6ijbZtIwL/54C28FFX2PwLdQX8u4N0AsK020I78

pS+tYCBzzwGt88EkGXYp71eKslSyybayDLAdh2xJGRAkRirU2bmsyB8SU6I5yBKgpjBPfdjMwN7QEDpBXhawSkCkollCG1kJmCMAqxF8oBYAfNgJS4EmMQm5kNSJoO0jJ5hw3BNjNHGYHxsU4SBEKL+X7Tp9mkHg9wvsCtbSVm+TMQtmP1SRwC1klvbXpLyCjoYO+zA0YOzBDp7pSh8wJ/lamYHulA48wUMEBnaGHxPeU1JPgEmYGTk/mQBZvpOX

h7X9eu3A37hYzZLPcwAbeV8lWVAHMDCSHQ5Ye0JT4iMl+pkEwb0IQaRFsBiKHfs43kH/1uWuwjzoYOmFoogoF7E4e5w7oSE9KNCa4TsNuEb17h6wsPAFCYo9lnhstO4X4P5Q85uK+LPoVwnyEYC3CEKfQe42YG5DA4XrE9HLk9a59JWGyZgVMRaTwcIE4PYxB+2lIThCh2CN4sQ3BFUJwMkYSwZKx1bywTYnVN1HLjJGTE4WPrOhtSMHC0jE8lHK

3HuCY6ldmuDHcsGFVMyBBnMpAVzKx3Y4JVvMxEXzDx1KBBZyg6VWzGwHSwcAAASnhHJB6gNOkIXCMVkGBaNhyQUfeLkhOhMIIABkKMMbF2CL5x26iAKGaNs7cAAovibGi50Wqq1/IXnKbKdkShzZUo8QBAAGIDHBdcooXP0cVAurEgEQ0XaqKKDuzxcfRT1ZLgl3S5HYExGEJ7DlxS4QB3sqoArsjlGjahiuf2OjmUFmjzQBcDoWGueCmANdfqTX

AQGjQVAhgIoCvbGrjiugKgkgBNDscTWeiQQowGyEeLSzG4IBFuVOOmo2AZrHdjQ4NVnItyMSjhNEAEDZA2QgC7cJu+MMoOWHiqVByQmIbAFAHjCoAmQjAAABR1g4QxAAAJTIAAAOhwFQBPjUA+gVAAAF5UAl40gMQG0DBBoo6gB8c+MWjvjPxIkb8fkE2Amhfx2QZQABMfHPizArAXsCBNlAUBUANIMcWeOvGATnxjgQIIePjDMAQJ+QfIIqEgnU

BjQdWagORONBfB4gZoCCdQDqwmgTQOEp8fuOehHjOAqAD8MwDPF/AKAFEvQPgFvFsSgJqAQEDABAkAADYAAJLIjOBgAwksiNJLElATCA5IVAIhLUCBhtAsVPiZJNEnwTxJ4kwINuFIAcA1Jz4jSagAEmoAAAPKgE2CoBwQtktgGhIAB8H418a5OEkOSnJLk0gKgD8leTFo944ySZOfFmSRAj4qyU+JslfjiA+QASSaHyDCSTQ74j8XeIgBCdsp4U

yKaZLHExS4pWkwgEhN0m4AGgZ4wySVMSnJT3JqU9KSBOyk0hspJU8kK5PyBkAKJxAbABlLYCaS8JCAAiZwHkAlSgJkkmScADIAABqeSYpN6kzTlJqkiKQVJskABCbSb2D0mhBqpWVa8agGsDEBQJV4rqaQDmkNSup2AJaaCAylvispEAKTnlPGmRTeJZ42aQJJ6nXThJ2EiKR1KCl+SPxzkqAGwEWh1Z8pkUhKWBKSmQS0pt0zKagAADkUnRGRDI

KlPi3pXwYKaCF+lrTNJdU/QMxLhn4A7pH45GajJekYzyQfEwmYqGxkiSxJ/0tyWhKBmoAQZL48GSVKhmnSUpEE0mUjJRloz0Zb0z6U5NxmQz8Z0M+qRQFSkuB6JCM8mULIKkiz3JFEuWb9LEmMzXJdk1mezNfHOBkcSs58UzMBkBT2Zj4g2fECNkmTuZ4E3mU1PumoBspT0lAJTPEl1T7Z8Mh6blIgBuyggYQVALbKSmeySZCsmkBTNWnoynxHsy

6Q7IFmIyxJ7oSgBKL3EHiuJj408QgAvHQyjJQE18R+MSnQT/xkgMSY+ILlSzIJRc2CSXIilbTAwKEhAGhIwlQAsJYkoaSNMJDETSJ1Es0JRLIm9zGJ9E6gIxOYmsS/pac48SrMEn0zc5kUyaR+NknzSlJoIFSVzM0l1yfx+kvaTAFnlRzopFkteczP8nOTtZ7k1AKFJ8kAzQQx8wKfTPPkfiOA1swqeZNimRz4pksnmbHK9neznpb85+cVL/kbzt

AlU4gNvPFkmSY5Ms4mXdKdkQBWpvsv+UzLOlfT+pg0wgPhPTljS/5E0rKlNI+nuSFJ0076SvJWlRz35qATaWVJ0mbzdphkw6ViBOngT8FUCxaQ7Iekuyn5ys6me9POmizWFOMrWVfPwAgTgZoMuWU/KDl8zoFCswWW7MxlCSBFf8yRbTManfz45nC3CdwtpkKKGZf00+SzLNmgzaZEij+XbMumQSZFEcshTxO4WizNg4C8SZIt5lyz+ZisuRbYtV

lgz4gGsiKYIqPm6yjFhkQ2e1N8nXyAlwEy2RovIWQLVFocx2c7N/nWKgJMS6RT/IQXWL/ZCAQOaYuDlfy4lZM8OVEvdlSyQ5MC8mYnPNCcAoANIQgEYEghD9+QHUnIAADE5oVIXqjcB3FQBeIRAZQAmHQDBByQFUPrqQCPHuAel9wfpdAGVAsg9AOQXAI6CYBQ0UaZQcEPcEdAEAU59VCedxMznZyrxu8l8SBMLl/jq5pc45RXKgmnK4JQEjeQ3K

bmYSHF7czBV3P7kUT8gVEmiYPIYlfBR5jMnZY+Knk6LDlOCqSQvLkkELFJy0w+UAq3mGSil+8yyUos0l2THJJ8oKXZIvm3y/JaK7FdfNCmPy3ZiKp2cisYW5KoFbC2BT7IRVFSD5gCqhdtJAVgLapJSvJTApaltTEFnU7qTxL6kuS0FGCwiUUvnmoBZJzCwhfwvwCrzsF1kzSZQvKk0KDJ+0+hcdLqnMLUpkq/mQktdkyqTJb05hV9Jum6KgJJss

JYYq8UmKyVUiylW4t1U2K+JWMn6YfIJlEybVsiu1W9O0Uzy/FOs81cYudWsqoFFix2bausVAqxZAaz+VApcWWKil4a9WQ+M1l6KMVZ88JfrOCVcqhFIitmWIqCVWy3ZTitlQjO1VFLklga2JeypymcqMlvmbJVatKVhyrFSS6OeWtSXxyKl/IXAEIBBmqjwgtS5jqKIO681ZQVQAbL5GRwpBxRnmTbhOKnCbcloso4oHxwkB6gAAUhMDwiExZOmw

NMFUFXVxYFgzARIDUC0gfg8I2o+qlp0ap6jFIBYBwdMHFRXgcEFkF5hhFqyMp5mX5eGJGlMjWdHRiYGWG3z4xcwtk8wXnLcAWrjrL0OCKatki0aO5sabwDaglzC57UgxgY3oEdVDFAxUNEXS6tGMaX7ZYuGXdMc13ahJc7O2Yx6h1DjF3VSNkATMb9WzG5jPsBY4GsWNBqziAcc0IHBVxWXBZqxtXRIHWO9CVj/QTY1AAASKbyxsxvY9GmuN7H45

6lgCRfHbH3JVdyc43GmluMgC04pxoMGcczgwjzikcHOK8L+AHD/ENuUorbouCFraah1e4MWozigiS0zuaTKYhzmeD4IwoSQdTdTEjJaU8kzKZlO5HaYexkOAHB5BRgxHzB3maTV9heXM1axlYjGYfHzCFiHAHkLqSYFcMjIgVXir5OTGaSHDUphwWyEcAfG0i5Ef6fpZGKBQ2AyUeGahbcs8BdQKC7SpaNYdMPX4/tEYJhEcN5uzI/w4gABZ4MET

Mjmb52nDNXIOG5pjg8E42rNNaWXj6tUk4YDZD/Vm39beMi2gsFmjFSXAkgPub8NgQnxP1M6RJdDABEOAvqY8M8PBBlFVq5gbIqqBel7G0qHxrIjWtSMyJgggVngh6dDGqTUgEtEWYYRGFGAPi6R5YquP0uGFDRhkfwjcEkWUx/CL4s65yPMCdCWISJngR0PMMjpsio6vunJQCmuW8GqbScJKeHfjtRwpwNIm2pHhrXqy0s9gY4HkrjrDB06kdjOk

naUDrh2wQwDsEYIvhF1fQTUtOxHYTr52goyW3WC8mvA2Bx1/03O6XQzpR079RYBaRfBSWV0NKadeO9XUTqZ3rDGKT4d6DMC5iFs4dRugnRruJ1y5A8gcVSCcURijgD4KXD2FLvt0m7+dMEBwYBx/Dc4rIyMbFJklxRcw0cPycHkMRUEQ6U4nwh9PdsTJHQamVW6PnpTj2K4q4gCJRhpSbJlEJwrcUtMnEthy5s9oYXPUnq1hMZdMx0ULXMLtjxbK

ipBRglXpk016C9+PNPPVsuAv0w4Feh7Tns70K5a9P8dzrmgQyFtAOse4fR3sT1j6NKgGvBH4ntGnQJ6i/SvQnrz3J7RUM8ehjJuHDd8/E+fLPfPp31d6X2DiZOPUTm0tDptnGNvfHur1L7jcTyZlIRhnZjgW9aFJstcmAgRQhWgFUrV8Ush2x/4eCbsaWhwQSUdgNov1CN3JHhaYI3cZvYNUAwWQ1SZ+94bOjm1K6w4xegvWgZUFvEMyv4IknLiq

H/x6SC2s0iOCnYIxAKSMZdtUL8Gt9SULMB5Iyk1D+1/IhwZg6HrHBsHJe6yB8C0kuSrcUDvpXFBZHFRXAtYFWUyEzy9iDh8ESqPjOGFcbqow4lkQtg+iUPOVQ4t+sos+qgNtYOyOhuQ/ocUNTVnKfpLOpeT1wxE30aZKw3odOgGG7Dp5WdOnCFa55wo7MXOu4fkNeHqePh88n7CuAqMoSx0NfiEZsMUpwjG8Kjodx5GliBA/IuzExxFFijnOcVSU

VxxIiLr5RIWCAECFXXOBmloWPCKFgACODYKoLxDGBQB4gmgOLEYFIAbAjwnSvLHuKvWyQb1hkAsHXAeT2w5Mv8SYNjQtHGIG2/WlrPLBGAOiOsvAdVL+GOjF7y4EYeWNZzdHjr9gM8f+ABGHCBw7SLwTtdFGQ2JjZsm2fzuhuDErZsN+UXDdtnw3DKZoRG2jXFxOyvUhQFGl6mRrerEa0xPxsoIxtE1XY8uANAyD+HY26gSxc3RpeVzE1VdBNkOX

iCJt2gC1WQEmtQ6dFHD+bIAcmtAFyxGUPQlN2YIDGhlzDZiypP0McZuMc16bgY04lzUZshgLdTNy3EtCnDhHWb0YDY9cfZv25GZnNUuNzYbADrrD96YUSnapDhHNZ3Nre1/KEOThCptdgcIQlKemHGx/6gFNWv0zLgaVtTC7VoL2gdh9MC2h8OGMkn9ouDRwaGMMArhujaRzISptCpOTCHBRPBTLY010K9ORgfTLPY03zC1hdbbtgqJ8o/qnR1wr

gYQvpvbH1b8N3SB9dHU+C4LN9zT0wePCdA2RoYgo1+wNH5ox3swce/uuIOVsAKAdGdltd9HQnMiF0Z2WsY6DrhZ3zA2dE4FpLJQpjgZNks8YCJCiAM+HHw+wehJaMWAtI3TE+jLVHvlPmpcK3W003fVDhDpU4tLScxYaoTssWkuh8KE8h3M4Get1pPBJ7utEd7NzhiXtGGUe1lxucQu5vs4HMEFhXdNpSHg2xIydJk4DO2Qh1wiE+l8MLuIxK+Zd

MfmdgX5n8D+a5h/nt2o2iKDoN81CxsdLDUgi0O/NSsoLi5+AtuUIPapE9CQ+igETAvYFWMGyDC8nnZpXAwo4eT3YmVAuoWIL6FuWiobRyjxNE4YDYFcDovgWSLv5zC5xivM3QLBGwRXBGFzBZFcGHVGYC0kTKqRDzS5/wbgy5qiERLFkOOjOk2THGnY6iNtH4IEtKXhLoYUS2pbJHhg8wUYG7apf916WhL0Wp9WJcl3oo1ItLC/JMmcrWWdIBluy

yrsfZElQhz6l9W5cUs2WVL9lklEzEHAAsSkosAk6dBUPNnJEhwA+JeW7MnIhiBaN8k3Gdj6In9AGOTC7iJwuRKaJqNvJMB3RHa1aUJWUojHMgAEPoA4ZBgUg4JRgcBSZLSAzofOxozaisDfdqg2CNXH2Rx1dKcbGY/1OSoacwgdTvJCEDjiZQhCcfdRKMiyHhN6ESQ6oEZ+GM1wa/NbOO/6d696nY3IYtQc5NUA1suMcdgI7WG6KQL8yuhHDsxBL

/Vw42daGsLXngkZQDRsH+JBRD45kaoSdaetzWLrI1n0uBlaHAR2YakBQ4bUzinXAbw1xaxdqUaCXRdUxpRv9dmvnX4bb1sBmgbeIGmSmkYR6xjZeuXXtagebhGbmq02RBU6Nra0DYRvbsZUp/S2HLX6Y03M4saCQ2XFay+bQwclmbcvxZtU3TLN6MhlzYeTMoc0qLFI1yOMzhVaOiJ+jvoGswCicjkVQdVOo44zrij/mVKlV3SqJA8IxVeIPxyBA

1BNgvEZwHFjqMwBnAWEYsPgDGDYBiwTEC9egAaqDH5IawSMFEUyiDgEY6x8bDVjWD2JLyRiMKGOHq3tZnqiYK0ZzDzA2QFcbLXY2Ot5Dqp4mRiePN33RwXHJsaATatRtQ0pR7jmGjCDlDWw4bwx4XV41GPeNljPjh2bqAl3+OQnfjgIVMU3ay5+AfqEJ3LhhBY35jYTRXeE5xvZMUhkT/NbbgJrWgQ5cA6WTEyiea4SbBq8GcuJnkJqY4STPY/rn

2IJx3laEySHOxpvpPjiRaSIabqyd5GQATN7Obk1XDGPY1+ck9uzTjBFPi4xTEtSolLRNMR06tSsTorrpOK9tfuYQ0Sw7FW4nQZamsO8g+CmOPhkL/BsyDgLDhR7+9UDl+i5FgfkpF8I6JMtQiuBLHg9S1wg48nzD2FrTF55hLg29Or7S99JQLQaTrxzAJ60iaYDemSCpxsCe+SMKVb8GtVGHACFOHGacZYUqE2wV4i3H0HjbNQ/u/hw/CYdCO0MI

jm9KRmjgYp623O/loHQEcpxFHrD0R4YiVb2xBYUcG6NGbSZ/wBzujlh8o7r3tDTLuSZszeyWu37A0KjZrD/rUIiFAM+YdmKulwSjXnUYUaI2ZbXhFWdM8GTwScfLitD/dPl0XYNrFhmcJdET0PYqUoqxPIhgqXJMknqxDgs0gGlOAWFDStZEr/N/iwkCcu4VDL/+UcPdpk3FOG4V4Mpy4PFa8OzahV4YPU6KcS2j0E4JupXxd1Vo4YPGQ9N0/oYl

PmnAzvSoxUsjJIuzIYQAmpHGeNO+nLTh4YLcpvu0RbKz3p6U+me4HKzFde5J8KKIfoJnTT/p4ODlz5sfrv4Uizw1DbiXIn6Tm0pk/P3FI1TCOgOClbGTeP/ioscXQE70pt4yHVZx54WBG3XWutjiD9trhBfwH8E0wO3HmjjprINgKcBs6a3kfmPKi/6Q4FIMSS5pc8LDMVMLpqtKPcEukT1HKUJcDhiX+J6/Usdkx7wB0mWmlwS+/BEuEMjL9Lfc

kPrxpIMQsDl3rjjzE5+2ig4OGHn/rZJbwEUR7eU6nT4vRX3LiVwg6CeXB/DsmIDCK7pfiuSXwRpBixlW6fOKBuLtCsq71cMvJXJjFSDdEQuDVXWuwc1zbSSBRF+9P1vMMkipPcs7XycEKNT32DuoXXt8f5LDsJsHALYPzf4pq+tGBGzLiIr2DJkT048o4ybG2HmFjeG4G9wr8/RODDZhhD4dsQhK4wzfzACH2bgqzc5njeDJE70Q+F9tLfRly3gq

KclW70q7tXUOYCW7rsHD90Y3Fbttwm5mehmxezZoWO5C90CMB3rb+N7m/WE6GN9Tp1SBQynfplM3g7ud330OMEuToHu+kk25ndxuc3zlP1ocAtRlFgnmiftxu9ncnuXBeZt8uokMqyWb3Lb49+25Eau8g8N0Si/sGwJruy3Wbod/O51N3pK4IW/YPc4/pAfN397/nuB6KYNsoPqlt98B63ecjUK3I+W+ZkVt8jlbIVVWzh9yOOb9JEozjvtxKPLr

0AdR/MDUF4iJBlAmAViMVUfPpZMAhAIQJgHiBGAgQPIXo3VXdsDGisXtxSMDwnD1YxdOCceNMbWBhh5KChtUtpfXv/rkcQ8M1IjEuDsXR4BNPY7yAbR3qNBiVjqmuKQ3edrjRdkuyGIrvPGq70AGu7thjEd3MubdxLisao1pdgTndjMdlyY3/U8xMJwsRhBBpX2IaPG5Zdieq6z2gQC95++JqRxgVvB694k6gHH0YRFNg3LsXakPvr26T1NN+2XY

vsGa2Tc4zk7fbhg8nWxm1J+7Zqxiv3pROmpzZLk/uA93TNtcRxOj8Slw9cEYG1+fQ6+RuG4rp54NzR1xUWww2BRMgfGJ2GuAEfGehvqzQwHwVDw3oDNzWRiWQy4s3zr0N8W+je5i2eSrJDauBAHrRFaCg2bgBJZaAOLgnRrpE1zTf+2U7pmNZD3hC69DFBvizGYAwWwHvPDIWM98tZyH8nsly8rd+AR/fyULka9mJlEIPIei70Zyrqe8Es9fL5cR

Dmad+YTtwoFqUMLrp1z8wm05mnBMW/D3P5DjLucKJ2cRhlDZSnwgy8MEh6/gUnSHakzugtRmlafPpe1IIbvjDw9gYGXTHIUuAKH2usBmsknDe97lMopF841QjVyloLNmBOBG9u3bstevutHAdeCPuGIVzI3DRF+c5yRkrztbiO+12MrQIk3+v0/qpWHDvX+SpjFrJBnAcF6G0hDo7X7cuSyPkg34GYIl9ISEmxkbv51B781Y6RZHaVig1KzLoHsU

D/KJtL76Rhh/TdPW8KxZGAiW6uYG+19YY/koh+k/l5FP/JajJSPOagB/MM7Dj/B/E/7VQv7I8P6QpEfB8My3mazTV/gntfr36NegINvBL1uiHUYQcpYGZHqlgjF98lr71dDoRlLbaS8f+RwDhlndDG9lKp5rDnhmfxgXEsa4hY8PZs/QxX8GUPDUNg4Jv5/h3InygZuPG33H9f3J/a/4/7P5IwgVy3Thr18392uOk7/R/h9Cf8Ph6lJ/uaEOACwI

wE9zyW2wKv7f+G/n/4SkfWmXDYuOeI+A3+LtLToCwErm1oyY1sEqzs6dsCOCDI+/hL4SGv7nEbVoCgpgG64xepzR4BBYAw6F0G7J+i9IlDh7BYBFAbgHDc1Ado4gBohAhgvIyMGQEK43CKwGPI7AduyxmwEOmiBwPqFsA6+JyMwECBVzPgHbsRSAD57AX2i5BHaKBsDz8BOAfIHCBPWs7itCZ1oOK54tfCaiyB2gVQGyObePK7C6HQhGA4OpgeQF

yBFgfb48MycCLrtCdgSwyaB2AZQFsBzRKkaQActkKK4eXGkFQEejHMR7q2eRjFQFGFHg15+YYAAFhyi1HhADOAyWPoDkgsnOSAAAilUBGAzSmmBYQCwIQBVAsnGmBXADYFqICemnAdCe2zVIMAcEU5NEhQeakOBrvqESHeYAoXZg3rY0qnj3S/qNPsSTZiengqDzM6iEv5jga3FXS52Vxq56WeGGg8ZYaNnqdR2eeGrXbXUsYo3YuegJn8bueKYl

57bBDGr5692zGvlyBecJp2AImoQWVzhefGpF5omuADlhfU20PWL8aOJgl7U+KcLwFkm3XKgA80G9njiZeyOAcDmwnNP8F5eWmgV7n29NMV6heN9mzQVeVcNzbZiNXoKYbiDmqKbNeJ3BKbBwP9pxjfc8uOXTEkQUNeZqQVVlsC6OygXdaOIvrpWSqQEwee5hgzfGriUWXSJWRs+0hq5D0ID8PMDpoUwc3y6mUlm9BoYsBAwYXcdITyEeWjIdS4He

DlEHjwonMLBq0h3IQyH8hLgjuSswt5lsBruXIeMG8hkwcdAyhRgguS9eGgjqFjB9IfqHShcBAEHYewQaF6sA4QUR7BBJHpraFGlHrra8c+tpUCSAqoslj0ARgPQBTAXANUE6iu4qJ6GQfiDRSIWizPqzlwxnM2LWk4UJ6Q2Q0cATSqeeDOIz9YkGryAcEGpisLtC4GmZ7eicwXZ7F2CwaXZIgIXJXa3G1dpGKOehGjFxfGJGqCapcZ2HsHXGznvR

oQA4JkaCnB0JkDTD2lwaPbg05YrxqL209jVyQ4DYLF61eqNEjj4mEDl1ydiqAPMDLhu9pBCCwr2tFajip9pNyFeMIQzhwhZXgiGjgFzBDZy+O3MKbxBnSrqISAWEF0BZKIIPoA+AWAGqAPimWN+JMAJ4ngCPiygGwDhALkrGDmqqoiqrmqQICeKgyUnGeKqiB0jNKoA0EUCC/SvEqgBMydYF+FBSPYKgAUA4ID8ClSSEkRIEAwivQAEArmERKCAC

ETBGYASEQ+KUgHAAQAniFANJBwAh0soALKj4ltKER1IFpKkRgERRHQRqotRG/SIMlEDCKH4gJFwRlEUhGoA8ETwACRQkSBLyR0kfBESRMkVJG/SFAF5CBAh0kRJ6AL4cSA5qlEYJHSRoEUdKoAEEQZGyg7wOsqaAwQJBFGRQkYmocANICqBPhBgK+EcesAE5FMQDKvXJRAgIIRFQA2EbhFBRRETxG+AgEaED4R1CvZFKRv0u4DCKPwKtj8q5IHoA

iAAcv5GARjoA5E0RsoIwCPi6gNkA5qokSeKuRgcswBxRSchQBbK6AA+FZA5ke5HBAnkTAAfh4IGtBBSzAL+GoA/4YBFsAwEaIqoApkQwoDREEfxEwRkkYhHIR1MqhGuS6Ee1GHSQUThEsAQUZxGHS3ESRERR5EVBFURuUXREMRzAExEIALEdEDsR0UbkBrRxEbxFbROUcJFsAJUeJHjRakZNFqRckTtEHSD0cZETRj0SpFniuUZpFMAWSlFF6Rl1

IZFxRg0WBEWR2kVZG9KhALZFZKY0Z9FORLkSiBuRL4U1HvhSKj5EKqbMrgABRC0cFHLRF0eFFkROkWdH1yCMY5HPQYUUlGogKUWlEsAWSplFES2UXFEPiCAPlFsyXkAVF3R+0WVFlSlUZUo5ANSnUotQBNE0pQArSvoDtKTwLeHxUEyn0qVAgynXZEmTAGMoEA8sVMogyqEDcBzKUQIsqkAEXlPY5ipAOsr0RnEHeG1Rj4Q1Foxb4V5EcAn4fNGd

R1gN1EARREn1HfhA0UNHHSI0bFHfR6kQ+IoRaEW1HfhWEUtF4Rq0WFEbRJMRTG7RGyolGHRx0WxHZREcetFXRvsYjE5APMWJFGRX0cpG8AYMR9EKRP0bBFPRv0RpFaRgMbpHuRBkezJgxXseZGHSUMQgDWRqgHDHpxlMQ+LIxYgNbEeRGMQ+JYxMUUzH4xYcaFGpxm0aTF3KMcfFHUxUQLTEDSqUcIAMxOMXjEsxb0WzEcxhUdzElRRIN3H8xb0S

yBdqPan2oixUQY5rTgCAKOo5howWuJke06jZqzqqMPOrzgVHt6ESA6Culi/Aq6naBu20ALqIRhj5qHbmQQKLbBmiBkIRhjBAKCpp5o6YSsZsO2Ya5wKgtpJ6IzB5nqWG1he1DwDkgiQAgAOw1nidQbYRUHWGlQ6wU54HB3YdRot2fdjsHt2ZCa2E9hxwX2H+erGkPZFiI9qF5jhhsVWIz2LoM0qzhgpi1zBggBv7Cq86XjvZOi7YjvYUmiYLCY9w

w2sfb5eN4VNyHhs3NcEcm0MFyaqaIoVSaoidXntyKJGEF0qVACgAABUxiYBLGJqAAAACZUHNCoASkrFTkAh4kwCmgpoGRBkq5iVYnEqwAPQBEwxAG4nFgYindG2StKo+LWAMAOoCHgFEvoBsAjgOSBSSiUoHIuAPgCjGJJPwCEA/i5iQoAPiJER1GggjACBIcSHcvsrfiB0sABiScynhFBS5cleJVy6gAADc5SaNJBR2ABcqnSlctcqSADSRFIVJ

K0b5HHSD8o3LoSjyl0lASPSTxLoKw0i8ofiJEm8ofKbyrRLUAQ8gsmjyIyc+JKA2MrGCHgOasdEMKdYDIAGAREgJJESTkSaoAq9qvxKeKP0mUl/yv0BJK4KC8gAAkEKhQAKSTyctKrJNsppJnisKrQr7S14tcnWKiKiVJkQJyRLKoAFyWhK4qAAD5QpR8qFJBSMKXfLQpsKSFIfi2AKUlEqIScCmHyxSeSoVqmUmkoHSQKUioFSKSnHIcqEAB8ni

SQCkyqGSVKSaquSZ4mMnIKvKqgrjJgqqNL/JbsiKrSSTyeKrOAfKcQpSqpCmQo2SZ4vKrUKO0kqo7yXKXapAS+qrwqeKkqg4oFSIKX/JqpQEmql+KZ4rcmmymwHUlIpwUganCSM0jNKypeMuCl1SsMmwrsK2UualkK8it6rqpoKZ8mWpJSq6rfytqRAD2pUciLJUSTqaqliSWqcmrgptyb6r6pR8o5KkABqQJKmpPqY4pfJKSsGrxKj0nakApDqR

4qCS9itikkpYKbinSyjUsxLxpXCnxKiy2AHVgqpz4hqlVpLqagDrJe0fHHMRqAHAD6SCAIIo6pY4v4pOSMaWfJRpPaRQBxp6aSZJMyHac0lmqEaTipGp9MoOkFqiaa2o2psCi7LFpZCmSleyVKtWpkKZEJkrZK+aQ2r3SD0vArLpUcqulxKi6RulRy1aSZKXpqAGqlkQdSVVE1REACYlmJj4hYnWJcILYn2JH6U4mkALiSaBuJiUh4mWJXiT4kkA

/iYElBRxKmEkRJ0UFEkxJGkvEnQyiSd4AhUu8YSDlglUtoCZJ2SXCCQR+APkkfihSenK4pGKd0lNJtkq0nfitSZ0mNJ6GcFKUZMMlcowS9SbRnhxfSfcpDJLcteJUpYyc8qESryj3LDynygPJ0SImUxL0SJoFSnrJegJsnRQ2yWBF7JIMvoCHJ7kscm5p7EmcnhqVySVK3JPKU8nzSbySQr0psquCk/J0qdeJHp/8nSqBp6mQmngpqKgFKIpmKh+

IIpKKdfLIpd8qFLopdiZikvyOaRam7pRavunrp3qcEl+ZtmWWpRq+KQenZSxmU+I0pVUnSkhKQUkynkZLKb1JspfGZylDp6MnpnTSiqS8kCpRCkarSq1imKkSp20nCp/JOWWGrcKBqrypGqlaVen+ZNabZkjpuqeOnGp7mVOkmpZqTVkmZ+adamepZ6d6n9ZeqtwqOqiijZk4pHsh6n5KXqZZnyptiv6lOqzqRFLBpDKSllhpqat2mRptkv2kzpp

KoFlBqpMgtljZ4kkCrZpa2TNnzpRaedlLZpaZckVpLWU+IbZayQoCoRccYxFNpLaaEBtpyaqOldpEaQ5nRpzModkFS7WZ2l6pXWcIqOS2ADDng5oqXOlRZqSimlLp92ZFInplaj7JuyW6bWoaSx2dFkpph6RjkQK86WunaquOS9k3pD4nenHgVSsLH1KYsVUqSx0sWgDWcXShrGKxCAEMosgsYGrH4AXOfiAzKOsVUrsRSyncFGxayv4CbKFsU+m

mJQGTYmviX6Y4nlgv6alL/p7ia+meJISXYmgZfiagABJi0EElQZHAOEmSAkSS+LwZcSWSrIZySWhlpJmGdhkcAOSXhkEZqEQCokZPmWRl0ZVSWSrUZPGeRktJ1SeBLtJzGTRk+5bGdjEDJDylxmB5dGVlmdy0yd3LkScyYJkLJSySPISZUmR9kyZTAFslaxCmXdFKZKmRQBqZ/ypxKTymacCrnZumfcmiq+mZCqGZwqXFl1q3yX0lSpYCotlRSWK

ddlHZDmc5JOZZ8vCmoAiKZOmD5bmcIpeZpGYCm95NmQFlY5BKSFlEpveSyoo55KXAqxZJUglmgKSWZmrgpzKTyoZZ/KuymTJhEt3lPieWfymCpJWSKlRy5WWZld5pORdl1ZBWYaqrZ1itemapQabWmQ5Y6dnETp3WfDnTpfWTdltJROWdnuKDqsCo5pYBXbJzZp2SNkX55yaQArZU2ZFLXpb2exKMp22QYrA5vaftlg5oBUdlJpiBdqrIFl2U1k0

5EWQNlkpd2VAUQpQks9lrZ3+bZn1pX2QdE/Zrae2m4FIiv2n+SoObGnEFEOTgVQ5nWYanAFvWcgVipi+cFnkFz+ZFlmKFKhTlVq6SpunbpBObIXE5aaW7KKFeKW2qU5dql/mtZrBXTmvA3amwC9qrACfFsyGtnOojqqdtfFuhcQahFn2w6gKbPxnockGvx4XKur8cCAMlg0gHIDVShh+IH/H1BJJhhx+aBaBHaOI1nDCanQDlOjpYGxFNAEYQGYY

BpgUroo4W8AZosWH52KGmWFWejxssEEJu1GsENhHxk2FbB5CeRodhrnl2F0JvYQCaQAA9ucFDhJXBkZheFYnF6om3CeeA1AfCW8ECJCoHzanaOkJtQpecwOuFSJq4VpY7mu4YyaTiLJrCFdF8IbDBnh5mlBwv2eia4X7h24nLl0gq2A+mHFs8bOCCx1Sv2pp2Fxazn4AHSvyCc5vSlMpKxfOarHmA6sU8WQgIuUhBi5+sZwlvYJsTLnmxu4hIBHF

qIAfEWFVhVcWnx1mhfE5F25M4Xa2+xe4UC4L8dRDpUNQECBQA/wLMD8cq6qxA/xhiRGHRa/eE8j9sTWH27B2sMJyThghNrSx4+KnrAlBec1DkVnQyPAWEdCXogUUWeRRRWF4JYYugkVFUXI2GbB8YnQkUJ9RdQk0aNRU0UMJLRTmJnBg4awnDh7CRPZzhYOP0W1c6nM8Gw4vdvwm4mlWpMDBQ64S1CI+MxUCHWQoUCyQ+s5QJpoMmGIUon6aR4Ws

UnhGxZHYB2GPkKb1eexY16GJ2ypXm7KeSVnKJShyn7knK4eTxkMZfMgHlJq8qRMkdyREsnnzJaeV8qiZw8r8oSZYkncox5nGa3IRSNMf8DESY8qckBlgKtTJ6gauT2CEA54mWk4yT8gWXaAcADuCSAZ4tLI6KJoFQWaRVIFnINlHSRQpAyyBfkDoKFEuYAwKDZYTBwAeZdYo8pwAOgqEK5gKVlI5ZMYqpgKaALrGOgrmLOmByQUriquS6CvfIUZe

5S0n2S6KoHItJXmaCBrlVShuX/ZZWTkpDlpAKlKjlxaqoVXlOQDeVuyO+cyp2qdUugpPlfKjFlqFUckgpH5fKgNKn5CZaWrPiM5bNJzlC0tdILld+UkobSj+fCq6FkUuOXNlrZbBWkAhqqOVUFWBTNFZq4SuWn5qpKlalE56ilAUVlTAFWXnik2capgpdUqRWUVoahmnMANFeQBHi54qRUwFIaeGmGR/quRWtqyaVRUeq5ZZWXcVWcnYpUFhalAq

oF8siGruqtWRxWSV1ZdJWeKClT4pASPqjtkDRQUpErJZd8iRV5qRSnJWUVJauhUtq6+SoU45dqhoX3le6QUpNqzarIXxyJxSCXu2ZyXsohlQsmGXQyMZd0lRlYecXJUpbcvGVTJxoCnkDywme8pplWeSxJZl7GTmXNyU5c+IFlRZRXkdy9qpxV0VGldPI/S9ZWcWNlWFW2X0yHZSVJdlwQGeK9l4ef2Viyz+Q+UjlAFSeLFVE5WlVRyM5XBWzl2A

IuX3568h3lVZO8m+VHitoLeVLl+5buVBS+5SPlHlDkqeXmAB5cJIjVH5XaqSKf5UOUAVaSitVjVn5R3m0p+0m7K/lj5ZtWVq8Cm7IgVuFaykn5ieVgrNql+fXliq50t1WLSiFVZV1qFWbpJDVIKvdWYVzAC2VnSM0sOUNZ+FbAUhpeqYZGkVlqhRWo5YlSpW5VUlWeIMVslfeUsVsNWxW+pElbRWI1vFQGnGy+itmp6ynMsJUo5olRjXCyWNVxXq

VjBRGok1ShalIKVrispXsVCNdTWiyWlbWm6VeBYZEGVGaiIXEV5qi0mGVa1Y5VBZXqVBXWV9NQYWqFfsvjmi1yhfkpIyhSu9VuV5MvTlCx0JWp43FbSncUyxDxbhBC5AyjznKxhNALmG10ytrE/F8yn8WS5SoICVxxj6URnHiPlTnJ+VDGYFWjJwVUxmhVsZbhIRV/GUmXp5KZWJlDyCVcWUISyVYtCDJqVQ4oZV0yeHUaZpZTlVqVNZZcl1lJUn

9UA1tZSTKdlFudVW1VxcvVX2KjVcDXPlH4uOXKgHVblmPVs5aQDzlvVUhUWpqFftI7Vm5SLXblN8nuVBSs1dNXHlC1eeVopl5djLvlu1e3XHV/5Vqqvlw9aNVt11il+U1SP5VLIbVZdbArnVdqpdUoKN1f7WjSEtXclgqoqvllA1ddfBVA1Dde9UoVg1b8nDV71UBKZ12Fc9VXVr1X1IEVv+aEoAFkNcTUWpMNW6ouVFNapXY11NcjWRq4EmjU/1

capTV5VTKWgWMV2BSmrc1RNWRVf1IlUzW/1JaazWp108ldlINKOYzWxq1FSnX5VFEhzW2ZXNYTWgyvNYg2RSpqu/XsyQtXzVLlWhSNm71bldlJ2VNagHLmV6NcrVypz4qrUoyEJUfHWFA6tEE7ciypfEIJE6jfGxBSJY16ohnhYkHgA00JDhwAcAEcXlg3AFRDQAXkFkCVA3YKQDnFRQAwCEAjculjVhtnugkpQ5IFY3WNiIBADYAIgOVA0V+gHS

DbUvJehq2N9jaQCON5YBlhmNKwYKUOewpWUCeN3jZkDNKDdmKUPYwTQ40kgTjS427BMdlQl2NMTTkBxNnns2EgmUTZAAhNsTT42qicpa3bZNKTVABONUnIqWFchjTk2pNPjc0os5OtfcXRNXjbk1hNDOZrUG6RTU03VNmQBKLm1LxX0DJNnTSU0+NRxaMq8QXje5JeQlUovYDNoTfoANgWIGM0CSkzelRwgAkh43FNTjYs3uSWEH0YSA62Os2DNT

jc0qA4+TWKBNcrIMhCgg+AEJwtQ5cA4J4Y4DrwaF0/TZ1F/A1IKFgtQ1Ipp454/+LwaBIEAEYBsABgBo13QvEZ8DdwIwLhSLqMzc036A+TS8G929CflC2N6ICQCM51xYY2otxAHSBHR10P01YtrEDEkIA8zbgBwxDpWUBYtYXPKKZY+AOlSkAygMiBniagRRLMtvANHhOSu8NeIsgvasoDWYu1PS2MtYgSy3vQwrVjKxoXLdC1VN1Su1BlNmCtM1

jhvak6Amx0UCC0YQ2QKS3BAC0CxxIQRAKhAwl/IPRE6N+rf3bdq58a6H8g3QPo1MAaYDxrmtGEJa2AgpACS1ktJHtC12A/hYeLMANIPRFwAhLWtDOtmrVCGQ4BEowBYQQLfgCqt24rs3igGQB3KzKO4Epk7NgnmiHXhPpY5oWgBgBhLBAcbfok7coQN0ohtCAGG2ggqJV4WQAjgMwAats2DkC4QrENkDNA8QeABJBkkN2VGgwAGRAgAZEEAA
```
%%