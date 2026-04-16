---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
Largest Rectangle in histogram ^ZXQPdUwG

[2,1,5,6,2,3] ^3zrjroi4

1. In case of multiple bars the height would be min of all bars we are considering.
as in this array max area is 10 for 5 6 bars where height is 5 and length is 2.
2. We are limited to extend rectangle to left or right based on fact that let say at i = 2 we have 5 
if we go right we see 6 valid, more to right we see 2 which is less than 5 and would decrease overall area 
so better would be to look for number either equal or greater but never smaller as it will reduce area
3. NO Idea ^PqYRuEkr

2 ^u2ELLJub

1 ^jmb3Jp9e

5 ^KF7yTMJF

6 ^9lwcyUQd

2 ^5OQ4FlfL

3 ^45cImcHD

for i = 2 ^9lFy2jaF

for j = 3 ^5D9FRJ6Y

height = min(nums[i], nums[j]) = min(5,6) = 5
width = 3 - 2 + 1 = 2
area = heigth * width  ^rdhcBoCu

var largestRectangleArea = function(heights) {
    let minHeight = Infinity
    let width = 0
    maxArea = 0
    for i = 0 to heights.length - 1 {
        for j = i to heights.length - 1 {
            for k = i to j {
                minHeight = min(heights[k], minHeight)
            }
            width = j - i + 1
            let area = minHeight * width
            maxArea = max(maxArea, area)
            minHeight = Infinity
        }

    }
}; ^iigVAlvP

Time COmplexity 
Since we have to loops which run O(N) times thus
simply O(N*2) while third loop also runs at worst O(N) 
so totally O(N^3)

Space Complexity
its constant since we are only using variables  ^QIDTnPLD

Hint: For i=0:

j=1 → k scans [0,1]
j=2 → k scans [0,1,2]
j=3 → k scans [0,1,2,3] ^YKWYgCtp

- we are recomputing entries between i and j for instance for i = 0 
and j = 3 we alreadt have calculated 0,1 and 2 indexes but now we 
will repeat them ^axt0Rqa6

var largestRectangleArea = function(heights) {
    let minHeight = Infinity
    let width = 0
    maxArea = 0
    for i = 0 to heights.length - 1 {
        for j = i to heights.length - 1 {
            minHeight = min(heights[j], minHeight)
            width = j - i + 1
            let area = minHeight * width
            maxArea = max(maxArea, area)
        }
        minHeight = Infinity
    }
}; ^xRrXFvxc

Approach 2 : Remove inner loop  ^0HdPUBfm

why ? beuase between i and j we are uneccessarily calculating the 
repeated values, minHeight remembers what was min height we saw 
from i to j so no need to repeat calculations again n again ^YPYQknXQ

1 ^0zFaVHB0

2 ^SVUISPSQ

5 ^YKc9mDDp

6 ^3CL8vvzh

2 ^BKivkhs5

3 ^Y8zBVlZe

Now the bridge to optimal. This problem has a different flavor than Next Greater Element.
Instead of asking "what's the next greater bar?", think about it from each bar's perspective:

"If I am the shortest bar in some rectangle, how far left and right can that rectangle extend?"

For heights = [2,1,5,6,2,3], bar at i=2 (height 5):

How far right can it extend before hitting a shorter bar?
How far left?

What stops it from extending in either direction? ^iP4c8EWp

until i = 4 where it see shorter bar 2 and for left at i = 1 where bar is of height 1 ^dnZFOBZW

So for bar i=2 (height 5):

Left boundary stops at i=1 (height 1 < 5)
Right boundary stops at i=4 (height 2 < 5)
Width = 4 - 2 = 2, area = 5 * 2 = 10 ✅ — that's the answer!

So the question becomes — for every bar, how do we efficiently find:

Previous Smaller Element (left boundary)
Next Smaller Element (right boundary)

You've already solved "Next Greater Element" with a monotonic stack. What kind of monotonic stack would find the next smaller element? And what would change in the stack condition? ^GX78LMUl

    That would be monotonic increasing stack where stack.top() if is lesser than curren element means we found next smaller element for given i

12:06 pm

Almost but flip it around —

If stack.top() is greater than current element, that means the current element is the next smaller for whatever is on top.

So the pop condition is: pop when heights[current] < heights[stack.top()]

Now the key design question before writing pseudocode:

For each bar i, you need both left and right boundaries. When exactly do you know both boundaries for a bar?

    You know the right boundary when you find the next smaller element
    You know the left boundary when...? ^SF4WokDh

left boundar when heights[current] > heights[stack.pop()] i think ?

Close! Think about it this way —

When you pop index idx because heights[i] < heights[idx]:

    Right boundary = i (current index, first smaller to the right) ✅
    Left boundary = what's left on top of stack after popping idx

Why? Because the stack is increasing — whatever is below idx on the stack is the last bar to the left that is smaller than idx.

So width = i - stack.top() - 1

And if stack is empty after popping, left boundary extends all the way to index 0, so width = i. ^BLmNNSc2

The stack is always increasing from bottom to top. So when you pop idx=3 (h=6), whatever remains on top — idx=2 (h=5) — is by definition the nearest bar to the left that is shorter than 6. That's exactly your left boundary.
If the stack is empty after popping, it means nothing to the left is shorter — the rectangle extends all the way to index 0, so width = i. ^U5wQcG6n

