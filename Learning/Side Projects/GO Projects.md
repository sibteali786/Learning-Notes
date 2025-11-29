# GO Projects

# Json Parser

## Step 1

### 1. **Lexical Analysis (Tokenization)**

This is the first phase where we break down the input string into meaningful chunks called **tokens**. Think of it like breaking a sentence into words.

For JSON `{"key": "value"}`, the tokens would be:

- `{` (LEFT_BRACE)
- `"key"` (STRING)
- `:` (COLON)
- `"value"` (STRING)
- `}` (RIGHT_BRACE)

### 2. **Syntactic Analysis (Parsing)**

This is where we check if the sequence of tokens follows the JSON grammar rules and build a data structure representing the parsed JSON.

### 3. **Tokens**

Tokens are the basic building blocks. In JSON, we have:

- Literals: `{`, `}`, `[`, `]`, `:`, `,`
- Values: strings, numbers, booleans, null
- Whitespace (which we usually ignore)

## Step 2 : Recursive Descent Parsing

Let me explain these concepts using simple analogies and JSON examples!

## What is an AST (Abstract Syntax Tree)?

Think of an AST like a **family tree, but for code structure**.

### Real-World Analogy

Imagine you're organizing a bookshelf:

- The bookshelf is your "program"
- Each shelf is a "section"
- Each book is a "piece of data"
- The way you organize them shows their relationships

### JSON Example

Let's say you have this JSON:

```json
{
  "name": "John",
  "age": 30
}

```

Your brain naturally understands this as:

- An **object** that contains
    - A **property** called "name" with **value** "John"
    - A **property** called "age" with **value** 30

An AST is just a way to represent this understanding in a tree structure:

```
    Object
   /      \
Property  Property
  |         |
"name"    "age"
  |         |
"John"     30

```

### Why Do We Need an AST?

### The Problem

Your lexer gives you individual tokens like:
`{`, `"name"`, `:`, `"John"`, `,`, `"age"`, `:`, `30`, `}`

But these are just individual pieces - like having puzzle pieces but no picture of what the completed puzzle should look like.

### The Solution

An AST shows the **meaning** and **relationships** between these pieces.

### What is Recursive Descent Parsing?

Think of it like **following a recipe** where some steps tell you to "follow another recipe."

### Real-World Analogy

Imagine you're making a sandwich:

1. Make sandwich = Get bread + Add filling + Close sandwich
2. Add filling = Add meat + Add vegetables
3. Add vegetables = Add lettuce + Add tomatoes

Notice how "Make sandwich" calls "Add filling," which calls "Add vegetables." Each step breaks down into smaller steps.

### JSON Parsing Example

To parse JSON, you need rules like:

1. **Parse JSON** = Parse a value
2. **Parse Value** = Parse object OR Parse array OR Parse string OR Parse number OR Parse boolean OR Parse null
3. **Parse Object** = `{` + Parse properties + `}`
4. **Parse Properties** = Parse property + (`,` + Parse property)*
5. **Parse Property** = Parse string + `:` + Parse value

Notice the **recursion**: "Parse Value" can call "Parse Object," which calls "Parse Value" again!

### Step-by-Step Example

Let's parse this JSON: `{"name": "John"}`

### Step 1: Tokens from Lexer

```
[{, "name", :, "John", }]

```

### Step 2: Recursive Descent Process

**Call parseJSON():**

- "I need to parse a JSON value"
- Current token: `{`
- "This looks like an object, so call parseObject()"

**Call parseObject():**

- "I expect a `{` token" ✓
- "Now I need to parse properties"
- "Call parseProperty()"

**Call parseProperty():**

- "I expect a string token" → Got `"name"` ✓
- "I expect a `:` token" ✓
- "Now I need to parse the value"
- "Call parseValue()"

**Call parseValue():**

- Current token: `"John"`
- "This is a string, so create a StringNode"
- Return StringNode("John")

**Back to parseProperty():**

- Got the value, create PropertyNode("name", StringNode("John"))
- Return this property

**Back to parseObject():**

- Got one property
- Check next token: `}`
- "No more properties, so close the object"
- Create ObjectNode with the property
- Return ObjectNode

**Back to parseJSON():**

- Got the complete object
- Return it as the root of our AST

### Step 3: The Resulting AST

```
ObjectNode
    |
PropertyNode
    |       \
"name"   StringNode("John")

```

### Types of AST Nodes for JSON

Think of these as different **types of boxes** to hold different kinds of data:

```go
// Base interface - like saying "this is some kind of box"
type Node interface {
    String() string
}

// Different types of boxes:
type ObjectNode struct {
    Properties []PropertyNode
}

type ArrayNode struct {
    Elements []Node
}

type PropertyNode struct {
    Key   string
    Value Node
}

type StringNode struct {
    Value string
}

type NumberNode struct {
    Value int
}

type BooleanNode struct {
    Value bool
}

type NullNode struct{}

```

### Complex Example

Let's see how this works with nested JSON:

```json
{
  "person": {
    "name": "John",
    "hobbies": ["reading", "coding"]
  }
}

```

### The Parsing Process

1. **parseJSON()** → calls **parseObject()**
2. **parseObject()** → finds property "person"
3. **parseProperty()** → key is "person", value needs parsing
4. **parseValue()** → sees `{`, so calls **parseObject()** again! (RECURSION!)
5. **parseObject()** → finds property "name"
6. **parseProperty()** → "name": "John"
7. **parseObject()** → finds property "hobbies"
8. **parseProperty()** → key is "hobbies", value needs parsing
9. **parseValue()** → sees `[`, so calls **parseArray()**
10. **parseArray()** → parses each string element
11. Everything unwinds back up...

### The Resulting AST

```
ObjectNode
    |
PropertyNode("person")
    |
ObjectNode
    |        \
PropertyNode  PropertyNode
("name")      ("hobbies")
    |             |
StringNode    ArrayNode
("John")      /        \
         StringNode  StringNode
         ("reading") ("coding")

```

### Why "Recursive Descent"?

- **Recursive**: Functions call themselves (like parseValue calling parseObject calling parseValue)
- **Descent**: We start from the top (whole JSON) and work our way down to individual pieces

### Benefits of This Approach

1. **Natural**: Matches how we think about nested structures
2. **Readable**: Code looks similar to the grammar rules
3. **Flexible**: Easy to add new features
4. **Debuggable**: Easy to trace through the parsing steps

# Which

## Intuition

### What is the `which` command?

The `which` command is a Unix utility that helps you locate executable programs in your system's PATH. When you type a command like `ls` or `python3`, your shell searches through directories listed in the `$PATH` environment variable to find the executable file. The `which` command shows you exactly where that executable is located.

For example:

- `which ls` might return `/bin/ls`
- `which python3` might return `/usr/bin/python3`

### Why is this useful?

1. **Debugging**: When you have multiple versions of a program installed
2. **Scripting**: To ensure you're using the correct binary
3. **System administration**: To understand which version of a tool will be executed

### `os.Args`

