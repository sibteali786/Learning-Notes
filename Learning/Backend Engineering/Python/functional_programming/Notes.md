```
Immutability

In FP, we strive to make data immutable. Once a value is created, it cannot be changed. Mutable data, on the other hand, can be changed after it's created.
Who Cares?

Immutable data is easier to think about and work with. When 10 different functions have access to the same variable, and you're debugging a problem with that variable, you have to consider the possibility that any of those functions could have changed the value.

When a variable is immutable, you can be sure that it hasn't changed since it was created. It's a helluva lot easier to work with.

Generally speaking, immutability means fewer bugs and more maintainable code.
Tuples vs. Lists

Tuples and lists are both ordered collections of values, but tuples are immutable and lists are mutable.

You can append to a list, but you can not append to a tuple. You can create a new copy of a tuple using values from an existing tuple, but you can't change the existing tuple.
Lists Are Mutable

ages: list[int] = [16, 21, 30]
# 'ages' is being changed in place
ages.append(80)
# [16, 21, 30, 80]

Tuples Are Immutable

ages: tuple[int, ...] = (16, 21, 30)
# note the comma after 80! It's required for a single-element tuple
more_ages: tuple[int, ...] = (80,)
# 'all_ages' is a brand new tuple
all_ages: tuple[int, ...] = ages + more_ages
# (16, 21, 30, 80)

# or we can even reassign the same variable to point to a new tuple:
ages = ages + more_ages
# (16, 21, 30, 80)

The ... in tuple[int, ...] means the tuple can contain any number of int values.
Assignment

The add_prefix function accepts 2 arguments:

    "document": a string
    "documents": the current tuple of strings

It should do 2 things:

    Add a prefix of X. to the beginning of the new document, where X is the next index in the tuple. (The first document should be 0. , next should be 1. , etc.)
    Return the documents tuple with the new document added to the end.

You don't need to write any loops yourself. The provided test code will call add_prefix() multiple times in a loop, gradually building up the documents tuple for you.

    Run the code to see the error. Whoever wrote this code assumed that documents is a list, but it's a tuple!
    Fix the bug. Instead of attempting to mutate the input tuple, create a brand new tuple with the new document added to the end and return that.


```

first lesson and its code

```python
def add_prefix(document: str, documents: tuple[str, ...]) -> tuple[str, ...]:
    prefix = f"{len(documents)}. "
    new_doc: tuple[str, ...] = (prefix + document,)
    documents = documents + new_doc
    return documents

```

```
Declarative Programming

Click to hide video
Your browser does not support playing HTML5 video. You can instead. Here is a description of the content: Declarative code

Functional programming aims to be declarative. We prefer to declare what we want the computer to do, rather than muck around with the details of how to do it.

Let's take an extreme example and pretend we wanted to style a webpage with CSS. (Obviously a hypothetical because, well, why would anyone want to work on the frontend???)
Declarative Styling

The following CSS changes all button elements to have red text:

button {
  color: red;
}

It does not execute line-by-line like an imperative language. Instead, it simply declares the desired style, and it's up to a web browser to figure out how to apply and display it.
Imperative Styling

Unlike functional programming (and CSS), a lot of code is imperative. We write out the exact step-by-step implementation details. This Python script draws a red button on a screen using the Tkinter library:

from tkinter import Button, Tk # first, import the library
master: Tk = Tk() # create a window
master.geometry("200x100") # set the window size
button: Button = Button(master, text="Submit", fg="red") # create a button
button.pack()
master.mainloop() # start the event loop

```

```
It's Math

Functional programming tends to be popular among developers with a strong mathematical background. After all, a math equation isn't procedural – it's declarative. Take the following equation:

avg = Σx/N

To put this calculation in plain English:

    Σ is just the Greek letter Sigma, and it represents "the sum of a collection."
    x is the collection of numbers we're averaging.
    N is the number of elements in the collection.
    avg is equal to the sum of all the numbers in collection x divided by the number of elements in collection x.

So, the equation really just says that avg is the average of all the numbers in collection x. This math equation is a declarative way of writing "calculate the average of a list of numbers." Here's some imperative Python code that does the same thing:

def get_average(nums: list[int]) -> float:
    total = 0
    for num in nums:
        total += num
    return total / len(nums)

However, with functional programming, we would write code that's a bit more declarative:

def get_average(nums: list[int]) -> float:
    return sum(nums) / len(nums)

Here we're not keeping track of state (the total variable in the first example is "stateful"). We're simply composing functions together to get the result we want.
Assignment

In the world of document conversion, we sometimes need to handle fonts and font sizes.

Complete the get_median_font_size function. Given a list of numbers representing font sizes, return the median of the list.

For example:

[1, 2, 3] => 2
[10, 8, 7, 5] => 7

    Notice the second list is out of order. Sort the list so that it's in ascending order, then find the middle index, and return the middle number.
    If there's an even amount of numbers, return the smaller of the two middle numbers (I know it's not a true median, but it's good for our purposes).
    If the list is empty, just return None.

Here are some helpful docs:

    sorted
    len
    // (floor division)

To be a good little functional programmer, your code for this lesson should not:

    Use loops
    Mutate any variables (it's okay to create new ones)


```

code

```
def get_median_font_size(font_sizes: list[int]) -> int | None:
    if len(font_sizes) == 0:
        return None

    sorted_font_sizes = sorted(font_sizes)
    middle_index = len(font_sizes)//2
    if len(font_sizes) % 2 == 0:
        return sorted_font_sizes[middle_index - 1]
    else:
        return sorted_font_sizes[middle_index]
```

```
Classes vs. Functions

I run into new developers who, after learning about classes, want to use them everywhere. They assume that because they learned about functions first, functions are somehow inferior.

Nope. They're just different.
Should I Use Functions or Classes?

Here's my rule of thumb:

If you're unsure, default to functions. I find myself reaching for classes when I need something long-lived and stateful that would be easier to model if I could share behavior and data structure via inheritance. This is often the case for:

    Video games
    Simulations
    GUIs

The difference is:

    Classes encourage you to think about the world as a hierarchical collection of objects. Objects bundle behavior, data, and state together in a way that draws boundaries between instances of things, like chess pieces on a board.

    Functions encourage you to think about the world as a series of data transformations. Functions take data as input and return a transformed output. For example, a function might take the entire state of a chess board and a move as inputs, and return the new state of the board as output.

Use what feels right to you in your projects, and adjust and refactor as you improve your skills.

```

```
Debugging FP

It's nearly impossible, even for tenured senior developers, to write perfect code the first time. That's why debugging is such an important skill. The trouble is, sometimes you have these "elegant" (sarcasm intended) one-liners that are tricky to debug:

def get_player_position(
    position: float, velocity: float, friction: float, gravity: float
) -> float:
    return calc_gravity(calc_friction(calc_move(position, velocity), friction), gravity)

If the output of get_player_position is incorrect, it's hard to know what's going on inside that black box. Break it up! Then you can inspect the moved, slowed, and final variables more easily:

def get_player_position(
    position: float, velocity: float, friction: float, gravity: float
) -> float:
    moved = calc_move(position, velocity)
    slowed = calc_friction(moved, friction)
    final = calc_gravity(slowed, gravity)
    print("Given:")
    print(f"position: {position}, velocity: {velocity}, friction: {friction}, gravity: {gravity}")
    print("Results:")
    print(f"moved: {moved}, slowed: {slowed}, final: {final}")
    return final

Once you've run it, found the issue, and solved it, you can remove the print statements.
Assignment

Fix the format_line function. It should apply the following transformations in order:

    Strip whitespace from the beginning and end of the line.
    Capitalize every character in the line.
    Remove any periods from the line.
    Append an ellipsis ... to the end of the line: words go here...

Run the code. You should see that some subtle bugs are present.

Break up the function to make it easier to debug. Use print() statements to see what's going on at each step.
Tips

Be careful about whitespace! It's easy to miss in console output. I sometimes add a character, like a | to the beginning and end of a string to make whitespace more obvious when print debugging.

    .replace(old, new) can be used to replace all occurrences of a character in a string.
    .upper() capitalizes an entire string, .capitalize() capitalizes the first letter.
    .strip() removes whitespace from the beginning and end of a string, .lstrip() and .rstrip() remove whitespace from the left and right respectively.

```
code

```python
def format_line(line: str) -> str:
    # return f"{line.rstrip().capitalize().replace(',', '')}...."
    stripped_whitespace = line.strip()
    capitalized = stripped_whitespace.upper()
    strip_periods = capitalized.replace(".", "")
    ellipsis_appended = strip_periods + "..." 
    return ellipsis_appended
```

Functional vs. OOP

Functional programming and object-oriented programming are styles for writing code. One isn't inherently superior to the other, but to be a well-rounded developer you should understand both well and use ideas from each when appropriate.

You'll encounter developers who love functional programming and others who love object-oriented programming. However, contrary to popular opinion, FP and OOP are not always at odds with one another. They aren't opposites. Of the four pillars of OOP, inheritance is the only one that doesn't fit with functional programming.

Inheritance isn't seen in functional code due to the mutable classes that come along with it. Encapsulation, polymorphism and abstraction are still used all the time in functional programming.

When working in a language that supports ideas from both FP and OOP (like Python, JavaScript, or Go) the best developers are the ones who can use the best ideas from both paradigms effectively and appropriately.

Statements vs. Expressions

Studying functional programming is really about returning to the most basic aspects of programming and looking at them in a new way. Statements and expressions are a great example of that.
Statements

"Statements" are actions to be carried out. For example:

    "Set n to 7"
    "Define a function named greet"
    "If x > 10, print a greeting to Alice"

In Python, such statements look like this:

n: int = 7  # Variable assignment statement

def greet(name: str) -> str:  # Function definition statement
    return f"Hello, {name}!"

i

def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    print("Hex Color",hex_color)
    if is_hexadecimal(hex_color) == False or len(str(hex_color)) != 6 :
        raise Exception("not a hex color string")
    else:
        r = int(hex_color[:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:], 16)
        return r, g, b
        
    


# Don't edit below this line


def is_hexadecimal(hex_string: str) -> bool:
    try:
        int(hex_string, 16)
        return True
    except Exception:
        return False
```

def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    print("Hex Color",hex_color)
    if is_hexadecimal(hex_color) == False or len(str(hex_color)) != 6 :
        raise Exception("not a hex color string")
    else:
        r = int(hex_color[:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:], 16)
        return r, g, b
        
    


# Don't edit below this line


def is_hexadecimal(hex_string: str) -> bool:
    try:
        int(hex_string, 16)
        return True
    except Exception:
        return False
```f x > 10:  # `if` statement
    print(greet("Alice"))

for i in range(n):  # `for` loop statement
    print(i)

Every complete instruction is a statement.
Expressions

Expressions are a subset of statements that produce values. Evaluating an expression results in a value that can be used in whatever way is needed. It can be assigned to a variable, returned from a function, etc.

result: int = 2 + 2  # Arithmetic expression
length: int = len("hello")  # Function call expression
total_cost: float = len(items) * cost  # Multiple expressions combined into one

One thing that may surprise you is that, in most languages (including Python), every function call is an expression. When you call a function, it returns a value – whether or not you realize it or do anything with that value.

Even if a Python function doesn't have a return statement, it still implicitly returns None. You can test this by assigning a print call to a variable:

x: None = print("hello")  # hello
print(x)                  # None

Sure enough: print, the first function we all learn, technically returns a value.
Expressions Over Statements

Because expressions always produce values, they're reusable and declarative. You can compose expressions and nest them within each other – but you can't always do that with other kinds of statements.

Functional programming encourages the use of expressions over statements where possible, because expressions tend to minimize side effects, and make the code easier to reason about. For example, a function that returns a sum is an expression:

total: int = sum([1, 2, 3, 4])

We can get the same result with a loop, but that involves a series of statements:

total: int = 0
for n in [1, 2, 3, 4]:
    total += n

Again, it's simple to combine expressions:

print(sum([1, 2, 3, 4]) * 2)  # 20

But we can't really do the same thing with our series of statements:

# This doesn't work!
print((
total = 0
for n in [1, 2, 3, 4]:
    total += n
) * 4)

Expressions tend to be concise and logically pure. Some languages that are designed for functional programming, like Haskell, treat everything as an expression. In those languages, even control flow constructs like if and case are expressions that return values.

Ternary Expressions

Ternaries are a great way to reduce a series of statements, like an if/else block, to a single expression. When you first learned how to use conditional logic in Python, it probably looked like this:

result: float = 0
if number % 2 == 0:
    result = number / 2
else:
    result = (number * 3) + 1

This code sets result to a dummy value like 0 (None would also work), then overwrites it with its "real" value based on the condition. A ternary lets us do all that in one expression:

result: float = number / 2 if number % 2 == 0 else (number * 3) + 1

Note that we also avoided mutating the result variable! Ternary expressions are good for maintaining immutability.

The syntax for a ternary in Python is:

value_a if condition else value_b

This qualifies as an expression because it's a single statement that evaluates to a value – one of two values, depending on the condition.
When to Use Ternaries

Ternary expressions are cool, but don't overdo it. If you're dealing with complex conditional logic, it's often easier to work with full if/else blocks than to try to nest ternaries inside each other.

msg: str = (
    "Access granted"
    if (
        user.is_authenticated
        and (user.role == "admin" or (user.role == "editor" and not user.suspended))
    )
    else ("Access limited" if user.is_authenticated else "Access denied")
)

Assignment

Our Doc2Doc utility is designed to accept input documents in a variety of formats. It chooses the appropriate parser for a document based on the extension of the file name. Currently, only Markdown and plain-text parsers are supported.