var largestRectangleArea = function(heights) {
    let stack = []
    let maxArea = 0
    for i = 0 to heights.length - 1 {
        while ( stack.length > 0 && heights[i] < heights[stack.top()] ) {
            let idx = stack.pop()
            let leftBoundary = -1
            if ( stack.length !== 0 ) {
                leftBoundary = stack.top() 
            }
            let width = i - leftBoundary - 1
            let area = heights[idx] * width
            maxArea = max(maxArea, area)
        }
        stack.push(i)
    }
}; ^mery1hhC

[2, 1, 5, 6, 2, 3] ^5ECy3Rnf

[2, 1, 5, 6, 2, 3] ^yaVcMVHC

stack =  ^NJ3ReMqz

[2, 1, 5, 6, 2, 3] ^MeTUrrGE

i = 0 ^OK6hWYj9

stack.length = 0 so  ^XwO0i21S

stack.push(i) = stack.push(0) ^7E9f67Cd

stack = [0] ^xkTe40YF

[2, 1, 5, 6, 2, 3] ^jE5OE7l5

i = 1 ^JyWp8jjk

stack.length = 1  AND heights[1] < heights[stack.top()] => 1 < 2 ^Zonrx2w8

stack = [0] ^P22L64Hg

idx = 0
stack.length = 0 
leftBoundary  = -1
width = i - leftBoundary - 1 => 1 - (-1) -1 = 1
area = heights[idx] * width = 2 * 1 = 2
maxArea = max(0,2) = 2 ^nPVw9Wv2

stack.push(1) ^cZcBJl62

stack =[1] ^kUvqUFN5

[2, 1, 5, 6, 2, 3] ^17Gj8qdV

i = 2 ^lnwtm9lO

stack.length = 1  AND heights[2] < heights[stack.top()] => 5 < 2 ^wCL56xFR

stack = [1] ^mAiwx1He

stack.push(2) ^k1rHCiOB

stack =[1,2] ^AIa0CYRc

[2, 1, 5, 6, 2, 3] ^v0S5OwdX

i = 3 ^GkquVayx

stack.length = 2  AND heights[3] < heights[stack.top()] => 6 < 5 ^NDSGOSPH

stack.push(3) ^Z4zK8mBi

stack =[1,2,3] ^onDEqhmY

stack =[1,2] ^cp8UpOag

[2, 1, 5, 6, 2, 3] ^JZ8suQLK

i = 4 ^7DdbicPt

stack.length = 3   AND heights[4] < heights[stack.top()] => 2 < 6 ^kiwEOQVZ

stack = [1,2,3] ^O6hXBCek

idx = stack.pop() = 3
stack.length = 2  ts[idx] * width = 6 * 1 = 6
maxArea = max(2 ,6) = 6 ^7fnJ7QsT

stack.push(4) ^VUJLtpZI

stack = [1,2,4] ^UQUAFpQ0

var largestRectangleArea = function(heights) {
    let stack = []
    let maxArea = 0
    for i = 0 to heights.length - 1 {
        while ( stack.length > 0 && heights[i] < heights[stack.top()] ) {
            let idx = stack.pop()
            let leftBoundary = -1
            if ( stack.length !== 0 ) {
                leftBoundary = stack.top() 
            }
            let width = i - leftBoundary - 1
            let area = heights[idx] * width
            maxArea = max(maxArea, area)
        }
        stack.push(i)
    }
    while stack is not empty {
        idx = stack.pop()
        leftBoundary = -1
        if stack not empty {
            leftBoundary = stack.top()
        }
        width = heights.length - leftBoundary - 1
        area = heights[idx] * width
        maxArea = max(maxArea, area)
    }
    return maxArea
}; ^vhyo0OpE

Time Complexity 
- One for loop which runs N times so O(N)
inner while loop runs at worst case when we have ascending order array O(N) times so O(2N) = O(N)
- while loop again for worst case runs O(N) times so 
total = O(N) + O(N) = O(N)
Space complexity i
O(N) in worst case when stack is never popped or even when only last element is smaller than stack.pop()
i.e desending order   ^x3Q59r36

/**
 * @param {number[]} heights
 * @return {number}
 */
var largestRectangleArea = function(heights) {
    let stack = []
    let maxArea = 0
    for(let i = 0 ; i < heights.length; i++) {
        while ( stack.length > 0 && heights[i] < heights[stack[stack.length - 1]] ) {
            let idx = stack.pop()
            let leftBoundary = -1
            if ( stack.length !== 0 ) {
                leftBoundary = stack[stack.length - 1]
            }
            let width = i - leftBoundary - 1
            let area = heights[idx] * width
            maxArea = Math.max(maxArea, area)
        }
        stack.push(i)
    }
    while (stack.length > 0) {
        idx = stack.pop()
        leftBoundary = -1
        if ( stack.length > 0 ) {
            leftBoundary = stack[stack.length - 1]
        }
        width = heights.length - leftBoundary - 1
        area = heights[idx] * width
        maxArea = Math.max(maxArea, area)
    }
    return maxArea
}; ^3tVCuUKI

## Embedded Files
ffdee05e86439dd31c65dcdc9f74678b47fd19a2: [[Pasted Image 20260413110200_923.png]]

%%
## Drawing
```compressed-json
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
```
%%