- A slice (Go's version of arrays) containing command-line arguments
- `os.Args[0]` is always the program name
- `os.Args[1:]` contains the actual arguments passed by the user

### Questions for You to Think About:

- What happens when you run the program without arguments?
    
    ✅ **With arguments**: It correctly shows `Programs to search for: [ls python3 go]`
    
- What do you see when you run it with arguments like `ls` and `python3`?
    
    ✅ **Without arguments**: It shows the usage message and exits with status 1
    
- Why do you think `os.Args[0]` contains the program name?
    
    **The long path**: That's the temporary executable Go creates when you run `go run main.go`
    
    ## Answer to Question 3: Why `os.Args[0]` Contains the Program Name
    
    This is a **Unix convention** that dates back decades! When any program starts, the operating system always passes the program's name (or path) as the first argument. This allows programs to:
    
    1. **Know their own name** for error messages
    2. **Behave differently** based on how they were called (some programs have multiple names/symlinks)
    3. **Print helpful usage messages** that include the correct program name
    
    For example, the real `which` command uses this to show: `which: command not found` instead of just `command not found`.
    

![image.png](image.png)

## Step1

main.go 

```go
package main

import (
	"fmt"
	"os"
	"strings"
)

// parseCommandLine extracts and validates command line arguments
func parseCommandLine() []string {
	args := os.Args[1:] // Skip the program name
	
	if len(args) == 0 {
		fmt.Fprintf(os.Stderr, "Usage: %s <program1> <program2> ...\n", os.Args[0])
		os.Exit(1)
	}
	
	// Let's validate that none of the arguments are empty
	var validCommands []string
	for _, command := range args {
		// Trim whitespace and check if it's not empty
		command = strings.TrimSpace(command)
		if command != "" {
			validCommands = append(validCommands, command)
		}
	}
	
	if len(validCommands) == 0 {
		fmt.Fprintf(os.Stderr, "Error: No valid commands provided\n")
		os.Exit(1)
	}
	
	return validCommands
}

func main() {
	fmt.Println("Go Which - A which command implementation")
	
	// Step 1: Parse command line arguments
	commands := parseCommandLine()
	
	fmt.Printf("Searching for commands: %v\n", commands)
	
	// TODO: Step 2 - Read PATH environment variable
	// TODO: Step 3 - Search directories for binaries
	// TODO: Step 4 - Output results
}
```

# Why Caching is important

[code::dive conference 2014 - Scott Meyers: Cpu Caches and Why You Care](https://youtu.be/WDIkqP4JbkE?si=MV5LI3EEKrP5mdaI)

- Any kind of data access / instruction access that fits this pattern will be faster
    
    ![Screenshot 2025-08-09 at 10.03.57 PM.png](Screenshot_2025-08-09_at_10.03.57_PM.png)
    
- That is why row access is quite faster than the column access because when fetching r[0] we will prefetch r[1] but that is not gonna happen in case c[0] and c[1].
- Things on same cache line are mostly cached as their neighbour might have been fetched earlier.

## False Sharing

### Cache Line Basics

Modern CPUs don't cache individual bytes or words - they cache entire "cache lines" (typically 64 bytes on x86-64). When a CPU reads from memory, it loads the entire cache line containing that data.

### The False Sharing Scenario

Consider this memory layout where two variables happen to be in the same cache line:

```go
Cache Line (64 bytes):
[Variable A (Core 1)][Variable B (Core 2)][Other data...]
```

Even though Core 1 only cares about Variable A and Core 2 only cares about Variable B, they end up fighting over the same cache line.

## How False Sharing Occurs

1. **Core 1** reads/writes Variable A → Loads entire cache line into its L1 cache
2. **Core 2** reads/writes Variable B → Loads the same cache line into its L1 cache
3. When Core 1 modifies Variable A, the cache line becomes "dirty"
4. **Cache coherency protocol** invalidates Core 2's copy of the cache line
5. Core 2 must reload the cache line from memory (or Core 1's cache)
6. This ping-pong effect continues with every write

**Performance Impact**

```go
Without False Sharing:    With False Sharing:
Core 1: [Fast L1 cache]   Core 1: [Cache miss] → [Memory fetch]
Core 2: [Fast L1 cache]   Core 2: [Cache miss] → [Memory fetch]
                          
Result: ~1-3 cycles       Result: ~100-300 cycles per access
```

## Tips

![Screenshot 2025-08-09 at 11.25.41 PM.png](Screenshot_2025-08-09_at_11.25.41_PM.png)

- Arrays are better mostly
- a boolean in an object is a performance problem as to know what entire object is worth it or not we have to fetch it entriely and then reject based on 1 property ?

# Compression Tool

## Huffman Encoding

### Intuition

- A technique to reduce the size of data sent across systems

![Screenshot 2025-08-10 at 5.57.55 PM.png](Screenshot_2025-08-10_at_5.57.55_PM.png)

- In 8 bits we can represent 256 characters and in our case for 5 characters its more than enough and kind of un-necessary
- Here we only use 3 bits to represent 5 characters

![Screenshot 2025-08-10 at 6.05.14 PM.png](Screenshot_2025-08-10_at_6.05.14_PM.png)

- When this message is received by other end how would it know which number means what ?
- Send table wtih ASCII codes for symbols and code ( compressed one ) as well
    
    ![Screenshot 2025-08-10 at 6.09.05 PM.png](Screenshot_2025-08-10_at_6.09.05_PM.png)
    

### Technique

- Sort in order of increasing count of frequency
- Form a tree by always selecting two minimum values
- Mark left branches as 0 and mark right branches as 1
- For code of a given letter follow path from root to letter
    
    ![Screenshot 2025-08-10 at 6.30.24 PM.png](Screenshot_2025-08-10_at_6.30.24_PM.png)
    

![Screenshot 2025-08-10 at 7.06.03 PM.png](Screenshot_2025-08-10_at_7.06.03_PM.png)

![Screenshot 2025-08-10 at 11.06.05 PM.png](Screenshot_2025-08-10_at_11.06.05_PM.png)

## Decoding

- We need binary tree for decoding
- Then simply decode message using tree going from root to leaf nodes
- for instance start with 001 so from root we go like left left right and we get B
    
    ![Screenshot 2025-08-10 at 11.17.47 PM.png](Screenshot_2025-08-10_at_11.17.47_PM.png)
    

## Prefixing

Great question! Let me explain **why** we need `VerifyPrefixFree` and **how** it works with detailed examples.

### What is the Prefix-Free Property?

In Huffman coding, **no code should be a prefix of another code**. This is crucial for unambiguous decoding.

### Why is this important?

When decoding a bit stream, you need to know where one code ends and another begins **without any delimiter**.

### Example: Problem WITHOUT Prefix-Free Codes

### Bad Code Table (NOT prefix-free):

```
'A' → "1"
'B' → "10"
'C' → "101"

```

**Problem:** When you see the bit stream `"101"`, what does it mean?

- Could be: 'A' + 'C' (1 + 01)? ❌ But 'C' is "101" not "01"
- Could be: 'A' + '?' (1 + 01)? ❌ No code "01" exists
- Could be: 'B' + '1' (10 + 1)? That's 'B' + 'A'
- Could be: 'C' (101)

**Ambiguous!** We can't tell where codes start/end.

## Example: Good Prefix-Free Codes

### Good Code Table (Prefix-free):

```
'A' → "00"
'B' → "01"
'C' → "10"
'D' → "11"

```

**No code is a prefix of another!**

- "00" is NOT a prefix of "01", "10", or "11" ✅
- "01" is NOT a prefix of "00", "10", or "11" ✅
- etc.

When decoding `"001011"`:

- Read "00" → 'A' (found!)
- Read "10" → 'C' (found!)
- Read "11" → 'D' (found!)
- Result: "ACD" ✅ Unambiguous!

### How `VerifyPrefixFree` Works

Let's trace through the code with examples:

### Example 1: Valid Prefix-Free Codes

```go
// Code table:
// 'A' → HuffmanCode{bits: 0, length: 2}   // "00"
// 'B' → HuffmanCode{bits: 1, length: 2}   // "01"
// 'C' → HuffmanCode{bits: 2, length: 2}   // "10"

codes := []HuffmanCode{
    {bits: 0, length: 2},  // "00"
    {bits: 1, length: 2},  // "01"
    {bits: 2, length: 2},  // "10"
}

// Check all pairs:

// Pair (i=0, j=1): "00" vs "01"
isPrefix({bits:0, len:2}, {bits:1, len:2})?
// lengths equal (2 == 2), so return false ✅

// Pair (i=0, j=2): "00" vs "10"
isPrefix({bits:0, len:2}, {bits:2, len:2})?
// lengths equal (2 == 2), so return false ✅

// Pair (i=1, j=2): "01" vs "10"
isPrefix({bits:1, len:2}, {bits:2, len:2})?
// lengths equal (2 == 2), so return false ✅

// Result: true (prefix-free!) ✅

```

### Example 2: Invalid - Has Prefix

```go
// Code table:
// 'A' → HuffmanCode{bits: 1, length: 1}   // "1"
// 'B' → HuffmanCode{bits: 2, length: 2}   // "10"

codes := []HuffmanCode{
    {bits: 1, length: 1},  // "1"
    {bits: 2, length: 2},  // "10"
}

// Check pair: "1" vs "10"
isPrefix({bits:1, len:1}, {bits:2, len:2})?

code1.length = 1
code2.length = 2
// 1 < 2, so continue checking...

// Create mask to isolate first 1 bit of code2
mask = (1 << 1) - 1          // = 2 - 1 = 1
mask = 1 << (2 - 1)           // = 1 << 1 = 2
// mask = 0b10 (isolates position 1)

// Extract first 1 bit of code2
(code2.bits & mask) >> (code2.length - code1.length)
= (2 & 2) >> (2 - 1)
= 2 >> 1
= 1

// Compare: 1 == 1? YES!
// "1" IS a prefix of "10" ❌

// Result: false (NOT prefix-free!)

```

### Detailed `isPrefix` Function Breakdown

Let's visualize how `isPrefix` works:

### Visual Example: Check if "10" is prefix of "1010"

```go
code1 = {bits: 2, length: 2}  // "10" in binary
code2 = {bits: 10, length: 4} // "1010" in binary

Step 1: Length check
code1.length < code2.length?
2 < 4? YES, continue

Step 2: Create mask for first 2 bits of code2
mask = (1 << code1.length) - 1
     = (1 << 2) - 1
     = 4 - 1
     = 3
     = 0b0011

Then shift left by (code2.length - code1.length):
mask = 3 << (4 - 2)
     = 3 << 2
     = 12
     = 0b1100

Visual:
code2.bits = 10    = 0b1010
mask       = 12    = 0b1100
                      ↑↑
                      These positions

Step 3: Extract and compare
(code2.bits & mask) >> (code2.length - code1.length)
= (10 & 12) >> 2
= (0b1010 & 0b1100) >> 2
= 0b1000 >> 2
= 0b0010
= 2

Compare: 2 == 2? YES!
"10" IS a prefix of "1010" ✅

```

### Real Huffman Tree Example

```go
// Huffman tree:
//        *
//       / \
//      A   *
//         / \
//        B   C

// Codes:
// 'A' → "0"     (bits: 0, length: 1)
// 'B' → "10"    (bits: 2, length: 2)
// 'C' → "11"    (bits: 3, length: 2)

// Verify:
// "0" vs "10"  → isPrefix? 0 < 2, check bits...
//                Extract first 1 bit of "10" = "1"
//                "0" != "1" ✅ Not a prefix
// "0" vs "11"  → Similar check... ✅ Not a prefix
// "10" vs "11" → Same length, ✅ Not a prefix

// Result: Prefix-free! ✅

```

## Why Huffman Trees ALWAYS Generate Prefix-Free Codes

**Key insight:** In a Huffman tree, **characters are only at leaf nodes**, never at internal nodes.

```
If you reach a leaf → you found a complete code
If you're at an internal node → keep reading bits

This guarantees no code is a prefix of another!

```

### Visual Proof:

```
        *  (internal - not a code)
       / \
      A   *  (internal - not a code)
         / \
        B   C

'A' is at a leaf → code ends here
You CANNOT continue from 'A' to form another code!

So 'A's code "0" cannot be a prefix of anything else.

```

### When Would `VerifyPrefixFree` Return False?

Only if someone **manually creates** a bad code table:

```go
// Manually created (WRONG):
badTable := CodeTable{
    'A': HuffmanCode{bits: 1, length: 1},    // "1"
    'B': HuffmanCode{bits: 2, length: 2},    // "10"
    'C': HuffmanCode{bits: 3, length: 2},    // "11"
}

VerifyPrefixFree(badTable) // Returns false ❌
// Because "1" is a prefix of "10" and "11"

```

### Use Cases for `VerifyPrefixFree`

1. **Debugging:** Verify your Huffman tree implementation is correct
2. **Testing:** Ensure generated codes are valid
3. **Custom codes:** Validate manually created code tables
4. **File format validation:** Check if loaded codes from a file are valid

### Summary

- **Purpose:** Ensure no code is a prefix of another (required for unambiguous decoding)
- **How:** Compare all pairs of codes, check if shorter one matches the start of longer one
- **Why it matters:** Without prefix-free property, you can't decode bit streams correctly
- **Huffman guarantee:** Properly built Huffman trees ALWAYS produce prefix-free codes (this function is mainly for validation/debugging)

### What is Masking?

**Masking** is using bitwise AND (`&`) to **isolate** or **extract** specific bits from a number while zeroing out all other bits.

Think of it like putting a stencil over a number - only the bits under the "holes" remain visible.

### Basic Masking Example

```go
number = 0b11010110  // Some bits
mask   = 0b00111100  // Mask to extract middle 4 bits
       & -----------
result = 0b00010100  // Only the masked bits remain

```

The mask has `1`s where we want to keep bits, and `0`s where we want to zero out bits.

### Why Do We Need Masking in `isPrefix`?

We need to **extract the first N bits** from `code2` and compare them with `code1`.

### Problem:

```
code1 = "10"    (2 bits)
code2 = "1011"  (4 bits)

Question: Is "10" a prefix of "1011"?

We need to:
1. Extract the first 2 bits of "1011" → "10"
2. Compare "10" with "10" → Match! It's a prefix!

```

### Step-by-Step Breakdown with Example

Let's use a concrete example:

```go
code1 = HuffmanCode{bits: 2, length: 2}  // "10"
code2 = HuffmanCode{bits: 11, length: 4} // "1011"

// Check if "10" is prefix of "1011"

```

### Step 1: Length Check

```go
if code1.length >= code2.length {
    return false
}

2 >= 4? NO, continue...

```

### Step 2: Create the Mask

This is the tricky part. We build a mask in TWO steps:

### Step 2a: Create a mask with code1.length bits set to 1

```go
(1 << code1.length) - 1

// For code1.length = 2:
1 << 2           // Shift 1 left by 2 positions
= 0b0001 << 2
= 0b0100         // = 4 in decimal

4 - 1 = 3
= 0b0011         // A mask with 2 bits set!

```

Visual:

```
Step 1: 1 << 2
   0b0001
   ↓ shift left 2
   0b0100

Step 2: Subtract 1
   0b0100
 - 0b0001
   ------
   0b0011  ← This has exactly 2 bits set to 1

```

### Step 2b: Shift the mask to the correct position

```go
mask << (code2.length - code1.length)

// Our mask from 2a: 0b0011
// Shift amount: 4 - 2 = 2

0b0011 << 2
= 0b1100

```

Visual:

```
Original mask:    0b0011 (rightmost 2 bits)
                     ↑↑

Shift left by 2:  0b1100 (now at leftmost 2 bits position in 4-bit number)
                  ↑↑

This mask will extract positions 3 and 2 (the first 2 bits) of a 4-bit number!

```

**Final mask value:**

```go
mask = uint64((1<<code1.length)-1) << (code2.length - code1.length)
     = (1<<2 - 1) << (4 - 2)
     = 3 << 2
     = 0b0011 << 2
     = 0b1100
     = 12 in decimal

```

### Step 3: Apply the Mask to Extract Bits

```go
code2.bits & mask

// code2.bits = 11 = 0b1011
// mask = 12 = 0b1100

  0b1011  (code2.bits = 11)
& 0b1100  (mask = 12)
  ------
  0b1000  (result = 8)

```

Visual explanation:

```
code2 bits:  1 0 1 1  (positions 3,2,1,0)
mask:        1 1 0 0
             ↑ ↑      (only these positions have 1s in mask)

After AND:   1 0 0 0  (only positions 3,2 remain)

```

### Step 4: Shift Back to Compare

Now we have `0b1000` but we need to shift it right to align with `code1.bits`:

```go
(code2.bits & mask) >> (code2.length - code1.length)

= 0b1000 >> (4 - 2)
= 0b1000 >> 2
= 0b0010
= 2 in decimal

```

Visual:

```
After masking:  0b1000
                ↑↑
                These are the first 2 bits

Shift right 2:  0b0010
                  ↑↑
                  Now aligned for comparison

```

### Step 5: Final Comparison

```go
(code2.bits & mask) >> (code2.length - code1.length) == code1.bits

2 == 2?  YES! ✅

// "10" IS a prefix of "1011"

```

## Huffman Encoder

- In our case we store in LSB format so `110` would be stored as `011` instead.
- In isPrefix we check if code1 is prefix of code2

```go
func isPrefix(code1, code2 HuffmanCode) bool {
	if code1.length >= code2.length {
		return false
	}

	// Both codes store bits LSB-first (position 0 = first bit appended)
	// To check if code1 is a prefix, we compare the first code1.length bits

	// Extract the first code1.length bits from code2
	// Since both are stored the same way, we just mask the lower bits
	mask := uint64((1 << code1.length) - 1)
	code2Prefix := code2.bits & mask

	return code2Prefix == code1.bits
}
```

- Lets take an example

### Example

```go
code1 = {bits: 3, lenght: 2} = 11
code2 = {bits: 3, length: 3} = 110
```

- first we compare lengths i.e but it fails as code1 is smaller in size

```go
if code1.length >= code2.length then return false
```

- Then we create mask from `code1` length so we can extract out `N` bits from `code2` where `N = code1.length`
- which is left shift 1 by code1.length and - 1.

```go
mask := (1 << code1.length ) - 1
mask := (1 << 2 ) - 1 => 100 - 001 => 4 - 1 => 3 or 011
```

- Then we extract prefix for `code2` by applying `And` operation to code2 bits

```go
code2Prefix := code2.bits & mask
code2Prefix := 3 && 3 => 011 OR 011 => 011
```

- finally we compare code2Prefix bits with code1 bits and see if they are same then its prefix

```go
code2Prefix == code1.bits
```

## How Masking works

Let me break down **why we use `1` and left shift** to create masks.

### The Goal of Masking

We want to **isolate specific bits** from a number. To do this, we need a mask that has:

- `1`s in positions we want to **keep**
- `0`s in positions we want to **ignore**

### Why Start with `1`?

The number `1` in binary is:

```
1 = 0b00000001

```

It has exactly **one bit set** at position 0. This is our building block.

### Why Left Shift `1`?

Left shifting `1` moves that single bit to different positions:

```
1 << 0 = 0b00000001  (bit at position 0)
1 << 1 = 0b00000010  (bit at position 1)
1 << 2 = 0b00000100  (bit at position 2)
1 << 3 = 0b00001000  (bit at position 3)

```

Each shift creates a **power of 2**:

- `1 << 0 = 1 = 2^0`
- `1 << 1 = 2 = 2^1`
- `1 << 2 = 4 = 2^2`
- `1 << 3 = 8 = 2^3`

### Creating a Mask: The Formula

To create a mask with N consecutive `1`s starting from position 0:

```
(1 << N) - 1

```

### Why This Works

Let's trace `N = 3`:

**Step 1: `1 << 3`**

```
1 << 3 = 0b00001000 = 8
         ↑
         Position 3 has a 1

```

**Step 2: Subtract 1**

```
  0b00001000  (8)
- 0b00000001  (1)
--------------
  0b00000111  (7)
  ↑↑↑↑↑↑↑↑
  Positions 2,1,0 all became 1!

```

### Why Subtracting 1 Creates All 1s Below

When you subtract 1 from a power of 2:

- The single `1` bit becomes `0`
- All bits **below** it become `1`

Visual examples:

```
1000 - 1 = 0111
 ↓          ↓↓↓
 8 - 1 = 7

0100 - 1 = 0011
 ↓          ↓↓
 4 - 1 = 3

0010 - 1 = 0001
 ↓          ↓
 2 - 1 = 1

0001 - 1 = 0000
 ↓
 1 - 1 = 0

```

### Example: Create a Mask for First 2 Bits

```go
mask = (1 << 2) - 1

Step 1: 1 << 2
  0b00000001 << 2
= 0b00000100  (moved bit to position 2)
= 4

Step 2: Subtract 1
  0b00000100
- 0b00000001
--------------
  0b00000011  (positions 1,0 are now 1)
= 3

```

Now we have a mask `0b11` that covers positions 1 and 0.

### Using the Mask

```go
code2.bits = 0b00001011  (some number)
mask       = 0b00000011  (from (1<<2)-1)
           & -----------
result     = 0b00000011  (extracted positions 1,0)

```

The mask **keeps** bits at positions 1,0 and **zeros out** everything else.

### Why Not Start with a Different Number?

You could, but it's less flexible:

**Starting with 3:**

```
3 = 0b11  (already has 2 bits)
3 << 1 = 0b110  (now 2 bits shifted left)

```

This doesn't give you control over creating arbitrary-length masks easily.

**Starting with 1 is universal:**

```
(1 << N) - 1 always gives you N consecutive 1s

```

### Visual Summary

```
Want mask for first N bits?

Step 1: Create a 1 at position N
(1 << N)

Step 2: Subtract 1 to get all 1s below position N
(1 << N) - 1

Examples:
N=1: (1<<1)-1 = 2-1 = 1 = 0b1
N=2: (1<<2)-1 = 4-1 = 3 = 0b11
N=3: (1<<3)-1 = 8-1 = 7 = 0b111
N=4: (1<<4)-1 = 16-1 = 15 = 0b1111

```

The pattern `(1 << N) - 1` is a standard bit manipulation idiom precisely because it cleanly creates a mask of N consecutive 1s starting from position 0.

## BitBuffer

- **Purpose:** Handles **writing** and **reading** individual bits when you can only work with bytes
- **When:** Used during **encoding** (writing bits) and **decoding** (reading bits)
- **Example:** Accumulates bits until you have 8, then writes a byte to the file

**They work together:**

1. BitBuffer writes the prefix-free codes as a continuous bit stream
2. The prefix-free property ensures you can decode that bit stream correctly

## How BitBuffer Works

Think of BitBuffer as a **temporary storage bin** that:

1. Collects individual bits
2. When it has 8 bits (1 byte), writes them to the file
3. Keeps any leftover bits for the next batch

### Visual Example

```
Let's encode "abc" with codes:
'a' = "10"    (2 bits)
'b' = "110"   (3 bits)
'c' = "1111"  (4 bits)

BitBuffer Process:
┌─────────────────────────────────────────┐
│ buffer: [........] (8 bits available)   │
│ position: 0                             │
└─────────────────────────────────────────┘

Step 1: Write 'a' code "10"
┌─────────────────────────────────────────┐
│ buffer: [10......] ← added 2 bits       │
│ position: 2                             │
└─────────────────────────────────────────┘

Step 2: Write 'b' code "110"
┌─────────────────────────────────────────┐
│ buffer: [10110...] ← added 3 more bits  │
│ position: 5                             │
└─────────────────────────────────────────┘

Step 3: Write 'c' code "1111"
┌─────────────────────────────────────────┐
│ buffer: [101101111] ← 9 bits total!     │
│         ^^^^^^^^ → Write to file (8)    │
│                ^ → Keep 1 bit           │
└─────────────────────────────────────────┘

File gets: 0b10110111 = 183
Buffer now: [1.......] (1 bit remaining)
position: 1
```

Great question! Let me break down **why we left shift and then OR** in the BitBuffer.

We want to **build a byte from left to right** (MSB to LSB), filling it bit by bit as codes come in.

### Why Left Shift?

We need to place each incoming bit at the **correct position** in the buffer.

### Visual: Building a Byte Left-to-Right

```
We want to fill the buffer like this:
Position: 7 6 5 4 3 2 1 0  (bit positions in a byte)
Buffer:   [. . . . . . . .]

First bit goes to position 7 (leftmost/MSB)
Second bit goes to position 6
Third bit goes to position 5
... and so on

```

### The Formula

```go
buffer |= (1 << (7 - position))

```

Let's break this down:

**Part 1: `(7 - position)`** - Calculate where to place the bit

```
position = 0 → place at (7-0) = 7 (leftmost)
position = 1 → place at (7-1) = 6
position = 2 → place at (7-2) = 5
position = 3 → place at (7-3) = 4
...
position = 7 → place at (7-7) = 0 (rightmost)

```

**Part 2: `1 << (7 - position)`** - Create a bit mask at that position

```
1 << 7 = 0b10000000  (bit at position 7)
1 << 6 = 0b01000000  (bit at position 6)
1 << 5 = 0b00100000  (bit at position 5)
1 << 4 = 0b00010000  (bit at position 4)

```

**Part 3: `buffer |= ...`** - Add that bit to the buffer

### Complete Example: Writing Bits "1", "0", "1"

### Initial State

```
buffer = 0b00000000
position = 0

```

### Write First Bit: "1"

```go
WriteBit(1):

Step 1: Calculate position
7 - position = 7 - 0 = 7

Step 2: Create mask at position 7
1 << 7 = 0b10000000

Step 3: OR with buffer
buffer |= 0b10000000

  0b00000000  (current buffer)
| 0b10000000  (mask)
-------------
  0b10000000  (new buffer)
  ^
  position 7 is now 1

position++  → position = 1

```

Visual:

```
Position: 7 6 5 4 3 2 1 0
Buffer:   [1 . . . . . . .]
           ↑
        Just set!

```

### Write Second Bit: "0"

```go
WriteBit(0):

Step 1: Calculate position
7 - position = 7 - 1 = 6

Step 2: Bit is 0, so we DON'T set anything
(If bit is 0, we skip the OR operation)

buffer stays: 0b10000000
position++  → position = 2

```

Visual:

```
Position: 7 6 5 4 3 2 1 0
Buffer:   [1 0 . . . . . .]
             ↑
        Stayed 0 (no operation)

```

### Write Third Bit: "1"

```go
WriteBit(1):

Step 1: Calculate position
7 - position = 7 - 2 = 5

Step 2: Create mask at position 5
1 << 5 = 0b00100000

Step 3: OR with buffer
buffer |= 0b00100000

  0b10000000  (current buffer)
| 0b00100000  (mask)
-------------
  0b10100000  (new buffer)
    ^
    position 5 is now 1

position++  → position = 3

```

Visual:

```
Position: 7 6 5 4 3 2 1 0
Buffer:   [1 0 1 . . . . .]
               ↑
           Just set!

```

### Why Use OR (`|`) Instead of Assignment?

**Because we want to ADD bits without destroying existing ones.**

### Example: What if we used assignment?

```go
// WRONG APPROACH:
buffer = (1 << (7 - position))  // Assignment instead of OR

```

This would **erase** all previous bits:

```
buffer = 0b10000000  (after writing first "1")
buffer = 0b00000000  (after writing second "0" - ERASED!)
buffer = 0b00100000  (after writing third "1" - LOST FIRST BIT!)

```

### Correct Approach with OR:

```go
// CORRECT:
buffer |= (1 << (7 - position))  // OR adds bits

```

OR **accumulates** bits:

```
buffer = 0b00000000  (start)
buffer = 0b10000000  (after OR with 0b10000000)
buffer = 0b10000000  (after skipping 0 bit)
buffer = 0b10100000  (after OR with 0b00100000)

```

### Visual: How OR Works

```
Current buffer: 0b10000000
New bit mask:   0b00100000
OR operation:   ↓

  0b10000000
| 0b00100000
-------------
  0b10100000  ← Both bits are preserved!

```

The OR operation:

- Keeps all existing `1`s
- Adds new `1`s
- Doesn't affect `0`s

### Complete Flow Visualization

```
Writing code "101" (3 bits):

Start:
Position: 7 6 5 4 3 2 1 0
Buffer:   [0 0 0 0 0 0 0 0]

Write bit "1" at position 0:
  Shift: 1 << 7 = 0b10000000
  OR:    buffer |= 0b10000000
Position: 7 6 5 4 3 2 1 0
Buffer:   [1 0 0 0 0 0 0 0]

Write bit "0" at position 1:
  (skip, bit is 0)
Position: 7 6 5 4 3 2 1 0
Buffer:   [1 0 0 0 0 0 0 0]

Write bit "1" at position 2:
  Shift: 1 << 5 = 0b00100000
  OR:    buffer |= 0b00100000
Position: 7 6 5 4 3 2 1 0
Buffer:   [1 0 1 0 0 0 0 0]

Final buffer = 0b10100000 = 160

```

### Conclusion

1. **Left Shift (`1 << (7 - position)`)**: Creates a bit mask with `1` at the correct position
2. **Bitwise OR (`|=`)**: Adds the new bit to the buffer **without erasing** existing bits
3. **Why OR?**: Because `0 | 1 = 1` and `1 | 0 = 1` and `1 | 1 = 1` - it accumulates bits
4. **Result**: We build the byte from left to right, one bit at a time

The combination of shift + Bitwise OR is the standard pattern for **setting individual bits** in bit manipulation!

## Why Huffman Tree Prefix Free ?

- When generation code each code we assign to each character is only at LEAF node.
- No character in Priority Queue ( kinda Tree ) is at internal nodes but always a LEAF

### Why this gurantees that tree would be prefix free ?

Code is only asigned when we reach a leaf node 

- Once we assign a code at a leaf, we cannot go any deeper.
- different characters are at different leaves
- no leaf is ancestor of other aka no character is parent of another

```
Tree paths:
'a': Root → Left → STOP        (code: "0")
'b': Root → Right → Left → STOP (code: "10")
'c': Root → Right → Right → STOP (code: "11")

Can "0" be a prefix of "10"?
- "0" ends at 'a' (a leaf)
- To get "10", you'd need to continue from 'a'
- But 'a' is a leaf with NO children!
- So NO, "0" cannot be extended ✓

Can "0" be a prefix of "11"?
- Same logic - 'a' has no children
- So NO ✓

Can "10" be a prefix of "11"?
- "10" ends at 'b' (a leaf)
- "11" is a different path
- They don't overlap ✓
```

### An Interesting look of why its not possible in Theorem way

**Theorem:** If all codes are assigned only at leaf nodes of a binary tree, the codes are prefix-free.

**Proof:**

1. Each code corresponds to a unique path from root to a leaf
2. If code A is a prefix of code B, then A's path must be a prefix of B's path
3. That means A's leaf must be an ancestor of B's leaf
4. But leaves have no children, so they can't be ancestors
5. Therefore, no code can be a prefix of another

#### BitReader Code Explanation
```go

package internal

import "io"

type BitReader struct {
	reader      io.Reader // where to read bytes from
	currentByte byte      // Current byte being read
	bitPosition int       // position in current byte (0-7)
	finished    bool      // No more data to read
}

func NewBitReader(reader io.Reader) *BitReader {
	return &BitReader{
		reader:      reader,
		currentByte: 0,
		bitPosition: 8, // Start at 8 to trigger first read
		finished:    false,
	}
}
```
- Explanation for what we do in bitValue code in bitReader.go to extract a bit from byte we receive.
![[Pasted image 20251013211746.png]]

- [ ] How are we sure that while looping in decompress we wont visit same character twice 
The reason it does not visit same place is because we are reading byte values in binary and they can never be same and would always be unique.