Fix the choose_parser function. The logic is correct, but we want to simplify the conditional block to a one-line ternary expression.

Functions Practice

Doc2Doc should seamlessly convert hex triplet color codes to RGB values. Hex colors are an efficient means of representing color with only 6 characters. RGB values combine red, green and blue light to electronically display the entire color spectrum.
Assignment

Debug the hex_to_rgb function. hex_to_rgb should take a hex triplet color code and return three integers for the RGB values using int().

    Some of the arguments passed to int() on lines 4, 5, and 6 are incorrect. Review the linked documentation to see how to convert hexadecimal (base 16) values.
    Use the provided is_hexadecimal function inside of hex_to_rgb to check if hex_color is a valid hexadecimal string.
    If the input is not six characters long or is not a valid hex string, raise the exception "not a hex color string".

Example:

red_val: int
green_val: int
blue_val: int
red_val, green_val, blue_val = hex_to_rgb("A020F0")

print(red_val)
# prints 160

print(green_val)
# prints 32

print(blue_val)
# prints 240

code 

```python

def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    print("Hex Color",hex_color)
    if is_hexadecimal(hex_color) == False or len(str(hex_color)) != 6 :
        raise Exception("not a hex color string")
    else:
        r = int(hex_color[:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:], 16)
        return r, g, b
        
    


# Don't edit below this line


def is_hexadecimal(hex_string: str) -> bool:
    try:
        int(hex_string, 16)
        return True
    except Exception:
        return False
```
Functions As Values

In Python, functions are just values, like strings, integers, or objects. For example, we can assign an existing function to a variable:

from collections.abc import Callable

def add(x: int, y: int) -> int:
    return x + y

# assign the function to a new variable
# called `addition`. It behaves the same
# as the original `add` function
addition: Callable[[int, int], int] = add
print(addition(2, 5))
# 7

Callable is the type hint for a function. Callable[[int, int], int] means a function that takes two ints as arguments and returns an int.
Assignment

With the popularity of generative AI (like ChatGPT), we need to be able to convert files into pure text to be injected into prompts.

