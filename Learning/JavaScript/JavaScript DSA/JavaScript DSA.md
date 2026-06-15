
```table-of-contents
```
## Links

[The Last Algorithms Course You'll Need](https://theprimeagen.github.io/fem-algos/)

# Big O Complexity

### Intro

[Time And Space – The Last Algorithms Course You'll Need](https://theprimeagen.github.io/fem-algos/lessons/algorithms-and-time-space-complexity/time-and-space-complexity)

# Arrays

- setting a value in array is practically over-writing as when it was first created it had memory space assigned so now that particular offset value multiplied by memory width ( usually  bytes ) is actually being over-written.
    
    ![Screenshot 2024-01-28 at 11.52.22 AM.png](Screenshot_2024-01-28_at_11.52.22_AM.png)
    

### Getting at a specific index

- Like here the ArrayBuffer ( each unit ) is of 8 Bytes, unless we make a new array of same units every index we assign gets value at index / offset we expect.
- like a8[2] gets value at index 2 but in case of a16[2] it gets value at index 4 ? because the offset 2 x 16 is 32, that is why.
- in reality index is
    
    $a + (width)(offset) = index n$ 
    
    where `a` is the variable pointing to memory ( location ) of array 
    
    The big O here is `O(1)` because we know width, a ‘s memory and offset, so we can directly move to this location without going through a series of things.
    
    Same for Deletion 
    
    the repo to clone 
    

## Linear Search

### Resources

`git clone [git@github.com](mailto:git@github.com):ThePrimeagen/kata-machine.git`

the [instructions](https://github.com/ThePrimeagen/kata-machine#how-it-works) to follow.

## Binary Search

[Your second Algorithm – The Last Algorithms Course You'll Need](https://theprimeagen.github.io/fem-algos/lessons/our-first-algorithms/binary-search)

## Two Crystal Ball problem

> 
> 
> 
> // Given two crystal balls that will break if dropped from high enough
> // distance, determine the exact spot in which it will break in the most
> // optimized way.
> 

Its a more general way, otherwise instead of height N we’ll be asked for 100 floors or 50 floors maybe.

![Screenshot 2024-02-01 at 12.00.55 PM.png](Screenshot_2024-02-01_at_12.00.55_PM.png)

![Screenshot 2024-02-01 at 11.58.51 AM.png](Screenshot_2024-02-01_at_11.58.51_AM.png)

1. Start by dropping the first crystal ball from a height of sqrt(N).
2. If the first ball breaks, iterate from 1 to sqrt(N) to find the exact floor where it breaks. This requires at most sqrt(N) additional drops, bringing the total drops to 2*sqrt(N).
3. If the first ball doesn't break, increment the height of the drop by sqrt(N) and repeat the process until the first ball breaks or you reach the top floor.
4. Once the first ball breaks, use the second ball to iterate from the last safe height to find the exact floor where the ball breaks. This requires at most sqrt(N) additional drops.
5. The total number of drops is kept to a minimum by adjusting the drop heights based on the sqrt(N) interval.

## Bubble Sort

[Sort – The Last Algorithms Course You'll Need](https://theprimeagen.github.io/fem-algos/lessons/our-second-algorithms/sort)

formula is very simple that 

1. Check for adjacent elements where if $X_i > X_{i+1}$ then we just swap them, if $X_i < X{i+1}$ then no swap.
2. This counts as one loop, at end of each loop last element is largest of all.
3. Then we run upto last largest but not including it. keep repeating until all are sorted.

### Complexity

N, N-1, N-2, N-3….N-N+1 = N(N+1)/2 so $O(N^2)$

## Linked List

[List DataStructures – The Last Algorithms Course You'll Need](https://theprimeagen.github.io/fem-algos/lessons/list-datastructure/list-datastructure)

### Complexity

Insertion → O(1)

Deletion → O(1)

deletions from end → O(1)

deletion from middle → traversal time + deletion 

## Queue

[Queue time – The Last Algorithms Course You'll Need](https://theprimeagen.github.io/fem-algos/lessons/list-datastructure/queue-me-up-scotty)

![Screenshot 2024-02-10 at 6.53.24 PM.png](Screenshot_2024-02-10_at_6.53.24_PM.png)

so its just a FIFO ( First In First Out )

## Stack

[Lets Talk – The Last Algorithms Course You'll Need](https://theprimeagen.github.io/fem-algos/lessons/comparing/comparing)

## ArrayList

[ArrayList – The Last Algorithms Course You'll Need](https://theprimeagen.github.io/fem-algos/lessons/comparing/array-list)

- It has fixed length and capacity ( length is current filled value ) while capacity is how much it can carry like [1,2,…] its length is 2 but capacity is maybe 5
- When an element is puhsed into ArrayList such that len == capacity we increase capacity by making a new array with at least twice the size, copy elements from old array and now push element.
- For Enqueuing its a bit different we shift each element to right by one until first index is empty and then put element into first index.
- Dequeuing is reverse of it, so we shift to left by one, removing first element.
- Inserting at middle or any specific index will have to shift all values beyond that index to left.

## ArrayBuffer

[What is [] in javascript? – The Last Algorithms Course You'll Need](https://theprimeagen.github.io/fem-algos/lessons/comparing/what-is-javascript)

- It has a head and tail pointer, which points to a particular location in memory seperated by some space
- If remove from front, we head + 1 i.e O(1) , add to tail, add tail + 1 and we added it, shifting and unshifting all is O(1) .
- What if tail crosses the end as shown here , it goes round to start and starts there again.
    
    ![Screenshot 2024-02-14 at 1.49.07 PM.png](Screenshot_2024-02-14_at_1.49.07_PM.png)
    

## Recursion

[Recursion – The Last Algorithms Course You'll Need](https://theprimeagen.github.io/fem-algos/lessons/recursion/recursion)

1. One important thing to remember is that we have several steps 
    1. Pre recursion which in our code is nth value
    2. recursion → calling function again with new argument 
    3. Its after we do something when base case is returned so that every function returns and we execute code after our recursive function call.

![Screenshot 2024-02-14 at 3.31.49 PM.png](Screenshot_2024-02-14_at_3.31.49_PM.png)

### Problem

![Screenshot 2024-02-15 at 2.03.57 PM.png](Screenshot_2024-02-15_at_2.03.57_PM.png)

- Recurse also has three steps
    - pre
    - recurse
    - post
- Why we need all these ?
    - Actually lets take an example
    - Here starting at point S we traverse in Css order ( up right bottom left ), we moves from S to `X0` and then Css order up → a dead end , come back move right → to `X1` and this is how we track it by pushing and poping points we traverse.
    - To pop a point we have to first check all of our directions and then pop off if there is no way.
        
        ![Screenshot 2024-02-18 at 5.23.05 PM.png](Screenshot_2024-02-18_at_5.23.05_PM.png)
        
    
    MazeSolver.ts in KataMachine its code 
    

## Quick Sort

[Divide and Conquer – The Last Algorithms Course You'll Need](https://theprimeagen.github.io/fem-algos/lessons/recursion/divide-and-conquer)

> THe idea is to put elements on left and right side of the pivot, where left side elements are either lesser or equal to Pivot while right ones are greater than Pivot.
> 
> 
> ![Screenshot 2024-06-03 at 11.47.23 AM.png](Screenshot_2024-06-03_at_11.47.23_AM.png)
> 
> ![Screenshot 2024-06-03 at 11.47.56 AM.png](Screenshot_2024-06-03_at_11.47.56_AM.png)
> 

![Screenshot 2024-02-18 at 7.45.27 PM.png](Screenshot_2024-02-18_at_7.45.27_PM.png)

- Chose a pivot point and then take two pointers, we name this function partition.

```tsx
function partition (arr: number[], lo: number, hi: number ){
	const pivot = arr[hi];
	let idx = lo-1;

	for(let i = lo; i < hi; ++i){
		if(arr[i] <= pivot){
			idx++;
			const temp = arr[i];
			arr[i] = arr[idx];
			arr[idx] = temp;
		}
	}
	idx++;
	arr[hi] = arr[idx];
	arr[idx] = pivot;

	return idx; // return index of pivot 
}
```

- variable `i` which moves all over the array, `idx` which is at start ( lo - 1 ) and when we find an element lesser than pivot
- Then increment `idx` , swap `ith` element  in `idx` ’s position and continue `i`th pointer until we reach pivot.
    
    ![Screenshot 2024-02-19 at 8.38.18 AM.png](Screenshot_2024-02-19_at_8.38.18_AM.png)
    
- after all iteration for `i`th pointer in array we replace `pivot` with `idx` so it be at a point where left things are all smaller than `Pivot`  while right things are all greater than `Pivot.`
    
    ![Screenshot 2024-02-19 at 8.40.50 AM.png](Screenshot_2024-02-19_at_8.40.50_AM.png)
    
- Re-peat,

Referring start as Lo and high as Hi as end. ( both are inclusive in this case honestly )

![Screenshot 2024-02-18 at 10.57.50 PM.png](Screenshot_2024-02-18_at_10.57.50_PM.png)

- But this does not always happens like this, pivot may not always lie in middle what if we takes a revsered sorted array like [9,8,7…..1], this would have to be sorted in n, n-1, n-2, n-3 ….. n(n+1)/2 which O(N2) thus worst time complexity is different.
- Also after we done

## Trees

[Trees – The Last Algorithms Course You'll Need](https://theprimeagen.github.io/fem-algos/lessons/trees/trees)

Trees are every where from DOM in javascript to AST for the dom.
### Tree Traversal

![Screenshot 2024-02-21 at 10.46.03 AM.png](Screenshot_2024-02-21_at_10.46.03_AM.png)

In simple words Pre-Order means visit Node and then traverse all children and vise versa for post order.

Tree traversal is a crucial operation performed on trees to visit each node exactly once. The order in which nodes are visited defines the type of traversal. There are three primary depth-first traversal methods:

1. **Pre-order Traversal (Root, Left, Right):** In pre-order traversal, the root node is visited first, then the left subtree, and finally the right subtree. This method is commonly used for binary tree copying or cloning, as well as for getting a prefix expression on a binary expression tree.
2. **In-order Traversal (Left, Root, Right):** In in-order traversal, the left subtree is visited first, then the root node, and finally the right subtree. This method is commonly used for binary search trees, as it yields nodes in non-decreasing order.
3. **Post-order Traversal (Left, Right, Root):** In post-order traversal, the left subtree is visited first, then the right subtree, and finally the root node. This method is useful for deleting trees and solving certain types of mathematical expressions.

**Comparison**

- Pre-order traversal is ideal when you need to replicate the tree structure, as it reads the root node before its children.
- In-order traversal is useful when you need to read data in the tree in a specific order, such as with a binary search tree. It reads left children, then the root node, then right children, effectively reading the data in ascending order.
- Post-order traversal is useful for operations that need to happen on the children before the root, such as deallocation of memory or certain mathematical operations.

Remember that these traversal methods are depth-first, meaning they will visit all nodes on a tree's depth before moving to the next level.

### Ordering

In the context of tree data structures, the terms "weak ordering" and "strong ordering" are often used to describe the hierarchical relationship between nodes. These terms are especially relevant in binary search trees, where the position of each node is determined by comparisons with other nodes.

1. **Weak Ordering:** In weak ordering, the tree is ordered such that for any given node, all nodes in its left subtree are less than or equal to the node, and all nodes in its right subtree are greater than or equal to the node. This allows for duplicate values in the tree.
2. **Strong Ordering:** In strong ordering, duplicates are not allowed. For any given node, all nodes in its left subtree are less than the node, and all nodes in its right subtree are greater than the node.

It's worth noting that the choice between weak and strong ordering can have significant implications for the performance of certain operations. For example, in a strongly ordered tree, search operations can be more efficient because the equality condition can be determined without having to traverse both subtrees. 

Sure, here's a text-based diagram to illustrate the difference between weak and strong ordering in binary trees:

- **Weak Ordering:**

Binary Search Tree (BST) with weak ordering may look like this:

```
      8
     / \\
    3   8
   / \\   \\
  1   6   9
     / \\
    4   7

```

In this BST, all nodes in the left subtree of root (8) are less than or equal to 8, and all nodes in the right subtree of root are greater than or equal to 8. Note the duplicate 8 on the right.

- **Strong Ordering:**

Binary Search Tree (BST) with strong ordering may look like this:

```
      8
     / \\
    3   10
   / \\   \\
  1   6   14
     / \\  /
    4   7 13

```

In this BST, all nodes in the left subtree of root (8) are less than 8, and all nodes in the right subtree of root are greater than 8. Note that there are no duplicates.

## Tree Traversal Implementation

### Pre-Order

here // pre is pushing a node, because its a pre-order while recurse is to call recursion while no post recursion.

1. base case is simple when we got no more childrens to traverse.
2. returnin path has no meaning here its only for the purpose of avoiding ts errors for the fucntions.

```tsx
function walk(curr: BinaryNode<number> | null, path: number[]): number[] {
    if (!curr) {
        return path;
    }
    // pre
    path.push(curr.value);
    // recurse
    walk(curr.left, path);
    walk(curr.right, path);
    // post

    return path;
}

export default function pre_order_search(head: BinaryNode<number>): number[] {
    return walk(head, []);
}
```

## Breadth First Search

[Learn Breadth-First Search – The Last Algorithms Course You'll Need](https://frontendmasters.com/courses/algorithms/breadth-first-search/)

![Screenshot 2024-05-24 at 1.07.23 PM.png](Screenshot_2024-05-24_at_1.07.23_PM.png)

Its like a tree level visit,  visiting all nodes at same level first then going down .

They simply use a queue instead of stack unlike in DFS.

- Also using js arrays might ne causing O(N2) because of the fact that shifting and unshifting requires O(N) in arrayList
    - While each when poping an element from arrayList we do need to shift all elements by one.

```tsx
export default function bfs(head: BinaryNode<number>, needle: number): boolean {
    const q = [head];
    while (q.length) {
        const curr = q.shift() as BinaryNode<number>;
        // search
        if (curr.value === needle) {
            return true;
        }
        if (curr.left) {
            q.push(curr.left);
        }
        if (curr.right) {
            q.push(curr.right);
        }
    }

    return false;
}

```

## Search Example

`Depth first Search preserves the Shape of traversal`

1. Just like in this example where traversing with BFS for left circled trees will result in conclusion that they both are equal but in reality they are not because if we compare left and right using BFS it will appear to be equal but is it really ? no its not 
2. Thus using DFS will preserve shape if its really, here we use recursion / stack.

The question was to find if two trees are equal or not

![Screenshot 2024-02-26 at 9.23.57 AM.png](Screenshot_2024-02-26_at_9.23.57_AM.png)

### Code

[Learn Implement Binary Tree Comparison – The Last Algorithms Course You'll Need](https://frontendmasters.com/courses/algorithms/implement-binary-tree-comparison/)

**Base case 1**

both are null  ( reached end of traversal ) 

**Base Case 2**

any one is null

**Base Case 3**

 if both have different values 

```tsx
export default function compare(
    a: BinaryNode<number> | null,
    b: BinaryNode<number> | null,
): boolean {
	// structural check
    if (a === null && b === null) {
        return true;
    }
    if (a === null || b === null) {
        return false;
    }
	// value check
    if (a.value !== b.value) {
        return false;
    }

    return compare(a.left, b.left) && compare(a.right, b.right);
}

```

## Binary Search Tree

Where left is smaller or equal to node while right is greater than node.

![Screenshot 2024-02-26 at 12.21.11 PM.png](Screenshot_2024-02-26_at_12.21.11_PM.png)

### Find

Finding a node in binary search tree is simply a binary search on an array. 

Pseudocode for finding → Running time O(logn ) to O(N) if tree is single side as in pic then O(n) where n is height of the tree while logn when tree is complete . 

- The logn - n range shows us that for a height of n we have o(n) time complexity while for a height of logn we have O(logn) time complexity .
- Explanation here

[ChatGPT](https://chatgpt.com/c/ccf2821c-d849-4e18-9814-8a43367009bd)

![Screenshot 2024-02-26 at 12.21.59 PM.png](Screenshot_2024-02-26_at_12.21.59_PM.png)

### Insert

Similar to find it always follows the main principle of BST and then we simply insert a particular value at suitable node.

### Delete

Deleting a node is a bit complex then just inserting a node.

1. The node has no child , it can be deleted without any issues.
    
    ![Screenshot 2024-06-04 at 10.12.54 AM.png](Screenshot_2024-06-04_at_10.12.54_AM.png)
    
2. When we have only one child for given node to be deleted like 7 in this case has 4 as only child ( seems like a linked list operation ), we can make 15 point directly to 4.
3. Case 3 is where we have to delete a node having both childs, like 51 in this case, For such a case we can do either of given operations and replace this with our node to be deleted.
    1. Smallest node on the right side of node ( to be deleted ).
    2. Largest node on left side of node. 
    
    Keep in mind that when we find replaceable node here it can pose one of the two cases above case 1 and case 2.
    
    ![Screenshot 2024-06-04 at 11.05.18 AM.png](Screenshot_2024-06-04_at_11.05.18_AM.png)
    

Now why would we chose either depends on a certain information, if we can somehow preserve the information about the max height of given node then we can chose the side with larger height so to make a attempt to shrink up the tree.

### DFS ( Depth First Search )

The binary search on BST is not always logn where as in case of array its 100% logn.

```tsx
export default function dfs(
    head: BinaryNode<number> | null,
    needle: number,
): boolean {
    return search(head, needle);
}

function search(curr: BinaryNode<number> | null, needle: number): boolean {
    if (!curr) {
        return false;
    }

    if (curr.value === needle) {
        return true;
    }

    if (curr.value < needle) {
        return search(curr.right, needle);
    }
    return search(curr.left, needle);
}

```

# DSA LEETCODE

### Contains Duplicate

[LeetCode - The World's Leading Online Programming Learning Platform](https://leetcode.com/problems/contains-duplicate/)

- It has many solutions, the ones i tried in js
1. I went straight and pushed every element to array if it was not already there, if it was return true. But it was slower much slower that if array was larger it failed.
2. Sorted array using bubble sort and then compared consecutive values, which helped my find solution but still using bubble sort has $O(N^2)$  while $O(N)$.
3. Then came the hashSet solution where insert is O(1) while pushing is simply $O(N)$. I do not know why but its faster then counter part arrays in JS.

There are some available in code

```jsx
/**
 * Brute Force - Linear Search
 * Time O(N^2) | Space O(1)
 * https://leetcode.com/problems/contains-duplicate/
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = (nums) => {
    for (let right = 0; right < nums.length; right++) {/* Time O(N) */
        for (let left = 0; left < right; left++) {         /* Time O(N) */
            const isDuplicate = nums[left] === nums[right];
            if (isDuplicate) return true;
        }
    }

    return false;
}

/**
 * Sort - HeapSort Space O(1) | QuickSort Space O(log(N))
 * Time O(N * log(N)) | Space O(1)
 * https://leetcode.com/problems/contains-duplicate/
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = (nums) => {
    nums.sort((a, b) => a - b);/* Time O(N * log(N)) | Space O(1 || log(N)) */

    return hasDuplicate(nums);
}

const hasDuplicate = (nums) => {
    for (let curr = 0; curr < (nums.length - 1); curr++) {/* Time O(N) */
        const next = (curr + 1);

        const isNextDuplicate = nums[curr] === nums[next];
        if (isNextDuplicate) return true;
    }

    return false;
}

/**
 * Hash Set
 * Time O(N) | Space O(N)
 * https://leetcode.com/problems/contains-duplicate/
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = (nums) => {
    const numsSet = new Set(nums);/* Time O(N) | Space O(N) */
    const isEqual = numsSet.size === nums.length;

    return !isEqual;
};

/**
 * Hash Set - Early Exit
 * Time O(N) | Space O(N)
 * https://leetcode.com/problems/contains-duplicate/
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = (nums, numsSet = new Set()) => {
    for (const num of nums) {/* Time O(N) */
        if (numsSet.has(num)) return true;

        numsSet.add(num);       /* Space O(N) */
    }

    return false;
};
```

### Valid Anagram

[LeetCode - The World's Leading Online Programming Learning Platform](https://leetcode.com/problems/valid-anagram/)

1. The first method is simply using HashMaps or objects in Javascript. Just count the occurence of each value in each string and then just compare  the counts where if each key is of same count its anagram.
2. The other way is to sort and then just get length if of same length they are anagram.

```jsx
/**
 * Sort - HeapSort Space O(1) | QuickSort Space O(log(N))
 * Time O(N * logN) | Space O(N)
 * https://leetcode.com/problems/valid-anagram/
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = (s, t) => {
    const isEqual = s.length === t.length;
    if (!isEqual) return false;

    return reorder(s) === reorder(t); /* Time O(N * logN) | Space O(N) */
};

const reorder = (str) => str
    .split('')                         /* Time O(N)          | Space O(N) */
    .sort((a, b) => a.localeCompare(b))/* Time O(N * log(N)) | Space O(1 || log(N)) */
    .join('');                         /* Time O(N)          | Space O(N) */

/**
 * Hash Map - Frequency Counter
 * Time O(N) | Space O(1)
 * https://leetcode.com/problems/valid-anagram/
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = (s, t, map = new Map()) => {
    const isEqual = s.length === t.length;
    if (!isEqual) return false;

    addFrequency(s, map);      /* Time O(N) | Space O(1) */
    subtractFrequency(t, map); /* Time O(N) | Space O(1) */

    return checkFrequency(map);/* Time O(N) */
};

const addFrequency = (str, map) => {
    for (const char of str) {/* Time O(N) */
        const count = (map.get(char) || 0) + 1;

        map.set(char, count);   /* Space O(1) */
    }
}

const subtractFrequency = (str, map) => {
    for (const char of str) {/* Time O(N) */
        if (!map.has(char)) continue;

        const count = map.get(char) - 1;

        map.set(char, count);   /* Space O(1) */
    }
};

const checkFrequency = (map) => {
    for (const [ char, count ] of map) {/* Time O(N) */
        const isEmpty = count === 0;
        if (!isEmpty) return false;
    }

    return true;
}

```

### Two Sum

The first solution i made is using bruteForce of nested loops to span all elements. 

1. The second way is more efficient where we use maps to store key ( value ) and value ( index ) as shown below.

Explanation at neetcode 

[Two Sum - Leetcode 1 - HashMap - Python](https://www.youtube.com/watch?v=KLlXCFG5TnA)

[LeetCode - The World's Leading Online Programming Learning Platform](https://leetcode.com/problems/two-sum/)

```jsx
var twoSum = function(nums, target) {
    let hashMap = new Map();
    for (let i = 0; i < nums.length; ++i){
        let diff = target - nums[i];
        if(!hashMap.has(diff)){
            hashMap.set(nums[i],i);
        }else{
            let res = hashMap.get(diff);
            return [res,i];
        }
    }
    return [-1,1];
};
```

### Group Anagrams

[LeetCode - The World's Leading Online Programming Learning Platform](https://leetcode.com/problems/group-anagrams/description/)

This was a tough one for me, so i had to directly go to solution to get it for even worst case solution.

1. In this solution, 
    1. we simply sort the each str and store it in a map as key with values as an nested array.
    2. if map is empty we return an array and store our str in it and set map key as sorted and value as thsi array
    3. if in next iteration str sorted is similar one then map will have it as index so we can get the array where we can append the similar anagram group value.

```jsx
/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs, map = new Map()) {
    if(!strs.length) return [];
    groupWords(strs, map);    

    return [ ...map.values() ];
};

function groupWords(strs, map){
    for(const str of strs){
        const sorted = str.split('').sort((a, b) => a.localeCompare(b)).join('');
				// getting sorted value ( which should be same for group of anagrams ) 
        const values = map.get(sorted) || [];  // if map has already it then we will append to that same array ( forming a group )

        values.push(str);   // adding or appending value
        map.set(sorted, values);   // setting mutated or new array as value to sorted key so it can identifed in next iterations
    }
}
```

1. The other solution is similar one using hashMap but this time with a different approach
    1. instead of sorting we count the frequency of characters in a word and store this frequency in form of string ( to be used as key for map ). 
    2. This allows us to get common string / key for anagrams thus we can use it to form a group.
    
    ```jsx
    var groupAnagrams = function(strs, map = new Map()) {
        if(!strs.length) return [];
        groupWords(strs, map);    
        return [ ...map.values() ];
    };
    
    function groupWords(strs, map){
        for(const str of strs){
            const sorted = getHash(str);
            const values = map.get(sorted) || [];
    
            values.push(str);
            map.set(sorted, values);
        }
    }
    
    function getHash(str){
        let frequency = new Array(26).fill(0);
        for (const char of str){
            const charCode = getCode(char);
            frequency[charCode]++;
        }
        return buildHash(frequency);
    }
    
    const getCode = (char) => char.charCodeAt(0) - 'a'.charCodeAt(0);
    const buildHash = (frequency) => frequency.toString();
    ```
    

## **Top K Frequent Elements**

[LeetCode - The World's Leading Online Programming Learning Platform](https://leetcode.com/problems/top-k-frequent-elements/description/)

[Top K Frequent Elements - Bucket Sort - Leetcode 347 - Python](https://www.youtube.com/watch?v=YPTqKIgVk-k)

- This time. didnt tried any fancy method which i couldn’t understand, on second try with chat i came up with this

```jsx
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
    const frequencyMap = new Map();

    // Build the frequency map
    nums.forEach(num => {
        frequencyMap.set(num, (frequencyMap.get(num) || 0) + 1);
    });

    // Convert the frequency map to an array and sort it by frequency in descending order
    const sortedEntries = Array.from(frequencyMap.entries()).sort((a, b) => b[1] - a[1]);

    // Extract the top k frequent elements
    return sortedEntries.slice(0, k).map(entry => entry[0]);
};
```

However the efficient solution according to chat is 

```jsx
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    const frequencyMap = new Map();

    // Build the frequency map
    nums.forEach(num => {
        frequencyMap.set(num, (frequencyMap.get(num) || 0) + 1);
    });

    // Min-heap to keep the top k elements
    const heap = new MinPriorityQueue({ priority: x => x[1] });

    frequencyMap.forEach((value, key) => {
        heap.enqueue([key, value]);
        if (heap.size() > k) {
            heap.dequeue();
        }
    });

    // Extract the elements from the heap
    return heap.toArray().map(x => x.element[0]);
};

// Example usage:
console.log(topKFrequent([1, 1, 1, 2, 2, 3], 2)); // Output: [1, 2]
console.log(topKFrequent([1], 1)); // Output: [1]

```

- Explanation and Min-Heap Usage
    
    ### Explanation
    
    1. **Build the Frequency Map:**
        - We create a `Map` to count the frequency of each number in the `nums` array.
        - For each number in `nums`, we either increment its count in the map or initialize it to 1 if it doesn't exist yet.
    2. **Initialize the Min-Heap:**
        - We use a `MinPriorityQueue` to keep track of the top `k` elements by their frequency.
        - The `priority` function is set to the second element of each pair, which is the frequency.
    3. **Populate the Min-Heap:**
        - We iterate over the frequency map, adding each key-value pair to the heap.
        - After adding a new element, if the size of the heap exceeds `k`, we remove the element with the smallest frequency (i.e., the root of the heap).
    4. **Extract the Top K Elements:**
        - Once all elements have been processed, the heap contains the `k` most frequent elements.
        - We convert the heap to an array and map it to extract the keys (original elements).
    
    ### Detailed Steps
    
    ### Step 1: Building the Frequency Map
    
    ```jsx
    javascriptCopy code
    const frequencyMap = new Map();
    
    nums.forEach(num => {
        frequencyMap.set(num, (frequencyMap.get(num) || 0) + 1);
    });
    
    ```
    
    Here, `frequencyMap` will contain the frequency count of each element in the `nums` array. For example, for `nums = [1, 1, 1, 2, 2, 3]`, `frequencyMap` will be:
    
    ```jsx
    javascriptCopy code
    Map {
      1 => 3,
      2 => 2,
      3 => 1
    }
    
    ```
    
    ### Step 2: Initializing the Min-Heap
    
    ```jsx
    javascriptCopy code
    const heap = new MinPriorityQueue({ priority: x => x[1] });
    
    ```
    
    This initializes a min-heap where each element is a pair `[key, value]`, and the heap is ordered by the frequency (`value`).
    
    ### Step 3: Populating the Min-Heap
    
    ```jsx
    javascriptCopy code
    frequencyMap.forEach((value, key) => {
        heap.enqueue([key, value]);
        if (heap.size() > k) {
            heap.dequeue();
        }
    });
    
    ```
    
    - For each entry in the `frequencyMap`, we enqueue it to the heap.
    - If the heap's size exceeds `k`, we remove the smallest element to ensure the heap only keeps the `k` most frequent elements.
    
    ### Step 4: Extracting the Top K Elements
    
    ```jsx
    javascriptCopy code
    return heap.toArray().map(x => x.element[0]);
    
    ```
    
    - We convert the heap to an array and map it to get only the keys (original elements).
    - `x.element[0]` extracts the key from each pair `[key, value]`.
    
    ### Why Use a Min-Heap?
    
    The min-heap helps in efficiently keeping track of the top `k` elements:
    
    - The heap property ensures that the smallest element is always at the root.
    - By maintaining the heap size at most `k`, we can efficiently discard elements that are not among the top `k` frequent.

The clever solution is to make use of Bucket Sort actually

- Bucket Sort
    
    Bucket sort is a sorting algorithm that distributes elements into several "buckets" and then sorts each bucket individually. Here's a simple explanation:
    
    ### Imagine a Classroom Scenario
    
    1. **Students and Their Grades:**
        - Imagine you have a group of students, each with a different grade on a test. The grades range from 0 to 100.
    2. **Buckets:**
        - You have 10 bins (or buckets) labeled 0-9, 10-19, 20-29, and so on, up to 90-100.
    3. **Distributing Grades:**
        - You go through each student's grade and place their test paper in the corresponding bucket. For example:
            - A grade of 45 goes into the 40-49 bucket.
            - A grade of 88 goes into the 80-89 bucket.
    4. **Sorting Each Bucket:**
        - Once all the grades are distributed into buckets, you sort the grades within each bucket. This is usually done using a simpler sorting method like insertion sort.
    5. **Collecting the Sorted Grades:**
        - After sorting the grades within each bucket, you collect all the grades from the buckets in order, from the lowest bucket to the highest. This gives you the grades in sorted order.
    
    ### Why Bucket Sort Works
    
    - **Distribution:** By distributing the elements into buckets, you reduce the problem of sorting a large list into sorting several smaller lists.
    - **Efficiency:** Sorting smaller lists is faster, and combining the sorted lists at the end is straightforward.
    
    ### Example
    
    Let's say we have the grades: `[78, 23, 45, 12, 89, 67, 34, 56]`.
    
    1. **Distribute into Buckets:**
        - 0-9: []
        - 10-19: [12]
        - 20-29: [23]
        - 30-39: [34]
        - 40-49: [45]
        - 50-59: [56]
        - 60-69: [67]
        - 70-79: [78]
        - 80-89: [89]
        - 90-99: []
    2. **Sort Each Bucket:** (Already sorted in this simple example)
        - 0-9: []
        - 10-19: [12]
        - 20-29: [23]
        - 30-39: [34]
        - 40-49: [45]
        - 50-59: [56]
        - 60-69: [67]
        - 70-79: [78]
        - 80-89: [89]
        - 90-99: []
    3. **Collect the Sorted Grades:**
        - [12, 23, 34, 45, 56, 67, 78, 89]
    
    ### Key Points
    
    - **Distribution:** Divides the problem into smaller, more manageable parts.
    - **Sorting Small Lists:** Sorting smaller buckets is usually more efficient.
    - **Combining Results:** After sorting, simply concatenate the buckets to get the final sorted list
- Now in our case we are gonna use bucket sort but a little but modified, how, instead of index as key and count as values we are gonna use index as count and values as arrays of values with that count
- Also the size of array would be equal to size of input array ? why
    - becuase the max count for given element of input array would be equal to its length, so if input array is 6 , then max count can be 6 as well.
    
    ![Screenshot 2024-07-29 at 10.00.58 PM.png](Screenshot_2024-07-29_at_10.00.58_PM.png)
    
    ```jsx
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    var topKFrequent = function (nums, k) {
        const count = {};
        const freq = Array.from({ length: nums.length + 1 }, () => []);
    
        for (let n of nums) {
            count[n] = (count[n] || 0) + 1;
        }
    
        for (let [n, c] of Object.entries(count)) {
            freq[c].push(n);
        }
    
        const res = [];
        for (let i = freq.length - 1; i > 0; i--) {
            for (let n of freq[i]) {
                res.push(n);
                if (res.length === k) {
                    return res;
                }
            }
        }
    };
    ```
    

### Encode and Decode Strings

- A simple yet interesting problem

```jsx
class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        return strs.map((str) => `${str.length}#${str}`).join("")
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let res = [];
        let i = 0;
        while (i < str.length) {
            let j = i;
            while (str[j] !== "#") {
                j = j + 1;
            }
            let length = parseInt(str.substring(i, j));
            res.push(str.substring(j + 1, j + 1 + length));
            i = j + 1 + length;
        }
        return res;
    }
}

```

- we simply use delimiter as any sign like `#` and length of string, to make sure it never mixes even if `#` is part of input strings as well.

## Product of Array Except Self

[LeetCode - The World's Leading Online Programming Learning Platform](https://leetcode.com/problems/product-of-array-except-self/)

This was a tough one as well 😓 and i know since i have started this journey , these lines are only reminder to my future self that if i improved anything at all or not.

### Approaches

1. I tried brute force but that wasn’t successful and i had to watch solution to get even non optimised answer at first. So this uses the idea of Prefix and Postfix arrays.
    1. Actually Prefix Sums is an Alogorithm, so here instead of sum we just multiply values. 
        
        ![Screenshot 2024-02-15 at 12.25.32 PM.png](Screenshot_2024-02-15_at_12.25.32_PM.png)
        
    2. Secondly comes the postfix where we start at end and multiply values backwards. 
        
        ![Screenshot 2024-02-15 at 12.26.36 PM.png](Screenshot_2024-02-15_at_12.26.36_PM.png)
        
    3. Now for output at index ith , we need prefix of values before it and postfix of values after it. 
        1. Lets consider index 1, nums[1] = 2, while prefix for values before it is 1 as we can see, postfix of values after it is 12, so we multiply them to get total product i.e 12.
        
        ![Screenshot 2024-02-15 at 12.28.29 PM.png](Screenshot_2024-02-15_at_12.28.29_PM.png)
        
        ![Screenshot 2024-02-15 at 12.29.54 PM.png](Screenshot_2024-02-15_at_12.29.54_PM.png)
        
        for first index we have no prefix products so we assume value as 1, similaly for postfix of last we assume 1 as postfix of all previous values.
        
    
    ```jsx
    var productExceptSelf = function(nums) {
        let prefix = [];
        let product = 1;
        for ( let i = 0; i < nums.length ; ++i){
            product *= nums[i];
            prefix[i] = product;
        }
        product = 1;
        let postfix = []
        for(let i = nums.length - 1; i >= 0 ; --i){
            product *= nums[i];
            postfix[i] = product;
        }
        let res = [];
        for(let i = 0; i < nums.length ; ++i){
            let prefixValue = i === 0 ? 1 : prefix[i-1];
            let postfixValue = i === nums.length - 1 ? 1 :postfix[i+1];
            res.push(prefixValue*postfixValue);
        }
    
        return res;
    };
    ```
    
2. The second approach to get sapce complexity of O(1) we simply use prefix and postfix as 1.
    1. For first index we simply use 1 as value assigned to result array. For every later index like 1, 2 … we set value which when multiplied by the potfix will give us our result.
    2. Same here get first index ( from last → kinda backward ) as 1.

```jsx

var productExceptSelf = function(nums) {
    let res = new Array(nums.length).fill(1);
    let prefix = 1;
    for (let i =0; i < nums.length ; ++i){
        res[i] = prefix;
        prefix *= nums[i];
    }
    let postfix = 1;
    for (let i = nums.length - 1; i >= 0 ; --i){
        res[i] *= postfix;
        postfix *= nums[i];
    }

    return res;

};
```

## Valid Sudoku

[LeetCode - The World's Leading Online Programming Learning Platform](https://leetcode.com/problems/valid-sudoku/description/)

1. This had a simple approach although couldn’t figure out the third condition for squares. Lets break this down 
    1. To see if a row has 1-9 unique digits without any repetition which is checked by this part of the code 
        
        ```jsx
        rows.has(`${r}-${board[r][c]}`)
        ```
        
    2. While this code makes sure if there is no such value we can add true to it 
        
        ```jsx
        rows.set(`${r}-${board[r][c]}`, true);
        ```
        
2. Similar for column
3. Last condition is of squares in Sudoku Grid 9x9.
    1. The way to identify a particular square is using index number, which in case of square can get is using integer division as 
    2. this way the index will be like 0-0-8 ( where 0 → square row index  , 0→ square col index and value at that square index )
        
        ```jsx
        squares.has(`${Math.floor(r / 3)}-${Math.floor(c / 3)}-${board[r][c]}`)
        ```
        
        ![Screenshot 2024-02-16 at 12.15.58 PM.png](Screenshot_2024-02-16_at_12.15.58_PM.png)
        

```
function isValidSudoku(board) {
        const cols = new Map();
        const rows = new Map();
        const squares = new Map();

        for (let r = 0; r < 9; r++) {
            for (let c = 0; c < 9; c++) {
                if (board[r][c] === ".") {
                    continue;
                }

                if (
                    rows.has(`${r}-${board[r][c]}`) ||
                    cols.has(`${c}-${board[r][c]}`) ||
                    squares.has(`${Math.floor(r / 3)}-${Math.floor(c / 3)}-${board[r][c]}`)
                ) {
                    return false;
                }

                rows.set(`${r}-${board[r][c]}`, true);
                cols.set(`${c}-${board[r][c]}`, true);
                squares.set(`${Math.floor(r / 3)}-${Math.floor(c / 3)}-${board[r][c]}`, true);
            }
        }

        return true;
    }
```

## **Longest Consecutive Sequence**

[LeetCode - The World's Leading Online Programming Learning Platform](https://leetcode.com/problems/longest-consecutive-sequence/description/)

[https://www.youtube.com/watch?v=P6RZZMu_maU](https://www.youtube.com/watch?v=P6RZZMu_maU)

[https://www.notion.so](https://www.notion.so)

1. Create a number line 
2. notice how start of sequence has no element to its left, like 100 if is tarting point of sequence should not have 99 in input array, if we form a set and check if given value has any givenValue+1 in current set, increment a counter, and do so until counter + value is existing in set.
3. Then update a longest counter becuase a given array can contain many sequences

```jsx
var longestConsecutive = function (nums) {
    let numSet = new Set(nums);
    let longest = 0;
    for (let i of nums) {
        // Check if its the start of a seqeunce
        if(!numSet.has(i-1)){
            let length = 1;
            while(numSet.has(i + length)){
                length++;
            }
            longest = Math.max(length, longest);
        }
    }
    return longest;
};
```

# Two Pointers

## Valid Palindrom

[LeetCode - The World's Leading Online Programming Learning Platform](https://leetcode.com/problems/valid-palindrome/submissions/1179477403/)

Can be solved using a simple two pointers approach.

```jsx
/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    s= s.toLowerCase().trim();
    s = s.replace(/[^a-z0-9]/gi, '');
    let i =0;
    let j = s.length - 1;
    while(i < j ){
        if (i === j) break;
        if(s.charCodeAt(i) === s.charCodeAt(j)){
            i++;
            j--;
        }else{
            return false;
        }
    }
    return true;
};
```

But remember we can avoid using ,replace and form a loop checking each character if its a alphanumeric or not and then compare. 

- I forgot that we also have to consider 0-9 and beside that everything was perfect

```
/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
    s = removeNonAlphanumeric(s);
    let start = 0;
    let end = s.length - 1;
    while (start < end) {
        if (s[start] === s[end]) {
            start++;
            end--;
        } else {
            return false;
        }
    }
    return true;
};

function removeNonAlphanumeric(str) {
    str = str.toLowerCase();
    let newStr = "";
    for (let c of str) {
        if ((c.charCodeAt(0) >= 97 && c.charCodeAt(0) <= 122) || (c.charCodeAt(0) >= 48 && c.charCodeAt(0) <= 57)) {
            newStr += c;
        }
    }
    return newStr;
}

```

## **Two Sum II - Input Array Is Sorted**

[LeetCode - The World's Leading Online Programming Learning Platform](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)

This is a simple Two Pointer solution where one pointer starts at 0th index and another at end.

```jsx
/**  
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    let i = 0;
    let j = numbers.length - 1;
    while ( i < j ){
        if(numbers[i] + numbers[j] === target){
            return [i+1,j+1];
        }else if(numbers[i] + numbers[j] > target){
            --j;
        }else{
            ++i;
        }
    }
    return [-1,-1];
};
```

## **3Sum**

[LeetCode - The World's Leading Online Programming Learning Platform](https://leetcode.com/problems/3sum/description/)

We used similar approach as in two sum II, along with an addition

1. First we sort the array 
2. We make first loop to run over all elements
3. Then if its a positive number we break as positive + positive  ≠ 0 , 
4. we also continue iteration if two consecutive numbers are similar becuase then they will yield similar triplets. 
5. then we use two pointer approach this time adding third element as well from outer iteration and target as 0

```jsx
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    const res = [];
    nums.sort((a,b) => a-b);
    for(let i = 0; i < nums.length ; ++i){
        const a = nums[i];
        if(a > 0) break;
        if(i > 0 && nums[i - 1] === a) continue;
        let l = i+1;
        let r = nums.length - 1;
        while ( l < r ){
            const threeSum = a + nums[l] + nums[r];
            if(threeSum > 0){
                --r;
            }else if(threeSum < 0){
                ++l
            }else{
                res.push([a, nums[l], nums[r]]);
                ++l;
                --r;
                while(nums[l] === nums[l-1] && l < r){
                    ++l;
                }
            }
        }
    }
    return res;
};
```

1. besides pushing values to res array. we increment and decrement left and right pointers pretty obvious becuase we do have to get out of loop 
    1. but we also check if new left pointer is same as last one so we ignore it.

```jsx
else{
  res.push([a, nums[l], nums[r]]);
  ++l;
  --r;
  while(nums[l] === nums[l-1] && l < r){
      ++l;
  }
}
```

### Container With Most Water

[LeetCode - The World's Leading Online Programming Learning Platform](https://leetcode.com/problems/container-with-most-water/description/)

Used simple approach of two pointer and getting area using width ( large index - small index ) and height ( min of of both numbers ). 

1. Using min for height is becuase it would be holding water otherwise larger vertical line would spill water from the smaller vertical side 

```jsx
/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
    let l = 0;
    let r = height.length - 1;
    let max = 0;
    while (l < r) {
        let width = r - l;
        let heightM = Math.min(height[l], height[r]);
        let area = width * heightM;
        max = Math.max(max, area);
        if (height[l] < height[r]) ++l;
        else if (height[l] > height[r]) --r;
        else {
            ++l;
            --r;
        }
    }

    return max;
};
```

## Trapping Rain Water

[Trapping Rain Water - LeetCode](https://leetcode.com/problems/trapping-rain-water/description/)

The algorithm has a time complexity of O(n) and a space complexity of O(1).

First, it explains how to solve the problem using a brute force approach. The brute force approach has a time complexity of O(n^2) and requires a lot of extra space.

Then, it introduces a more efficient method using two pointers, left and right, to calculate how much rainwater can be trapped at each position.

Here are the steps of the algorithm:

1. Initialize the left and right pointers to point to the first and last elements of the array, respectively.
2. Initialize two variables maxLeft and maxRight to store the maximum amount of rainwater that can be trapped before the left and right pointers, respectively.
3. Compare maxLeft and maxRight. If maxLeft is smaller, move the left pointer one position to the right and update the value of maxLeft. Otherwise, move the right pointer one position to the left and update the value of maxRight.
4. Calculate the amount of rainwater that can be trapped at the current position and add it to the result.
5. Repeat steps 3 and 4 until the left and right pointers meet.

Here is the JavaScript code for the algorithm:

**JavaScript**

```jsx
/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function (height) {
    if (!height) return 0;
    let l = 0;
    let r = height.length - 1;
    let maxL = height[l];
    let maxR = height[r];
    let res = 0;
    while (l < r) {
        if (maxL < maxR) {
            ++l;
            maxL = Math.max(maxL, height[l]);
            res += maxL - height[l];
        } else {
            --r;
            maxR = Math.max(maxR, height[r]);
            res += maxR - height[r];
        }
    }

    return res;
};
```

Few things to explain which are not in above summary 

### Q: Why does we are not considering the maxR or maxL in cases where we haven’t even visited the whole right or left array ?

Since we are taking 

$WaterEntrapped = min(maxL, maxR) - height[i]$

where i is current index, maxL and maxR are as per current Index

![Screenshot 2024-02-23 at 11.18.35 AM.png](Screenshot_2024-02-23_at_11.18.35_AM.png)

1. This picture explains better about our intent, as you can at each step in given array `height` we evaluate the `min(maxL, maxR)` which are stored in `maxLeft` and `maxRight` and subtract current element `height[i]` .
2. Now as we can see at `height[i]` the maxL is 0 while current maxR is 1 so we are pretty sure that even if `currentMaxR` is not actually maxRight ( ideally its 3 ) but still its larger than currentMaxL for `height[i]` thus makes complete sense to ignore maxR as we are lokking for `min(maxL, maxR)` .
    
    ![Screenshot 2024-02-23 at 12.47.30 PM.png](Screenshot_2024-02-23_at_12.47.30_PM.png)
    

## Stack

### Min Stack

[Min Stack - LeetCode](https://leetcode.com/problems/min-stack/description/)

This was a only an implementation for stack with a new thing to get minElement 

```jsx
/** 
 * https://leetcode.com/problems/min-stack
 * Time O(1) | Space O(N)
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(x)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
class MinStack {
    /**
     * @constructor
     */
    constructor () {
        this.stack = [];
        this.minStack = [];
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push (val, { minStack } = this) {
        this.stack.push(val);             /* Space O(N) */

        const isMinEmpty = !minStack.length;
        const hasNewMin = val <= this.top(minStack);
        const canAddMin = isMinEmpty || hasNewMin;
        if (canAddMin) minStack.push(val);/* Space O(N) */
    }

    /**
     * @return {void}
     */
    pop ({ stack, minStack } = this) {
        const top = stack.pop();          /* Time O(1) */

        const canPopMin = top === this.getMin();
        if (canPopMin) minStack.pop();    /* Time O(1) */
    }

    /**
     * @param {Array}
     * @return {number}
     */
    top (stack = this.stack) {
        return stack.length
            ? stack[stack.length - 1]     /* Time O(1) */
            : null;
    }

    /**
     * @return {number}
     */
    getMin (minStack = this.minStack) {
	        return this.top(minStack);       /* Time O(1) */
    }
}

/** 
 * https://leetcode.com/problems/min-stack
 * Time O(1) | Space O(1)
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(x)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
class MinStack {
    constructor () {
        this.head = null
    }

    push (val) {
        this.head = (!this.head)   /* Space O(1) */
            ? new Node(val, val, null)
            : new Node(val, Math.min(val, this.head.min), this.head);
    }

    pop () {
        this.head = this.head.next;/* Time O(1) */
    }

    top () {
        return this.head.val;      /* Time O(1) */
    }

    getMin () {
        return this.head.min;      /* Time O(1) */
    }
}

class Node {
    constructor (val, min, next) {
        this.val = val;
        this.min = min;
        this.next = next;
    }
}

```

### Reverse Polish Notation

[Evaluate Reverse Polish Notation - LeetCode](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/)

/**

- [https://leetcode.com/problems/evaluate-reverse-polish-notation](https://leetcode.com/problems/evaluate-reverse-polish-notation)
- Time O(N^2) | Space(1)
- @param {string[]} tokens
- @return {number}
*/
var evalRPN = function(tokens, index = 0) {
while (1 < tokens.length) {/* Time O(N) */
const isOperation = () => tokens[index] in OPERATORS;
while (!isOperation()) index++;/* Time O(N) */
    
    ```
     const value = performOperation(tokens, index);
    
     tokens[index] = value;
     tokens.splice((index - 2), 2);/* Time O(N) */
     index--;
    
    ```
    
    }
    
    return tokens[0];
    };
    

var OPERATORS = {
'+': (a, b) => a + b,
'-': (a, b) => a - b,
'*': (a, b) => a * b,
'/': (a, b) => Math.trunc(a / b),
};

var performOperation = (tokens, index) => {
const [ rightNum, leftNum ] = [ Number(tokens[index - 1]), Number(tokens[index - 2]) ]
const operation = OPERATORS[tokens[index]];

```
return operation(leftNum, rightNum);

```

}

/**

- [https://leetcode.com/problems/evaluate-reverse-polish-notation](https://leetcode.com/problems/evaluate-reverse-polish-notation)
- Time O(N) | Space(N)
- @param {string[]} tokens
- @return {number}
*/
var evalRPN = function (tokens, stack = []) {
for (const char of tokens) {/* Time O(N) */
const isOperation = char in OPERATORS;
if (isOperation) {
const value = performOperation(char, stack);
    
    ```
         stack.push(value);      /* Space O(N) */
    
         continue;
     }
    
     stack.push(Number(char));   /* Space O(N) */
    
    ```
    
    }
    
    return stack.pop();
    }
    

var OPERATORS = {
'+': (a, b) => a + b,
'-': (a, b) => a - b,
'*': (a, b) => a * b,
'/': (a, b) => Math.trunc(a / b)
};

var performOperation = (char, stack) => {
const [ rightNum, leftNum ] = [ stack.pop(), stack.pop() ];
const operation = OPERATORS[char];

```
return operation(leftNum, rightNum);

```

}

```jsx
/**
 * https://leetcode.com/problems/evaluate-reverse-polish-notation
 * Time O(N^2) | Space(1)
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function(tokens, index = 0) {
    while (1 < tokens.length) {/* Time O(N) */
        const isOperation = () => tokens[index] in OPERATORS;
        while (!isOperation()) index++;/* Time O(N) */

        const value = performOperation(tokens, index);

        tokens[index] = value;
        tokens.splice((index - 2), 2);/* Time O(N) */
        index--;
    }

    return tokens[0];
};

var OPERATORS = {
    '+': (a, b) => a + b,
    '-': (a, b) => a - b,
    '*': (a, b) => a * b,
    '/': (a, b) => Math.trunc(a / b),
};

var performOperation = (tokens, index) => {
    const [ rightNum, leftNum ] = [ Number(tokens[index - 1]), Number(tokens[index - 2]) ]
    const operation = OPERATORS[tokens[index]];

    return operation(leftNum, rightNum);
}

/**
 * https://leetcode.com/problems/evaluate-reverse-polish-notation
 * Time O(N) | Space(N)
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function (tokens, stack = []) {
    for (const char of tokens) {/* Time O(N) */
        const isOperation = char in OPERATORS;
        if (isOperation) {
            const value = performOperation(char, stack);

            stack.push(value);      /* Space O(N) */

            continue;
        }

        stack.push(Number(char));   /* Space O(N) */
    }

    return stack.pop();
}

var OPERATORS = {
    '+': (a, b) => a + b,
    '-': (a, b) => a - b,
    '*': (a, b) => a * b,
    '/': (a, b) => Math.trunc(a / b)
};

var performOperation = (char, stack) => {
    const [ rightNum, leftNum ] = [ stack.pop(), stack.pop() ];
    const operation = OPERATORS[char];

    return operation(leftNum, rightNum);
}
```

- my solution in simple way

```jsx
var evalRPN = function (tokens) {
    let stack = [];
    let symbols = ['+', '-', '/', '*'];
    for (let token of tokens) {
        if (symbols.includes(token)) {
            const a = parseInt(stack.pop());
            const b = parseInt(stack.pop());
            const res = performOperation(token, a, b);
            stack.push(res);    // push back the result to stack
        } else {

            stack.push(token);  // push numbers on to stack
        }
    }
    return stack.pop();
};

const performOperation = (symbol, a, b) => {
    if (symbol === '+') {
        return a + b;
    }
    if (symbol === '-') {
        return b - a;
    }
    if (symbol === '*') {
        return a * b;
    }
    if (symbol === '/' && a !== 0) {
        return Math.trunc(b / a);
    }
}
```

### **Generate Parentheses**

[Generate Parentheses - LeetCode](https://leetcode.com/problems/generate-parentheses/description/)

This approach is a of backtracking and using a tree concept

The conditions are that close parenthesis count if is less than open can only then be used 

1. we start with empty array, then use only an open parenthesis, 
2. As per conditon `openCount = 1` and `closeCount=0` so we have two choices 
    1. either add an open parenthesis ( to left ) or add a close parenthesis as `closeCount` < `openCount`
    2. So at each level of tree we will check these two counts and use close parenthesis only if its count is less than that of open. While open can be used until uit does not cross value of `n`.  
    
    ![Screenshot 2024-02-27 at 8.11.40 AM.png](Screenshot_2024-02-27_at_8.11.40_AM.png)
    
    ![Screenshot 2024-02-27 at 9.49.27 AM.png](Screenshot_2024-02-27_at_9.49.27_AM.png)
    

![Screenshot 2024-02-27 at 8.10.50 AM.png](Screenshot_2024-02-27_at_8.10.50_AM.png)

Code

```jsx

var generateParenthesis = function(n) {
    let stack = [];
    let res = [];

    const backtrack = function(openN, closedN) {
        if (openN === closedN && openN === n) {
            res.push(stack.join(''));
            return;
        }

        if (openN < n) {
            stack.push('(');
            backtrack(openN + 1, closedN);
            stack.pop();
        }

        if (closedN < openN) {
            stack.push(')');
            backtrack(openN, closedN + 1);
            stack.pop();
        }
    };

    backtrack(0, 0);
    return res;
};

```

This is a recursive approach which uses stack though

It has three base cases 

1. That count for closedN and openN and n is equal 
2. recursive condition is that either openN  < n or closedN is < openN

I recursive condition we have three steps 

1. Pre 
    1. Here we push things to stack 
2. Recursive 
    1. Here we recall our function with updated arguments 
3. Post 
    1. Here we pop stack.

### Daily temperatures

[Daily Temperatures - LeetCode](https://leetcode.com/problems/daily-temperatures/description/)

This was a bit tricky one with stack 

1. We an temperatures array with temperature values and return output with values showing that each index represent how many days from current index we will have a warmer temperature day.
    
    ![Screenshot 2024-02-28 at 12.39.00 PM.png](Screenshot_2024-02-28_at_12.39.00_PM.png)
    
2. We use stack for this, first we fill res array with all 0 as temperature values.
3. we do a O(N) loop , where if stack has any elements and currentTemperature is greater than stack top.
    1. The inner loop works only if stack has values and currentTemperature value is greater than stack top. ( Monotonic Stack ( decreasing Order Stack ) not strict becuase can have duplicate values )
    2. Otherwise we always push values to stack.
    3. Stack value is poped until currentTemperature is no longer lesser than stack top\
        1. like in case of `72` being currentTemperature, each stack top until `75` is lesser so we pop them and get difference of indexes.
    
    ![Screenshot 2024-02-28 at 12.42.38 PM.png](Screenshot_2024-02-28_at_12.42.38_PM.png)
    

```jsx
var dailyTemperatures = (temperatures) => {
    const res = new Array(temperatures.length).fill(0);
    const stack = [];  // pair: [temp, index]

    for (let i = 0; i < temperatures.length; i++) {
        const t = temperatures[i];
        while (stack.length && t > stack[stack.length - 1][0]) {
            const [stackT, stackInd] = stack.pop();
            res[stackInd] = i - stackInd;
        }
        stack.push([t, i]);
    }
    return res;
}
```

### **Car Fleet**

[Car Fleet - LeetCode](https://leetcode.com/problems/car-fleet/description/)

1. In this question we are looking to find point of intersection of cars before they reach destination so to find if they form a fleet or not.
2. The car with slow speed is the one which will be left while comparing two cars, becuase at each adjacent comaprison we will compare the time taken by them to reach destination. 
    1. Logically if time for `car A` ≤ `carB` it means they both would have collided somewhere before to form a fleet because carA is reaching destination before carB.
3. The next idea is to sort pairs with reverse order ( decreasing order ) because the car moving ahead should be the one to be left after a fleet is confirmed. Becuase the carB which reaches carA will surpass it so it has definitely more speed than carA thus according to question condition carB’s speed will fall to carA speed to form fleet.
    
    ![Screenshot 2024-02-29 at 10.27.45 AM.png](Screenshot_2024-02-29_at_10.27.45_AM.png)
    
4. The next important thing is to measure time taken by cars to reach destination which is key to determine if they collide or not. If 5’s t is ≥ 7’s t then its a fleet

![Screenshot 2024-02-29 at 10.13.38 AM.png](Screenshot_2024-02-29_at_10.13.38_AM.png)

```jsx
/**
 * @param {number} target
 * @param {number[]} position
 * @param {number[]} speed
 * @return {number}
 */
var carFleet = function (target, position, speed) {
    const pair = position.map((p, i) => [p, speed[i]]);
    pair.sort((a, b) => b[0] - a[0]); // arranging in decreasing order
    // reverse order becasue when we reach previous car we need to know what was time for car ahead so as to know if they will form a fleet or not
    const stack = [];   // for storing time values ( allows us to compare two adjacent time values )
    // the car with more time is of lesser speed and will remain in stack because fleet speed == car with slow speed / more time
    for (const [p, s] of pair) {
        // pusing time to stack
        stack.push((target - p) / s);   // (Miles1 - Miles0)/speed
        // comapring last two upper elements ( this condition fails when we have distinct fleet )
        if (stack.length >= 2 && stack[stack.length - 1] <= stack[stack.length - 2]) {
            // only when fleet is formed we pop value lesser time ( fleet speed is slower / more time )
            stack.pop();
        }
    }
    return stack.length;
};
```

## Largest Rectangle in Histogram

[Largest Rectangle in Histogram - LeetCode](https://leetcode.com/problems/largest-rectangle-in-histogram/description/)

This can be understood in three parts 

### Intuition

- If current Height is larger than proceeding one then it an be extended and we have to calculate area it occupies. Also we pop it since it cannot be extended
    - Since proceeding is smaller it can be extended to left, so calculate its extended area.
- if proceeding is larger then current then it can be extended to right and we can calculate area needed.
- if both are same height, can be extended to right
    
    ![Screenshot 2024-03-01 at 8.50.53 AM.png](Screenshot_2024-03-01_at_8.50.53_AM.png)
    
- Noe if we have increasing order, all can be extended to right except last one, but none can be extended to left.
    
    ![Screenshot 2024-03-01 at 8.53.41 AM.png](Screenshot_2024-03-01_at_8.53.41_AM.png)
    
- Observe that since 4 cannot be extended to right, calculate area it can acquire, pop it then
    - 3 can be extended to right so compute area from where it start until it extends ,
    - if next is 2, check 4’s area, pop, check 3’s extended area, pop, check 2’s extended area.
    
    ![Screenshot 2024-03-01 at 8.55.48 AM.png](Screenshot_2024-03-01_at_8.55.48_AM.png)
    

Since we are poping recent ones thus stack is best choice for this.

### Example Explanation ( Code Explanation )

![Screenshot 2024-03-01 at 10.31.05 AM.png](Screenshot_2024-03-01_at_10.31.05_AM.png)

- We push to stack only when next element is larger than before,
    - Otherwise we pop becuase current element cannot be extended to right, so we pop until we find one which can be extended to right,
    - we poped 6, after calculating area, 5 after calculating area until this element with value 2, didn’t poped 1 becuase it can be extended to 2

![Screenshot 2024-03-01 at 10.34.45 AM.png](Screenshot_2024-03-01_at_10.34.45_AM.png)

- At last when we reached 3, its last element so cannot be extended obviously.
    - here we have another loop to check area covered by remaining stack elements
    - 3 occupies, only 3, poped
    - 2 occupies from 3 ( index 5 ) until index 2 i.e 8
    - next is 1 which occupies from index 0 to index 5 i.e 6.

![Screenshot 2024-03-01 at 10.35.58 AM.png](Screenshot_2024-03-01_at_10.35.58_AM.png)

```
/**
 * @param {number[]} heights
 * @return {number}
 */
function largestRectangleArea(heights) {
        let maxArea = 0;
        let stack = [];  // pair: [index, height]

        for (let i = 0; i < heights.length; i++) {
            let start = i;
            while (stack.length > 0 && stack[stack.length - 1][1] > heights[i]) {
                let [index, height] = stack.pop();
                maxArea = Math.max(maxArea, height * (i - index));
                start = index;
            }
            stack.push([start, heights[i]]);
        }

        for (let [index, height] of stack) {
            maxArea = Math.max(maxArea, height * (heights.length - index));
        }

        return maxArea;
    }
```

```jsx
/**
 * @param {number[]} heights
 * @return {number}
 */
function largestRectangleArea(heights) {
        let maxArea = 0;
        let stack = [];  // pair: [index, height]

        for (let i = 0; i < heights.length; i++) {
            let start = i;
            while (stack.length > 0 && stack[stack.length - 1][1] > heights[i]) {
                let [index, height] = stack.pop();
                maxArea = Math.max(maxArea, height * (i - index));
                start = index;
            }
            stack.push([start, heights[i]]);
        }

        for (let [index, height] of stack) {
            maxArea = Math.max(maxArea, height * (heights.length - index));
        }

        return maxArea;
    }
```

## Binary Search

### Implementation

```tsx
export default function bs_list(haystack: number[], needle: number): boolean {
    let lo = 0;
    let hi = haystack.length;
    do {
        const m = Math.floor(lo + (hi - lo) / 2);
        const v = haystack[m];
        if (v === needle) {
            return true;
        } else if (v > needle) {
            hi = m;
        } else {
            lo = m+1;
        }
    } while (lo < hi);
    return false;
}

```

### Search a 2D matrix

[Search a 2D Matrix - LeetCode](https://leetcode.com/problems/search-a-2d-matrix/description/)

Its solution was determined by myself, may be because i remembered it from somewhere earlier.

1. We have a matrix where rows are in non-decreasing order. So last element of each row is lesser than first element of proceeding row.
2. So i simply check in each row if target is greater than last element, if its then surely check in next row, if not then check in current row using binary search.
3. Its seems its time complexity is O(n*logn) where for each row we run binary search. 

```jsx
/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    for ( let row = 0; row < matrix.length ; ++row){
        if(target > matrix[row][matrix[row].length - 1]) continue;
        let lo = 0; 
        let hi = matrix[row].length;
        do{
            const m = Math.floor(lo + (hi - lo)/2);
            if( target === matrix[row][m]) return true;
            else if(matrix[row][m] > target) {
                hi = m;

            }else{
                lo = m + 1;
            }
        }while(lo < hi);    
    }

    return false;
};
```

Method 2

1. Here we follow same pattern but we start at mid row check if target can exist here or not and decide to move either up or below mid row.
2. It provides a complexity of O(logm + logn )

```jsx
/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    const ROWS = matrix.length;
    const COLS = matrix[0].length;

    let top = 0;
    let bot = ROWS - 1;

    while (top <= bot) {
        const row = Math.floor((top + bot) / 2);

        if (target > matrix[row][COLS - 1]) {
            top = row + 1;
        } else if (target < matrix[row][0]) {
            bot = row - 1;
        } else {
            break;
        }
    }

    if (!(top <= bot)) {
        return false;
    }

    const row = Math.floor((top + bot) / 2);
    let l = 0;
    let r = COLS - 1;

    while (l <= r) {
        const m = Math.floor((l + r) / 2);

        if (target > matrix[row][m]) {
            l = m + 1;
        } else if (target < matrix[row][m]) {
            r = m - 1;
        } else {
            return true;
        }
    }

    return false;
};

```

1. 

/**

- @param {number[][]} matrix
- @param {number} target
- @return {boolean}
*/
var searchMatrix = function(matrix, target) {
const ROWS = matrix.length;
const COLS = matrix[0].length;
    
    let top = 0;
    let bot = ROWS - 1;
    
    while (top <= bot) {
    const row = Math.floor((top + bot) / 2);
    
    ```
     if (target > matrix[row][COLS - 1]) {
         top = row + 1;
     } else if (target < matrix[row][0]) {
         bot = row - 1;
     } else {
         break;
     }
    
    ```
    
    }
    
    if (!(top <= bot)) {
    return false;
    }
    
    const row = Math.floor((top + bot) / 2);
    let l = 0;
    let r = COLS - 1;
    
    while (l <= r) {
    const m = Math.floor((l + r) / 2);
    
    ```
     if (target > matrix[row][m]) {
         l = m + 1;
     } else if (target < matrix[row][m]) {
         r = m - 1;
     } else {
         return true;
     }
    
    ```
    
    }
    
    return false;
    };
    

### Koko Eating Bananas

[Koko Eating Bananas - LeetCode](https://leetcode.com/problems/koko-eating-bananas/)

1. A bit tricky it was, we had an array of numbers which represent `n` piles ( lenght of array ) of Bananas where each `index` shows bananas in that pile.
2. We have `h` hours to eat them, while `koko` can eat only `k` bananas each hour, so we have to find min `k` such that koko can eat all bananas in `h` hours.
    1. So we have to check for k = 1 to k = Max(…piles) , because its the max bananas koko can eat.
    2. using binary search over this range from 1 to max we find min `k` for which total hours are less or equal to `h` .
    3. We use Math.ceil becuase division results in float and we need max integer. Add all of them to get total hours koko took for given `k` 
    4. If given k ≤ hours we assign res with min value of `res` and `k` or `m` in terms of coding. Then reduce our right or hi range to `m` or `mid of the range`    

```jsx
/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
var minEatingSpeed = function(piles, h) {
  let lo = 1
  let hi = Math.max(...piles);
  let res = hi;
  do{
      const m = Math.floor(lo+ (hi - lo)/2);
      let hours = 0;
      for ( let i = 0; i < piles.length ; ++i){
          hours += Math.ceil(piles[i]/m);
      }

      if(hours <= h){
          res = Math.min(res,m);
          hi = m;
      }else{
          lo = m + 1;
      }
  }while(lo < hi);

  return res;
};
```

With few adjustments i was able to get to this solution thanks to discussions 

```jsx
/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
var minEatingSpeed = function (piles, h) {
    let lo = 1;
    let hi = Math.max(...piles);
    let res = hi;
    while (lo <= hi) {
        let m = Math.floor(lo + (hi - lo) / 2);
        let sum = 0;
        piles.forEach((pile) => {
            sum += Math.ceil(pile / m);
            return sum;
        })
        if (sum <= h) {
            res = Math.min(res, m)
            hi = m - 1;
        } else {
            lo = m + 1;
        }
    }

    return res;
};
```

### Find Minimum in Sorted Array

[Find Minimum in Rotated Sorted Array - LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)

My code seems a bit rough, could be simplified. But i think its a good solution, the solution from neetcode is also good given we keep track of min value .

```jsx
/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    let lo = 0;
    let hi = nums.length - 1;
    if(nums.length === 1) return nums[0];
    do{
        const m = Math.floor(lo + (hi - lo)/2);
        if(nums[hi] > nums[0]) return nums[0];

        if(m < hi && nums[m] > nums[m+1]){
            return nums[m+1];
        }
        if (m > lo && nums[m] < nums[m-1]){
            return nums[m];
        }

        // case 3
        if(nums[m] < nums[lo]){
                hi = m;
        }else{
            lo = m + 1;
        }
    }while(lo < hi);

    return -1;
};
```

### Search in a rotated sorted array

[Java_DSA](https://www.notion.so/Java_DSA-8a6e1ebb79f14151904c5561d1de7707?pvs=21) There is a similar question i did back in Uni for JAVA, so it can be checked there. Its solution follows to find pivot, 

- If its sorted array it will be there its simple ascending order array.
- If pivot is there find if target should be right or left side of pivot and use simple binary search to return index.

[Search in Rotated Sorted Array - LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/description/)

```jsx
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    const pivot = findPivot(nums);
    if(pivot === -1){
        return binarySearch(nums, target, 0, nums.length - 1);
    }
    if(target === nums[pivot]){
        return pivot;
    }
    if(target >= nums[0]){
        return binarySearch(nums,target,0,pivot-1);
    }
    return binarySearch(nums, target, pivot + 1, nums.length - 1);
};

function binarySearch(nums, target,lo, hi){
    while(lo <= hi){
        const m = Math.floor(lo+(hi-lo)/2);
        if(nums[m] === target){
            return m;
        }else if(target > nums[m]){
            lo = m+1;
        }else{
            hi = m-1;
        }

    }
    return -1;
}

function findPivot(nums){
    let lo = 0;
    let hi = nums.length - 1;

    while(lo <= hi){
        const m = Math.floor(lo+ (hi - lo)/2);
        if(m < hi && nums[m] > nums[m+1]){
            return m;
        }
        if(m > lo && nums[m] < nums[m-1]){
            return m-1;
        }
        if(nums[m] <= nums[lo]){
            hi = m - 1;
        }else{
            lo = m+1;
        }
    }
    return -1;
}
```

### [Time Based Key Value Store](https://leetcode.com/problems/time-based-key-value-store/)

This was a deisgn question and using binary search to get values 

1. We save value for given key in a list
2. so it means a given key has value as list of values 
3. where each value is a pair of (`value, timestamp`)
4. When we are making a get operation we provide a key, to navigate specific list of values, and a timestamp,
5. The resultant value returned by `get` should be less than or equal to timestamp or the most recent timestamp to current timeStamp value like if timeStamp is 4, the most recent will be either 4 or any lesser one which-ever is available in the list of pair values. 

```jsx
class TimeMap {
    constructor(){
        this.map={};
    }
    /**
     * @param {string} key
     * @param {string} value
     * @param {number} timestamp
     * Time O(1) | Space O(1)
     * @return {void}
     */
    set(key,value,timestamp){
        const bucket = this.map[key] || [];
        this.map[key] = bucket;
        bucket.push([value, timestamp]);
    }
    /**
     * @param {string} key
     * @param {number} timestamp
     * Time O(log(N)) | Space O(1)
     * @return {string}
     */
    get(key, timestamp, value = '', bucket = this.map[key] || []) {
        let [lo, hi] = [0, bucket.length - 1];

        while (lo <= hi) {
            const mid = (lo + hi) >> 1;
            const [guessValue, guessTimestamp] = bucket[mid];

            const isTargetGreater = guessTimestamp <= timestamp;
            if (isTargetGreater) {
                value = guessValue;
                lo = mid + 1;
            }

            const isTargetLess = timestamp < guessTimestamp;
            if (isTargetLess) hi = mid - 1;
        }

        return value;
    }
}
```

or this one 

```jsx
class TimeMap {
    constructor(){
        this.map={};
    }
    /**
     * @param {string} key
     * @param {string} value
     * @param {number} timestamp
     * Time O(1) | Space O(1)
     * @return {void}
     */
    set(key,value,timestamp){
        const bucket = this.map[key] || [];
        this.map[key] = bucket;
        bucket.push([value, timestamp]);
    }
    /**
     * @param {string} key
     * @param {number} timestamp
     * Time O(log(N)) | Space O(1)
     * @return {string}
     */
    get(key, timestamp, value = '', bucket = this.map[key] || []) {
        let [lo, hi] = [0, bucket.length - 1];

        while (lo <= hi) {
            const mid = (lo + hi) >> 1;
            if(bucket[mid][1] <= timestamp){
                value = bucket[mid][0];
                lo = mid + 1;
            }else{
                hi = mid - 1;
            }
        }

        return value;
    }
}
```

### Median of Two Sorted Arrays

This was a really tough question to digest even its solution.

The overall run time complexity should be O(log (m+n)).

**Statment**
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

I ll share the important points here only

- In case of Odd length simply middle is the median.
    
    ![Untitled](Learning/JavaScript/JavaScript%20DSA/attachments/Untitled.png)
    
- In case of even length array its simply the last element of Left half ( rightmost ) and first or leftMost of 2nd half.
    
    ![Untitled](Learning/JavaScript/JavaScript%20DSA/attachments/Untitled%201.png)
    
- The intuition is to somehow find the left half, so left partition to be roughly half of the total length.
- We get left half for smaller array using binary search and using it we get left half of larger array as well using
    - Half - midLength of Smaller array.
        
        ![Untitled](Learning/JavaScript/JavaScript%20DSA/attachments/Untitled%202.png)
        
- Now time to verfiy if its correct Left partition,
    - Since arrays are ordered then rightMost in left partition of  `A` is definitely lesser or equal to leftMost in the right partition of `B` .
        
        ![Untitled](Learning/JavaScript/JavaScript%20DSA/attachments/Untitled%203.png)
        
    - Same for rightmost of Left partition of `B` is lesser or equal to leftMost of right partition of `A`.
    - The median is min of leftMost of right partitions of Both `A and B` .
        
        ![Untitled](Learning/JavaScript/JavaScript%20DSA/attachments/Untitled%204.png)
        
- Another case might be where total is even.
    - In this case the left partition calculated might not be correct in first try when checking conditions we specified earlier for rightMost of left partition of both A and B to be lesser to leftMost of right partition of both `A` and `B`.
        
        ![Untitled](Learning/JavaScript/JavaScript%20DSA/attachments/Untitled%205.png)
        
    - So we simply increment left pointer.
    - however median is Max of rightmost of ;eft partitions of both + Min of leftMost of right partition of both
    
    ![Untitled](Learning/JavaScript/JavaScript%20DSA/attachments/Untitled%206.png)
    
- Edge case, if smaller array has zero elements then we take positive and negative infinity to e checked for our conditions.

![Untitled](Learning/JavaScript/JavaScript%20DSA/attachments/Untitled%207.png)

![Untitled](Learning/JavaScript/JavaScript%20DSA/attachments/Untitled%208.png)

```jsx
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
   let A = nums1, B = nums2;
    let total = nums1.length + nums2.length;
    let half = Math.floor(total / 2);

    // Ensure A is the shorter array.
    if (B.length < A.length) {
        [A, B] = [B, A];
    }

    let l = 0, r = A.length - 1;
    while (true) {
        let i = Math.floor((l + r) / 2); // Mid index for A
        let j = half - i - 2; // Complementary index for B

        // Handling the edges of A and B
        let Aleft = i >= 0 ? A[i] : -Infinity;
        let Aright = (i + 1) < A.length ? A[i + 1] : Infinity;
        let Bleft = j >= 0 ? B[j] : -Infinity;
        let Bright = (j + 1) < B.length ? B[j + 1] : Infinity;

        // Correct partition
        if (Aleft <= Bright && Bleft <= Aright) {
            // If total is odd
            if (total % 2) {
                return Math.min(Aright, Bright);
            }
            // If total is even
            return (Math.max(Aleft, Bleft) + Math.min(Aright, Bright)) / 2;
        } else if (Aleft > Bright) {
            r = i - 1;
        } else {
            l = i + 1;
        }
    }
};
```

- Explanation in lay terms
    
    **Imagine a Card Game:**
    
    Suppose you and a friend each have a deck of cards that are already sorted by value (from smallest to largest). You want to find the median card (the middle card) if you combined both decks together. The median is the card that splits the combined decks into two equal halves.
    
    **The Problem:**
    
    If you simply merge the two decks together and find the median, it would take time proportional to the total number of cards, which is slow. You want to do it faster, without fully merging the decks.
    
    **The Idea:**
    
    Instead of merging, think about how you can directly find the middle by **cutting** or **dividing** the decks in a way that balances them.
    
    **Key Observations:**
    
    1.	**Median Concept**:
    
    •	The median is the value where half of the combined cards are smaller, and half are larger.
    
    2.	**Balanced Split**:
    
    •	You need to find a point in both decks where you can “cut” them such that the number of cards on the left side of the cut (in both decks combined) is equal to the number on the right side.
    
    **Visual Example:**
    
    Imagine:
    
    •	Deck A has 5 cards: [1, 3, 8, 9, 15]
    
    •	Deck B has 6 cards: [7, 11, 18, 19, 21, 25]
    
    You want to find the median of these two decks combined without merging them fully.
    
    **How to Cut:**
    
    1.	**Think of dividing one of the decks** (the smaller one) at some point:
    
    •	Let’s try cutting Deck A after the first 2 cards. So, Deck A is split into:
    
    •	Left side of A: [1, 3]
    
    •	Right side of A: [8, 9, 15]
    
    2.	**Now, automatically cut Deck B** at a position that balances the number of cards:
    
    •	Since Deck B has 6 cards, cut it so that the combined left sides from both decks have the same number of cards as the combined right sides.
    
    •	This gives:
    
    •	Left side of B: [7, 11, 18, 19]
    
    •	Right side of B: [21, 25]
    
    **How to Know If the Cut Is Correct:**
    
    To ensure you’ve found the correct cut, check two things:
    
    1.	**All cards on the left side should be less than or equal to all cards on the right side.**
    
    •	This means:
    
    •	The largest card on the left side of both decks (max(A_left) and max(B_left)) should be less than or equal to the smallest card on the right side of both decks (min(A_right) and min(B_right)).
    
    2.	**Specifically, we need to check two conditions:**
    
    •	max(A_left) <= min(B_right): The largest card in the left side of Deck A should be less than or equal to the smallest card in the right side of Deck B.
    
    •	max(B_left) <= min(A_right): The largest card in the left side of Deck B should be less than or equal to the smallest card in the right side of Deck A.
    
    **Why These Conditions Matter:**
    
    If both conditions are met, you have perfectly balanced the two halves, meaning that the largest element on the left is smaller than the smallest on the right. This means you’ve correctly found the median, or you are in a position to calculate it.
    
    **Recap with Intuition:**
    
    •	**Dividing the smaller deck** allows us to more quickly and easily balance the total number of cards on either side of the cut.
    
    •	**Checking the largest left and smallest right** ensures that we have indeed found a valid split where the median could be calculated.
    
    The formula for partitionY might seem unintuitive at first, but it’s derived from the requirement that the combined left halves of both arrays should have an equal (or almost equal) number of elements as the combined right halves. Let’s break it down.
    
    **Understanding partitionY:**
    
    When you split both arrays, you’re effectively dividing them into four parts:
    
    •	**Left side of A (A_left)**
    
    •	**Right side of A (A_right)**
    
    •	**Left side of B (B_left)**
    
    •	**Right side of B (B_right)**
    
    The goal is to ensure that the number of elements in the combined left halves (A_left + B_left) is the same as in the combined right halves (A_right + B_right).
    
    **Balancing the Two Halves:**
    
    If the total number of elements in both arrays combined is even:
    
    •	The left half will contain exactly half of the elements.
    
    •	The right half will contain the other half.
    
    If the total number of elements is odd:
    
    •	The left half will contain one more element than the right half.
    
    **Formula for partitionY:**
    
    Let’s derive the formula for partitionY:
    
    1.	**Total Elements:**
    
    •	Let the total number of elements be m + n.
    
    •	Half of this total, plus one more (to handle odd numbers), would be (m + n + 1) / 2.
    
    2.	**Split the Elements:**
    
    •	partitionX is the number of elements you put on the left side of the partition in Array A.
    
    •	Then, to balance the total elements, the remaining elements on the left side must come from Array B.
    
    3.	**Ensuring Balance:**
    
    •	If you already have partitionX elements on the left from Array A, then you need (m + n + 1) / 2 - partitionX elements from Array B to maintain the balance.
    
    •	This calculation ensures that the total number of elements on the left side (A_left + B_left) equals the total number on the right side (A_right + B_right).
    
    **Why Not Use Midpoint for B (partitionY)?**
    
    If you used (low + high) / 2 for partitionY, you would ignore the constraint that both halves must be balanced according to the total number of elements in both arrays. The formula (m + n + 1) / 2 - partitionX directly addresses this by automatically adjusting partitionY based on how you split Array A.
    

## Sliding Window

### Algorithm Intuition

![image.png](Learning/JavaScript/JavaScript%20DSA/attachments/image.png)

![Screenshot 2024-08-19 at 9.37.13 AM.png](Screenshot_2024-08-19_at_9.37.13_AM.png)

The basic idea behind the sliding window technique is to transform two nested loops into a single loop. Below are some fundamental clues to identify sliding window algorithm problems:

- The problem will be based on an array, list or string type of data structure.It will ask to find subranges in that array to give the longest, shortest or target values of a string.
- Its concept is mainly based on ideas like the longest sequence or shortest sequence of something that satisfies a given condition perfectly.

details at 

[Sliding Window Algorithm Explained | Built In](https://builtin.com/data-science/sliding-window-algorithm)

### **Best Time to Buy and Sell Stock**

[Best Time to Buy and Sell Stock - LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)

Based on the fact that we have to sell after we buy and we are trying to maximize profit, we can iterate through the prices and only need to consider two things:

1.) **Is this price cheaper than any other price I've seen before?**

2.) If I subtract current price by the cheapest price I've found, **does this yield a greater profit than what I've seen so far?**

*A fun thing to note is if #1 is true, then #2 cannot be true as well so there isn't a need to check*

Let's consider an example of [4,1,5,2,7]

- 4 is the cheapest price we see to start, and we can't sell on the first day so maxProfit is 0
- 1 is now the cheapest price we've seen. Selling now would lose us money, so we can't update maxProfit
- 5 is not cheaper than 1, but if we sell now we get a maxProfit of 4! Better save that for later
- 2 is not cheaper than 1 and if we sell, we only get a profit of 1, no need to do anything here
- 7 is not cheaper than 1, but if we sell here, we'll increase maxProfit to 6, making this the best profit to return.

```jsx
/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let cheapestPrice = prices[0];
    let maxProf = 0;
    for (let i = 1; i < prices.length; ++i){
        if(cheapestPrice > prices[i]){ 
            maxProf = Math.max(maxProf,prices[i] - cheapestPrice);
            cheapestPrice = prices[i];
        }
        else{
            maxProf = Math.max(maxProf,prices[i] - cheapestPrice);
        }
    }
    return maxProf;
};

```

### Longest Substring Without Repeating Characters

[](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)

Here we approach problem using sliding window technique and Set

1. Use `Set` to store unique values ( so no repetitive/ duplicate values ).
2. if current looping value is not there in the set we add it to set and update max substring as `res`.
3. if value is there in `Set` then we remove left most and increment left pointer.

```jsx
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let charSet = new Set();
    let l = 0;
    let res = 0;
    for ( let r = 0; r < s.length ; ++r){
        while (charSet.has(s[r])){
            charSet.delete(s[l]);
            l++;
        }
        charSet.add(s[r]);
        res = Math.max(res, charSet.size);
    }
    return res;
};
```

### **Longest Repeating Character Replacement**

[Longest Repeating Character Replacement - LeetCode](https://leetcode.com/problems/longest-repeating-character-replacement/description/)

This is a tricky question in a way that we have to count maxSubstring where we could replace characters `k` times. 

1. The first thing is window length `r - l + 1` where r is `right pointer` which moves ahead while `l` is `left pointer` which is initially set at start.
2. Then we have a `count` object which shows `count` of each `character`.
3. Third important thing is to verify if the window is valid, which is `windowLen - maxCharCount` we need to find the count of elements that can replaced `k` times so as to match count of maxCharacterCount or maxSubstring. 
    
    ![Screenshot 2024-04-02 at 11.19.43 AM.png](Screenshot_2024-04-02_at_11.19.43_AM.png)
    
4. If the result is ≤ k then window size is correct. It actually shows the number of characters which can be replaced. And it should not be greater than k.
5. If greater we are gonna increment left pointer `l` and decrement the count of left pointer value.  
6. The first thing when we start let suppose a window and in that window the maxSubstring can be get by 
7. We also update our `result` in each iteration after we have made sure our window is of right length. Res is actually the max length of window. 
    
    ![Screenshot 2024-04-02 at 10.58.24 AM.png](Screenshot_2024-04-02_at_10.58.24_AM.png)
    

```jsx
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function(s, k) {
    let count = {};
    let res = 0;
    let l = 0;
    for(let r = 0; r < s.length ; ++r){
        count[s[r]] = 1 + (count[s[r]] || 0);
        while ((r- l + 1) - Math.max(...Object.values(count)) > k){
            count[s[l]] -= 1;
            l += 1;
        }
        res = Math.max(res, r - l + 1);
    }

    return res;
};
```

The second way considers the usage of `maxFrequency` to avoid getting maxCount values from has table.

1. Maximum frequency is the max count of character in hash table.
2. The new formula becomes `window len - maxFrequency <= k` where final purpose is to maximize the `window length` which ultimately becomes `result` .
3. To maximize the window length we also need to maximize the maxFreq as `windowLeng = maxF + k` where k is constant so only variable is maxFreq
4. Thus if ever maximum frequency gets `decrement` we are not gonna change `result` . Because res is maximum window length. But increment does have afect `result` so we can increment it but no need to decrement.

```jsx
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function(s, k) {
    let count = {};
    let res = 0;
    let l = 0;
    let maxF = 0;
    for(let r = 0; r < s.length ; ++r){
        count[s[r]] = 1 + (count[s[r]] || 0);
        maxF = Math.max(maxF, count[s[r]]);
        while ((r- l + 1) - maxF > k){
            count[s[l]] -= 1;
            l += 1;
        }
        res = Math.max(res, r - l + 1);
    }

    return res;
};
```

Now even when we decrement left pointer `l` we do not decrement `maxF` as it does not needs to be.

### **Permutation in String**

[Permutation in String - LeetCode](https://leetcode.com/problems/permutation-in-string/description/)

- It means that if we have two strings `s1` and `s2` .
- Then `s1` permutation should be in the `s2` in other words exact same characters with same or different order should be substring of `s2`.
- The first way is to use hash map.
    - Where we use sliding window technique, and window size is length of `s1` .
    - Then we use same window size and move it over the whole `s2` .
    - We will be using  hash maps for both and where first has count of each `s1` while hash map for `s2` has count of characters in current window.
    - At last we compare both hash maps that is O(26).
- The second algorithm uses a `matches` which show exactly how many characters match for two strings `s1` and `s2` .
    - if `a` is in both strings, its match count is same, let’s suppose a,b and in `s1` and a,b in `s2` are same while c in `s1` and x in `s2` are not matching, this will make Matches value as 24 . Once its over the matches would have exact same count for each character.
    
    ![Untitled](Learning/JavaScript/JavaScript%20DSA/attachments/Untitled%209.png)
    
    - Our window size is = length of string `s1` . We move to right by removing one from left and adding one to right in `s2`. Now count of b 0 and count of y is 1 , thus mismatches, and also y mismatches so in total remove 2 from 24. so `22`
    
    ![Untitled](Learning/JavaScript/JavaScript%20DSA/attachments/Untitled%2010.png)
    
    ```jsx
    /**
     * @param {string} s1
     * @param {string} s2
     * @return {boolean}
     */
    var checkInclusion = function(s1, s2) {
        if (s1.length > s2.length) {
                return false;
            }
    
            let s1Count = new Array(26).fill(0);
            let s2Count = new Array(26).fill(0);
    
            for (let i = 0; i < s1.length; i++) {
                s1Count[s1.charCodeAt(i) - 'a'.charCodeAt(0)] += 1;
                s2Count[s2.charCodeAt(i) - 'a'.charCodeAt(0)] += 1;
            }
    
            let matches = 0;
            for (let i = 0; i < 26; i++) {
                matches += s1Count[i] === s2Count[i] ? 1 : 0;
            }
    
            let l = 0;
            for (let r = s1.length; r < s2.length; r++) {
                if (matches === 26) {
                    return true;
                }
    
                let index = s2.charCodeAt(r) - 'a'.charCodeAt(0);
                s2Count[index] += 1;
                if (s1Count[index] === s2Count[index]) {
                    matches += 1;
                } else if (s1Count[index] + 1 === s2Count[index]) {
                    matches -= 1;
                }
    
                index = s2.charCodeAt(l) - 'a'.charCodeAt(0);
                s2Count[index] -= 1;
                if (s1Count[index] === s2Count[index]) {
                    matches += 1;
                } else if (s1Count[index] - 1 === s2Count[index]) {
                    matches -= 1;
                }
                l += 1;
            }
            return matches === 26;
    };
    ```
    

### **Minimum Window Substring**

[Minimum Window Substring - LeetCode](https://leetcode.com/problems/minimum-window-substring/description/)

1. Using a similar approach of Sliding window Technique.
    1. First lets see a brute force approach. 
    2. We use two hash maps `window` and `t` .
    3. The dea is to find minimum window in `S` that contains `t` hash map ( count and characters )
    
    ![Screenshot 2024-04-16 at 11.29.34 AM.png](Screenshot_2024-04-16_at_11.29.34_AM.png)
    
    d.  `Window` is how we have and `t` is what we need, in current window 
    
    ![Screenshot 2024-04-16 at 11.34.28 AM.png](Screenshot_2024-04-16_at_11.34.28_AM.png)
    
    e. In the brute force approach we will have to compare the hash maps again n again while in a optimized case we will have two integers `have` and `need` where we compare these.
    
    f. `have` can be larger than `need` .
    
    g. This is O(1) as we will only compare each relevant character in `window` and `t` and integers `have` and `need` .
    
    ![Screenshot 2024-04-16 at 12.00.27 PM.png](Screenshot_2024-04-16_at_12.00.27_PM.png)
    
2. Until this position, given window has all the characters as in `t`. But its only a possible result.
    
    ![Screenshot 2024-04-16 at 12.04.46 PM.png](Screenshot_2024-04-16_at_12.04.46_PM.png)
    
3. At this point we store the length of the window in `res` so that when we are gonna move right pointer and left pointers we will make sure that next time when window has `have` and `need` similar count and hash maps equal we compare res value which should be lesser and not larger.
    
    ![Screenshot 2024-04-16 at 12.21.02 PM.png](Screenshot_2024-04-16_at_12.21.02_PM.png)
    
4. We move left pointer after our `window` has same character count as `t` . while we move right until we do not reach a point where window === t and have === need.
5. We pop out characters ln left pointer until we do not reach a point where `window` ≠ `t` .
6. Remember, when `window === t` we gonna update have to be `have === need` and then move left pointer until `have ≠ neeed` . Once its there we start moving right until it again is `have === need`.

```jsx
/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function(s, t) {
    if(t === "") return "";
    let countT = {};
    let window = {};

    // initialzied the count of t
    for( let c of t) {
        countT[c] = 1  + (countT[c] || 0);
    }

    let have = 0
    let need = Object.keys(countT).length;
    let res = [-1, -1];
    let resLen = Infinity;
    let l = 0;
    for(let r = 0; r < s.length ; r++){
        let c = s[r];
        window[c] = 1 + (window[c] || 0); 

        if(countT[c] && window[c] === countT[c]){
            have++;
        }
        while (have === need){
            // Update the res and resLen 
            if((r - l + 1) < resLen){
                res = [l,r];
                resLen = r - l + 1;
            }
            // pop from the left until condition breaks
            window[s[l]] -= 1;
            if(countT[s[l]] && (window[s[l]] < countT[s[l]])){
                have -= 1;
            }
            l++;
        }
    }
    // Extract the minimum length window
    l = res[0], r = res[1];
    return resLen === Infinity ? "" : s.slice(l, r + 1);
};
```

### Maximum Window Substring

[Sliding Window Maximum - LeetCode](https://leetcode.com/problems/sliding-window-maximum/description/)

- The reason why we are suing deque here is we have to remove things from both sides but first lets understand why ?
    - We have an array like `[1,2,3,4]` where k = 3 ( window size) now in first window maxElement = 3, then when we move ahead the maxElement = 4 but we know now that 3 > 2 so why even check it at all, we should remove it and only check for ones that are on right or only greater than the current largest.
    - This means we could have to remove elments from both ends.
    
    ![Screenshot 2024-04-23 at 10.54.31 AM.png](Screenshot_2024-04-23_at_10.54.31_AM.png)
    
    - We pop the element from left when either its out of bounds for our window.
    - When current element in window is not greater than top element in dequeue we can add it to dequeue.
    
    ![Screenshot 2024-04-23 at 11.02.07 AM.png](Screenshot_2024-04-23_at_11.02.07_AM.png)
    
    - In this line we make sure that top does not contain any element which is lesser than current element otherwise remove it from top.
    
    ```jsx
    // Remove elements from the deque while the element at these indices is less than the current element
            while (deq.length && nums[deq[deq.length - 1]] < nums[i]) {
                deq.pop();  // equals pop_right or pop_end
            }
    ```
    
    - this removes values which are out of bounds for our current window , i.e if left pointer ( l ) is greater than the the right pointer ( deq[0] is bottom value or leftmost value )
    
    ```jsx
    // Remove indices that are out of the current window
            if (l > deq[0]) {
                deq.shift();    // equals pop_left()
            }
    ```
    
    - At last we make sure to check if our window has atleast elements of window size k . then we push the top left most element to result. As leftmost is largest until now.
        
        ```jsx
        // If the window has filled at least k elements, add the maximum to the result
                if (i + 1 >= k) {
                    result.push(nums[deq[0]]);
                    l++;
                }
        ```
        

```jsx
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSlidingWindow = function (nums, k) {
    const deq = []; // This will simulate our deque
    const result = [];
    let l = 0;
    for (let i = 0; i < nums.length; i++) {

        // Remove elements from the deque while the element at these indices is less than the current element
        while (deq.length && nums[deq[deq.length - 1]] < nums[i]) {
            deq.pop();  // equals pop_right
        }

        // Add the current index at the end of the deque
        deq.push(i);
        // Remove indices that are out of the current window
        if (l > deq[0]) {
            deq.shift();    // equals pop_left()
        }

        // If the window has filled at least k elements, add the maximum to the result
        if (i + 1 >= k) {
            result.push(nums[deq[0]]);
            l++;
        }
    }

    return result;
};
```

## Linked List

### **Reverse Linked List**

[Reverse Linked List - LeetCode](https://leetcode.com/problems/reverse-linked-list/description/)

Iterative approach 

```jsx
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    let prev = null;
    let curr = head;
    while(curr){
        let next = curr.next;   // null
        curr.next = prev;   // 5 -> 4
        prev = curr;    // prev -> 5
        curr = next;    // curr => null
    }
    return prev
};
```

Recursive Approach

```jsx
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    if (head === null){
        return null 
    }

    let newHead = head;
    if(head.next){
        newHead = reverseList(head.next);
        head.next.next = head;
    }
    head.next = null;
    return newHead;
};
```

### Merge two linked lists

[Merge Two Sorted Lists - LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/)

```jsx
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    let dummy = new ListNode(0,null);
    let tail = dummy;   // a empty dummy node 
    while(list1 && list2){
        if(list1.val < list2.val){
            tail.next = list1;
            list1 = list1.next;
        }else{
            tail.next = list2;
            list2 = list2.next;
        }
        tail = tail.next;
    }
    // in case if any one of the list is larger than other, there would be portion still left to explore
    tail.next = list1 || list2;

    return dummy.next;
};
```

Recursive approach

```jsx
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    // base case if either of the list is empty 
    if(!list1) return list2;
    if(!list2) return list1;

    // pre recursion : make sure samller node gets to start of merged list
    if(list1.val < list2.val){
        list1.next = mergeTwoLists(list1.next, list2);
        // post recursion : merge the remainig merged list 
        return list1;
    }
    else{
        list2.next = mergeTwoLists(list1, list2.next);
        // post recursion : merge the remainig merged list 
        return list2;
    }
};
```

### **Steps and Recursion Details**

**1. Base Case**:

- The base cases occur when one of the lists is empty (**`null`**). If **`list1`** is **`null`**, we return **`list2`**, and if **`list2`** is **`null`**, we return **`list1`**. This is because an empty list merged with a non-empty list results in the non-empty list.

**2. Pre-Recursion Step**:

- Determine which node from the two lists has the smaller value. This node will be the starting node of the merged list. This is done before the recursion call.

**3. Recursion Step**:

- Recursively merge the rest of the lists starting from the next node of the smaller node found in the pre-recursion step.

**4. Post-Recursion Step**:

- After the recursion call returns the merged list of the smaller sub-problems, connect the smaller node (identified in pre-recursion) to this result. This step effectively builds the final linked list from the end to the beginning as each recursive call completes and unwinds.

### **Recursive JavaScript Function**

Here is how you can write this recursively in JavaScript:

```jsx
javascriptCopy code
class ListNode {
    constructor(val = 0, next = null) {
        this.val = val;
        this.next = next;
    }
}

function mergeTwoLists(list1, list2) {
    if (list1 === null) {
        return list2;
    } else if (list2 === null) {
        return list1;
    }

    if (list1.val < list2.val) {
        // Pre-recursion: Determine the smaller node
        list1.next = mergeTwoLists(list1.next, list2); // Recursion step
        return list1; // Post-recursion: Attach the remaining merged list
    } else {
        list2.next = mergeTwoLists(list1, list2.next); // Recursion step
        return list2; // Post-recursion: Attach the remaining merged list
    }
}

```

### **Explanation:**

- **Base Case**: When either **`list1`** or **`list2`** is **`null`**, we simply return the other list since there's nothing left to merge.
- **Pre-Recursion Step**: Before making a recursive call, we compare the values of the heads of **`list1`** and **`list2`**.
- **Recursion Step**: We call **`mergeTwoLists`** recursively, depending on which head is smaller. If **`list1`**'s value is smaller, then **`list1.next`** will point to the result of **`mergeTwoLists(list1.next, list2)`**.
- **Post-Recursion Step**: The current smallest node's **`next`** pointer is set to the result of the recursive call, effectively building the list backward from the end to the beginning as each call returns.

This recursive approach elegantly divides the problem into smaller and simpler problems, and solves each recursively, thereby merging the lists.

[](https://lh3.googleusercontent.com/a/AEdFTp4esAzbDwFi5kGW4-1Ws9SqQ_1zxMuFQtRE7yPBEw=s96-c)

**You**

can you provide an example with a diagram maybe to i illustrate it

ChatGPT

**ChatGPT**

Sure, let's visualize the recursive merging process of two linked lists with an example and a diagram. Suppose we have two linked lists:

- **List1**: 1 → 3 → 5
- **List2**: 2 → 4 → 6

We want to merge these two lists into a single sorted list.

### **Step-by-Step Process**

1. **Initial Call**:
    - Compare the heads of both lists. Since **`1`** (from List1) is less than **`2`** (from List2), **`1`** will be the head of the merged list.
    - Recursively merge the rest: **`3 → 5`** with **`2 → 4 → 6`**.
2. **Recursive Call 1**:
    - Now compare **`3`** (List1) with **`2`** (List2). **`2`** is smaller.
    - Recursively merge the rest: **`3 → 5`** with **`4 → 6`**.
3. **Recursive Call 2**:
    - Compare **`3`** (List1) with **`4`** (List2). **`3`** is smaller.
    - Recursively merge the rest: **`5`** with **`4 → 6`**.
4. **Recursive Call 3**:
    - Now compare **`5`** (List1) with **`4`** (List2). **`4`** is smaller.
    - Recursively merge the rest: **`5`** with **`6`**.
5. **Recursive Call 4**:
    - Compare **`5`** (List1) with **`6`** (List2). **`5`** is smaller.
    - Recursively merge the rest: **`null`** with **`6`**.
6. **Recursive Call 5**:
    - List1 is now **`null`**, so return **`6`**.

### **The Unwinding Phase**

Each call now begins to unwind and constructs the final list:

- **Return from Recursive Call 5**: Returns **`6`**.
- **Complete Call 4**: Attaches **`5`** to **`6`**. Returns **`5 → 6`**.
- **Complete Call 3**: Attaches **`4`** to **`5 → 6`**. Returns **`4 → 5 → 6`**.
- **Complete Call 2**: Attaches **`3`** to **`4 → 5 → 6`**. Returns **`3 → 4 → 5 → 6`**.
- **Complete Call 1**: Attaches **`2`** to **`3 → 4 → 5 → 6`**. Returns **`2 → 3 → 4 → 5 → 6`**.
- **Complete Initial Call**: Attaches **`1`** to **`2 → 3 → 4 → 5 → 6`**. Returns **`1 → 2 → 3 → 4 → 5 → 6`**.

### **Diagram**

Here's a simple diagram illustrating the merging:

```rust
rustCopy code
List1: 1 -> 3 -> 5
       |
       v
       1 -> MERGE(3 -> 5, 2 -> 4 -> 6)
            |
            v
            2 -> MERGE(3 -> 5, 4 -> 6)
                 |
                 v
                 3 -> MERGE(5, 4 -> 6)
                      |
                      v
                      4 -> MERGE(5, 6)
                           |
                           v
                           5 -> MERGE(null, 6)
                                |
                                v
                                6 -> MERGE(null, null)

```

Each step involves a decision to move forward with the smaller node and a recursive call to handle the remainder of the list not chosen. This recursive merging continues until the base cases are hit, and then the list is constructed backward as the recursion unwinds. This process combines simplicity with the effectiveness of recursion to deal with merging sorted lists.

### Reorder a linked list

[Reorder List - LeetCode](https://leetcode.com/problems/reorder-list/description/)

- Slow and fast pointers approach allows us to find exact middle node ( odd case ) and edge of middle ( even case ).
    - In case of Even nodes the start of right half is next of the (**Slow**) first pointer.
    - While in case of Odd number of nodes, the second half is obviously the nodes after the Slow pointer
- The algorithm is to find middle and then right part if reversed and merged with first to get final result

```jsx
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function (head) {
    let slow = head, fast = head ? head.next : null;
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
    }

    // reverse second half
    let second = slow ? slow.next : null;
    let prev = slow ? (slow.next = null) : null;
    while (second) {
        let tmp = second.next;
        second.next = prev;
        prev = second;
        second = tmp;
    }

    // merge two halves
    let first = head, secondHalf = prev;
    while (secondHalf) {
        let tmp1 = first.next, tmp2 = secondHalf.next;
        first.next = secondHalf;
        secondHalf.next = tmp1;
        first = tmp1;
        secondHalf = tmp2;
    }

};
```

### Remove Nth node from end of list

[](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/)

```jsx
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function (head, n) {
    let dummy = new ListNode(0, head);
    let left = dummy;
    let right = head;
    while (n > 0) {
        right = right.next;
        n--;
    }

    while (right) {
        left = left.next;
        right = right.next

    }
    left.next = left.next.next
    return dummy.next
};
```

- Here we take two pointers where one is at start and one `n` points away. We increment until right pointer is null.
    
    ![Screenshot 2024-05-07 at 10.33.00 AM.png](Screenshot_2024-05-07_at_10.33.00_AM.png)
    
- Now our left pointer is exactly at the node to be deleted, but technically we should be one step behind.
- For that we initialise left with a `dummy` node one step behind head.
- Now when right is null we are at node to deleted.

### **Copy List with Random Pointer**

[Copy List with Random Pointer - LeetCode](https://leetcode.com/problems/copy-list-with-random-pointer/description/)

- Here we use 2 pass ( 2 loops ) where in first loop we we only create copies of each node and make a hash map to reference the copied node with original node.

![Screenshot 2024-05-13 at 2.40.51 PM.png](Screenshot_2024-05-13_at_2.40.51_PM.png)

- In second loop we are gonna link these, if a random pointer is a node in future we can easily refer it from the hash map.

```jsx
/**
 * // Definition for a Node.
 * function Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

/**
 * @param {Node} head
 * @return {Node}
 */
var copyRandomList = function (head) {
    let oldToCopy = new Map();
    
    let cur = head;
    while (cur) {
        let copy = new Node(cur.val);
        oldToCopy.set(cur, copy);
        cur = cur.next;
    }
    
    cur = head;
    while (cur) {
        let copy = oldToCopy.get(cur) ?? null;
        copy.next = oldToCopy.get(cur.next) ?? null;
        copy.random = oldToCopy.get(cur.random) ?? null;
        cur = cur.next;
    }
    
    return oldToCopy.get(head);
};
```

### Add Two numbers

[Add Two Numbers - LeetCode](https://leetcode.com/problems/add-two-numbers/submissions/1257705928/)

```jsx
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let dummyHead = new ListNode(0);
    let current = dummyHead;
    let carry = 0;
    while(l1 || l2){
        const x = l1 ? l1.val : 0;
        const y = l2 ? l2.val : 0;
        const sum = x + y + carry;
        carry = Math.floor(sum/10);
        current.next = new ListNode(sum%10);
        current = current.next;
        if(l1)  l1 = l1.next;
        if(l2) l2 = l2.next;
    }
    // dealing with case if carry is still > 0 ( for last two numbers resulting in a carry )
    if(carry > 0){
        current.next = new ListNode(carry);
    }
    return dummyHead.next;
};
```

### **Linked List Cycle**

[Linked List Cycle - LeetCode](https://leetcode.com/problems/linked-list-cycle/description/)

```jsx
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
    let slow = head;
    let fast = head;
    while(fast && fast.next){
        slow = slow.next;
        fast = fast.next.next;
        if(slow === fast) return true;
    }
    return false;
};
```

### Find the duplicate number

[Find the Duplicate Number - LeetCode](https://leetcode.com/problems/find-the-duplicate-number/description/)

```jsx
/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
    let slow = 0
    let fast = 0
    while(true){
        slow = nums[slow];
        fast = nums[nums[fast]]
        if(slow === fast) break;
    }

    let slow2 = 0;
    while(true){
        slow = nums[slow];
        slow2 = nums[slow2];
        if(slow === slow2) break;
    } 

    return slow;
};
```

[https://www.notion.so](https://www.notion.so)

### LRU Cache

[LRU Cache - LeetCode](https://leetcode.com/problems/lru-cache/description/)

- We are gonna use hashMap for each key and its value where value points to a node containing value , the nodes themselves are Doubly LinkedList point back forth to each other.
- We also have Left Recent Used pointer and MRU pointers as well for keeping record of which are Least Recently used and which are most recently used values.

![Screenshot 2024-05-18 at 3.02.58 PM.png](Screenshot_2024-05-18_at_3.02.58_PM.png)

This picture denoted how we remove middle node from a set of three nodes

![Screenshot 2024-05-18 at 3.35.07 PM.png](Screenshot_2024-05-18_at_3.35.07_PM.png)

Inserting 

![Screenshot 2024-05-18 at 3.37.17 PM.png](Screenshot_2024-05-18_at_3.37.17_PM.png)

Code

```

class Node {
    constructor(key, val) {
        this.key = key;
        this.val = val;
        this.prev = null;
        this.next = null;
    }
}

class LRUCache {
    constructor(capacity) {
        this.cap = capacity;
        this.cache = new Map();

        this.left = new Node(0, 0);
        this.right = new Node(0, 0);
        this.left.next = this.right;
        this.right.prev = this.left;
    }

    // remove node from list
    remove(node) {
        let prev = node.prev;
        let next = node.next;
        prev.next = next;
        next.prev = prev;
    }

    // insert node at right
    insert(node) {
        let prev = this.right.prev;
        let next = this.right;
        prev.next = node;
        node.prev = prev;
        node.next = next;
        next.prev = node;
    }

    get(key) {
        if (this.cache.has(key)) {
            this.remove(this.cache.get(key));
            this.insert(this.cache.get(key));
            return this.cache.get(key).val;
        }
        return -1;
    }

    put(key, value) {
        if (this.cache.has(key)) {
            this.remove(this.cache.get(key));
        }
        let node = new Node(key, value);
        this.cache.set(key, node);
        this.insert(node);

        if (this.cache.size > this.cap) {
            // remove from the list and delete the LRU from map
            let lru = this.left.next;
            this.remove(lru);
            this.cache.delete(lru.key);
        }
    }
}

/** 
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
```

### Merge K Sorted Lists

[NeetCode](https://neetcode.io/problems/merge-k-sorted-linked-lists)

```jsx
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode[]} lists
     * @return {ListNode}
     */
    mergeKLists(lists) {
         if (lists.length === 0) {
            return null;
        }
        while (lists.length > 1) {
            let mergedLists = [];
            for (let i = 0; i < lists.length; i += 2) {
                if (i + 1 < lists.length) {
                    mergedLists.push(this.mergeLists(lists[i], lists[i + 1]));
                } else {
                    mergedLists.push(lists[i]);
                }
            }
            lists = mergedLists;
        }
        return lists[0];
    }
    mergeLists(list1, list2){
        let dummyList = new ListNode(0);
        let tail = dummyList;
        while(list1 && list2){
            if(list1.val < list2.val){
                tail.next = list1;
                list1 = list1.next;
            }else{
                tail.next = list2;
                list2 = list2.next;
            }
            tail = tail.next;
        }
        tail.next = list1 || list2;
        return dummyList.next;
    }
}

```

This was my solution, there is also a better version using merge sort logic.

```jsx
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode[]} lists
     * @return {ListNode}
     */
    mergeKLists(lists) {
        if (!lists || lists.length === 0) {
            return null;
        }

        while (lists.length > 1) {
            const mergedLists = [];
            for (let i = 0; i < lists.length; i += 2) {
                const l1 = lists[i];
                const l2 = (i + 1) < lists.length ? lists[i + 1] : null;
                mergedLists.push(this.mergeList(l1, l2));
            }
            lists = mergedLists;
        }
        return lists[0];
    }

    mergeList(l1, l2) {
        const dummy = new ListNode();
        let tail = dummy;

        while (l1 && l2) {
            if (l1.val < l2.val) {
                tail.next = l1;
                l1 = l1.next;
            } else {
                tail.next = l2;
                l2 = l2.next;
            }
            tail = tail.next;
        }
        if (l1) {
            tail.next = l1;
        }
        if (l2) {
            tail.next = l2;
        }
        return dummy.next;
    }
}

```

### **Reverse Nodes in K-Group**

[NeetCode](https://neetcode.io/problems/reverse-nodes-in-k-group)

```jsx
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @param {number} k
     * @return {ListNode}
     */
    reverseKGroup(head, k) {
        if (head === null || k === 1) return head;

        let dummy = new ListNode(0);
        dummy.next = head;
        let curr = dummy, nex = dummy, pre = dummy;
        let count = 0;

        // Count the number of nodes in the list
        while (curr.next !== null) {
            curr = curr.next;   
            count++;
        }

        // Reverse every k nodes of the linked list
        while (count >= k) {
            curr = pre.next;    // 1
            nex = curr.next;    // 2
            for (let i = 1; i < k; i++) {
                curr.next = nex.next;   // 3
                nex.next = pre.next;    // 2 -> 1
                pre.next = nex; // head -> 2
                nex = curr.next; // 2 
            }
            pre = curr;
            count -= k;
        }

        return dummy.next;
    }
}

```

Another one with a different code logic 

 

```jsx
class ListNode {
    constructor(val = 0, next = null) {
        this.val = val;
        this.next = next;
    }
}

function reverseKGroup(head, k) {
    let dummy = new ListNode(0, head);
    let groupPrev = dummy;

    while (true) {
        let kth = getKth(groupPrev, k);
        if (!kth) break;
        let groupNext = kth.next;

        // Reverse group
        let prev = kth.next;
        let curr = groupPrev.next;
        while (curr !== groupNext) {
            let tmp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = tmp;
        }

        let tmp = groupPrev.next;
        groupPrev.next = kth;
        groupPrev = tmp;
    }

    return dummy.next;
}

function getKth(curr, k) {
    while (curr && k > 0) {
        curr = curr.next;
        k--;
    }
    return curr;
}

// Helper function to create a linked list from an array
function createLinkedList(arr) {
    let dummy = new ListNode();
    let current = dummy;
    for (let val of arr) {
        current.next = new ListNode(val);
        current = current.next;
    }
    return dummy.next;
}
```

## Trees

### Invert Binary Tree

- I used an approach of recursive function to invert Binary Trees and it works.

```jsx
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {TreeNode}
     */
    invertTree(root) {
        this.invert(root);
        return root;
    }

    invert(curr) {
        if (!curr) {
            return false;
        }
        const temp = curr.right;
        curr.right = curr.left;
        curr.left = temp;
        // Invert both subtrees, regardless of their existence
        this.invert(curr.left);
        this.invert(curr.right);
    }
}

```

### Maximum Depth of Binary Tree

Code by me but it wasn’t working becuase of unexpected class initialization 

```jsx
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    constructor(maxDepth=0){
        this.maxDepth = maxDepth;
    }
    maxDepth(root) {;
        this.traverse(root, 0);
        return this.maxDepth;
    }

    traverse(curr, level, depth){
        if(!curr){
            return false;
        }
        level++;
        this.maxDepth = Math.max(level,this.maxDepth);
        if(curr.left){
            return this.traverse(curr.left, level);
        }
        if(curr.right){
            return this.traverse(curr.right, level);
        }
    }
}

```

solution by chat 

```jsx
class Solution {
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    maxDepth(root) {
        return this.traverse(root);
    }

    traverse(curr) {
        if (!curr) {
            return 0;
        }
        let leftDepth = this.traverse(curr.left);
        let rightDepth = this.traverse(curr.right);
        return Math.max(leftDepth, rightDepth) + 1;
    }
}
```

### Diameter of a Binary Tree

Starting from bottom most node is best

![Screenshot 2024-06-06 at 1.11.23 PM.png](Screenshot_2024-06-06_at_1.11.23_PM.png)

- We are marking the height of a null tree as -1 so as to favour our calculations.
    
    ```
    /**
     * Definition for a binary tree node.
     * class TreeNode {
     *     constructor(val = 0, left = null, right = null) {
     *         this.val = val;
     *         this.left = left;
     *         this.right = right;
     *     }
     * }
     */
    
    class Solution {
        /**
         * @param {TreeNode} root
         * @return {number}
         */
        diameterOfBinaryTree(root) {
            const res = [0];
            function dfs(root){
                if(!root){
                    return -1;
                }
                const left = dfs(root.left);
                const right = dfs(root.right);
                res[0] = Math.max(res[0],2+left+right);
                // return height 
                return 1 + Math.max(left,right);
            }
            dfs(root);
            return res[0];
        }
    }
    
    ```
    
- The height of lowest node is 0.
- We start from bottom up and find Diameter ( longest path ).
- Height = `1 + max(left,rigth)` . using max because we want to take value large value at a given node ( to measure height obviously ).
- Diameter is Left Height and Right Height + 2 ( 1 for each node to cancel -1 height  ).

## Balanced Binary Tree

Here is the code for this 

- I am simply using the mere fact that for a given node the left and right subtree height diff should not be greater than 1.

```
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {boolean}
     */
    isBalanced(root) {
        let isBalanced = true;

        function traverse(node) {
            if (!node) {
                return 0;
            }
            const left = traverse(node.left);
            const right = traverse(node.right);
            
            if (Math.abs(left - right) > 1) {
                isBalanced = false;
            }
            
            return Math.max(left, right) + 1;
        }

        traverse(root);
        return isBalanced;
    }
}

```

### Same Tree / Equiavalent Tree

- We use dfs becuase it maintains structure / shape of the tree which is cruicial for checking this specific case.

```jsx
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} p
     * @param {TreeNode} q
     * @return {boolean}
     */
    isSameTree(p, q) {
        return this.compare(p,q);
    }

    compare(a, b) {
        if (a === null && b === null) {
            return true;
        }
        if (a === null || b === null) {
            return false;
        }

        if (a.val !== b.val) {
            return false;
        }

        return this.compare(a.left, b.left) && this.compare(a.right, b.right);
    }
}

```

### **Subtree of a Binary Tree**

The logic goes similar to same tree where we make use of dfs. But here we use the same function only not to compare the whole tree but also the subpart of it as well.

- Dealing with edge cases like if subRoot is null, its surely part of Root.
- if root is null obviously not sub tree.
- if isSameTree returns true even then subRoot can be called as subTree
- Then we check for left side of Root or Right side of tree to see if they might be similar to subTree.

```jsx
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @param {TreeNode} subRoot
     * @return {boolean}
     */
    isSubtree(root, subRoot) {
        if (!subRoot) {
            return true;
        }

        if (!root) {
            return false;
        }
        if (this.sameTree(root, subRoot)) {
            return true;
        }

        return this.isSubtree(root.left, subRoot) || this.isSubtree(root.right, subRoot);
    }

    sameTree(root, subRoot) {
        if (root === null && subRoot === null) {
            return true;
        }
        if (root === null || subRoot === null) {
            return false;
        }

        if (root.val !== subRoot.val) {
            return false;
        }

        return this.sameTree(root.left, subRoot.left) && this.sameTree(root.right, subRoot.right);

    }
}

```

### Lowest Common Ancestor

Lowest node in the tree such that p and q are desendants of this node or p or q can be equal to this node.  

- The point where the split happens is the point where we will find the LCA, why ?
    
    ![Screenshot 2024-06-12 at 11.33.46 AM.png](Screenshot_2024-06-12_at_11.33.46_AM.png)
    
- Like in this case if i have to find LCA for p = 2, i move to left as 2 < 6 ( so left side of tree ). Now can `2` be ancestor of 2 and 8, offcourse not becuase its in a different subtree.
- Similar for 8.
- Thus going deep further is not gonna help us any further. Another example where split happens a bit deeper.
    
    ![Screenshot 2024-06-12 at 11.38.24 AM.png](Screenshot_2024-06-12_at_11.38.24_AM.png)
    
    ```jsx
    /**
     * Definition for a binary tree node.
     * class TreeNode {
     *     constructor(val = 0, left = null, right = null) {
     *         this.val = val;
     *         this.left = left;
     *         this.right = right;
     *     }
     * }
     */
    
    class Solution {
        /**
         * @param {TreeNode} root
         * @param {TreeNode} p
         * @param {TreeNode} q
         * @return {TreeNode}
         */
        lowestCommonAncestor(root, p, q) {
            let curr = root;
            while (curr) {
                if (p.val > curr.val && q.val > curr.val) {
                    curr = curr.right;
                } else if (p.val < curr.val && q.val < curr.val) {
                    curr = curr.left;
                } else {
                    return curr;
                }
            }
        }
    }
    
    ```
    

### Binary Tree Level Order Traversal

This was BFS kind of question with only a slight change to BFS , usually we just move over and print values.

- Here we for each level make sure to loop over all values of same level and push them to nested array. Only then we move ahead to another level.

```jsx
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number[][]}
     */
    levelOrder(root) {
        const result = [];
        const q = [root];
        while (q.length) {
            const level = [];
            const qLen = q.length;
            for (let i = 0; i < qLen; ++i) {
                const node = q.shift();
                if (node) {
                    level.push(node.val);
                    q.push(node.left);
                    q.push(node.right);
                }
            }
            if (level.length) {
                result.push(level);
            }

        }
        return result;

    }

}

```

### Binary Tree Right Side View

A simple way is to push the last value at same level for Level Order Traversal ( Breadth First Traversal )

```jsx
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number[]}
     */
    rightSideView(root) {
        const result = [];
        const q = [root];
        while(q.length){
            const qLen = q.length;
            let rightSide = null;
            for(let i = 0; i < qLen ; ++i){
                const node = q.shift();
                if(node){
                    rightSide = node;
                    q.push(node.left);
                    q.push(node.right);
                }
            }
            if(rightSide){
                result.push(rightSide.val)
            }
        }
        return result;
    }
}

```

### Count Good notes in Binary Tree

[Count Good Nodes in Binary Tree - LeetCode](https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/)

- We follow an approach of DFS simply.
- Depth first serach goes deeper, meaning we can identify a path. This way if we just keep track of current max in given path, we can tell if given node is max or not.

```jsx
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var goodNodes = function(root) {
    const head = root;
    let count = 0;
    var dfs = function(head,maxVal){
        if(!head){
            return true;
        }
        if(head.val >= maxVal){
            count++;
        }
        maxVal = Math.max(maxVal, head.val);
        const left = dfs(head.left, maxVal);
        const right = dfs(head.right,maxVal);
    }
    dfs(root,root.val);
    return count;
};

```

### Validate Binary Search Tree

- To validate a bianry tree we have to make sure every node left subtree is smaller than current node value and vise versa for right left subtree.
- In this regard we start with -Infinity and Infinity and first node is checked for these two values.
- Then for left we pass node as node.left, left remians same as it should be greater than -Infinity while right becomes node.val to make sure left subtree is always smaller than parent node.
- Similar for right subtree with left replaced with parent and right remains same ( Infinity ).

```jsx
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function (root) {
    const valid = (node, left, right) => {
        if (!node) {
            return true;
        }
        if (!(node.val < right && node.val > left)) {
            return false;
        }

        return valid(node.left, left, node.val) && valid(node.right, node.val, right);
    }
    return valid(root, -Infinity, Infinity);
};
```

### Kth Smallest element in BST

[Kth Smallest Element in a BST - LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/)

The first solution is simply the in-order traversal

```jsx
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function(root, k) {
    const path = [];
    const walk = (node, path) => {
        if(!node){
            return path;
        }

        // pre
        walk(node.left,path)
        // recurse
        path.push(node.val);
        // post
        walk(node.right,path);
    }
    walk(root,path);
    return path[k-1];
};
```

this one slightly optimised to stop when we find result 

```
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function(root, k) {
    let count = 0;
    let result = null;
    const walk = (node) => {
        if(node === null || result !== null ){
            return;
        }

        // pre
        // recurse
        walk(node.left)
        count++;
        if (count === k) {
            result = node.val;
            return;
        }
        walk(node.right);
        // post
    }
    walk(root);
    return result;
};
```

### **Construct Binary Tree from Pre-Order and In-Order Traversal**

[Construct Binary Tree from Preorder and Inorder Traversal - LeetCode](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/)

- We are given with In-Order and Pre-Order traversals
- Where we can identify root from Pre-Order traversal as its always the first node.
- We take `root` and find its index inside In-Order array. The In-Order array shows that everything on left side of `root` is gonna go left side of tree while everything on right of `root`
- Then we mark an index as separation line pre-order showing that its the point where left and right subtree diverge. We also mark 20 as `mid` so that we know its point where left and right values are respectively left and right child nodes of `mid`
    
    [https://www.notion.so](https://www.notion.so)
    
    ```jsx
    /**
     * Definition for a binary tree node.
     * function TreeNode(val, left, right) {
     *     this.val = (val===undefined ? 0 : val)
     *     this.left = (left===undefined ? null : left)
     *     this.right = (right===undefined ? null : right)
     * }
     */
    /**
     * @param {number[]} preorder
     * @param {number[]} inorder
     * @return {TreeNode}
     */
    var buildTree = function (preorder, inorder) {
        if (!preorder.length || !inorder.length) {
            return null;
        }
    
        const root = new TreeNode(preorder[0]);
        const mid = inorder.indexOf(preorder[0]);
    
        root.left = buildTree(preorder.slice(1, mid + 1), inorder.slice(0, mid));
        root.right = buildTree(preorder.slice(mid + 1), inorder.slice(mid + 1));
    
        return root;
    }
    
    ```
    

### **Binary Tree Maximum Path Sum**

[Binary Tree Maximum Path Sum - LeetCode](https://leetcode.com/problems/binary-tree-maximum-path-sum/description/)

- Once a split happens it will never happen again, because otherwise it wont be again a path.
    
    ![Screenshot 2024-07-04 at 11.35.11 AM.png](Screenshot_2024-07-04_at_11.35.11_AM.png)
    
- Once a split happens we can no longer access its parents then for a path.
- We will go from bottom to top so at the base case we will do 2 things
    - Assume the path can be split, then get max Value we can get here like at 3 what is max we can get if we go right / left. 3+4 = 7 or 3+5 = 8
    - Assume it cannot be split and get sum of all nodes, this is what our Response value would be ( the max value we can get ).
    
    ![Screenshot 2024-07-04 at 11.48.38 AM.png](Screenshot_2024-07-04_at_11.48.38_AM.png)
    
- We can also chose to ignore all the childs if they are negative values.
    
    [https://www.notion.so](https://www.notion.so)
    
    ```jsx
    /**
     * Definition for a binary tree node.
     * function TreeNode(val, left, right) {
     *     this.val = (val===undefined ? 0 : val)
     *     this.left = (left===undefined ? null : left)
     *     this.right = (right===undefined ? null : right)
     * }
     */
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    var maxPathSum = function (root) {
        let res = [root.val];
        const dfs = (node) => {
            if (!node) {
                return 0;
            }
            let leftMax = dfs(node.left);
            let rightMax = dfs(node.right);
            leftMax = Math.max(leftMax, 0);
            rightMax = Math.max(rightMax, 0);
            // compute max path sum WITH split
            res[0] = Math.max(res[0], node.val + leftMax + rightMax);
            return node.val + Math.max(leftMax,rightMax);
        }
    
        dfs(root);
        return res[0];
    };
    ```
    

# JAVASCRIPT Problems

## Implement a mapLimit async function

```jsx
Array.prototype.chop = function (size) {
  const temp = [...this];
  // if the size is not defined
  if (!size) {
    return temp;
  }

  // output
  const output = [];
  let i = 0;

  // iterate the array
  while (i < temp.length) {
    //slice the sub-array of a given size
    //and push them in output array
    output.push(temp.slice(i, i + size));
    i = i + size;
  }

  return output;
};

const mapLimit = (arr, limit, fn) => {
  // return a new promise
  return new Promise((resolve, reject) => {
    // chop the input array into subarrays
    let chopped = arr.chop(limit);
    // all the sub-arrays of arr are run in series
    const final = chopped.reduce((accumulator, currentValue) => {
      return accumulator.then((val) => {
        // all the values of each sub-array will run in parallel
        return new Promise((resolve, reject) => {
          const results = [];
          let tasksCompleted = 0;
          currentValue.forEach((e) => {
            fn(e, (error, value) => {
              if (error) {
                reject(error);
              } else {
                results.push(value);
                tasksCompleted++;
                if (tasksCompleted >= currentValue.length) {
                  resolve([...val, ...results]);
                }
              }
            });
          });
        });
      });
    }, Promise.resolve([]));
    // based on final promise state
    // invoke the final promise.
    final
      .then((result) => {
        resolve(result);
      })
      .catch((e) => {
        reject(e);
      });
  });
};

let numPromise = mapLimit([1, 2, 3, 4, 5], 3, function (num, callback) {
  setTimeout(function () {
    num = num * 2;
    console.log(num);
    callback(null, num);
  }, 2000);
});

// let numPromise = mapLimit([1, 2, 3, 4, 5], 3, function (num, callback) {
//   setTimeout(function () {
//     num = num * 2;
//     console.log(num);

//     // throw error
//     if (num === 6) {
//       callback(true); // takes two arguments ( error, value )
//     } else {
//       callback(null, num);
//     }
//   }, 2000);
// });

numPromise
  .then((result) => console.log('success:' + result))
  .catch(() => console.log('no success'));
```

### Basics of Promises

A Promise in JavaScript represents a value that may be available now, or in the future, or never. Promises are used for handling asynchronous operations. A Promise has three states:

1. **Pending**: The initial state, neither fulfilled nor rejected.
2. **Fulfilled**: The operation completed successfully.
3. **Rejected**: The operation failed.

A Promise is created using the `new Promise` constructor, which takes a function as an argument. This function has two parameters, `resolve` and `reject`:

- **`resolve(value)`**: Marks the promise as fulfilled and provides the value.
- **`reject(reason)`**: Marks the promise as rejected and provides the reason for the rejection.

### Simple Example of a Promise

Here’s a simple example to illustrate how Promises work:

```jsx
javascriptCopy code
const myPromise = new Promise((resolve, reject) => {
  const success = true; // Change this to false to see the rejection case.

  setTimeout(() => {
    if (success) {
      resolve('Operation succeeded!');
    } else {
      reject('Operation failed.');
    }
  }, 1000);
});

myPromise
  .then((result) => {
    console.log(result); // Logs: 'Operation succeeded!'
  })
  .catch((error) => {
    console.error(error); // If success was false, logs: 'Operation failed.'
  });

```

### Breakdown

1. **Promise Creation**:
    - `new Promise((resolve, reject) => { ... })`: Defines an asynchronous operation.
    - Inside the function, after 1 second (`setTimeout`), either `resolve` or `reject` is called based on the `success` variable.
2. **Handling the Promise**:
    - `.then((result) => { ... })`: Handles the fulfilled state. The `result` parameter gets the value passed to `resolve`.
    - `.catch((error) => { ... })`: Handles the rejected state. The `error` parameter gets the reason passed to `reject`.

### Detailed Explanation of mapLimit

Now, let’s explain the `mapLimit` function with a focus on how Promises are used.

1. **Function Definition**:
    
    ```jsx
    javascriptCopy code
    const mapLimit = (arr, limit, fn) => {
      return new Promise((resolve, reject) => {
        let chopped = arr.chop(limit);
        const final = chopped.reduce((accumulator, currentValue) => {
          return accumulator.then((val) => {
            return new Promise((resolve, reject) => {
              const results = [];
              let tasksCompleted = 0;
              currentValue.forEach((e) => {
                fn(e, (error, value) => {
                  if (error) {
                    reject(error);
                  } else {
                    results.push(value);
                    tasksCompleted++;
                    if (tasksCompleted >= currentValue.length) {
                      resolve([...val, ...results]);
                    }
                  }
                });
              });
            });
          });
        }, Promise.resolve([]));
        final
          .then((result) => {
            resolve(result);
          })
          .catch((e) => {
            reject(e);
          });
      });
    };
    
    ```
    
2. **Chopping the Array**:
    - `let chopped = arr.chop(limit);`: Splits the array into sub-arrays of `limit` size.
3. **Processing Sub-Arrays in Series**:
    - `chopped.reduce((accumulator, currentValue) => { ... }, Promise.resolve([]))`: Uses `reduce` to process each sub-array in series.
    - `accumulator` is a Promise that ensures each chunk waits for the previous chunk to complete.
4. **Processing Elements in Parallel**:
    - `currentValue.forEach((e) => { ... })`: Processes elements of the current sub-array in parallel.
    - `fn(e, (error, value) => { ... })`: Applies the provided function `fn` to each element.
5. **Promise Chain**:
    - `accumulator.then((val) => { ... })`: Ensures the next sub-array processing starts only after the previous sub-array is processed.
    - `Promise.resolve([])`: Initial value for the accumulator, representing the initial fulfilled state with an empty array.
6. **Handling Results**:
    - `results.push(value);`: Collects results.
    - `if (tasksCompleted >= currentValue.length) { resolve([...val, ...results]); }`: Resolves the Promise for the current sub-array when all elements are processed.
    - `return accumulator.then((val) => { ... });`: Chains Promises so that each sub-array waits for the previous one.
7. **Final Resolution**:
    - `final.then((result) => { resolve(result); }).catch((e) => { reject(e); });`: Resolves or rejects the outer Promise based on the final Promise state.

### Simpler Example Using mapLimit

Let’s apply `mapLimit` with a simpler function:

```jsx
javascriptCopy code
const asyncDouble = (num, callback) => {
  setTimeout(() => {
    callback(null, num * 2);
  }, 100);
};

const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

mapLimit(numbers, 3, asyncDouble)
  .then((result) => {
    console.log('Results:', result); // Results: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
  })
  .catch((error) => {
    console.error('Error:', error);
  });

```

### Explanation

1. **Chopping**:
    - The array `[1, 2, 3, ..., 10]` is chopped into sub-arrays of size 3: `[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]`.
2. **Processing Sub-Arrays**:
    - The first sub-array `[1, 2, 3]` is processed in parallel using `asyncDouble`.
    - Once all elements of the first sub-array are processed, the next sub-array `[4, 5, 6]` is processed, and so on.
3. **Promise Chain**:
    - Each sub-array processing returns a Promise that resolves with the processed results.
    - The `reduce` method ensures sub-arrays are processed in series, while elements within each sub-array are processed in parallel.

## Implement a function which runs all async tasks in parallel

```jsx
function asyncParallel(tasks, callback) {
  // store the results
  const results = [];

  // track the task executed
  let tasksCompleted = 0;

  // run each task
  tasks.forEach((asyncTask) => {
    // invoke the async task
    asyncTask((value) => {
      // store the output of the task
      results.push(value);

      // increment the tracker
      tasksCompleted++;
      if (tasksCompleted >= tasks.length) {
        callback(results);
      }
    });
  });
}

function createAsyncTask() {
  const value = Math.floor(Math.random() * 10);
  return function (callback) {
    setTimeout(() => {
      callback(value);
    }, value * 1000);
  };
}

const taskList = [
  createAsyncTask(),
  createAsyncTask(),
  createAsyncTask(),
  createAsyncTask(),
  createAsyncTask(),
  createAsyncTask(),
];

asyncParallel(taskList, (result) => {
  console.log('results', result);
});
```

### Function Explanation

1. **Function Signature**:
    - `asyncParallel(tasks, callback)`: This function takes two arguments:
        - `tasks`: An array of asynchronous tasks (functions that accept a callback and invoke it after some time).
        - `callback`: A function to be called once all tasks have completed, with the results of those tasks.
2. **Variables**:
    - `results`: An array to store the results of each task.
    - `tasksCompleted`: A counter to keep track of how many tasks have completed.
3. **Running the Tasks**:
    - The `tasks` array is iterated over using `forEach`.
    - Each `asyncTask` is invoked, passing a callback function.
4. **Handling Task Completion**:
    - Inside the callback function of each `asyncTask`:
        - The result of the task is pushed into the `results` array.
        - `tasksCompleted` is incremented.
        - If `tasksCompleted` is equal to the number of tasks, the `callback` function is called with the `results` array.

### Example Explanation

1. **Creating Asynchronous Tasks**:
    - `createAsyncTask()` returns an asynchronous task which calls its callback with a random number after a delay proportional to that number (e.g., if the random number is 3, the delay will be 3 seconds).
2. **Task List**:
    - An array of six asynchronous tasks is created using `createAsyncTask()`.
3. **Running the Parallel Execution**:
    - `asyncParallel(taskList, (result) => { console.log('results', result); });` is called.
    - This runs all six tasks in parallel, and once all tasks are complete, the results are logged.

### Example Run

Here's an example run:

1. Six tasks are created, each with a random delay.
2. The delays could be, for instance, 1, 6, 7, 7, 9, and 9 seconds.
3. Each task runs in parallel and completes after its respective delay.
4. Once all tasks complete, the results are logged.

### Key Points

- **Parallel Execution**: Tasks run in parallel because each `asyncTask` is immediately invoked without waiting for the others to complete.
- **Callback Invocation**: The main `callback` is only called once all tasks have completed.
- **Asynchronous Nature**: The delays are achieved using `setTimeout`, which simulates asynchronous behavior.

### Using Promise

```jsx
function asyncParallel(tasks, callback) {
  // store the result
  const results = [];

  const errors = [];

  // track the task executed
  let tasksCompleted = 0;

  // run each task
  tasks.forEach((asyncTask) => {
    // invoke the async task
    // it can be a promise as well
    // for a promise you can chain it with then
    asyncTask
      .then((value) => {
        // store the output of the task
        results.push(value);
      })
      .catch((error) => {
        errors.push(error);
      })
      .finally(() => {
        // increment the tracker
        tasksCompleted++;

        // if all tasks are executed
        // invoke the callback
        if (tasksCompleted >= tasks.length) {
          callback(errors, results);
        }
      });
  });
}

function createAsyncTask() {
  const value = Math.floor(Math.random() * 10);
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (value < 5) {
        reject(`Error ${value}`);
      } else {
        resolve(value * 1000);
      }
    }, value * 1000);
  });
}

const taskList = [
  createAsyncTask(),
  createAsyncTask(),
  createAsyncTask(),
  createAsyncTask(),
  createAsyncTask(),
];

asyncParallel(taskList, (error, result) => {
  console.log('errors', error);
  console.log('results', result);
});

//errors (4) ["Error 0", "Error 1", "Error 1", "Error 2"]
//results (2) [5000, 9000]

'results'[(1, 6, 7, 7, 9, 9)]; // [object Array] (6)

```

[Kubernetes path](Kubernetes%20path%20ce7a68365a764555b24021ec7a6a7469.md)

## HTML encoding of a string

 

```
function Stack() {
  let items = [];
  let index = 0;
  this.push = function (val) {
    return (items[index++] = val); // first store value a given index and then increment it
    // value at index 0 while index = 1
  };
  this.pop = function () {
    return items[--index]; // first decrement index ( as current value is at index - 1 ), value at index 0 while index before decremen is 1
  };
  this.peek = function () {
    return items[index - 1];
  };
}

function Tag(start, end, tag) {
  this.start = start;
  this.end = end;
  this.tag = tag;
  this.text = '';

  this.getRange = () => {
    return this.end - this.start;
  };
}

function addAndSort(track, index, tag) {
  if (!track[index]) track[index] = [];
  track[index] = [...track[index], tag];
  track[index].sort((a, b) => a.getRange() - b.getRange());
}

function parse(str, markups) {
  // create an empty array for all the indexes of the string
  const track = new Array(str.length).fill(null);

  // add the tag at the starting point
  // of each text mentined in the markups
  for (let markup of markups) {
    const [start, end, tag] = markup;
    // since i and u both start at 0, we will first apply the tag which has greater range and then the smaller one this is what sorting is for
    addAndSort(track, start, new Tag(start, end, tag));
  }

  // create a new stack
  const html = new Stack();

  // initilize with a new Tag that has max range and empty string
  html.push(new Tag(0, Number.MAX_VALUE, ''));

  // iterate each character of the string
  for (let i = 0; i < str.length; i++) {
    // check for opening tags and add them
    while (track[i] && track[i].length > 0) {
      const cur = track[i].shift();
      // for first time its always false as first number pushed is infinity
      // in current loop it the stack top would contain large range tag like 0,3,'u', this check makes sure that both i and u close at index 2 and then u opens again closes at 3 for single character it has left.
      cur.text = `<${cur.tag}>`;

      // for example in [0, 2, 'i'] , [1, 3, 'b']
      // b is starting from 1 and ending at 3, i is inbetween b.
      // <i> <b> </b> </i> <b> </b>
      // if the end of the nested tag is larger than the parent, split the tag
      // and insert the remaining split to the bucket after its parent
      if (cur.end > html.peek().end) {
        const split = new Tag(html.peek().end + 1, cur.end, cur.tag);
        cur.end = html.peek().end;
        addAndSort(track, html.peek().end + 1, split);
      }

      // push the new tag
      html.push(cur);
    }

    // add the current character to the currently topmost tag
    html.peek().text += str[i];

    // heck for closing tags and close them.
    while (html.peek().end === i) {
      html.peek().text += `</${html.peek().tag}>`;
      const temp = html.pop().text;
      html.peek().text += temp;
    }
  }

  // return the topmost
  return html.pop().text;
}
const encoded = parse('Hello, World', [
  [0, 2, 'i'],
  [7, 10, 'u'],
  [4, 9, 'b'],
  [2, 7, 'i'],
  [7, 9, 'u'],
]);

console.log(encoded);

('<i>He<i>l</i></i><i>l<b>o, <u><u>W</u></u></b></i><b><u><u>or</u></u></b><u>l</u>d');
('Hello, World');
```

## **Implement an in-memory search engine**

```jsx
// having a constructor function to create unique instances
function InMemorySearch() {
  this.entities = new Map(); // in-built for key-value pair
  // best for quick retreival
  // rest operator ... for getting all arguments after namespace
  this.addDocuments = function (namepSpace, ...documents) {
    const exisiting = this.entities.get(namepSpace);
    if (exisiting) {
      this.entities.set(namepSpace, [...exisiting, ...documents]);
    } else {
      this.entities.set(namepSpace, [...documents]);
    }
  };

  this.search = function (nameSpace, filterFn, orderBy) {
    const documents = this.entities.get(nameSpace);
    const filtered = documents.filter(filterFn);
    if (orderBy) {
      const { key, asc } = orderBy;
      return filtered.sort((a, b) => {
        if (asc) {
          return a[key] - b[key]; // if value is +ve then sort in asc otherwise desc
        } else {
          return b[key] - a[key]; // if positive then asc / -ve desc
        }
      });
    }
    return filtered;
  };
}

const searchEngine = new InMemorySearch();
searchEngine.addDocuments(
  'Movies',
  { name: 'Avenger', rating: 8.5, year: 2017 },
  { name: 'Black Adam', rating: 8.7, year: 2022 },
  { name: 'Jhon Wick 4', rating: 8.2, year: 2023 },
  { name: 'Black Panther', rating: 9.0, year: 2022 }
);
console.log(
  searchEngine.search('Movies', (e) => e.rating > 8.5, {
    key: 'rating',
    asc: false,
  })
);

/*
[
  {
    "name": "Black Panther",
    "rating": 9,
    "year": 2022
  },
  {
    "name": "Black Adam",
    "rating": 8.7,
    "year": 2022
  }
]
*/

```

## Implement Highlight Keywords Text

- Highlight the provided text in words array
- If parts of same word are in words array, the whoe word should be highlighted.

```jsx
const highlight = (str, keywords) => {
  // find unique keywords from list of keywords, means ignore duplicate
  const uniqueKeywords = new Set(keywords); // the best way i think
  // Extract all words from our gievn string
  const words = str.split(' ');
  const result = words.map((word) => {
    let output = '';
    // cases where wole word might be there in unique words
    if (uniqueKeywords.has(word)) {
      output = `<strong>${word}</strong>`;
    } else {
      // handle sub-words like End, Front which combines to become FrontEnd
      for (let i = 0; i < word.length; ++i) {
        const prefix = word.slice(0, i + 1); // prefix is upto current index
        const suffix = word.slice(i + 1); // remaining
        if (uniqueKeywords.has(prefix) && uniqueKeywords.has(suffix)) {
          output = `<strong>${prefix + suffix}</strong>`;
        } else if (uniqueKeywords.has(prefix) && !uniqueKeywords.has(suffix)) {
          output = `<strong>${prefix}</strong>${suffix}`;
        } else if (uniqueKeywords.has(suffix) && !uniqueKeywords.has(prefix)) {
          output = `<strong>${suffix}</strong>${prefix}`;
        }
      }
    }
    return output !== '' ? output : word;
  });
  return result.join(' ');
};

console.log(highlight(text, keywords));
appDiv.innerHTML = highlight(text, keywords);

```

- There can also be a requirement to make it case insensitive.

```jsx
const text = document.querySelector('p').innerHTML;
const keywords = ['Front', 'End', 'Javascript'];

const highlight = (str, keywords, caseInsensitive = false) => {
  if (caseInsensitive) {
    keywords = keywords.map((word) => {
      word.toLowerCase();
    });
  }
  // find unique keywords from list of keywords, means ignore duplicate
  const uniqueKeywords = new Set(keywords); // the best way i think
  // Extract all words from our gievn string
  const words = str.split(' ');

  // a fucntion to check if result has given words to be highlighted
  const hasWord = (word) => {
    word = caseInsensitive ? word.toLowerCase() : word;
    return uniqueKeywords.has(word);
  };

  const result = words.map((word) => {
    let output = '';
    // cases where wole word might be there in unique words
    if (hasWord(word)) {
      output = `<strong>${word}</strong>`;
    } else {
      // handle sub-words like End, Front which combines to become FrontEnd
      for (let i = 0; i < word.length; ++i) {
        const prefix = word.slice(0, i + 1); // prefix is upto current index
        const suffix = word.slice(i + 1); // remaining
        if (hasWord(prefix) && hasWord(suffix)) {
          output = `<strong>${prefix + suffix}</strong>`;
        } else if (hasWord(prefix) && !hasWord(suffix)) {
          output = `<strong>${prefix}</strong>${suffix}`;
        } else if (hasWord(suffix) && !hasWord(prefix)) {
          output = `<strong>${suffix}</strong>${prefix}`;
        }
      }
    }
    return output !== '' ? output : word;
  });
  return result.join(' ');
};

console.log(highlight(text, keywords));
appDiv.innerHTML = highlight(text, keywords);

```

## Implement Throttling Functions

- Restrict certain actions for certain time / count.Ï
- It has three different variations
    - Time throttling itself has two types leading and trailing.
        - Leading where first one execute immediately and subsequent after given time.
        
        ![Screenshot 2024-07-28 at 11.47.18 AM.png](Screenshot_2024-07-28_at_11.47.18_AM.png)
        
        - The trailing one has first one executes after time interval and same afterwards.
    
    ### Cont Based
    
    ```jsx
    const appDiv = document.getElementById('app');
    
    // Count based
    // invoke given function once for given count
    function throttle(fn, count) {
      let counter = 0;
      return function (...args) {
        // since we have to invoke only once for given count, we start from zero and go til count which if does not matches we return simply otherwise we return fucntion and reset counter
        if (++counter !== count) return;
        counter = 0;
        // set context for gievn callback fucntion
        fn.apply(this,args);
      };
    }
    const onClick = () => {
      console.log('clicked');
    };
    const throttleClick = throttle(onClick, 4);
    const button = document
      .querySelector('button')
      .addEventListener('click', throttleClick);
    
    ```
    
- This works fine and executes only the fourth time since count is.

### Delay Based

```jsx
function throttle(fn, delay) {
  // track the time when fucntion was last invoked and which was last function
  let lastTimerId; // timerId of last function executed
  let lastRan; //time when last function was executed

  return function (...args) {
    const context = this;
    if (!lastRan) {
      fn.apply(context, args);
      lastRan = Date.now();
    } else {
      clearTimeout(lastTimerId);
      lastTimerId = setTimeout(() => {
        if (Date.now() - lastRan >= delay) {
          fn.apply(context, args);
          lastRan = Date.now();
        }
      }, delay - (Date.now() - lastRan)); // remaining time after which the next time callback should be executed
    }
  };
}
```

### Trailing and Leading Both

```jsx
function throttle(fn, delay, option = { leading: false, trailing: true }) {
  let lastTimerID;
  let lastArgs;
  return function (...args) {
    const { leading, trailing } = option;
    // contains logic for all calls to functions
    const waitFn = () => {
      // trailing happens after the delay and all consecutive calls after the leading will be considered as trailing only as they happen after delay
      if (trailing && lastArgs) {
        // becaue of arrow fucntion we can direclty use the this keyword ( context of parent fucntion ) otherwsie in case of normal fucntion we should store it and then use that variable.
        fn.apply(this, lastArgs);
        lastArgs = null;
        lastTimerID = setTimeout(waitFn, delay);
      } else {
        lastTimerID = null;
      }
    };

    if (!lastTimerID && leading) {
      fn.apply(this, args);
    } else {
      lastArgs = args;
    }

    if (!lastTimerID) {
      lastTimerID = setTimeout(waitFn, delay);
    }
  };
}

const onClick = () => {
  console.log('clicked');
};
const throttleClick = throttle(onClick, 2000, {
  leading: true,
  trailing: true,
});
const button = document
  .querySelector('button')
  .addEventListener('click', throttleClick);

```

- Explanation
    
    ### Step-by-Step Execution
    
    Given:
    
    ```jsx
    javascriptCopy code
    const throttledFunc = throttle(myFunction, 1000, { leading: true, trailing: true });
    
    ```
    
    ### Initial State
    
    - `lastTimerID` is `undefined`
    - `lastArgs` is `undefined`
    
    ### First Call (Time = 0ms)
    
    ```jsx
    javascriptCopy code
    throttledFunc(1);
    
    ```
    
    1. **Arguments**: `args` is `[1]`.
    2. **Leading**:
        - `lastTimerID` is `undefined` and `leading` is `true`.
        - `myFunction(1)` is called immediately.
    3. **Store Arguments**: `lastArgs` is set to `[1]`.
    4. **Set Timeout**:
        - Since `lastTimerID` is `undefined`, `lastTimerID` is set with a timeout to call `waitFn` after 1000ms.
    
    ### During Delay (Time < 1000ms)
    
    If another call happens before the delay completes:
    
    ```jsx
    javascriptCopy code
    throttledFunc(2);
    
    ```
    
    1. **Arguments**: `args` is `[2]`.
    2. **Leading**:
        - `lastTimerID` is not `undefined` (timeout is still active), so the leading condition does not trigger.
    3. **Store Arguments**: `lastArgs` is updated to `[2]`.
    
    ### Timeout Triggered (Time = 1000ms)
    
    When the timeout completes:
    
    1. **Trailing**:
        - `trailing` is `true` and `lastArgs` is `[2]`.
        - `myFunction(2)` is called with the last stored arguments.
    2. **Reset**:
        - `lastArgs` is set to `null`.
        - `lastTimerID` is reset, and a new timeout is set with `waitFn` to handle any trailing calls.
    
    ### After First Timeout (Time > 1000ms)
    
    If another call happens after the first timeout completes:
    
    ```jsx
    javascriptCopy code
    throttledFunc(3);
    
    ```
    
    1. **Arguments**: `args` is `[3]`.
    2. **Leading**:
        - `lastTimerID` is `undefined` and `leading` is `true`.
        - `myFunction(3)` is called immediately.
    3. **Store Arguments**: `lastArgs` is set to `[3]`.
    4. **Set Timeout**:
        - Since `lastTimerID` is `undefined`, `lastTimerID` is set with a timeout to call `waitFn` after 1000ms.
    
    ### Summary
    
    - **Leading**: The function is called immediately on the first call within any delay period.
    - **Trailing**: The function is called at the end of the delay period with the last set of arguments if there were calls during the delay.
    
    This behavior ensures that:
    
    - The function executes immediately at the beginning (leading).
    - The function executes at the end of the delay if there were subsequent calls (trailing).
    
    ### Example in Action
    
    Let's consider a real timeline example with the throttle function set to 1000ms:
    
    - **Time = 0ms**: `throttledFunc(1)` is called.
        - `myFunction(1)` is called immediately (leading).
        - `lastArgs` is set to `[1]`.
        - Timeout is set for 1000ms.
    - **Time = 500ms**: `throttledFunc(2)` is called.
        - `lastArgs` is updated to `[2]`.
    - **Time = 1000ms**: Timeout completes.
        - `myFunction(2)` is called (trailing with last args).
    - **Time = 1500ms**: `throttledFunc(3)` is called.
        - `myFunction(3)` is called immediately (leading).
        - `lastArgs` is set to `[3]`.
        - Timeout is set for 1000ms.
    - **Time = 2000ms**: Timeout completes.
        - `myFunction(3)` is called again (trailing with last args).
    
    4o
    
    now one where leading is false and trailing is true
    
    ChatGPT
    
    Certainly! Let’s go through a step-by-step explanation of how the `throttle` function behaves when `leading` is set to `false` and `trailing` is set to `true`.
    
    ### Given
    
    ```jsx
    javascriptCopy code
    const throttledFunc = throttle(myFunction, 1000, { leading: false, trailing: true });
    
    ```
    
    ### Step-by-Step Execution
    
    ### Initial State
    
    - `lastTimerID` is `undefined`.
    - `lastArgs` is `undefined`.
    
    ### First Call (Time = 0ms)
    
    ```jsx
    javascriptCopy code
    throttledFunc(1);
    
    ```
    
    1. **Arguments**: `args` is `[1]`.
    2. **Leading**:
        - `lastTimerID` is `undefined`, so `leading` is `false`.
        - `myFunction` is **not** called immediately.
    3. **Store Arguments**: `lastArgs` is set to `[1]`.
    4. **Set Timeout**:
        - Since `lastTimerID` is `undefined`, a timeout is set to call `waitFn` after 1000ms.
    
    ### During Delay (Time < 1000ms)
    
    If another call happens before the delay completes:
    
    ```jsx
    javascriptCopy code
    throttledFunc(2);
    
    ```
    
    1. **Arguments**: `args` is `[2]`.
    2. **Leading**:
        - `lastTimerID` is not `undefined` (timeout is active), so `leading` is still `false`.
        - `myFunction` is **not** called immediately.
    3. **Store Arguments**: `lastArgs` is updated to `[2]`.
    
    ### Timeout Triggered (Time = 1000ms)
    
    When the timeout completes:
    
    1. **Trailing**:
        - `trailing` is `true` and `lastArgs` is `[2]`.
        - `myFunction(2)` is called with the last stored arguments.
    2. **Reset**:
        - `lastArgs` is set to `null`.
        - `lastTimerID` is reset, and a new timeout is set with `waitFn` to handle any trailing calls.
    
    ### After First Timeout (Time > 1000ms)
    
    If another call happens after the first timeout completes:
    
    ```jsx
    javascriptCopy code
    throttledFunc(3);
    
    ```
    
    1. **Arguments**: `args` is `[3]`.
    2. **Leading**:
        - `lastTimerID` is `undefined` and `leading` is `false`.
        - `myFunction` is **not** called immediately.
    3. **Store Arguments**: `lastArgs` is set to `[3]`.
    4. **Set Timeout**:
        - Since `lastTimerID` is `undefined`, `lastTimerID` is set with a timeout to call `waitFn` after 1000ms.
    
    ### Summary
    
    - **Leading**: The function is not called immediately on the first call within any delay period.
    - **Trailing**: The function is called at the end of the delay period with the last set of arguments if there were calls during the delay.
    
    ### Example in Action
    
    With the throttle function set to 1000ms:
    
    - **Time = 0ms**: `throttledFunc(1)` is called.
        - `lastArgs` is set to `[1]`.
        - Timeout is set for 1000ms.
    - **Time = 500ms**: `throttledFunc(2)` is called.
        - `lastArgs` is updated to `[2]`.
    - **Time = 1000ms**: Timeout completes.
        - `myFunction(2)` is called (trailing with last args).
        - `lastArgs` is reset to `null`.
        - Timeout is set for 1000ms.
    - **Time = 1500ms**: `throttledFunc(3)` is called.
        - `lastArgs` is set to `[3]`.
        - Timeout is set for 1000ms.
    - **Time = 2000ms**: Timeout completes.
        - `myFunction(3)` is called (trailing with last args).

## Throttle and array of tasks

- Make a throttle so that n number of tasks are executed where n is given as argument to us.

![Screenshot 2024-07-31 at 9.47.48 AM.png](Screenshot_2024-07-31_at_9.47.48_AM.png)

```jsx
const throttle = (array, limit, callback, delay) => {
  let timerId;
  let lastRan;
  // push all item except limit into queue
  let queue = [...array];
  return function () {
    if (!lastRan) {
      // retreieve number of elements === limit from queue
      const elements = queue.splice(0, limit);
      // pass them to callback
      callback(elements);
      //  initialize lastRan so that we can later know when was first function run
      lastRan = Date.now();
    } else {
      // if function is invoked before time clear timerId
      clearTimeout(timerId);
      timerId = setTimeout(() => {
        if (Date.now() - lastRan >= delay) {
          const elements = queue.splice(0, limit);
          callback(elements);
          lastRan = Date.now();
        }
      }, (delay = Date.now() - lastRan)); // it actually deontes the timeleft to execute the function
    }
  };
};
const throttleClick = throttle(
  [1, 2, 3, 4, 5, 6, 7, 8],
  2,
  (tasks) => {
    console.log(tasks);
  },
  2000
);
const button = document
  .querySelector('button')
  .addEventListener('click', throttleClick);
```

![Screenshot 2024-07-31 at 6.50.35 PM.png](Screenshot_2024-07-31_at_6.50.35_PM.png)

## Circuit Braker

![Screenshot 2024-07-31 at 10.18.54 PM.png](Screenshot_2024-07-31_at_10.18.54_PM.png)

- It mostly suits the backend server kind of scenario where if a sever has crashed and we are sending requests to it again n again, it would waste our resources, so circuit breaker would be best thing to avoid it happening.

```jsx
import './style.css';
// Import stylesheets

// Write Javascript code!
const appDiv = document.getElementById('app');
// Forming a closure is needed here as we need to know for sure
// 1. How many times function failed
// 2. How much time passed since it failed last
// so we can determine if time has exceeded so we can resume operation / not.
const circuitBreaker = (fn, failureCount, timeThreshold) => {
  // fn -> check if it fails / passing
  // failureCount -> limiting
  // timeThreshold => For how much time it should stop

  // track failure count
  let failures = 0;
  let timeSinceLastFailure = 0;
  // for making sure function is no longer able to be excuted.
  let isClosed = false;
  return function (...args) {
    // checks to make sure current function invoke is legal or not ( in terms of if it was halt and time passed or not)
    if (isClosed) {
      const diff = Date.now() - timeSinceLastFailure;
      if (diff > timeThreshold) {
        // service is avaialble
        isClosed = true;
      } else {
        console.error('Service unavailable');
        return;
      }
    }
    try {
      const result = fn(...args);
      failures = 0;
      return result;
    } catch (error) {
      failures++;
      timeSinceLastFailure = Date.now();
      if (failures >= failureCount) {
        isClosed = true;
      }
      console.log('Error');
    }
  };
};

// Create a test fnction

const testFunction = () => {
  let count = 0;

  return function () {
    count++;
    if (count < 4) {
      throw 'failed';
    } else {
      return 'hello';
    }
  };
};

let t = testFunction();
let c = circuitBreaker(t, 3, 200);

// Runs fine
c();
c();
c();
// Fails now
c();
setTimeout(() => {
  console.log(c());
}, 300);

```

## Get a different value of object property

[Proxy](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy) allows us to extend the existing object and return a proxy object with the getter and setters in which we can achieve the modification of property values.

This will increment the value of the property `i` every time it is accessed.

```jsx
let obj = {
  i: 0,
};
obj = new Proxy(obj, {
  get: (target, property) => {
    if (property === 'i') {
      target[property] += 1;
      return target[property];
    }
  },
});

console.log(obj.i); // 1
console.log(obj.i); // 2
console.log(obj.i); // 3

```

## Crash Analytics SDK

![Screenshot 2024-08-04 at 6.56.33 PM.png](Screenshot_2024-08-04_at_6.56.33_PM.png)

- stub function → mimics api calls / mock function.
- Stub function / events are passed every second fails every tenth time ( works nine times and fails the tenth time )
- Next event only sent after previous one resolves ( in 1 sec )
- retry if it fails.
    
    ![Screenshot 2024-08-04 at 7.25.35 PM.png](Screenshot_2024-08-04_at_7.25.35_PM.png)
    

```jsx
import './style.css';
// Import stylesheets

// Write Javascript code!
const appDiv = document.getElementById('app');

// creating constructors so that we can create multiple instances when needed

const SDK = function () {
  this.logs = []; // acting as queue
  this.count = 1; // to track function calls
  // first step is to take events and queue them
  this.log = function (event) {
    this.logs.push(event); // store events in order of newer at top and older at bottom
  };

  // for demo only n%5 ( can be increased )
  // calling wait as it resolves after one second
  // creating promise since we have to resolve reject based on n%5
  this.wait = () =>
    new Promise((resolve, reject) => {
      setTimeout(() => {
        if (this.count % 5 === 0) {
          reject();
        } else {
          resolve();
        }
      }, 1000); // since has to resolve/ reject in one second
    });
  // async because we are dealing promise here
  // if previous event resolves then only log next event
  this.sendAnalyticsEvent = async function () {
    // base condition
    if (this.logs.length === 0) {
      return;
    }

    const current = this.logs.shift(); // returns first entry in the array

    try {
      await this.wait();
      // reach this line after 1 sec
      console.log('logged : ', current);
      this.count++;
    } catch (e) {
      // 5th time event invoked
      console.log('-----------');
      console.log('Event Failed', current);
      console.log('Retrying : ', current);
      console.log('-----------');

      // since event failed so reset count
      this.count = 1;
      // retry now by pushing back to front
      this.logs.unshift(current);
    } finally {
      this.sendAnalyticsEvent(); // recursive call so that it may send next event
    }
  };
};

const sdk = new SDK();
sdk.log('Event 1');
sdk.log('Event 2');
sdk.log('Event 3');
sdk.log('Event 4');
sdk.log('Event 5');
sdk.log('Event 6');
sdk.log('Event 7');
sdk.log('Event 8');
sdk.log('Event 9');
sdk.log('Event 10');
sdk.log('Event 11');
sdk.log('Event 12');
sdk.log('Event 13');
sdk.log('Event 14');
sdk.log('Event 15');
sdk.sendAnalyticsEvent();

```

## Fetch with Timeout

- implement fetch and time it out in given time and  abort it otherwise.
- for my case i kept duration to 2000 and i works other wise its aborted
    
    ![Screenshot 2024-08-04 at 9.30.55 PM.png](Screenshot_2024-08-04_at_9.30.55_PM.png)
    
- 

```
// takes url and duration, if it resolves witin duration otherwise abort
const fetchWithTimeout = (url, duration) => {
  // promise because we want to abort if api do not resolves withtin time
  return new Promise((resolve, reject) => {
    // use abortController to abort any network call
    const controller = new AbortController();
    // signal property is passed to fetch and monitor the api call
    const signal = controller.signal;

    let timerID = null;
    fetch(url, { signal })
      .then((response) => {
        response
          .json()
          .then((e) => {
            clearTimeout(timerID);
            resolve(e);
          })
          .catch((error) => {
            reject(error);
          });
      })
      .catch((error) => {
        reject(error);
      });
    // abort api after timer expires
    timerID = setTimeout(() => {
      controller.abort();
    }, duration);
  });
};

fetchWithTimeout('https://jsonplaceholder.typicode.com/todos/1', 2000)
  .then((resp) => {
    console.log(resp);
  })
  .catch((error) => {
    console.error(error);
  });

// Aborted
// error

```

## Debounce function with leading and trailing options

- Used to reduce the network / function calls
- Like for example we have a user writes something in search bar and stop for certain time only then you can fire api calls
- Debounce functions gets a call back which is invoked after duration amount of user stopped writing / gives delay of duration between key press.

```jsx
const debounce = (fn, delay) => {
  // keep record of function invoke
  let timerId;
  // every argument passed to debouncedSearch has to be passed down to onChange, o this below fucntion gets all these args o be passed to fn
  return function (...args) {
    const context = this;
    // make sure input fn only when user stops for certain amount of time

    // if function (the one being returned) invoked before setTimeout completed
    clearTimeout(timerId);
    // only the fresh timeout will be held while previous will be cleared
    timerId = setTimeout(() => {
      fn.apply(context, args);
    }, delay);
  };
};

// Write Javascript code!
const appDiv = document.getElementById('app');
// basic debounce
const onChange = (e) => {
  console.log(e.target.value);
};
const debouncedSearch = debounce(onChange, 1000);
const search = document.getElementById('search');
search.addEventListener('keyup', debouncedSearch);
```

only invoke after user stops for 1 sec

reasons for resetting timer

- **Preventing Premature Invocation**: When you use `setTimeout`, it schedules the `fn` to be executed after `delay` milliseconds. However, if the user continues to interact (e.g., typing or clicking) before that `delay` expires, you want to cancel the previously scheduled invocation of `fn` to restart the timeout period.
- **Resetting the Timer**: By calling `clearTimeout(timerId)`, you ensure that any previously set timeout to invoke `fn` is canceled. This prevents multiple, rapid invocations of `fn` within a short period, effectively resetting the debounce timer.
- **Ensuring Delayed Execution**: The purpose of debounce is to delay invoking `fn` until after the user stops interacting for at least `delay` milliseconds. If you didn't clear the timeout and simply set a new one on every interaction, `fn` might execute multiple times in quick succession, defeating the purpose of debounce.

### Debounce With Leading and Trailing

Now comes the debounce with leading and trailing ( similar to throttle leading and trailing )

- leading only invokes at first
- trailing after the delay
- leading and trailing before and after the delay
- Explanation
    
    ### Explanation of Leading and Trailing Options
    
    1. **Leading Edge (`option.leading`)**:
        - **Purpose**: To invoke the function immediately on the first call within the debounce period.
        - **Line**: `if (option.leading && !timerId) { fn.apply(context, args); isLeadingInvoked = true; }`
        - **Function**: If `option.leading` is `true` and there's no existing timeout (`!timerId`), the function `fn` is invoked immediately. This is useful for scenarios where you want the function to respond immediately to the first event.
    2. **Trailing Edge (`option.trailing`)**:
        - **Purpose**: To invoke the function after the specified delay when the user stops interacting.
        - **Line**: `if (option.trailing && !isLeadingInvoked) { fn.apply(context, args); }`
        - **Function**: If `option.trailing` is `true` and the function has not been invoked on the leading edge (`!isLeadingInvoked`), the function `fn` is invoked after the delay period. This ensures the function executes after the user has finished interacting, useful for finalizing actions based on user input.
    
    ### Line-by-Line Breakdown
    
    - `const debounce = (fn, delay, option = { leading: true, trailing: false }) => {`
        - Defines the debounce function with default options for `leading` and `trailing`.
    - `let timerId;`
        - Declares a variable to store the timeout ID.
    - `let isLeadingInvoked = false;`
        - Declares a flag to track if the function was invoked on the leading edge.
    - `return function (...args) {`
        - Returns a debounced version of the input function `fn`.
    - `const context = this;`
        - Captures the context for applying the function later.
    - `if (timerId) { clearTimeout(timerId); }`
        - Clears any existing timeout to reset the debounce timer.
    - `if (option.leading && !timerId) {`
        - Checks if the leading edge execution is required and there is no existing timeout.
    - `fn.apply(context, args);`
        - Invokes the function immediately for the leading edge.
    - `isLeadingInvoked = true;`
        - Marks that the leading edge function has been invoked.
    - `} else { isLeadingInvoked = false; }`
        - Resets the leading invocation flag if the function is not invoked on the leading edge.
    - `timerId = setTimeout(() => {`
        - Sets a timeout for the trailing edge execution.
    - `if (option.trailing && !isLeadingInvoked) {`
        - Checks if the trailing edge execution is required and the function was not invoked on the leading edge.
    - `fn.apply(context, args);`
        - Invokes the function after the delay for the trailing edge.
    - `timerId = null;`
        - Resets the timeout ID to ensure the leading edge condition works correctly on subsequent calls.
    - `}, delay);`
        - Specifies the delay for the trailing timeout.

```jsx
const debounce = (fn, delay, option = { leading: true, trailing: false }) => {
  let timerId;
  let isLeadingInvoked = false;
  return function (...args) {
    const context = this;
    // if timer has run clear timeoue ( for trailing case )
    if (timerId) {
      clearTimeout(timerId);
    }

    // base condition for leading case
    if (option.leading && !timerId) {
      fn.apply(context, args);
      isLeadingInvoked = true;
    } else {
      isLeadingInvoked = false;
    }

    // trailing part
    timerId = setTimeout(() => {
      if (option.trailing && !isLeadingInvoked) {
        fn.apply(context, args);
      }
      timerId = null; // so that base conditon for leading works
    }, delay);
  };
};

// // Write Javascript code!
const appDiv = document.getElementById('app');
// basic debounce
const onChange = (e) => {
  console.log(e.target.value);
};
const debouncedSearch = debounce(onChange, 1000);
const search = document.getElementById('search');
search.addEventListener('keyup', debouncedSearch);

```

## Cached api call with expiry time

- It helps us minimize the api calls
- It actually takes a duration and caches the api data returned for that amount of time.
- This functions returns a callback which can be called with url.
- If we use this callback again with duration it wont call the fresh api but return cached data again.Ï
    
    ![Screenshot 2024-08-06 at 9.23.35 PM.png](Screenshot_2024-08-06_at_9.23.35_PM.png)
    

```
const cachedApiCall = (time) => {
  // responsible for caching
  const cache = {};
  // since its a promise thus async
  // configis optional
  return async (url, config = {}) => {
    // the identifier need to keep record of cache
    const key = `${url}${JSON.stringify(config)}`;
    // if entry is there return if not call api
    const entry = cache[key];
    // no entry or entry is expired
    if (!entry || Date.now() > entry.expiry) {
      console.log('Making afresh api call');
      try {
        let resp = await fetch(url, config);
        resp = await resp.json();
        // date.now() current time in ms + time ( total time after which it expires)
        cache[key] = { value: resp, expiry: Date.now() + time };
      } catch (e) {
        console.log('error while makinh api call', e);
      }
    }

    //return the cache
    return cache[key].value;
  };
};

const call = cachedApiCall(2000);

// first call
// an API call will be made and its response will be cached
call('https://jsonplaceholder.typicode.com/todos/1', {}).then((a) =>
  console.log('1', a)
);
setTimeout(() => {
  call('https://jsonplaceholder.typicode.com/todos/1', {}).then((a) =>
    console.log('2', a)
  );
}, 700);
setTimeout(() => {
  call('https://jsonplaceholder.typicode.com/todos/1', {}).then((a) =>
    console.log('3', a)
  );
}, 3000);

```

## Piping Function

![Screenshot 2024-08-08 at 8.56.52 PM.png](Screenshot_2024-08-08_at_8.56.52_PM.png)

- Input in an object with nested keys whose values are actual fucntions accepting arguments
- We have to make a function which return another function which accepts all the arguments as nested functions
- then Assign each keys its function result
    
    ![Screenshot 2024-08-08 at 9.10.27 PM.png](Screenshot_2024-08-08_at_9.10.27_PM.png)
    
    ```jsx
    let test = {
      a: {
        b: (a, b, c) => a + b + c,
        c: (a, b, c) => a + b - c,
      },
      d: (a, b, c) => a - b - c,
      e: 1,
      f: true,
    };
    
    function Fn(obj) {
      return function (...args) {
        for (let key in obj) {
          const val = obj[key];
          if (typeof val === 'function') {
            obj[key] = val(...args);
          } // recurse when encounter object
          else if (val && typeof val === 'object' && !Array.isArray(val)) {
            Fn(val)(...args); // the second parenthesis is to pass arguments to returned fucntion inside
          }
        }
      };
    }
    
    Fn(test)(1, 1, 1);
    console.log(test);
    
    ```
    

## Piping Functions

- Where we pass values through multiple functions

```jsx
const val = { salary: 10000 };

const getSalary = (person) => person.salary;
const addBonus = (netSalary) => netSalary + 1000;
const deductTax = (grossSalary) => grossSalary - grossSalary * 0.3;

const pipe = (...fns) => {
  return (val) => {
    fns.forEach((fn) => {
      val = fn(val);
    });

    return val;
  };
};

const result = pipe(getSalary, addBonus, deductTax)(val);
console.log(result);

```

- Object passed to first function is piped to second, then third and so on.