Complete the file_to_prompt function. It should take a file dictionary and a to_string function as inputs and return a formatted string. to_string converts a dictionary into a string.

    Pass the file dictionary to the to_string function to convert file to a string and assign it to a new variable.

    Wrap the result of the to_string function in triple backticks (```) to format it as a code block in Markdown. For example:

    an example string

    should become:

    ```
    an example string
    ```

    Including the newlines!

Tip

Notice the two newlines in the example above! You don't need a trailing newline, but you do need one after the first set of backticks, and another before the second set of backticks. You can achieve this by using the newline \n escape character. Here's an example:

print("I wish the ring had never come to me.\nI wish none of this had happened.")

becomes:

I wish the ring had never come to me.
I wish none of this had happened.

```python
from collections.abc import Callable


def file_to_prompt(
    file: dict[str, str], to_string: Callable[[dict[str, str]], str]
) -> str:
    fileAsStr = to_string(file)
    result = "```\n" + fileAsStr + "\n```"
    return result

```
Anonymous Functions

Anonymous functions have no name, and in Python, they're called lambda functions after lambda calculus. Here's a lambda function that takes a single argument x and returns the result of x + 1:

lambda x: x + 1

Notice that the expression x + 1 is returned automatically, no need for a return statement. Compare that to how you'd normally write a function:

def add_one(x: int) -> int:
    return x + 1

Because functions are just values, we can assign the function to a variable named add_one:

from collections.abc import Callable

add_one: Callable[[int], int] = lambda x: x + 1
print(add_one(2))
# 3

Lambda functions might look scary, but they're still just functions. Because they simply return the result of an expression, they're often used for small, simple evaluations. Here's an example that uses a lambda to get a value from a dictionary:

get_age: Callable[[str], int | str] = lambda name: {
    "lane": 29,
    "hunter": 69,
    "allan": 17
}.get(name, "not found")
print(get_age("lane"))
# 29

Assignment

Complete the file_type_getter function. This function accepts a list of tuples, where each tuple contains:

    A "file type" (e.g. "code", "document", "image", etc.)
    A list of associated file extensions (e.g. [".py", ".js"] or [".docx", ".doc"])

The function returns a function for looking up the file type of a given file extension.

    Create an empty dictionary to map each file extension to its file type.

    Loop through the file_extension_tuples:
        Loop through the file extensions.
            Add each extension to the dictionary and assign its value to the file type.

    For example, if given the following list of tuples:

    # list of tuples
    file_extension_tuples: list[tuple[str, list[str]]] = [
        ("document", [".doc", ".docx"]),
        ("image", [".jpg", ".png"])
    ]

    # resulting dictionary
    file_extensions_dict: dict[str, str] = {
        ".doc": "document",
        ".docx": "document",
        ".jpg": "image",
        ".png": "image",
    }

    Return a lambda function that accepts a string (a file extension) and returns its file type from the dictionary.

    Use the .get dictionary method in the lambda function. Return the file type of the extension if found or "Unknown" if it's missing.

from collections.abc import Callable


def file_type_getter(
    file_extension_tuples: list[tuple[str, list[str]]],
) -> Callable[[str], str]:
    pass
    res_dict = {}
    for tuple in file_extension_tuples:
        for extension in tuple[1]:
            res_dict[extension] = tuple[0]
    get_file_type: Callable[[str], str] = lambda extension: res_dict.get(extension, "Unknown")
    return get_file_type


First-Class and Higher-Order Functions

A programming language "supports first-class functions" when functions are treated like any other variable. That means functions can be passed as arguments to other functions, can be returned by other functions, and can be assigned to variables.

    First-class function: A function that is treated like any other value
    Higher-order function: A function that accepts another function as an argument or returns a function

Python does support first-class and higher-order functions.
First-Class Example

from collections.abc import Callable

def square(x: int) -> int:
    return x * x

# Assign function to a variable
f: Callable[[int], int] = square

print(f(5))
# 25

Higher-Order Example

def square(x: int) -> int:
    return x * x

def my_map(func: Callable[[int], int], arg_list: list[int]) -> list[int]:
    result: list[int] = []
    for i in arg_list:
        result.append(func(i))
    return result

squares: list[int] = my_map(square, [1, 2, 3, 4, 5])
print(squares)
# [1, 4, 9, 16, 25]


Map

"Map," "filter," and "reduce" are three commonly used higher-order functions in functional programming.

In Python, the built-in map function takes a function and an iterable (often a list) as inputs. It returns an iterator that applies the function to every item, yielding the results.

With map, we can operate on lists without using loops and nasty stateful variables. For example, given this code:

def square(x: int) -> int:
    return x * x

nums: list[int] = [1, 2, 3, 4, 5]
squared_nums: list[int] = []
for num in nums:
    num_squared: int = square(num)
    squared_nums.append(num_squared)

print(squared_nums)
# [1, 4, 9, 16, 25]

We could use map instead, like this:

from collections.abc import Iterator

def square(x: int) -> int:
    return x * x

nums: list[int] = [1, 2, 3, 4, 5]
squared_nums: Iterator[int] = map(square, nums)

print(list(squared_nums))
# [1, 4, 9, 16, 25]

map() returns a "map object," so the list() type constructor is needed to convert it back into a standard list.
Assignment

Markdown supports two different styles of bullet points, - and *. We prefer *, so, we need a function to convert any - bullet points to * bullet points.

Complete the change_bullet_style function. It takes a document (a string) as input, and returns a single string as output. The returned string should have any lines that start with a - character replaced with a * character.

For example, this:

- This is a bullet
- This is a bullet

Becomes:

* This is a bullet
* This is a bullet

Use the built-in map function to apply the provided convert_line function to each line of the input string. Use .split() and .join() to split the document into a list of lines, and then join the lines back together. This should preserve the original line breaks. Don't use the .replace() string method.

Examples of split and join:

# my_document is a string with newlines
lines_list: list[str] = my_document.split("\n")

rejoined_doc: str = "\n".join(lines_list)

```python
def change_bullet_style(document: str) -> str:
    iterable = document.split("\n")
    converted_result = map(convert_line, iterable)
    resulting_list = list(converted_result)
    resulting_str = "\n".join(resulting_list)
    return resulting_str

# Don't edit below this line


def convert_line(line: str) -> str:
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line

```

Filter

The built-in filter function takes a function and an iterable (often a list) and returns an iterator that keeps elements from the original iterable only where the result of the function on that item returned True.

In Python:

def is_even(x: int) -> bool:
    return x % 2 == 0

numbers: list[int] = [1, 2, 3, 4, 5, 6]
evens: list[int] = list(filter(is_even, numbers))
print(evens)
# [2, 4, 6]

Assignment

Complete the remove_invalid_lines function. It accepts a document string as input. It should:

    Use the built-in filter function with a lambda to make a filtered copy of the input document.
        Remove any lines that start with a - character.
        Keep all other lines and preserve any trailing newlines (\n).
    Return the result, all on one expression.

For example, this:

* Star Wars episode 1 is underrated
- Star Wars episode 9 is fine
* Star Wars episode 3 is the best

Should become:

* Star Wars episode 1 is underrated
* Star Wars episode 3 is the best

```python
def remove_invalid_lines(document: str) -> str:
    filter_lines = lambda line: False if len(line) > 0 and line[0] == "-" else True
    lines = document.split("\n")
    filtered_doc = "\n".join(list(filter(filter_lines, lines)))
    return filtered_doc
```

Reduce

The built-in functools.reduce() function takes a function and a list of values, and applies the function to each value in the list, accumulating a single result as it goes.

# import functools from the standard library
import functools

def add(sum_so_far: int, x: int) -> int:
    print(f"sum_so_far: {sum_so_far}, x: {x}")
    return sum_so_far + x

numbers: list[int] = [1, 2, 3, 4]
sum: int = functools.reduce(add, numbers)
# sum_so_far: 1, x: 2
# sum_so_far: 3, x: 3
# sum_so_far: 6, x: 4
# 10 doesn't print, it's just the final result
print(sum)
# 10

Notice that we're passing the function add without the ()! It means that reduce will take care of execution and pass the parameters for you. Think of passing add like handing someone a recipe (the instructions), instead of the finished dish (the result of the execution).
Assignment

Complete the join and the join_first_sentences functions.

    Complete the join function. It's a helper function we'll use in join_first_sentences.
        It takes two inputs:
            A doc_so_far accumulator string – similar to the sum_so_far variable in the example above.
            A sentence string – this is the next string we want to add to the accumulator.
        Returns the result of concatenating the "doc" and "sentence" strings together, with a period and a space in between. For example:

        doc: str = "This is the first sentence"
        sentence: str = "This is the second sentence"
        print(join(doc, sentence))
        # This is the first sentence. This is the second sentence

    Complete the join_first_sentences function.
        It accepts two arguments:
            A list of sentence strings
            An integer n
        Only use the first n sentences from the list. If n is zero, just return an empty string.
        Use functools.reduce() with your join function to combine the sliced sentences into a single string.
        Add a final period without a trailing space and return this string.

Use list slicing to get the first n sentences.

Here's an example of the expected behavior:

joined: str = join_first_sentences(
    ["This is the first sentence", "This is the second sentence", "This is the third sentence"],
    2
)
print(joined)
# This is the first sentence. This is the second sentence.

```python
import functools


def join(doc_so_far: str, sentence: str) -> str:
    doc_so_far += ". " + sentence
    return doc_so_far

def join_first_sentences(sentences: list[str], n: int) -> str:
    if n == 0: 
        return ""
    first_n = functools.reduce(join,sentences[:n])
    return first_n + "."
```

Map, Filter, and Reduce Review

Higher-order functions like map, filter, and reduce allow us to avoid stateful iteration and mutation of variables.

Take a look at this imperative code that calculates the factorial of a number:

def factorial(n: int) -> int:
    # a procedure that continuously multiplies
    # the current result by the next number
    result: int = 1
    for i in range(1, n + 1):
        result *= i
    return result

Here's the same factorial function using reduce:

import functools

def factorial(n: int) -> int:
    return functools.reduce(lambda x, y: x * y, range(1, n + 1))

In the functional example, we're just combining functions to get the result we want. There's no need to reassign variables or keep track of the program's state in a loop.

A loop is inherently stateful! Depending on which iteration you're on, the i variable has a different value.

Zip

The zip function takes two iterables (often lists), and returns a new iterable where each element is a tuple containing one element from each of the original iterables.

a: list[int] = [1, 2, 3]
b: list[int] = [4, 5, 6]

c: list[tuple[int, int]] = list(zip(a, b))
print(c)
# [(1, 4), (2, 5), (3, 6)]

Assignment

Complete the pair_document_with_format function. It takes two lists of strings as input:

    doc_names: the names of documents
    doc_formats: the file formats of the documents

    zip up the lists into a single list of tuples, with the name as the first index and the format as the second index in each tuple.
    filter the list of tuples to include only tuples where the format is one of the given valid_formats.
    Return the result as a list.

```python
valid_formats: list[str] = [
    "docx",
    "pdf",
    "txt",
    "pptx",
    "ppt",
    "md",
]

# Don't edit above this line


def pair_document_with_format(
    doc_names: list[str], doc_formats: list[str]
) -> list[tuple[str, str]]:
    new_list = list(zip(doc_names, doc_formats))
    res = filter(lambda tup: tup[1] in valid_formats,new_list)
    return list(res)
```
Pure Functions

If you take nothing else away from this course, please take this: pure functions are fantastic. They have two properties:

    They always return the same value given the same arguments.
    Running them causes no side effects.

In short: pure functions don't do anything with anything that exists outside of their scope.

Your browser does not support playing HTML5 video. You can instead. Here is a description of the content: Pure functions

Example of a Pure Function

def find_max(nums: list[int]) -> float:
    max_val: float = float("-inf")
    for num in nums:
        if max_val < num:
            max_val = num
    return max_val

Example of an Impure Function

# instead of returning a value
# this function modifies a global variable
global_max: float = float("-inf")

def find_max(nums: list[int]) -> None:
    global global_max
    for num in nums:
        if global_max < num:
            global_max = num

Assignment

There's a bug in the convert_file_format function! Right now, it relies on data outside its own scope. These global values can be changed by other parts of the code, so they are not guaranteed to be the same every time convert_file_format is called.

Fix the bug by making convert_file_format a pure function. It should depend only on data that is scoped inside the function.

Don't change the signature of convert_file_format.

Pure Function Review

Pure functions have a lot of benefits. Whenever possible, good developers try to use pure functions instead of impure functions. Remember, pure functions:

    Return the same result if given the same arguments. They are deterministic.
    Do not change the external state of the program. For example, they do not change any variables outside of their scope.
    Do not perform any I/O operations (like reading from disk, accessing the internet, or writing to the console).

These properties make pure functions easier to test, debug, and think about.

Refer to the following examples to answer the questions.
Example 1

def multiply_by2(nums: list[int]) -> list[int]:
    products: list[int] = []
    for num in nums:
        products.append(num*2)
    return products

Example 2

balance: int = 1000
cars: list[str] = []

def buy_car(new_car: str) -> None:
    global balance
    cars.append(new_car)
    balance -= 69

Example 3

import random

def roll_die(num_sides: int) -> int:
    return random.randint(1, num_sides)
Pure Function Review

Pure functions have a lot of benefits. Whenever possible, good developers try to use pure functions instead of impure functions. Remember, pure functions:

    Return the same result if given the same arguments. They are deterministic.
    Do not change the external state of the program. For example, they do not change any variables outside of their scope.
    Do not perform any I/O operations (like reading from disk, accessing the internet, or writing to the console).

These properties make pure functions easier to test, debug, and think about.

Refer to the following examples to answer the questions.
Example 1

def multiply_by2(nums: list[int]) -> list[int]:
    products: list[int] = []
    for num in nums:
        products.append(num*2)
    return products

Example 2

balance: int = 1000
cars: list[str] = []

def buy_car(new_car: str) -> None:
    global balance
    cars.append(new_car)
    balance -= 69

Example 3

import random

def roll_die(num_sides: int) -> int:
    return random.randint(1, num_sides)


here 
- Example 1 is pure
- Example 2 is impure since it affect out of its scope state
- Example 3 is Impure as its output is not deterministic

Reference vs. Value

When you pass a value into a function as an argument, one of two things can happen:

    It's passed by reference: The function has access to the original value and can change it.
    It's passed by value: The function only has access to a copy. Changes to the copy within the function don't affect the original.

There is more nuance to it, but this explanation works for an introduction. In Python, the following types are passed by reference:

    Lists
    Dictionaries
    Sets

These types, on the other hand, are passed by value:

    Integers
    Floats
    Strings
    Booleans
    Tuples

Most container types are passed by reference (except for tuples!), and most basic types are passed by value.
Example of Pass-By-Reference

Lists are passed by reference and are mutable:

def modify_list(inner_lst: list[int]) -> None:
    inner_lst.append(4)
    # the original "outer_lst" is updated
    # because inner_lst is a reference to the original

outer_lst: list[int] = [1, 2, 3]
modify_list(outer_lst)
# outer_lst = [1, 2, 3, 4]

Example of Pass-By-Value

Integers are passed by value; they can be copied freely but are immutable:

def attempt_to_modify(inner_num: int) -> None:
    inner_num += 1
    # the original "outer_num" is not updated
    # because inner_num is a copy of the original

outer_num: int = 1
attempt_to_modify(outer_num)
# outer_num = 1

Assignment

We have a way for Doc2Doc users to set their supported formats in their settings. In memory, we store those settings as a simple dictionary:

settings: dict[str, bool] = {
    "docx": True,
    "pdf": True,
    "txt": False
}

Unfortunately, there's a bug in our code. When a new format is added or removed, it not only updates the new dictionary, but it changes the defaults themselves! That's not good. We want to create a new dictionary with the updates, not change the original.

Fix the bug by making add_format and remove_format pure functions that don't mutate their inputs.
Tip

Simply assigning a new variable to an existing dictionary doesn't copy that dictionary; it points to the same dictionary. Instead, use the .copy() method to create a new copy of a dictionary.

```python
def add_format(default_formats: dict[str, bool], new_format: str) -> dict[str, bool]:
    new_dict = default_formats.copy()
    new_dict[new_format] = True
    return new_dict


def remove_format(default_formats: dict[str, bool], old_format: str) -> dict[str, bool]:
    new_dict = default_formats.copy()
    new_dict[old_format] = False
    return new_dict

```
Pass by Reference Impurity

Because certain types in Python are passed by reference, we can mutate values that we didn't intend to. This is a form of function impurity!

Remember, a pure function has no side effects. It shouldn't modify anything outside of its scope, including its inputs. It should return new copies of inputs instead of changing them.
Pure Function

def remove_format(default_formats: dict[str, bool], old_format: str) -> dict[str, bool]:
    new_formats: dict[str, bool] = default_formats.copy()
    new_formats[old_format] = False
    return new_formats

Impure Function

def remove_format(default_formats: dict[str, bool], old_format: str) -> dict[str, bool]:
    default_formats[old_format] = False
    return default_formats

Why Do We Care?

One of the biggest differences between good and great developers is how often they incorporate pure functions into their code. Pure functions are easier to read, easier to reason about, easier to test, and easier to combine. Even if you're working in an imperative language like Python, you can (and should) write pure functions whenever reasonable.

There's nothing worse than trying to debug a program where the order of function calls needs to be juuuuust right because they all read and modify the same global variable.

Input and Output

Comic by xkcd.

The term "i/o" stands for input/output. In the context of writing programs, i/o refers to anything in our code that interacts with the "outside world." And "outside world" just means anything that's not stored in our application's memory (like variables).
Examples of I/O

    Reading from or writing to a file on the hard drive
    Accessing the internet
    Reading from or writing to a database
    Even simply printing to the console!!

All i/o is a form of "side effect."
Assignment

In Doc2Doc, we frequently need to change the casing of some text. For example:
TitleCase

    Every Day Once A Day Give Yourself A Present

LowerCase

    every day once a day give yourself a present

UpperCase

    EVERY DAY ONCE A DAY GIVE YOURSELF A PRESENT

There's an issue in the convert_case function; our test suite can't test its behavior because it's printing to the console (eww, a side effect) instead of returning a value. Fix the function so that it returns the correct value instead of printing it.

```python
def convert_case(text: str, target_format: str) -> str:
    if not text or not target_format:
        raise ValueError("no text or target format provided")

    if target_format == "uppercase":
        return text.upper()
    if target_format == "lowercase":
        return text.lower()
    if target_format == "titlecase":
        return text.title()
    raise ValueError(f"unsupported format: {target_format}")

```

Should I I/O?

A program that doesn't do any i/o is pretty useless. What's the point of computing something if you can't see the results?

In functional programming, i/o is viewed as dirty but necessary. We know we can't eliminate i/o from our code, so we just contain it as much as possible. There should be a clear place in your project that does nasty i/o stuff, and the rest of your code can be pure.

For example, a Python program might:

    Read a file from the hard drive as the program starts
    Run a bunch of pure functions to analyze the data
    Write the results of the analysis to another file on the hard drive at the end


No-Op

A no-op is an operation that does... nothing.

If a function doesn't return anything, it's probably impure. Apart from returning a value, the only reason for a function to exist is to perform a side effect. Otherwise it would be a no-op, right?
Example No-Op

This function performs a useless computation, since it doesn't return anything or perform a side effect. It's a no-op.

def square(x: int) -> None:
    x * x

Example Side Effect

This function lacks a return statement but performs a side effect: it changes the value of the y variable that is outside of its scope. It's impure.

y: int = 5

def add_to_y(x: int) -> None:
    global y
    y += x

add_to_y(3)
# y = 8

The global keyword tells Python to allow modification of the outer-scoped y variable.
Printing Is Impure

Even the print function (technically) has a side effect! It doesn't return anything, but it does print text to the console, which is a form of I/O.
Assignment

Fix the remove_emphasis function by making it pure. remove_emphasis takes a document with any number of lines and removes any number of * characters that are at the start or end of a word. (In case you need it, here's a primer on emphasis in Markdown.)

For example, this:

I *love* Markdown.
I **really love** Markdown.
I ***really really love*** Markdown.

Should become:

I love Markdown.
I really love Markdown.
I really really love Markdown.

    The problem is that remove_emphasis currently modifies a global variable called doc. It should instead accept a document as an argument and return a new document with emphasis removed.
    Once you've purified remove_emphasis, you can also delete the global doc variable.

Tips

The functions in this assignment use some Python built-ins that are definitely worth knowing:

    str.split – splits a string into a list of substrings based on a separator (by default, whitespace)
    str.strip – removes leading and trailing characters (by default, whitespace) from a string
    map – applies a function to every item of an iterable (like a list) and returns an iterator of the results
    join – combines an iterable of strings into a single string, with a specified separator between them

The syntax of join is simple but can be a bit counterintuitive:

# We call join as a method on the separator, not on the list of strings
" ".join(["I", "love", "Python"])
# "I love Python"

```python
def remove_emphasis(doc: str) -> str:
    lines = doc.split("\n")
    new_lines = map(remove_line_emphasis, lines)
    doc = "\n".join(new_lines)
    new_doc = doc
    return new_doc

# Don't touch below this line


def remove_line_emphasis(line: str) -> str:
    words = line.split()
    new_words = map(remove_word_emphasis, words)
    return " ".join(new_words)


def remove_word_emphasis(word: str) -> str:
    return word.strip("*")


```

Memoization

Memoization is a technical term that basically means caching (storing a copy of) the result of a computation so that we don't have to compute it again in the future. For example, take this simple function:

def add(x: int, y: int) -> int:
    return x + y

A call of add(5, 7) will always evaluate to 12. If you think about it, once we know that add(5, 7) can be replaced with 12, we can just store 12 in memory as the result value. Then, the next time we need to add(5, 7), we can look up the value instead of repeating a (potentially expensive) CPU operation.

The slower and more complex the function, the more memoization can help speed things up.

It's pronounced "memOization," not "memORization." This confused me for quite a while in college. I thought my professor just didn't speak goodly...
Assignment

Counting the words in a document can be slow, so we want to memoize it. Complete the word_count_memo function. It takes two inputs:

    A document string.
    A memos dictionary. The keys are full document strings, and the values are the word count of the document.

It should return a tuple of two values:

    The word count of the given document.
    An updated memos dictionary.

Here are the steps to follow:

    Create a .copy() of the memos dictionary.
    If the document is in the memos dictionary, just return the associated word count and the memos copy. No need to recompute the count!
    Otherwise, use the provided word_count function to count the words in the given document.
    Store the word count in the memos copy.
    Return the word count and the updated memos copy.

```python

def word_count_memo(document: str, memos: dict[str, int]) -> tuple[int, dict[str, int]]:
    memos_cpy = memos.copy()
    if document in memos_cpy:
        return (memos_cpy[document], memos_cpy)
    word_cnt = word_count(document)
    memos_cpy[document] = word_cnt
    return (word_cnt, memos_cpy)
# Don't edit below this line


def word_count(document: str) -> int:
    count = len(document.split())
    return count
```

Referential Transparency

Pure functions are always referentially transparent.

"Referential transparency" is a fancy way of saying that a function call can be replaced by its would-be return value because it's the same every time. Referentially transparent functions can be safely memoized. For example add(2, 3) can be replaced by the value 5.

The great thing about pure functions is that it's always safe to memoize them. Impure functions often can't be memoized because they might perform a side effect in addition to returning a static value, or they might return different values given the same arguments.
Should I Always Memoize?

No! Memoization is a tradeoff between memory and speed. If your function is fast to execute, it's probably not worth memoizing, because the amount of memory your program will need to store the results will go way up.

It's also a bunch of extra code to write, so you should only do it if you have a good reason.

Pure Functions Practice

Doc2Doc is customizable. New commands can be configured to use whichever function suits the user. However, the new commands are causing bugs in other parts of the application by mutating global values and other unintended side effects.
Assignment

Fix the following issues to make the functions pure:

    add_custom_command is mutating an input
    add_format is mutating an input
    save_document is mutating an input
    add_line_break has a side effect (printing to stdout) and no return value

Pure Functions Practice

Doc2Doc is customizable. New commands can be configured to use whichever function suits the user. However, the new commands are causing bugs in other parts of the application by mutating global values and other unintended side effects.
Assignment

Fix the following issues to make the functions pure:

    add_custom_command is mutating an input
    add_format is mutating an input
    save_document is mutating an input
    add_line_break has a side effect (printing to stdout) and no return value


```python


from collections.abc import Callable

default_commands: dict[str, Callable[..., object]] = {}
default_formats: list[str] = ["txt", "md", "html"]
saved_documents: dict[str, str] = {}

# Don't edit above this line


def add_custom_command(
    commands: dict[str, Callable[..., object]],
    new_command: str,
    function: Callable[..., object],
) -> dict[str, Callable[..., object]]:
    commands_cpy = commands.copy()
    commands_cpy[new_command] = function
    return commands_cpy


def add_format(formats: list[str], format: str) -> list[str]:
    formats_cpy = formats.copy()
    formats_cpy.append(format)
    return formats_cpy


def save_document(docs: dict[str, str], file_name: str, doc: str) -> dict[str, str]:
    docs_cpy = docs.copy()
    docs_cpy[file_name] = doc
    return docs_cpy

def add_line_break(line: str) -> str:
    return line + "\n\n"

```
Pure Functions Practice

Datetimes are infamously a pain in the neck for programming. One of the easier items on the long list of problems is the order of the year, month, and day in a calendar date. Most of the world uses the day-month-year format, but some insane countries use month-day-year because they want everyone else to be miserable.
Assignment

Refactor the sort_dates function. It currently uses .sort(), which modifies the list in-place (an impure operation). We want to change it to use sorted() with a custom helper function, to sort the dates chronologically without modifying the original list.

    Define a helper function named format_date outside of sort_dates.
        It should accept a single string (a date) in "MM-DD-YYYY" format (e.g. "10-14-1995").
        Inside the function, split the input string and rearrange it to return a new string in YYYYMMDD format. For example: 10-05-2023 → 20231005.
    Update the sort_dates function.
        It should accept a list of date strings.
        It should return a new sorted list using the built-in sorted() function.
        Pass your format_date function as the key parameter to sorted().

When you pass key=format_date, Python runs your helper function on every item to figure out the sort order (using the YYYYMMDD format), but it puts the original dates (MM-DD-YYYY) into the final list.

Recursion

Recursion is a famously tricky concept to grasp, but it's honestly quite simple – don't let it intimidate you! A recursive function is just a function that calls itself.

    Recursion is the process of defining something in terms of itself.

Click to hide video
Your browser does not support playing HTML5 video. You can instead. Here is a description of the content: Recursion explained

Example of Recursion

If you thought loops were the only way to iterate over a list, you were wrong! Recursion is fundamental to functional programming because it's how we iterate over lists while avoiding stateful loops. Take a look at this function that sums the numbers in a list:

def sum_nums(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    return nums[0] + sum_nums(nums[1:])

print(sum_nums([1, 2, 3, 4, 5]))
# 15

Don't break your brain on the example above! Let's break it down step by step:
1. Solve a Small Problem

Our goal is to sum all the numbers in a list, but we're not allowed to loop. So, we start by solving the smallest possible problem: summing the first number in the list with the rest of the list:

return nums[0] + sum_nums(nums[1:])

2. Recurse

So, what actually happens when we call sum_nums(nums[1:])? Well, we're just calling sum_nums with a smaller list! In the first call, the nums input was [1, 2, 3, 4, 5], but in the next call it's just [2, 3, 4, 5]. We just keep calling sum_nums with smaller and smaller lists.
3. The Base Case

So what happens when we get to the "end"? sum_nums(nums[1:]) is called, but nums[1:] is an empty list because we ran out of numbers. We need to write a base case to stop the madness.

if len(nums) == 0:
    return 0

The "base case" of a recursive function is the part of the function that does not call itself.
Recursive Calls
Step into recursive calls, hit the base case, then watch return values unwind.
Current expression
1 + sum_nums([2, 3, 4, 5])
waiting on a smaller call
Call stack
0
sum_nums([1, 2, 3, 4, 5])
waiting for sum_nums([2, 3, 4, 5])
1
sum_nums([2, 3, 4, 5])
paused until the smaller call returns
2
sum_nums([3, 4, 5])
paused until the smaller call returns
3
sum_nums([4, 5])
paused until the smaller call returns
4
sum_nums([5])
paused until the smaller call returns
5
sum_nums([])
base case: return 0
Current step
Frame 0 saves 1 and calls sum_nums([2, 3, 4, 5]).
Each recursive call works on a smaller slice of the original list.
1 / 11
Assignment

Doc2Doc can automatically generate various layouts for a page. There are a lot of possible layouts, so we need a factorial function to calculate the total number of possible layouts.

Complete the factorial_r function. It should recursively calculate the factorial of a number.

A factorial is the product of all positive integers less than or equal to a number. For example, 5! (read: "five factorial") is 5 * 4 * 3 * 2 * 1, which is 120.

```python
def factorial_r(x: int) -> int:
	if x == 0:
		return 1
	return x * factorial_r(x-1)

```

Recursion Review

– xkcd

I hate explaining jokes, but in case you don't get the comic: The joke is that the characters within the Dungeons and Dragons game are also playing their own Dungeons and Dragons game. Maybe their characters' game of DnD also has characters playing DnD, and so on, recursively forever.
Another Example

def print_chars(word: str, i: int) -> None:
    if i == len(word):
        return
    print(word[i])
    print_chars(word, i + 1)

print_chars("Hello", 0)
# H
# e
# l
# l
# o


Zipmap

Let's practice another simple recursive function.

You may not understand recursion just yet, but by following the instructions, you will begin to grasp the fundamentals.
Assignment

Within Doc2Doc we need to map certain properties from one document to properties of another document. Complete the recursive zipmap function.

It takes two lists as input and returns a dictionary where the first list provides the keys and the second list provides the values.

Example usage:

zipped: dict[str, float] = zipmap(
    ["Avatar: The Last Airbender", "Avatar (in Papyrus font)", "The Last Airbender (Live Action)"],
    [9.9, 6.1, 2.1]
)

print(zipped)
# {
#   'Avatar: The Last Airbender': 9.9,
#   'Avatar (in Papyrus font)': 6.1,
#   'The Last Airbender (Live Action)': 2.1,
# }

Here's the pseudocode:

    If either the keys or the values list is empty, return an empty dictionary (base case). This takes care of creating a dictionary.
    Recursively call zipmap on all but the first elements from keys and values.
    Add the first element of keys to the resulting dictionary, and set its value to the first element in values.
    Return the updated dictionary.


Zipmap

Let's practice another simple recursive function.

You may not understand recursion just yet, but by following the instructions, you will begin to grasp the fundamentals.
Assignment

Within Doc2Doc we need to map certain properties from one document to properties of another document. Complete the recursive zipmap function.

It takes two lists as input and returns a dictionary where the first list provides the keys and the second list provides the values.

Example usage:

zipped: dict[str, float] = zipmap(
    ["Avatar: The Last Airbender", "Avatar (in Papyrus font)", "The Last Airbender (Live Action)"],
    [9.9, 6.1, 2.1]
)

print(zipped)
# {
#   'Avatar: The Last Airbender': 9.9,
#   'Avatar (in Papyrus font)': 6.1,
#   'The Last Airbender (Live Action)': 2.1,
# }

Here's the pseudocode:

    If either the keys or the values list is empty, return an empty dictionary (base case). This takes care of creating a dictionary.
    Recursively call zipmap on all but the first elements from keys and values.
    Add the first element of keys to the resulting dictionary, and set its value to the first element in values.
    Return the updated dictionary.
```python
def zipmap(keys: list[str], values: list[float]) -> dict[str, float]:
    if len(keys) == 0 or len(values) == 0:
        return {}
    result = zipmap(keys[1:],values[1:])
    result[keys[0]] = values[0]
    return result
```

Recursion Quiz

Consider the following function (assume n is a non-negative integer):

def countdown(n: int) -> None:
    print(n)
    if n == 0:
        return
    else:
        countdown(n - 1)

Nested Sum

Recursion is hard for all new developers. If you're struggling, that's okay! Take your time. That's why we're doing a few extra practice problems.
Assignment

In Doc2Doc, users can process files or entire directories. We need to know the total size of those files and directories (measured in bytes).

Due to the nested nature of directories, we represent a root directory as a list of lists. Each list represents a directory, and each number represents the size of a file in that directory. For example, here's a directory that contains 2 files at the root level, then a nested directory with its own two files:

root: list[int | list] = [
    1,
    2,
    [3, 4]
]
print(sum_nested_list(root))
# 10

Here's a more complex example:

root
├── scripts.txt (5 bytes)
├── characters (dir)
│   ├── zuko.txt (6 bytes)
│   └── aang.txt (7 bytes)
└── seasons (dir)
    ├── season1 (dir)
    │   ├── the_avatar_returns.docx (8 bytes)
    │   └── the_southern_air_temple.docx (9 bytes)
    └── season2_notes.txt (10 bytes)

Which would be represented as:

root: list[int | list] = [
    5,
    [6, 7],
    [[8, 9], 10]
]
print(sum_nested_list(root))
# 45

Complete the sum_nested_list function. It takes a nested list of integers as input and should return the total size of all files in the list. It's a recursive function.

Here's some pseudocode to help you get started:

    Create an integer variable to keep track of the total size.
    For each item in the list (use a loop here):
        If the item is an integer, add it to the total size.
        If the item is a list, use a recursive call to sum_nested_list to get the size of that list. Add that size to the total size.
    Return the total size when you're done iterating.

```python
def sum_nested_list(lst: list[int | list]) -> int:
    total_size = 0
    for item in lst:
        if isinstance(item, int):
            total_size += item
        else:
            total_size += sum_nested_list(item)

    return total_size
```

Recursion Review

Recursion is so dang useful with tree-like structures because we don't always know how deeply they're nested. Stop and think about how you would write nested loops to traverse a tree of arbitrary depth... it's not easy, is it?

for item in tree:
    for nested_item in item:
        for nested_nested_item in nested_item:
            for nested_nested_nested_item in nested_nested_item:
                # ... WHEN DOES IT END???

I most often use recursion on tree-like problems (file systems, nested dictionaries, etc.). If I'm just iterating over a one-dimensional list, then a loop (gasp...) is typically simpler, even if it's not as "pure" in the academic sense.

Remember: the rules of functional programming are just philosophies to help you write better code, but it's not always the right tool for the job. The same goes for any programming paradigm.


Recursion on a Tree

Recursion is often used in "tree-like" structures. For example:

    Nested dictionaries
    File systems
    HTML documents
    JSON objects

That's because trees can have unknown depth. It's hard to write a series of loops because you don't know how many levels deep the tree goes.

for entry_i in directory:
    if entry_i.is_dir:
        for entry_j in entry_i:
            if entry_j.is_dir:
                for entry_k in entry_j:
                    ...

Assignment

You're responsible for a module in Doc2Doc that can scan a file system (represented in our code as nested dictionaries) and create a list of the filenames.

Complete the recursive list_files function. It accepts two arguments:

    parent_directory: A dictionary of dictionaries representing the current directory. A child directory's value is a dictionary, and a file's value is None.
    current_filepath: A string representing the current path (e.g. /dir1/dir2/filename.txt).

The function should return a list of all filepaths in the parent_directory.
Steps

    Create an empty list to store the file paths.
    Use a for loop to iterate through the keys of the parent_directory dictionary. For each:
        Use the key to create a new file path by concatenating a slash / and the key to the end of the current_filepath.
        If the value is None, the key is a filename. .append() the new file path to the list of file paths.
        Otherwise, the value is a child directory dictionary. Recursively call list_files with the child directory dictionary and the new file path.
        Use .extend() to add the results of the recursive call to the list of file paths.
    Return the list of file paths.

Example parent_directory:

parent_directory: dict[str, dict | None] = {
    "Documents": {
        "Proposal.docx": None,
        "Receipts": {
            "January": {
                "receipt1.txt": None,
                "receipt2.txt": None
            },
            "February": {
                "receipt3.txt": None
            }
        }
    },
}

Resulting list of file paths:

file_paths: list[str] = [
    "/Documents/Proposal.docx",
    "/Documents/Receipts/January/receipt1.txt",
    "/Documents/Receipts/January/receipt2.txt",
    "/Documents/Receipts/February/receipt3.txt"
]

```python

def list_files(
    parent_directory: dict[str, dict | None], current_filepath: str = ""
) -> list[str]:
    lst = []
    for key, val in parent_directory.items():
        new_file_path = current_filepath + "/" + key
        if val is None:
            lst.append(new_file_path)
        else:
            lst.extend(list_files(val, new_file_path))

    return lst

```


Dangers of Recursion

Recursion is great because it's simple and elegant (simple != easy). It's often the most straightforward way to solve a problem. But there are some dangers to be aware of:

    Stack overflow: Each function call requires a bit of memory. So, if you recurse too deeply, you can run out of "stack" memory, which will crash your program. (This is what the famous website is named after.)
    If you don't have a solid base case, you can end up in an infinite loop (which will likely lead to a stack overflow).
    Especially in a language like Python, recursion is often slower than a for loop because each function call requires some memory. Tail call optimization can help with this, but Python doesn't support it.



Recursion Practice

In Doc2Doc, we have a search function to find the longest word in a document.
Assignment

Complete the find_longest_word function without a loop. It accepts two string inputs, document and (optionally) longest_word, which is the current longest word and defaults to an empty string.

    If document is empty or contains no words, return longest_word. (This is the base case.)
    Split the string into the first word and the rest of the string.

    You can use .split with maxsplit=1 to split a string into a list of [first_word, rest_of_string].
    Check if the first word is longer than longest_word, and update that if necessary.
    If the rest of the string exists, return the result of a recursive call on it.
    If no text remains, return the longest_word.

Assume that a "word" means any series of consecutive non-whitespace characters. For example, find_longest_word("How are you?") should return the string "you?".

Review the provided tests in main_test.py to see the expected behavior, including edge cases.


```python

def find_longest_word(document: str, longest_word: str = "") -> str:
    if not document.strip():
        return longest_word

    parts = document.split(" ", maxsplit=1)
    first_word = parts[0]
    rest_of_str = parts[1] if len(parts) > 1 else ""
    
    if len(first_word) > len(longest_word):
        longest_word = first_word
    
    if rest_of_str:
        return find_longest_word(rest_of_str, longest_word)
    return longest_word
```

Recursion Practice

In Doc2Doc, we might have documents nested inside other documents, forming a kind of tree. You know how crazy .docx files can get...

Anyway, we want to find out how deeply nested a given document is.
Assignment

Complete the count_nested_levels function. It takes a dictionary of nested documents, the target document ID, and the current level of the document.

    Iterate over the nested_documents dictionary. For each:
        If the current document_id matches the target_document_id, return its level of nesting.
        Otherwise, recursively call count_nested_levels on the nested dictionary for this document_id, with the level incremented by 1.
        If the recursive call found the target_document_id's level, return it.
    If the target_document_id doesn't exist, the function should return -1.

Example

In this dictionary, the document with ID 3 is nested 2 levels deep. Document 2 is nested 1 level deep.

nested_documents: dict[int, dict] = {
    1: {
        3: {}
    },
    2: {}
}

```python
def count_nested_levels(
    nested_documents: dict[int, dict], target_document_id: int, level: int = 1
) -> int:
    for key, val in nested_documents.items():
        print("First-> ","tagretId: ", target_document_id, " ", "doucmentId:", key, " Level:",level )
        if key == target_document_id:
            return level
        else:
            level_via_recurse = count_nested_levels(val, target_document_id, level+1)
            print("Second-> ","tagretId: ", target_document_id, " ", "doucmentId:", key, " Level:",level_via_recurse )
            if level_via_recurse != -1:
                return level_via_recurse
    return -1
                

```


Function Transformations

"Function transformation" is just a concise way to describe a specific type of higher-order function. It's when a function takes a function (or functions) as input and returns a new function. Let's look at an example:

from collections.abc import Callable

def multiply(x: int, y: int) -> int:
    return x * y

def add(x: int, y: int) -> int:
    return x + y

# self_math is a higher-order function
# input: a function that takes two arguments and returns a value
# output: a new function that takes one argument and returns a value
def self_math(math_func: Callable[[int, int], int]) -> Callable[[int], int]:
    def inner_func(x: int) -> int:
        return math_func(x, x)
    return inner_func

square_func: Callable[[int], int] = self_math(multiply)
double_func: Callable[[int], int] = self_math(add)

print(square_func(5))
# prints 25

print(double_func(5))
# prints 10

The self_math function takes a function that operates on two different parameters (e.g. multiply or add) and returns a new function that operates on one parameter twice (e.g. square or double).
Assignment

Doc2Doc needs a good logging system so that users and developers alike can see what's going on under the hood. Complete the get_logger function.

It takes a formatter function as a parameter and returns a new function. Steps:

    Define a new function, logger, inside get_logger (see self_math above as an example). It accepts two strings. You can just name them first and second if you like.
    The logger function should not return anything. It should simply print the result of calling the given formatter function with the first and second strings as arguments.
    Return the new logger function.

Tip

The colon_delimit and dash_delimit functions are "formatters" that will be passed into our get_logger function by the tests. You don't need to touch them, but it's important to understand that when you call formatter() in the get_logger function, you're calling one of these functions.


```python
from collections.abc import Callable


def get_logger(formatter: Callable[[str, str], str]) -> Callable[[str, str], None]:
    def logger(first: str, second: str) -> None:
        print(formatter(first, second))
    return logger
# Don't edit below this line


def test(first: str, errors: list[str], formatter: Callable[[str, str], str]) -> None:
    print("Logs:")
    logger = get_logger(formatter)
    for err in errors:
        logger(first, err)
    print("====================================")


def colon_delimit(first: str, second: str) -> str:
    return f"{first}: {second}"


def dash_delimit(first: str, second: str) -> str:
    return f"{first} - {second}"


def main() -> None:
    db_errors: list[str] = [
        "out of memory",
        "cpu is pegged",
        "networking issue",
        "invalid syntax",
    ]
    test("Doc2Doc FATAL", db_errors, colon_delimit)

    mail_errors: list[str] = [
        "email too large",
        "non alphanumeric symbols found",
    ]
    test("Doc2Doc WARNING", mail_errors, dash_delimit)


main()

```

Transformations Review

Example of a function transformation:

from collections.abc import Callable

def multiply(x: int, y: int) -> int:
    return x * y

def add(x: int, y: int) -> int:
    return x + y

def self_math(math_func: Callable[[int, int], int]) -> Callable[[int], int]:
    # inner_func is defined inside self_math.
    # It can only be referenced directly
    # inside self_math's scope. However, it is then
    # returned and can be captured into a new variable
    # like square_func or double_func, and called that way
    def inner_func(x: int) -> int:
        return math_func(x, x)
    return inner_func

square_func: Callable[[int], int] = self_math(multiply)
double_func: Callable[[int], int] = self_math(add)

print(square_func(5))
# 25

print(double_func(5))
# 10

More Transformations

Here's some example code for you to reference as you work through the assignment:

from collections.abc import Callable

def multiply(x: int, y: int) -> int:
    return x * y

def add(x: int, y: int) -> int:
    return x + y

def self_math(math_func: Callable[[int, int], int]) -> Callable[[int], int]:
    def inner_func(x: int) -> int:
        return math_func(x, x)
    return inner_func

square_func: Callable[[int], int] = self_math(multiply)
double_func: Callable[[int], int] = self_math(add)

print(square_func(5))
# prints 25

print(double_func(5))
# prints 10

Assignment

Complete the doc_format_checker_and_converter function. It takes a conversion_function and a list of valid_formats as parameters. It should return a new function that takes two parameters of its own:

    filename: The name of the file to be converted
    content: The content (body text) of the file to be converted

    If the file extension of the filename is in the valid_formats list, then return the result of calling the conversion_function on the content.
    Otherwise, raise a ValueError with the following message:

    invalid file format

Tips

    You can use the .split() method on the filename to get the file extension. Then use the in keyword to check if a value is in a list.
    capitalize_content and reverse_content are "conversion functions" that will be passed into our doc_format_checker_and_converter function by the tests.

```python
from collections.abc import Callable


def doc_format_checker_and_converter(
    conversion_function: Callable[[str], str], valid_formats: list[str]
) -> Callable[[str, str], str]:
    def inner(filename: str, content: str):
        if filename.split(".")[1] in valid_formats:
            return conversion_function(content)
        else:
            raise ValueError("invalid file format")
    return inner

# Don't edit below this line


def capitalize_content(content: str) -> str:
    return content.upper()


def reverse_content(content: str) -> str:
    return content[::-1]

```

Why Transform?

You might be wondering:

    "When would I use function transformations in the real world?"
    "Isn't it simpler to just define functions at the top level of the code, and call them as needed?"

Good questions. To be clear, we don't just transform functions at runtime for the fun of it! We use advanced techniques like function transformation only when they make our code simpler than it would otherwise be.
Code Reusability

Creating variations of the same function dynamically can make it a lot easier to share common functionality. Take a look at this formatter function. It accepts a "pattern" and returns a new function that formats text according to that pattern:

from collections.abc import Callable

def formatter(pattern: str) -> Callable[[str], str]:
    def inner_func(text: str) -> str:
        result: str = ""
        i: int = 0
        while i < len(pattern):
            if pattern[i:i+2] == '{}':
                result += text
                i += 2
            else:
                result += pattern[i]
                i += 1
        return result
    return inner_func

Now we can create new formatters easily:

bold_formatter: Callable[[str], str] = formatter("**{}**")
italic_formatter: Callable[[str], str] = formatter("*{}*")
bullet_point_formatter: Callable[[str], str] = formatter("* {}")

And use them like this:

print(bold_formatter("Hello"))
# **Hello**
print(italic_formatter("Hello"))
# *Hello*
print(bullet_point_formatter("Hello"))
# * Hello

Closures

90% of the time, when I use function transformations, it's because I want to create a closure. We'll talk about closures in the next chapter!


Function Transformations Practice

In Doc2Doc, users are asking for a filtering feature. They want a command that has dynamic options so that they can work as quickly as possible.
Assignment

Complete the get_filter_cmd function. It takes two functions as input, filter_one and filter_two, and returns a function, filter_cmd.

filter_cmd itself should take as input two strings: content and option.

    Set the default value of the option argument to "--one".
    Complete filter_cmd so that it filters and returns the content according to the input option.
        If "--one", use filter_one.
        If "--two", use filter_two.
        If "--three", use filter_one first, then filter_two.
        If any other option is passed, raise an exception:

        invalid option

```python

from collections.abc import Callable


def get_filter_cmd(
    filter_one: Callable[[str], str], filter_two: Callable[[str], str]
) -> Callable[[str, str], str]:
    def filter_cmd(content: str, option: str = "--one") -> str:
        if option == '--one':
            return filter_one(content)
        elif option == '--two':
            return filter_two(content)
        elif option == '--three':
            first = filter_one(content)
            return filter_two(first)
        else:
            raise Exception("invalid option")
    return filter_cmd


# Don't touch below this line


def replace_bad(text: str) -> str:
    return text.replace("bad", "good")


def replace_ellipsis(text: str) -> str:
    return text.replace("..", "...")


def fix_ellipsis(text: str) -> str:
    return text.replace("....", "...")

```

Closures

A closure is a function that references variables from outside its own function body. The function definition and its environment are bundled together into a single entity.

Put simply, a closure is just a function that keeps track of some values from the place where it was defined, no matter where it's executed later on.
Example

The concatter() function returns a function called doc_builder (yay higher-order functions!) that has a reference to an enclosed doc value.

from collections.abc import Callable

def concatter() -> Callable[[str], str]:
    doc: str = ""

    def doc_builder(word: str) -> str:
        # "nonlocal" tells Python to use the 'doc'
        # variable from the enclosing scope
        nonlocal doc
        doc += word + " "
        return doc

    return doc_builder

# save the returned 'doc_builder' function
# to the new function 'harry_potter_aggregator'
harry_potter_aggregator: Callable[[str], str] = concatter()
harry_potter_aggregator("Mr.")
harry_potter_aggregator("and")
harry_potter_aggregator("Mrs.")
harry_potter_aggregator("Dursley")
harry_potter_aggregator("of")
harry_potter_aggregator("number")
harry_potter_aggregator("four,")
harry_potter_aggregator("Privet")

print(harry_potter_aggregator("Drive"))
# Mr. and Mrs. Dursley of number four, Privet Drive

When concatter() is called, it creates a new "stateful" function that remembers the value of its internal doc variable. Each successive call to harry_potter_aggregator appends to that same doc!
nonlocal

Python has a keyword called nonlocal that is required to modify a variable from an enclosing scope. Most programming languages don't require this keyword, but Python does.
Assignment

Doc2Doc needs to keep track of how many words are in a collection of documents. Complete the word_count_aggregator function.

    Define a count variable to keep track of the total number of words across all documents. Initialize it to 0.
    Define an inner function that accepts a string argument – i.e., a single document – and returns an integer value. In the inner function:
        Calculate the number of words in the input string.
        Add that word count to the total count from the outer function. You'll need to use nonlocal for this.
        Return count, i.e., the nonlocal variable.
    From the outer function, return the inner function.

word_count_aggregator essentially keeps a running total of the count variable within a closure.
Tip

I used .split() to count the number of words in each document.

```python
from collections.abc import Callable


def word_count_aggregator() -> Callable[[str], int]:
    count: int = 0
    def inner(doc: str) -> int:
        nonlocal count 
        words = doc.split(" ")
        count += len(words)
        return count
    return inner
```


Closure Review

The whole point of a closure is that it's stateful. It's a function that "remembers" the values from the enclosing scope even after the enclosing scope has finished executing.

It's as if you're saving the state of a function at a particular point in time, and then you can use and update that state later on.

from collections.abc import Callable

def concatter() -> Callable[[str], str]:
    doc: str = ""
    def inner_func(word: str) -> str:
        # "nonlocal" tells Python to use the doc
        # variable from the enclosing scope
        nonlocal doc
        doc += word + " "
        return doc
    return inner_func

harry_potter_aggregator: Callable[[str], str] = concatter()
harry_potter_aggregator("Mr.")
harry_potter_aggregator("and")
harry_potter_aggregator("Mrs.")
harry_potter_aggregator("Dursley")
harry_potter_aggregator("of")
harry_potter_aggregator("number")
harry_potter_aggregator("four,")
harry_potter_aggregator("Privet")

print(harry_potter_aggregator("Drive"))
# Mr. and Mrs. Dursley of number four, Privet Drive

That means that in many cases, closures are not pure functions. They can mutate state outside of their scope and have side effects.


Closure Practice

Remember, a closure is a function that retains the state of its environment. That makes it useful for tracking data as it changes over time, but it can come at the cost of understandability.

When not to use the nonlocal keyword: when the variable is mutable – such as a list, dictionary, or set – and you're modifying its contents rather than reassigning the variable. You only need nonlocal if you're reassigning a variable (which you must do to update immutable values like strings and integers).

Let's try a closure without nonlocal.
Assignment

Doc2Doc needs a function to manage a growing collection of documents. Complete the new_collection function. It accepts:

    initial_docs: a list of strings

The new_collection function should:

    Create a copy of initial_docs (don't modify the original list!)
    Return a new function, add_doc, that:
        Accepts a single string argument (a document to add)
        Appends that document to the copied list
        Returns the updated list

Each time you call the returned function, it should add to the same list (the closure keeps track of the list's state).
Example Usage

from collections.abc import Callable

my_collection: Callable[[str], list[str]] = new_collection(["doc1", "doc2", "doc3"])
print(my_collection("doc4"))
# ['doc1', 'doc2', 'doc3', 'doc4']
print(my_collection("doc5"))
# ['doc1', 'doc2', 'doc3', 'doc4', 'doc5']


```python
from collections.abc import Callable


def new_collection(initial_docs: list[str]) -> Callable[[str], list[str]]:
    initial_docs_cpy = initial_docs.copy()
    def add_doc(doc: str) -> list[str]:
        initial_docs_cpy.append(doc)
        return initial_docs_cpy
    return add_doc
```

Closure Practice

Doc2Doc should be able to add CSS styling to an HTML file. CSS uses selectors to identify the HTML element to add the style property. Styles are essentially a chain of keys and values.

p {
  color: red;
}

    Selector: p (targets all <p> elements)
    Property: color
    Value: red

Assignment

Complete the css_styles function. It accepts a nested dictionary (initial_styles) as input, and returns a function (add_style).

    Copy initial_styles to avoid modifying the original dictionary.

    Because we're dealing with nested dictionaries here, the .copy() method will produce a shallow copy: the outer dict is a new object, but mutating inner dicts will still affect the original one. So, you should import copy and use copy.deepcopy() instead.
    Return an add_style function that:
        Takes three string arguments: selector, property, and value. selector is a key in the initial_styles dictionary, and its value should be a dictionary.
        Checks if the selector exists in the dictionary. If not, creates a new dictionary for the selector value.
        Adds or updates the property with the given value for the selector dictionary.
        Returns the updated dictionary.

For example:

from collections.abc import Callable

initial_styles: dict[str, dict[str, str]] = {
    "body": {
        "background-color": "white",
        "color": "black"
    },
    "h1": {
        "font-size": "16px",
        "padding": "10px"
    }
}

add_style: Callable[[str, str, str], dict[str, dict[str, str]]] = css_styles(initial_styles)

new_styles: dict[str, dict[str, str]] = add_style("p", "color", "grey")

# {
#    "body": {
#        "background-color": "white",
#        "color": "black"
#    },
#    "h1": {
#        "font-size": "16px",
#        "padding": "10px"
#    },
#    "p": {
#        "color": "grey",
#    }
# }

Tip

Remember, you can assign a value to a dictionary within a dictionary like so:

parent_dictionary[nested_dictionary_key][key] = value

```python

import copy
from collections.abc import Callable

Styles = dict[str, dict[str, str]]

# Don't touch above this line


def css_styles(initial_styles: Styles) -> Callable[[str, str, str], Styles]:
    initial_styles_cpy = copy.deepcopy(initial_styles)
    def add_style(selector: str, property: str, value :str ):
        if selector not in initial_styles.keys():
            initial_styles_cpy[selector] = {}
            initial_styles_cpy[selector][property] = value
        else:
            initial_styles_cpy[selector][property] = value
        return initial_styles_cpy
    return add_style


```

Currying

Function currying is a specific kind of function transformation, where we translate a single function that accepts multiple arguments into multiple functions that each accept a single argument.

This is a "normal" 3-argument function:

box_volume(3, 4, 5)

This is a "curried" series of functions that does the same thing:

box_volume(3)(4)(5)

Here's another example that includes the implementation:

def sum(a: int, b: int) -> int:
    return a + b

print(sum(1, 2))
# prints 3

And the same thing curried:

from collections.abc import Callable

def sum(a: int) -> Callable[[int], int]:
    def inner_sum(b: int) -> int:
        return a + b
    return inner_sum

print(sum(1)(2))
# prints 3

The sum function only takes a single input, a. It returns a new function that takes a single input, b. This new function, when called with a value for b, will return the sum of a and b. We'll talk later about why this is useful.
Assignment

In Doc2Doc, for some types of text files, we need to transform the font size of the text when rendering it onscreen.

Fix the converted_font_size function. We're using a third-party code library that expects our function to be a curried series of functions that each take a single argument.

    converted_font_size should just take a single argument, font_size and return a new function.
    The returned function should take a single argument, doc_type, and return font_size multiplied by the appropriate value for the given doc_type.

You can always click the "Reset lesson" button to restore the correct font_size multipliers, if you accidentally change them.


```python
from collections.abc import Callable


def converted_font_size(font_size: int) -> Callable[[str], int]:
    def inner_doc_type(doc_type: str):
        if doc_type == "txt":
            return font_size
        if doc_type == "md":
            return font_size * 2
        if doc_type == "docx":
            return font_size * 3
        raise ValueError("invalid doc type")
    return inner_doc_type
```

Why Curry?

It's fairly obvious that:

def sum(a: int, b: int) -> int:
    return a + b

is simpler than:

from collections.abc import Callable

def sum(a: int) -> Callable[[int], int]:
    def inner_sum(b: int) -> int:
        return a + b
    return inner_sum

So why would we ever want to do the more complicated thing? Well, currying can be used to change a function's signature to make it conform to a specific shape. For example:

def colorize(converter: Callable[[str], str], doc: str) -> None:
    # ...
    converter(doc)
    # ...

The colorize function accepts a function called converter as input, and at some point during its execution, it calls converter with a single argument. That means that it expects converter to accept exactly one argument. So, if I have a conversion function like this:

def markdown_to_html(doc: str, asterisk_style: str) -> str:
    # ...

I can't pass markdown_to_html to colorize because markdown_to_html wants two arguments. To solve this problem, I can curry markdown_to_html into a function that takes a single argument:

def markdown_to_html(asterisk_style: str) -> Callable[[str], str]:
    def asterisk_md_to_html(doc: str) -> str:
        # do stuff with doc and asterisk_style...

    return asterisk_md_to_html

markdown_to_html_italic: Callable[[str], str] = markdown_to_html("italic")
colorize(markdown_to_html_italic, doc)

Currying Practice

Remember, currying is when we take a function that accepts multiple arguments:

final_volume: int = box_volume(3, 4, 5)
print(final_volume)
# 60

and convert it into a series of functions that each accept a single argument:

final_volume: int = box_volume(3)(4)(5)
print(final_volume)
# 60

    box_volume(3) returns a new function that accepts a single integer and returns a new function
    box_volume(3)(4) returns another new function that accepts a single integer and returns a new function
    box_volume(3)(4)(5) returns the final result

Here's another way of calling it, where each function is stored in a variable before being called:

with_length_3 = box_volume(3)
with_len_3_width_4 = with_length_3(4)
final_volume: int = with_len_3_width_4(5)
print(final_volume)
# 60

Here are the function definitions:

from collections.abc import Callable

def box_volume(length: int) -> Callable[[int], Callable[[int], int]]:
    def box_volume_with_len(width: int) -> Callable[[int], int]:
        def box_volume_with_len_width(height: int) -> int:
            return length * width * height
        return box_volume_with_len_width
    return box_volume_with_len

Assignment

Doc2Doc needs to be able to find the number of lines in a document that contain a specific sequence of characters. For example, given the following document:

aaaa
bbbb
ccdd
aabb

How many lines contain the sequence aa? The answer is 2: aaaa and aabb.

Complete the lines_with_sequence function. It should return a series of curried functions so it can be called like this:

num_lines: int = lines_with_sequence(char)(length)(doc)

The "sequence" is generated by the first with_char that has been provided for you. It works like this:
Character 	Length 	Sequence
"a" 	3 	"aaa"
"b" 	2 	"bb"
"*" 	4 	"****"

You need to define and return a second curried function. I called mine with_length. It should accept the final parameter, a doc string, and return the number of lines that contain the sequence.

    Define the with_length function inside the with_char function; it should accept a doc.
    Split the doc into lines.
    Use a loop (or if you're feeling fancy, import and use reduce) to count the number of lines that have the given sequence in them.
    Return the count from the with_length function.
    Return the with_length function from the with_char function.

```python
from collections.abc import Callable
from functools import reduce

def lines_with_sequence(char: str) -> Callable[[int], Callable[[str], int]]:
    def with_char(length: int) -> Callable[[str], int]:
        sequence = char * length
        def with_length(doc: str):
            splitted = doc.split("\n")
            count = 0
            for i in range(0, len(splitted)):
                if sequence in splitted[i]:
                    count+=1
            return count
        return with_length
    return with_char

```

Currying Practice

Markdown makes displaying images as simple as possible. To add an image to a Markdown document, just use this syntax:

![alt text](url "title")

    alt text: a brief description for screen readers and web scrapers; required for accessibility.
    url: a URL or relative path to the image.
    title: shown on mouse hover; optional.

Assignment

Doc2Doc makes using markdown a breeze. This includes adding images to markdown documents.

Complete the create_markdown_image function using currying. It takes a string input, alt_text.

    Enclose the alt_text in square brackets prefixed with an exclamation point: ![alt_text]
    Define an inner function that also takes a string input, url:
        The inner function should first escape any parentheses in the URL by replacing them with encoded sequences.
            Use the .replace() string method to change any opening parenthesis ( into %28.
            Do the same to change any closing parenthesis ) into %29.
        Enclose the url with parentheses: (url)
        Add the enclosed url to the end of the enclosed alt_text: ![alt_text](url)
        Define the innermost function. It should take an optional string input for the title (title=None).
            If a title is passed:
                Enclose it in double quotes.
                Add the quoted title to the image syntax by first removing the closing parenthesis ) from the end of the image syntax.
                Add a space and the quoted title with a closing parenthesis ) to the end of the image syntax: ![alt_text](url "title")
            Return the finished image syntax.
        Return the innermost function.
    Return the inner function.

Currying Practice

Doc2Doc should include a feature for image resizing, allowing users to adjust image dimensions to specified ranges. This ensures that images in documents fit and aren't freakishly large or hilariously small.
Assignment

Complete the new_resizer function using currying. It should make sure the image dimensions are never smaller than the minimum width and height, or larger than the maximum width and height specified.

Check the example below to see how the function is intended to be called.

    Define an inner function that takes two optional integer inputs, min_width and min_height, both with default values of 0.
    In the inner function:
        If min_width is more than max_width, or min_height is more than max_height, raise an exception: "minimum size cannot exceed maximum size"
        Define an innermost function that takes two integer inputs, width and height. In the innermost function:
            Use the built-in min and max functions to reduce width if it's above max_width, or to increase it if it's below min_width. (See the tip below for info about how this works.)
            Do the same for height, making sure it's between min_height and max_height.
            Return the new width and height.
        Return the innermost function.
    Return the inner function.

Example

If our new_resizer function returns a set_min_size function, and set_min_size returns a resize_image function, we would use it like this:

from collections.abc import Callable

ResizeFunc = Callable[[int, int], tuple[int, int]]
SetMinSizeFunc = Callable[..., ResizeFunc]

# Step 1: Create the resizer with maximum dimensions
set_min_size: SetMinSizeFunc = new_resizer(800, 600)

# Step 2: Set the minimum dimensions
resize_image: ResizeFunc = set_min_size(200, 100)

# Step 3: Resize the image
new_width: int
new_height: int
new_width, new_height = resize_image(1000, 500)

# Step 4: Output the result
print(new_width, new_height)  # Output: 800, 500

# With currying syntax
print(new_resizer(800, 600)(200, 100)(1000, 500))  # Output: (800, 500)

Tip

If you have a value and an upper bound, using min(value, upper_bound) returns the value capped at the upper bound, i.e., the value will be returned as is unless it exceeds the upper bound.

value: int = 50
min(value, 100)  # returns 50

value = 120
min(value, 100)  # returns 100

The opposite works for lower bounds. Just use max instead.

value: int = 50
max(value, 0)  # returns 50

value = -2
max(value, 0)  # returns 0

```python
from collections.abc import Callable

ResizeFunc = Callable[[int, int], tuple[int, int]]
SetMinSizeFunc = Callable[..., ResizeFunc]

# Don't touch above this line

def new_resizer(max_width: int, max_height: int) -> SetMinSizeFunc:
    def min_sizer(min_width: int = 0, min_height: int = 0):
        if min_width > max_width or min_height > max_height:
            raise Exception("minimum size cannot exceed maximum size")
        def image_resizer(width: int, height: int):
            width = min(width, max_width) if width > max_width else max(width, min_width)
            height = min(height, max_height) if height > max_height else max(height, min_height)
            return width, height
        return image_resizer
    return min_sizer
        

```
Decorators

Remember function transformations, where a (higher-order) function takes a function and returns a function with new behavior? Python decorators offer a kind of syntactic sugar around that. ("Syntactic sugar" just means "a more convenient syntax.")

Example:

from collections.abc import Callable


def vowel_counter(func_to_decorate: Callable[[str], None]) -> Callable[[str], None]:
    vowel_count: int = 0

    def wrapper(doc: str) -> None:
        nonlocal vowel_count
        vowels: str = "aeiou"
        for char in doc:
            if char.lower() in vowels:
                vowel_count += 1
        print(f"Vowel count: {vowel_count}")
        func_to_decorate(doc)

    return wrapper


@vowel_counter
def process_doc(doc: str) -> None:
    print(f"Document: {doc}")


process_doc("What")
# Vowel count: 1
# Document: What

process_doc("A wonderful")
# Vowel count: 5
# Document: A wonderful

process_doc("world")
# Vowel count: 6
# Document: world

The @vowel_counter line is "decorating" the process_doc function with the vowel_counter function. vowel_counter is called once when process_doc is defined with the @ syntax, but the wrapper function that it returns is called every time process_doc is called. That's why vowel_count is preserved and printed after each time.
It's Just Syntactic Sugar

Python decorators are just another (sometimes simpler) way of writing a higher-order function. These two pieces of code are identical:
With Decorator

@vowel_counter
def process_doc(doc: str) -> None:
    print(f"Document: {doc}")


process_doc("Something wicked this way comes")

Without Decorator

def process_doc(doc: str) -> None:
    print(f"Document: {doc}")


process_doc = vowel_counter(process_doc)
process_doc("Something wicked this way comes")

Assignment

The provided file_type_aggregator function is intended to decorate other functions. It assumes that the function it decorates has exactly 2 positional arguments.

Create a process_doc function that is decorated by file_type_aggregator. It should return the following string:

f"Processing doc: '{doc}'. File Type: {file_type}"

Where doc and file_type are its positional arguments. (See the line where result is assigned to func_to_decorate(doc, file_type).)

```python
from collections.abc import Callable


def file_type_aggregator(
    func_to_decorate: Callable[[str, str], str],
) -> Callable[[str, str], tuple[str, dict[str, int]]]:
    # A map of file types to their counts
    counts: dict[str, int] = {}

    def wrapper(doc: str, file_type: str) -> tuple[str, dict[str, int]]:
        counts[file_type] = counts.get(file_type, 0) + 1
        result = func_to_decorate(doc, file_type)
        return result, counts

    return wrapper


# Don't touch above this line
@file_type_aggregator
def process_doc(doc: str, file_type: str):
    return f"Processing doc: '{doc}'. File Type: {file_type}"

```
Args and Kwargs

In Python, *args and **kwargs allow a function to accept and deal with a variable number of arguments.

    *args collects positional arguments into a tuple
    **kwargs collects keyword (named) arguments into a dictionary

def print_arguments(*args: object, **kwargs: object) -> None:
    print(f"Positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")


print_arguments("hello", "world", a=1, b=2)
# Positional arguments: ('hello', 'world')
# Keyword arguments: {'a': 1, 'b': 2}

Positional Arguments

Positional arguments are the ones you're already familiar with, where the order of the arguments matters. Like this:

def sub(a: int, b: int) -> int:
    return a - b


# a=3, b=2
res: int = sub(3, 2)
# res = 1

Keyword Arguments

Keyword arguments are passed in by name. Order does not matter. Like this:

def sub(a: int, b: int) -> int:
    return a - b


res: int = sub(b=3, a=2)
# res = -1
res = sub(a=3, b=2)
# res = 1

A Note on Ordering

Any positional arguments must come before keyword arguments. This will not work:

sub(b=3, 2)

Assignment

At Doc2Doc, we need better internal debugging tools. Complete the args_logger function. It takes a variable number of positional and keyword arguments and prints them to the console.

    Print each positional argument sequentially using numbers and periods as list markers, starting with 1. . For example:

    args_logger("what's", "up", "doc")

    prints to the console:

    1. what's
    2. up
    3. doc

    Sort the keyword arguments alphabetically by key with the sorted function.

    Then print the sorted keyword arguments using asterisks (*) as list markers, and with a colon (:) between the key and value. For example:

    args_logger("hi", "there", age=17, date="July 4 1776")

    prints to the console:

    4. hi
    5. there
    * age: 17
    * date: July 4 1776

Tips

    Don't feel guilty about using loops.
    kwargs is a dictionary, not a list. My recommendation is to use the .items() method to get the key-value pairs as a list of tuples, then sort that list before printing.
    When you call sorted on a list of tuples, by default it sorts by the first item in each tuple (which is what you want here).

```python
def args_logger(*args: object, **kwargs: object) -> None:
    for i in range(0,len(args)):
        print(f"{i+1}. {args[i]}")
    sortedKargs = sorted(kwargs.items())
    for i in range(0,len(sortedKargs)):
        print(f"* {sortedKargs[i][0]}: {sortedKargs[i][1]}")
    
```

Args and Kwargs Practice

Doc2Doc should be extensible to allow for third-party plugins. These plugins will be configurable.
Assignment

Complete the configure_plugin_decorator function. It decorates a function that expects keyword arguments, but it should return a wrapper that accepts positional arguments.

The positional arguments passed to the wrapper will be key-value tuples. For example, after configure_backups is decorated, this call:

plugin_config: dict[str, str] = configure_backups(
    ("path", "~/duplicates"), ("prefix", "duplicate_"), ("extension", ".rtf")
)

should behave like this call to the original function:

plugin_config: dict[str, str] = configure_backups(
    path="~/duplicates", prefix="duplicate_", extension=".rtf"
)

And the returned plugin_config should be:

{
    "path": "~/duplicates",
    "prefix": "duplicate_",
    "extension": ".rtf",
}

    Create a wrapper function that takes positional arguments *args:
        Convert the args into a dictionary with the dict() function. Each item in args is a (key, value) tuple.
        Return the result of calling func with that dictionary unpacked as keyword arguments using the ** operator.
    Return the wrapper function.

```python
from collections.abc import Callable

PluginConfig = dict[str, str | None]
PluginFunc = Callable[..., PluginConfig]

# Don't touch above this line


def configure_plugin_decorator(func: PluginFunc) -> PluginFunc:
    def wrapper(*args: tuple[str, str]):
        argsDict = dict(args)
        print("ARGS", argsDict)
        print(*argsDict.values())
        return func(**argsDict)
    return wrapper
```

Decorators

The *args and **kwargs syntax is great for decorators that are intended to work on functions with different signatures.
Example

The log_call_count function below doesn't care about the number or the types of the decorated function's (func_to_decorate) arguments. It just wants to count how many times the function is called. However, it still needs to pass any arguments through to the wrapped function.

from collections.abc import Callable


def log_call_count(func_to_decorate: Callable[..., object]) -> Callable[..., object]:
    count: int = 0

    def wrapper(*args: object, **kwargs: object) -> object:
        nonlocal count
        count += 1
        print(f"Called {count} times")
        # Pass any and all arguments to the decorated function
        return func_to_decorate(*args, **kwargs)

    return wrapper

Callable[..., object] is the most general type hint for a function. It means "any function that takes any arguments and returns anything."
Assignment

Complete the markdown_to_text_decorator function. It can decorate a function with any number of string arguments, no matter if they're positional or keyword args. It will run the decorated function, but first strip out any Markdown heading symbols (see below for an explanation of Markdown headings).

For example, if the decorated function is called like this:

format_as_essay(title="# My Title", body="Hello", conclusion="## Done")

The wrapper should convert the keyword argument values, then call the original function like this:

format_as_essay(title="My Title", body="Hello", conclusion="Done")

The same idea applies to positional arguments:

concat("# First", "## Second")

should become:

concat("First", "Second")

markdown_to_text_decorator should return a wrapper function that takes *args and **kwargs. The wrapper should:

    Convert every positional argument in args with convert_md_to_txt.
    Convert every value in kwargs with convert_md_to_txt, while keeping each key unchanged.
    Call the decorated function with the converted positional and keyword arguments.
    Return the decorated function's result.

```python

from collections.abc import Callable


def markdown_to_text_decorator(func: Callable[..., str]) -> Callable[..., str]:
    def wrapper(*args: str, **kwargs: str) -> str:
        converted_args = tuple(convert_md_to_txt(arg) for arg in args)
        converted_kwargs = dict([(key,convert_md_to_txt(kwarg)) for key, kwarg in kwargs.items()])      
        return func(*converted_args, **converted_kwargs)
    return wrapper


# Don't touch below this line


def convert_md_to_txt(doc: str) -> str:
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")
    return "\n".join(lines)

```

LRU Cache

lru_cache from the functools module is both a decorator and an example of memoization.

LRU stands for "least recently used." It's a type of cache that stores items up to a certain size limit. When it gets full, it makes space for new items by discarding the least recently used items first. The cache can be effective because items that are used a lot – like frequently repeated calls to the same function – are less likely to be discarded. They stay in-cache.

The lru_cache decorator memoizes the inputs and outputs of the decorated function. It speeds up repeated calls to a slow function with the same inputs. A function that reads from disk, makes network requests, or requires a lot of computation could be a good candidate for LRU caching if it also sees many identical calls.

Here's an example from the Python docs that perfectly illustrates how and why to use lru_cache:

from functools import lru_cache


@lru_cache()
def factorial_r(x: int) -> int:
    if x == 0:
        return 1
    else:
        return x * factorial_r(x - 1)


factorial_r(10)  # no cached results; makes 11 recursive calls
# 3628800
factorial_r(5)  # just looks up cached result value
# 120
factorial_r(12)  # makes 2 new recursive calls; the other 11 are cached
# 479001600

Because the factorial function is recursive and the inputs are sequential numbers, it does get called repeatedly with the same inputs. Without caching, the function would be called 30 times in the code above. With lru_cache, the function is only called 13 times. You don't often need to compute factorials, but this example ties together how to use a decorator and memoization and recursion.
Assignment

The creator of Doc2Doc is a huge fan of palindromes for some nerdy reason. Add a feature to check if a word is a palindrome.

    Import the lru_cache function from the functools module and use it to decorate the incomplete is_palindrome function.
    Complete the is_palindrome function. It takes as input a word string and returns True if the word is a palindrome (such as "racecar"), or False otherwise.

Try to use recursion. Check the outer characters first, then move inwards until you reach the base case or find that the word is not a palindrome.


```python
from functools import lru_cache

@lru_cache
def is_palindrome(word: str) -> bool:
    if len(word) == 1 or word == "":
        return True
    
    left = 0
    right = len(word) - 1
    print("start:",word[left], " ", "end:", word[right])
    
    if word[left] == word[right]:
        return is_palindrome(word[left+1:right])
    else:
        return False
    
```

Decorators Practice

You can stack decorators, and you can use currying with decorators.

from collections.abc import Callable

TextFunc = Callable[[str], None]


def to_uppercase(func: TextFunc) -> TextFunc:
    def wrapper(document: str) -> None:
        func(document.upper())

    return wrapper


def get_truncate(length: int) -> Callable[[TextFunc], TextFunc]:
    def truncate(func: TextFunc) -> TextFunc:
        def wrapper(document: str) -> None:
            func(document[:length])

        return wrapper

    return truncate


@to_uppercase
@get_truncate(9)  # currying
def print_input(input: str) -> None:
    print(input)


print_input("Keep Calm and Carry On")
# prints: "KEEP CALM"

Notice that get_truncate(9) first returns a decorator, which wraps print_input. Then to_uppercase wraps that already-wrapped function. When print_input is called, the text is converted to uppercase, then truncated to 9 characters before printing.
Assignment

Doc2Doc needs a feature that can take care of encoding characters as escape sequences in HTML documents.

You might not know anything about HTML. That's fine. This assignment isn't about HTML directly.

Just understand that it's a markup language like Markdown. Certain characters are interpreted as part of HTML syntax. In order to show those characters without interpreting them, they must be escaped. For example, < is replaced with &lt;.

Complete the replacer function.

    It takes as input two strings, old and new, and returns a function, replace.
    replace takes an input function, decorated_func, and returns a wrapper function.
    wrapper takes as input a string text. It uses the .replace() string method to replace instances of old with new in the text. Then it returns the result of passing the modified text to the decorated_func.
    Use a series of calls to the replacer function to decorate tag_pre. Pass the following pairs of strings to these decorator calls to encode the escape sequences:
        Replace "&" with "&amp;".
        Replace "<" with "&lt;".
        Replace ">" with "&gt;".
        Replace '"' with "&quot;".
        Replace "'" with "&#x27;".

```python

from collections.abc import Callable

TextFunc = Callable[[str], str]

# Don't touch above this line


def replacer(old: str, new: str) -> Callable[[TextFunc], TextFunc]:
    def replace(decorated_func: TextFunc) -> TextFunc:
        def wrapper(text: str):
            text = text.replace(old, new)
            return decorated_func(text)
        return wrapper
    return replace


@replacer("&","&amp;")
@replacer("<","&lt;")
@replacer(">","&gt;")
@replacer('"',"&quot;")
@replacer("'","&#x27;")
def tag_pre(text: str) -> str:
    return f"<pre>{text}</pre>"  # Don't change the body of tag_pre

```


# Sum Types

Remember when I said, "Pure functions are my favorite part of functional programming"? Well, [sum types](https://en.wikipedia.org/wiki/Tagged_union) are a close second.

A "sum" type is the opposite of a "product" type. This Python object is an example of a _product_ type:

```py
man.studies_finance = True
man.has_trust_fund = False
```

The total number of combinations a `man` can have is `4`, the _product_ of `2 * 2`:

|studies_finance|has_trust_fund|
|---|---|
|`True`|`True`|
|`True`|`False`|
|`False`|`True`|
|`False`|`False`|

If we add a third attribute, perhaps a `has_blue_eyes` boolean, the total number of possibilities multiplies again, to `8`!

|studies_finance|has_trust_fund|has_blue_eyes|
|---|---|---|
|`True`|`True`|`True`|
|`True`|`True`|`False`|
|`True`|`False`|`True`|
|`True`|`False`|`False`|
|`False`|`True`|`True`|
|`False`|`True`|`False`|
|`False`|`False`|`True`|
|`False`|`False`|`False`|

But let's pretend that we live in a world where there are _really_ only [three types of people](https://www.youtube.com/watch?v=tEt0IuQJX2o) that our program cares about:

1. Dateable
2. Undateable
3. Maybe dateable

We can _reduce_ the number of cases our code needs to handle by using a (fake Pythonic) sum type with only 3 possible _types_:

```py
class Person:
    def __init__(self, name: str) -> None:
        self.name = name


class Dateable(Person):
    pass


class MaybeDateable(Person):
    pass


class Undateable(Person):
    pass
```

Then we can use the [isinstance](https://docs.python.org/3/library/functions.html#isinstance) built-in function to check if a `Person` is an instance of one of the subclasses. It's a clunky way to represent sum types, but hey, it's Python.

```py
def respond_to_text(guy_at_bar: Person) -> str:
    if isinstance(guy_at_bar, Dateable):
        return f"Hey {guy_at_bar.name}, I'd love to go out with you!"
    elif isinstance(guy_at_bar, MaybeDateable):
        return f"Hey {guy_at_bar.name}, I'm busy but let's hang out sometime later."
    elif isinstance(guy_at_bar, Undateable):
        return "Have you tried being rich?"
    else:
        raise ValueError("invalid person type")
```

## Sum Types vs. Product Types

As opposed to product types, which can have many (often _infinite_) combinations, sum types have a _fixed_ number of possible values. To be clear: **Python doesn't really support sum types**. We have to use a workaround and invent our own little system and enforce it ourselves.

## Assignment

Whenever a document is parsed by Doc2Doc, it can either succeed or fail. In functional programming, we often represent errors as data (e.g., the `ParseError` class) rather than by raising exceptions, because exceptions are side effects. (_This isn't standard Python practice, but it's useful to understand from an FP perspective._)

**Complete the `Parsed` and `ParseError` subclasses.**

- `Parsed` represents success. It should accept a `doc_name` string and a `text` string and save them as properties of the same name.
- `ParseError` represents failure. It should accept a `doc_name` string and an `err` string and save them as properties of the same name.

The test suite uses the `isinstance` function to see if an error occurred based on the class type.

```python
class MaybeParsed:
    pass


# Don't touch above this line


class Parsed(MaybeParsed):
    def __init__(self, doc_name: str, text: str) -> None:
        self.doc_name = doc_name
        self.text = text


class ParseError(MaybeParsed):
    def __init__(self, doc_name: str, err: str) -> None:
        self.doc_name = doc_name
        self.err = err

```

# Union Types

We can simulate the shape of sum types in Python by using classes – like our `MaybeParsed` class with subclasses named `Parsed` and `ParseError`. That's better than nothing, but it's awkward.

The [type hints](https://docs.python.org/3/library/typing.html) system in modern Python offers a more direct way of describing a value that may be one type or another. We can use what's called a [union type](https://docs.python.org/3/library/stdtypes.html#union-type):

```py
def parse_document(doc_name: str, content: str) -> Parsed | ParseError: ...
```

The `Parsed | ParseError` annotation means, "This function returns either a `Parsed` value or a `ParseError` value." Crucially, the `|` ("or") operator lets us express that relationship without forcing both classes to inherit from the same parent class. `Parsed` and `ParseError` still need to be real types, but they don't need to belong to a shared class hierarchy.

A union type can list any number of possible types for a given value. One of the most common use cases is for _optional_ values like `str | None` – i.e., a value that may be a string, or may be `None` if the string isn't available yet or couldn't be retrieved.

In functional programming, union types are used constantly to make "this or that" situations explicit: _some_ value or _none_; a _result_ from a function or an _error_.

Python is still ultimately a dynamically typed language. The union type, like other type hints, is meant to help developers and their tools (code editors, type checkers). **It's not enforced at runtime.** But being able to document the shape of your data makes it easier to write robust programs.

## Assignment

Doc2Doc needs to parse documents without throwing exceptions for ordinary failures. **Complete the `parse_document` and `display_parse_result` functions.**

1. [ ] `parse_document` accepts 2 string arguments, `doc_name` and `content`. It should return a `Parsed` value if `content` is _not_ empty:
    - `doc_name`: the provided document name
    - `text`: the provided content
2. [ ] `parse_document` should return a `ParseError` if `content` is empty:
    - `doc_name`: the provided document name
    - `err`: `"no content"`
3. [ ] `display_parse_result` accepts a `Parsed | ParseError` value and returns a string:
    - If the provided value is `Parsed`, return `Parsed <doc_name>: <N> characters`, where `<N>` is the length of the parsed text.
    - If the provided value is `ParseError`, return `Failed <doc_name>: <err>`.

## Tip

Use [`isinstance`](https://docs.python.org/3/library/functions.html#isinstance) to check which type of value you're working with.

```python
class Parsed:
    def __init__(self, doc_name: str, text: str) -> None:
        self.doc_name = doc_name
        self.text = text


class ParseError:
    def __init__(self, doc_name: str, err: str) -> None:
        self.doc_name = doc_name
        self.err = err


# Don't touch above this line


def parse_document(doc_name: str, content: str) -> Parsed | ParseError:
    if content != '':
        return Parsed(doc_name, content)
    return ParseError(doc_name, "no content")
def display_parse_result(result: Parsed | ParseError) -> str:
    if isinstance(result, Parsed):
        return f"Parsed {result.doc_name}: {len(result.text)} characters"
    if isinstance(result, ParseError):
        return f"Failed {result.doc_name}: {result.err}"
```

# Enums

So far, we've used classes to model the different cases in a sum type, and union type hints as a simpler way of describing the possible types of a value (albeit with no automatic enforcement at runtime).

If what you're trying to represent is a **fixed set of values**, you have another good option in Python's type system: [enums](https://docs.python.org/3/library/enum.html).

Click to hide video

Your browser does not support playing HTML5 video. You can instead. Here is a description of the content: Python enums

Let's say we have a `Color` variable that we want to restrict to only three possible values:

- `RED`
- `GREEN`
- `BLUE`

We could use a plain old `str` to represent these values, but that's annoying because we have to keep track of the "valid" values and defensively check for invalid ones all over our codebase. Instead, we can use an `Enum`:

```py
from enum import Enum

Color = Enum("Color", ["RED", "GREEN", "BLUE"])
print(Color.RED)  # this works, prints 'Color.RED'
print(Color.TEAL)  # this raises an exception
```

There is also a manual class-based syntax:

```py
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print(Color.RED)  # this works, prints 'Color.RED'
print(Color.TEAL)  # this raises an exception
```

The class-based syntax is more verbose, but safer because it prevents ambiguity between the variable name and the enum name. With `Color = Enum("Color", ...)`, the string `"Color"` sets the enum class name, while `Color =` assigns that class to a variable. While those names normally _shouldn't_ be different, they _can_ be.

Now `Color` is a sum type! _At least, as close as we can get in Python._ There are a few benefits:

1. A `Color` can only be `RED`, `GREEN`, or `BLUE`. If you try to use `Color.TEAL`, Python raises an exception.
2. There is a central place to see the "valid" values for a `Color`.
3. Each `Color` has a "name" (e.g. `RED`) and an integer value (e.g. `1`). The value can be useful if you need to store, compare, or serialize the enum in a specific way.

## Assignment

**Create an `Enum` called `Doctype`** with values:

- `PDF`
- `TXT`
- `DOCX`
- `MD`
- `HTML`

## Tip

Don't forget to `import` the `Enum` class from the `enum` module!

```python
from enum import Enum

class Doctype(Enum):
    PDF = 1
    TXT = 2
    DOCX = 3
    MD = 4
    HTML = 5
```

# Sum Types

Unfortunately, Python does _not_ support sum types as well as some [statically typed](https://developer.mozilla.org/en-US/docs/Glossary/Static_typing) languages.

Python [doesn't enforce](https://docs.python.org/3/library/typing.html) your types before your code runs. That's why we need this line here to `raise` an `Exception` if a color is invalid:

```py
def color_to_hex(color: Color) -> str:
    if color == Color.GREEN:
        return "#00FF00"
    elif color == Color.BLUE:
        return "#0000FF"
    elif color == Color.RED:
        return "#FF0000"
    # handle the case where the color is invalid
    raise Exception("unknown color")
```

In a language like [Rust](https://www.rust-lang.org/), which has an exceptionally rich type system, we could write the same thing like this:

```rs
fn color_to_hex(color: Color) -> String {
    match color {
        Color::Green => "#00FF00".to_string(),
        Color::Blue => "#0000FF".to_string(),
        Color::Red => "#FF0000".to_string(),
    }
}
```

Notice how there isn't any case for an unknown enum variant? That's because the Rust code will _fail to compile_ (a step that happens before the code runs at all) if the types don't line up. The Rust compiler enforces that a `Color` value can only be one of the defined variants, and the `match color` block is required to handle every variant!

**This static enforcement is a huge benefit of sum types.** It's a shame we can't get that in Python.

# Match

Let's take another look at our example [`Enum`](https://docs.python.org/3/library/enum.html) from the previous lessons:

```py
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
```

## Working With Enums

Python has a [`match` statement](https://docs.python.org/3/tutorial/controlflow.html#match-statements) that tends to be a lot cleaner than a series of `if`/`elif`/`else` statements when we're working with a fixed set of possible values (like a sum type, or more specifically an enum):

```py
def get_hex(color: Color) -> str:
    match color:
        case Color.RED:
            return "#FF0000"
        case Color.GREEN:
            return "#00FF00"
        case Color.BLUE:
            return "#0000FF"

        # default case (invalid Color)
        case _:
            return "#FFFFFF"
```

If you have _two_ values to match, you can use a `tuple`:

```py
class Shade(Enum):
    LIGHT = 1
    DARK = 2


def get_hex(color: Color, shade: Shade) -> str:
    match (color, shade):
        case (Color.RED, Shade.LIGHT):
            return "#FFAAAA"
        case (Color.RED, Shade.DARK):
            return "#AA0000"
        case (Color.GREEN, Shade.LIGHT):
            return "#AAFFAA"
        case (Color.GREEN, Shade.DARK):
            return "#00AA00"
        case (Color.BLUE, Shade.LIGHT):
            return "#AAAAFF"
        case (Color.BLUE, Shade.DARK):
            return "#0000AA"

        # default case (invalid combination)
        case _:
            return "#FFFFFF"
```

The value we want to compare is set after the `match` keyword, which is then compared against different cases/patterns. If a match is found, the code in the block is executed.

## Assignment

**Complete the `convert_format` function.** Using the enum `DocFormat`, it should support 3 types of conversions:

1. [ ] From `MD` to `HTML`:
    - Assume the content is a single `h1` tag in Markdown syntax – one string representing one line. Replace the leading `#` with an `<h1>` and add a `</h1>` to the end.
    - Example: `# This is a heading` → `<h1>This is a heading</h1>`
2. [ ] From `TXT` to `PDF`:
    - Simply add a `[PDF]` tag to the beginning and end of the content.
    - **Notice the spaces** between `[PDF]` tags and the content: `This is some text` → `[PDF] This is some text [PDF]`
3. [ ] From `HTML` to `MD`:
    - Replace any `<h1>` tags with `#` and remove any `</h1>` tags.
    - Example: `<h1>This is a heading</h1>` → `# This is a heading`
4. [ ] Any other conversion:
    - If the input format is invalid, raise an `Exception`:
    - ```text
        invalid type
        ```

```python
from enum import Enum


class DocFormat(Enum):
    PDF = 1
    TXT = 2
    MD = 3
    HTML = 4


# Don't touch above this line


def convert_format(
    content: str, from_format: DocFormat, to_format: DocFormat | None
) -> str:
    match(from_format, to_format):
        case (DocFormat.MD, DocFormat.HTML):
            content = content.replace("# ","<h1>")
            content += "</h1>"
            return content
        case (DocFormat.TXT, DocFormat.PDF):
            newContent = "[PDF] " + content + " [PDF]"
            return newContent
        case (DocFormat.HTML, DocFormat.MD):
            content = content.replace("<h1>", "# ",1)
            content = content.replace("</h1>","")
            return content
        case _:
            return "invalid type"

```


# Sum Types Practice

Doc2Doc should be able to prepare and export a CSV file of whatever data you input. CSV ([Comma-Separated Values](https://en.wikipedia.org/wiki/Comma-separated_values)) is a ubiquitous text format that allows for information to be structured in a table. There is usually a header row, followed by data rows. Within rows, items are separated by commas.

## Assignment

**Complete the `get_csv_status` function.** It should use a `match` statement to select the correct response depending on the status of the export operation. Create functions to handle each operation as follows:

1. [ ] `PENDING`: return a tuple with the string `"Pending..."` and the raw table data converted from a list of lists of anything, to a prepared list of lists of strings.
    1. [ ] Try to use nested `map` functions to convert the data items into strings.
    2. [ ] Remember to convert from a `map` object back into a list.
2. [ ] `PROCESSING`: return a tuple with the string `"Processing..."` and the prepared list of lists of strings converted to one CSV-formatted string.
    1. [ ] For each list of strings, combine the strings with `join` with commas in between to form a row.
    2. [ ] For each row string, combine the strings with `join` with newlines (`"\n"`) in between to form a table.
3. [ ] `SUCCESS`: return a tuple with the string `"Success!"` and the data as-is.
4. [ ] `FAILURE`: return a tuple with the string `"Unknown error, retrying..."` and the data after it's been prepared and processed into a CSV string, by combining the steps for `PENDING` and `PROCESSING`.
5. [ ] For any other status, raise an `Exception`:
    
    ```text
    unknown export status
    ```

## Tip

It's better if you try this challenge without using loops for practice, but you _may_ use loops.

```python
from enum import Enum
from typing import Any


class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4


RawCSVData = list[list[object]]
PreparedCSVData = list[list[str]]
CSVStatusResult = tuple[str, PreparedCSVData | str]

# Don't touch above this line


def get_csv_status(status: CSVExportStatus, data: Any) -> CSVStatusResult:
    match(status):
        case (CSVExportStatus.PENDING):
            modData = [list(map(lambda val: str(val), lst)) for lst in data]
            return ("Pending...",modData)
        case (CSVExportStatus.PROCESSING):
            row = [",".join(lst) for lst in data]
            table = "\n".join(row)
            return ("Processing...", table)
        case (CSVExportStatus.SUCCESS):
            return ("Success!", data)
        case (CSVExportStatus.FAILURE):
            modData = [list(map(lambda val: str(val), lst)) for lst in data]
            row = [",".join(lst) for lst in modData]
            table = "\n".join(row)
            return ("Unknown error, retrying...", table)
        case _:
            raise Exception("unknown export status")

```