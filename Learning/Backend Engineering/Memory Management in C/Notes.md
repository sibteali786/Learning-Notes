```table-of-contents
```

# Welcome to Memory Management

Understanding how your _software_ runs on _hardware_ is important for writing fast, performant code. In this course we'll be talking all about one of the main aspects of software performance: **memory management**.

Click to hide video

Your browser does not support playing HTML5 video. You can instead. Here is a description of the content: Welcome To Memory Management

## Goals of This Course

1. **Understand how and where programs store data in memory**. Variables, functions and objects don't get to exist for free. Where do they live as your code runs?
2. **Learn how to make programs more efficient**. Most performance related problems in backend software are memory related (at least in my experience). Learn how it all works so you can troubleshoot and optimize.
3. **Practice programming in a lower-level language**. C gets you much closer to the hardware than Python, JavaScript, or Go. By writing C, you'll learn a lot about how software works closer to the metal.
4. **Learn about garbage collection (and build your own)**. You will likely work in a garbage collected language at some point, whether that's Python, Go, JavaScript or something else. Best to understand what trade-offs are being made.

This is not a C course. We will be writing C code, and we'll cover the basics of C that you'll need, but we're focusing on memory, not C.

## Prerequisites

- **Coding experience:** You should be comfortable writing code in at least one other language, like Python, JavaScript, or Go.
- **CS Basics:** We expect that you understand basic algorithms, data structures, OOP and FP concepts.

## Building Sneklang

If you're familiar with super high-level languages, you're probably used to _not_ thinking about memory. In this course, we'll be **building the "Sneklang" programming language** (okay just little parts of it) **in C**. We will study all about manually managing memory in C, and toward the end of the course, we'll build a simple garbage collector so that Sneklang devs don't have to think too hard.

A small bit of irony here is that C was originally considered a "high-level" language when it was released. And in fact, in some ways, it still is. Modern compilers & hardware are incredibly cool and make impressive optimizations. But even so, I think there is a lot we can learn together on our Sneklang journey 😃

## Assignment

The ultimate crime has been committed. Someone's confused "Python" with "Sneklang".

Update the code to print:

```text
Starting the Sneklang interpreter...
```

Make sure to keep the `\n` newline character at the end of the print statement.
```c
#include <stdio.h>

int main() {
  printf("Starting the Sneklang interpreter...\n");
  return 0;
}

```

# C Program Structure

Click to hide video

Your browser does not support playing HTML5 video. You can instead. Here is a description of the content: Using C to learn memory management

In Python you'd do something like this:

```sh
python slow_program.py
```

The Python interpreter then executes that file top-to-bottom. If you have a `print()` at the top level, then it will print something.

The entire file is _interpreted line by line_, _but that's not how C works_.

## Simplest C Program

The simplest C program is essentially:

```c
int main() {
    return 0;
}
```

But a lot is happening here...

- A function named `main` is _always_ the entry point to a [C program](https://www.youtube.com/watch?v=tas0O586t80) (unlike Python, which enters at the top of the file).
- `int` is the return type of the function and is short for "integer". Because this is the `main` function, the return value is the [exit code](https://en.wikipedia.org/wiki/Exit_status) of the program. `0` means success, anything else means failure.
    - You'll find a lot of abbreviations in C because 1) programmers are lazy, and 2) it used to matter how many bytes your source code was.
- The opening bracket, `{` is the start of the function's body (C ignores whitespace, so indentation is just for style, not for syntax)
- `return 0` returns the `0` value (an integer) from the function. Again, this is the exit code because it's the `main` function.
    - `0` represents "nothing bad happened" as a return value.
- The pesky `;` at the end of `return 0;` is required in C to terminate statements.
- The closing bracket, `}` denotes the end of the function's body.

## Print

It feels very different coming from Python, but printing in C is done with a function called `printf` from the [`stdio.h`](https://www.ibm.com/docs/en/zos/2.4.0?topic=files-stdioh-standard-input-output) (standard input/output) library with a lot of weird formatting rules. To use it, you need an `#include` at the top of your file:

```c
#include <stdio.h>
```

Then you can use [`printf`](https://devdocs.io/c/io/fprintf) from inside a function:

```c
printf("Hello, world!\n");
```

_Notice the `\n`: it's required to print a [newline character](https://en.wikipedia.org/wiki/Newline) (and flush the buffer in the browser), which `print()` in Python does automatically._

_In case you're wondering, the `f` in `printf` stands for "print formatted"._

## Assignment

Write a small C program that prints:

```text
Program in C!
```


```c
#include <stdio.h>

int main(){
  printf("Program in C!");
  return 0;
}
```

# Interpreted Quiz

Up until now, you've probably only worked with interpreted languages on Boot.dev. Use the following interpreted (in this case, Python) code to answer the question.

```python
print("starting")
func_that_doesnt_exist("uh oh")
print("finished")
```

_Assume `func_that_doesnt_exist` is a function that truly does not exist._

# C Is Compiled

This Python code prints "starting" _before_ it crashes:

```python
print("starting")
func_that_doesnt_exist("uh oh")
print("finished")
```

But in C, it crashes _before it can even run_. If there's a problem, the compiler tells us before the program even starts.

Now... C doesn't tell us about all the possible problems (read: skill issues) that might arise in our program. But it does tell us about _some_ of them.

Click to hide video

Your browser does not support playing HTML5 video. You can instead. Here is a description of the content: which type of programming is best

## Assignment

Run the code. Notice that the "starting..." message never prints.

Fix the bug by removing the nonexistent function call.

```c
#include <stdio.h>

int main() {
  printf("starting sneklang tools\n");
  printf("finished sneklang tools\n");
  return 0;
}

```
# Comments

In C, there are two ways to write comments:

```c
// This is a single-line comment

/*
This is a multi-line comment
I can just keep adding lines
and it will still be a comment
*/
```

`/*` and `*/` are used to denote the beginning and end of a multi-line comment.

## Assignment

Looks like someone on the team doesn't know how to terminate a comment.

Fix the bug.
```c
#include <stdio.h>

int main() {
  /*
    Sneklang is for nvim enjoyers
    who want to write their own garbage
    collectors instead of using off-the-shelf
    solutions
  */
  printf("i use sneklang btw\n");
  printf("i use nvim btw\n");
  printf("i use arch btw\n");
  return 0;
}

```

# Basic Types

- `int` – An integer
- `float` – A floating point number
- `char` – A character
- `char *` – An array of characters (more on this later... if you think about it, sounds kinda like a string doesn't it?)

You've already seen `int` in the example before – it's the return value in the special `main` function (the entry point for every C program).

When declaring a variable, you must specify its type before the name and assigning a value.

## Assignment

Someone allowed a Pythonista into our beautiful C codebase!

Fix the bugs caused by missing types on lines 4, 5, and 6.

## Tip

Here's the first variable for you:

```c
int max_recursive_calls = 100;
```

```c
#include <stdio.h>

int main() {
  int max_recursive_calls = 100;
  char io_mode = 'w';
  float throttle_speed = 0.2;

  // don't touch below this line
  printf("Max recursive calls: %d\n", max_recursive_calls);
  printf("IO mode: %c\n", io_mode);
  printf("Throttle speed: %f\n", throttle_speed);
  return 0;
}
```
# Strings

Most programming languages these days (even compiled ones) have a built-in `string` type of some sort. C... doesn't.

Instead, C strings are just arrays (like lists) of characters. We'll talk more about the specifics when we talk about arrays and pointers later, but for now know that this is how you get a "string" in C:

```c
char *msg_from_dax = "You still have 0 users";
```

Very (I repeat, **very**) loosely speaking, `char *` means `string`. Also note that it is required to use double quotes `"`. Single quotes (`'`) make `char`, not `char *`.

## Assignment

Fix the bug on line 4.

```c
#include <stdio.h>

int main() {
  char *will_never_hear_again =
      "Hey TJ, when is the memory course in C gonna be done?";

  // don't touch below this line
  printf("%s\n", will_never_hear_again);
  return 0;
}

```
# Printing Variables

You've already seen me do a `printf()` magic a few times. Unfortunately, in C it isn't as easy to do string interpolation (what f-strings do in Python).

Instead of:

```python
print(f"Hello, {name}. You're {age} years old.")
```

We have to tell C _how_ we want particular values to be printed using "format specifiers".

Common [format specifiers](https://cplusplus.com/reference/cstdio/printf/#:~:text=Parameters-,format,-C%20string%20that) are:

- `%d` – digit (integer)
- `%c` – character
- `%f` – floating point number
- `%s` – string (`char *`)

```c
printf("Hello, %s. You're %d years old.\n", name, age);
```

## Newline Character

The `print()` function in Python automatically adds a [newline character](https://en.wikipedia.org/wiki/Newline) (`\n`) at the end of the string. In C, we have to do this manually.

```c
printf("Hello, world!\n");
```

## Assignment

In the space provided print:

```text
Default max threads: A
Custom perms: B
Constant pi value: C
Sneklang title: D
```

Use format specifiers to replace A-D with the already provided variables.

Do not add precision to the floating point number.

```c
#include <stdio.h>

int main() {
  int sneklang_default_max_threads = 8;
  char sneklang_default_perms = 'r';
  float sneklang_default_pi = 3.141592;
  char *sneklang_title = "Sneklang";
  // don't touch above this line

  printf("Default max threads: %d\nCustom perms: %c\nConstant pi values: %f\nSneaklang title: %s", sneklang_default_max_threads, sneklang_default_perms, sneklang_default_pi, sneklang_title);

  return 0;
}

```


# Compilation: Types

You're probably familiar with the idea of `type`s from Python, but C does them quite a bit differently.

In Python, it's OK (but still disgusting) to change the type of a variable:

```python
x = 12345
x = "wow, a new type"
x = False
x = None
x = "ok a string again :'("
```

In C, changing the type of an existing variable is not allowed:

```c
int main() {
    char *max_threads = "5";

    // call badcop
    // this is illegal
    max_threads = 5;
}
```

# Variables

As we talked about, variables cannot change _types_:

```c
int main() {
    int x = 5;
    float x = 3.14; // error
}
```

However, a variable's _value_ can change:

```c
int main() {
    int x = 5;
    x = 10; // this is ok
    x = 15; // still ok
}
```

## Assignment

Run the code. You should get a compilation error.

When updating a variable's value, you don't need to redeclare the type. In fact, you can't. Fix the code so that it updates (`64 -> 32`) properly.


```c
#include <stdio.h>

int main(){
	int sneklang_int_size = 64;
	sneklang_int_size = 32;
	printf()
}
```

# Constants

So a variable's _value_ can change:

```c
int main() {
    int x = 5;
    x = 10; // this is ok
}
```

But what if we want to create a value that _can't_ change? We can use the [`const` type qualifier](https://en.cppreference.com/w/c/language/const).

```c
int main() {
    const int x = 5;
    x = 10; // error
}
```


# Functions

In C, functions specify the types for their arguments and return value.

```c
float add(int x, int y) {
    return (float)(x + y);
}
```

- The first type, `float` is the return type.
- `add` is the name of the function.
- `int x, int y` are the parameters to the function, and their types are specified.
- `x + y` adds the two arguments together.
- `(float)` casts the result to a float.
    - We'll talk more about what [`cast`](https://en.wikipedia.org/wiki/Type_conversion) means later, and the rules for casting to and from certain types.
    - The simple version is that it instructs C to convert the result of `x + y` to a `float` value.

Here's how you would call this function:

```c
int main() {
    float result = add(10, 5);
    printf("result: %f\n", result);
    // result: 15.000000
    return 0;
}
```

It's nice that C functions enforce returning the same type from all return statements, isn't it? In Python, it can be a pain to realize that a function returns different types depending on the path it took.

## Assignment

Write a `max_sneklang_memory` function in the space provided. It should:

1. [ ] accept two arguments:
    1. [ ] `int max_threads`
    2. [ ] `int memory_per_thread`
2. [ ] return an integer representing the total memory available to the Sneklang interpreter

## Tip

Multiplication is done with the `*` operator, just like most other languages.

```c
#include <stdio.h>

int max_sneklang_memory(int max_threads, int memory_per_thread){
  return (int)(max_threads*memory_per_thread);
}

// don't touch below this line

void init_sneklang(int max_threads, int memory_per_thread) {
  printf("Initializing Sneklang\n");
  printf("Max threads: %d\n", max_threads);
  printf("Memory per thread: %d\n", memory_per_thread);
  int max_memory = max_sneklang_memory(max_threads, memory_per_thread);
  printf("Max memory: %d\n", max_memory);
  printf("====================================\n");
}

int main() {
  init_sneklang(4, 512);
  init_sneklang(8, 1024);
  init_sneklang(16, 2048);
  return 0;
}

```

# Void

In C, there's a special type for function signatures: [`void`](https://en.wikipedia.org/wiki/Void_type). There are two primary ways you'll use `void`:

To explicitly state that a function takes no arguments:

```c
int get_integer(void) {
    return 42;
}
```

When a function doesn't return anything:

```c
void print_integer(int x) {
    printf("this is an int: %d", x);
}
```

It's important to note that `void` in C is not like `None` in Python. It's not a value that can be assigned to a variable. _It's just a way to say that a function doesn't return anything or doesn't take any arguments._

# Unit Tests

Up to this point, we've been checking the standard output of your code against our expected output. Now that you're familiar with functions, most of the lessons will be graded using [unit tests](https://en.wikipedia.org/wiki/Unit_testing).

## µnit

In particular, we'll be using the [µnit (munit)](https://nemequ.github.io/munit/) testing framework. It's a simple, lightweight testing framework for C.

## Run vs. Submit

At Boot.dev, the `Run` button is for debugging. The `Submit` button mimics the idea of publishing your code for production use.

You should be debugging your code using the `Run` button. You should be adding `printf()` statements to your code to make sure it's doing what you think it's doing at different points in the code.

- Write a line to calculate a value
- `printf()` the value you calculated
- Run the code
- Did it print what you expected? If not, fix it
- Repeat

You will never lose XP or be penalized on Boot.dev for using the run button. However, there are consequences for submitting broken code, just like there are career consequences for pushing broken code to your users!

> Like how edge cases can creep up on you after shipping code to production, some test cases are only executed on `Submit`

## File Layout

Take a look at the `main.c` file. You'll notice it's read-only: you can't change the tests (that would make it too easy to cheat- ha!). It [`#include`s](https://en.wikipedia.org/wiki/Include_directive) `exercise.h` at the top.

Open `exercise.h` and you'll see the _function prototype_ (signature) of the function you need to write. In C:

- `.c` files contain the implementation (c code).
- [`.h` files](https://utat-ss.readthedocs.io/en/master/c-programming/c_h_files.html) are header files that contain the function prototypes.

To import code from another file, you include the `.h` file.

- `exercise.c` includes `exercise.h`.
- `main.c` includes `exercise.h`.

This allows `main.c` to call the functions implemented in `exercise.c`.

## Assignment

Write the `get_average` ([mathematical average](https://en.wikipedia.org/wiki/Average)) function in `exercise.c` based on the function prototype expected in `exercise.h`.

## Tips

- The `+` operator adds two numbers: `1 + 2` is `3`.
- The `/` operator divides two numbers, however:
    - if both numbers are integers, **integer division** is performed. The result will be an integer.
    - if either number is a float, **floating point division** is performed. The result will be a float.


```c
#include "exercise.h"
#include <stdio.h>

float get_average(int x, int y, int z){
  float result = (x+y+z)/3.0f;
  return result;
}
```

# Math Operators

All the same operators you'd expect exist in C:

```c
x + y;
x - y;
x * y;
x / y;
```

If you're coming from Python, `+=`, `-=`, `*=`, `/=` are all the same.

In addition, there are also the [`++` and `--` operators](https://en.cppreference.com/w/cpp/language/operator_incdec):

```c
x++; // += 1
x--; // -= 1
```

_The name of C++ is a bit of a joke by the creator, it's meant to be "incremented C" or "better C"._

These increment (`++`) and decrement (`--`) operators can be used in two forms: postfix and prefix.

**Postfix (`x++` or `x--`):** The value of `x` is used in the expression first, and then `x` is incremented or decremented. For example:

```c
int a = 5;
int b = a++; // b is assigned 5, then a becomes 6
```

**Prefix (`++x` or `--x`):** `x` is incremented or decremented first, and then the new value of `x` is used in the expression. For example:

```c
int a = 5;
int b = ++a; // a becomes 6, then b is assigned 6
```

I generally avoid prefix operators. If I want to increment a variable but keep the original value, I do that in two steps. Postfix is more common, especially in loops, which we'll get to.

## Assignment

Complete the `snek_score` function in `exercise.c`. Sneklang is unique™ in that its toolchain gives developers a "project score" that's dependent on how maintainable and "high quality" their codebase is. The larger the score, the harder it is to work in the project. The score is calculated as follows:

1. [ ] Multiply the number of files by the number of commits to get the size factor
2. [ ] Add the size factor to the number of contributors to get the complexity factor
3. [ ] Multiply the complexity factor by the average bug criticality (a number between 0 and 1) to get the final score

## Tip

You can convert an integer to a float by casting it:

```c
int x = 5;
float y = (float)x;
```


```c
float snek_score(int num_files, int num_contributors, int num_commits,
                 float avg_bug_criticality) {
  int size_factor = num_files * num_commits;
  int complexity_factor = size_factor + num_contributors;
  float final_score = complexity_factor * avg_bug_criticality;
  return final_score;
}

```

# If Statements

`if` statements are the most basic form of control flow in C: very similar to other languages. Basic syntax:

```c
if (x > 3) {
    printf("x is greater than 3\n");
}
```

`if`/`else`/`else if` are also available:

```c
if (x > 3) {
    printf("x is greater than 3\n");
} else if (x == 3) {
    printf("x is 3\n");
} else {
    printf("x is less than 3\n");
}
```

## Janky Syntax

You _can_ write an `if` statement without braces if you only have one statement in the body:

```c
if (x > 3) printf("x is greater than 3\n");
```

Buuuuut this shorthand is easy to mess up and in my opinion isn't worth saving a couple lines. **There are enough ways to shoot yourself in the foot in C already.**

## Assignment

Take a look at `exercise.h`. Write the implementation for the function prototype found there back in `exercise.c`. It should calculate whether the given temperature is too cold or too hot (it's already in Fahrenheit of course, the most reasonable scale for regular living).

1. [ ] Less than `70` `return`s "too cold".
2. [ ] More than `90` `return`s "too hot".
3. [ ] Otherwise `return` "just right".

**Do not add the `\n` to the end of the strings.** That's done at print-time.

```c
#include "exercise.h"

char *get_temperature_status(int temp){
  if (temp < 70){
    return "too cold";
  }else if(temp > 90) {
    return "too hot";
  }else {
    return "just right";
  }
}
```

# Logical Operators

Logical operators let you combine multiple conditions in C. There are three main logical operators you'll use all the time:

- `&&` – Logical `AND`: true if _both_ conditions are true
- `||` – Logical `OR`: true if _either_ condition is true
- `!` – Logical `NOT`: inverts a boolean value

```c
int age = 25;
bool has_license = true;

if (age >= 18 && has_license) {
    printf("Can drive\n");
}
```

## Short-Circuit Evaluation

C uses short-circuit evaluation with logical operators. This means:

- With `&&`, if the first condition is false, the second isn't even checked (because the whole thing is already false)
- With `||`, if the first condition is true, the second isn't checked (because the whole thing is already true)

```c
if (x != 0 && 10 / x > 2) {
    // The division only happens if x != 0
    // This prevents a division by zero error
    printf("Safe!\n");
}
```
## Operator Precedence

Logical NOT (`!`) has higher precedence than AND (`&&`), which has higher precedence than OR (`||`). When in doubt, use parentheses to make your intent crystal clear:

```c
// without parentheses – might be confusing
if (!is_raining && is_sunny || is_weekend)

// with parentheses – much clearer
if ((!is_raining && is_sunny) || is_weekend)
```

## Assignment

The Sneklang package manager needs an access control system for its private package registry. Take a look at `exercise.h` and implement the function in `exercise.c`.

The `can_access_registry` function should return `1` (true) if a user can access the private registry, or `0` (false) if they cannot.

A user can access the private registry if **any** of these conditions are met:

1. [ ] They have `is_premium` set to `1` (true)
2. [ ] They have both `reputation >= 100` AND `has_2fa` (two-factor authentication) set to `1` (true)

In C, we use `1` for true and `0` for false when returning boolean-like values from functions that return `int`.

```c
#include "exercise.h"

int can_access_registry(int is_premium, int reputation, int has_2fa){
  if (is_premium == 1 || (reputation >= 100 && has_2fa == 1)){
    return 1;
  }
  return 0;
}
```

# Ternary

Like JavaScript, C has a ternary operator:

```c
int a = 5;
int b = 10;
int max = a > b ? a : b;
printf("max: %d\n", max);
// max: 10
```

Let's break down the syntax:

```c
a > b ? a : b
```

- `a > b` is the condition
- `?` begins the "then" value
- `a` is the final value if the condition is true
- `:` separates the "else" value
- `b` is the final value if the condition is false
- The entire expression (`a > b ? a : b`) evaluates to either `a` or `b`, which is then assigned to `max` in our example.

_Ternaries are a way to write a simple if/else statement in one line._

My recommendation? **Don't use 'em**. Okay just kidding, they're fine. Just don't use them like a JS Andy on every single line to just save 3 keystrokes. I find them most useful when you are trying to set a single value to the result of some boolean expression, like `max` in the example above. Generally speaking, I think you're better served with `if` statements in C.

# Type Sizes

In C, the "size" (in memory) of a type is not guaranteed to be the same on all systems. That's because the size of a type is dependent on the system's architecture. For example, on a 32-bit system, the size of an `int` is usually 4 bytes, while on a 64-bit system, the size of an `int` can sometimes be 8 bytes – of course, you never know until you run `sizeof` with the compiler you plan on using.

However, some types are always guaranteed to be the same. Here's a list of the basic C data types along with their typical sizes in bytes. Note that sizes can vary based on the platform (e.g., 32-bit vs. 64-bit systems):

## Basic C Types and Sizes

- **`char`**
    - Size: **1 byte**
    - Represents: Single character.
    - Notes: Always 1 byte, but can be signed or unsigned.
- **`float`**
    - Size: **4 bytes**
    - Represents: Single-precision floating-point number.
- **`double`**
    - Size: **8 bytes**
    - Represents: Double-precision floating-point number.

The actual sizes of these types can be determined using the `sizeof` operator in C for a specific platform, which we'll learn about next.



# Sizeof

C gives us a way to check the size of a type or a variable: [`sizeof`](https://en.cppreference.com/w/c/language/sizeof).

You can use `sizeof` like a function (although, technically it's a [unary operator](https://en.wikipedia.org/wiki/Unary_operation), but that distinction is generally only useful for winning _super important_ internet arguments).

We'll use the `sizeof` operator in the next few lessons to give us insight into the memory layout of different types in C. This will be particularly useful as we move deeper into C, and essential for understanding pointers.

Pointers are not too bad once you understand the basics! I promise!

## `size_t`

The [`size_t` type](https://en.cppreference.com/w/c/types/size_t) is a special type that is guaranteed to be able to represent the size of the largest possible object in the target platform's address space (i.e. can fit any single, non-struct value inside of it).

It's also the type that `sizeof` returns.

## Assignment

1. [ ] First, _run_ the function to see the size of a `char`.
2. [ ] Follow the same pattern of the first print statement so that `main` also prints the size of each of the following types in order:
    - [ ] `bool`
    - [ ] `int`
    - [ ] `float`
    - [ ] `double`
    - [ ] `size_t`

_Take a look at the results before moving on!_ Notice that a `char` and `bool` only take up 1 byte (8 bits), while the other types take up more space.

```c
#include <stdbool.h>
#include <stdio.h>

int main() {
  // Use %zu for printing `sizeof` result
  printf("sizeof(char)   = %zu\n", sizeof(char));
  printf("sizeof(bool)   = %zu\n", sizeof(bool));
  printf("sizeof(int)   = %zu\n", sizeof(int));
  printf("sizeof(float)   = %zu\n", sizeof(float));
  printf("sizeof(double)   = %zu\n", sizeof(double));
  printf("sizeof(size_t)   = %zu\n", sizeof(size_t));
}

```

# For Loop

A `for` loop in C is a control flow statement for repeated execution of a block of code. Very similar to Python, but with a different syntax.

The syntax of a `for` loop in C consists of three main parts:

1. Initialization
2. Condition
3. Final-expression.

There is no "for each" (iterables) in C. For example, there is no way to do:

```python
for car in cars:
    print(car)
```

Instead, we have to iterate over the numbers of indices in a list, and then we can access the item using the index.

## Syntax

```c
for (initialization; condition; final-expression) {
    // Loop Body
}
```

## Parts of a `for` Loop

1. **Initialization**
    - Executed only once at the beginning of the loop.
    - Is typically used to initialize the loop counter: `int i = 0;` for example
2. **Condition**
    - Checked before each iteration.
    - If `true`, execute the body. If `false`, terminate the loop
    - Often checks to ensure `i` is less than some value: `i < 5;` for example
3. **Final-expression**
    - Executed after each iteration of the loop body.
    - Can be used to update the loop counter or run any other code: `i++` for example
4. **Loop Body**
    - The block of code that is executed while the condition is true.

## Example: Basic Loop

```c
#include <stdio.h>

int main() {
  for (int i = 0; i < 5; i++) {
    printf("%d\n", i);
  }
  return 0;
}

// Prints:
// 0
// 1
// 2
// 3
// 4
```

## Assignment

Implement the `print_numbers` prototyped in `exercise.h` that takes a starting number and an ending number and prints all the numbers in that range **inclusive** (using a for-loop).

```c
#include <stdio.h>

void print_numbers(int start, int end){
  for (int i = start; i <= end ;i++){
    printf("%d\n", i);
  }
}

```

# While Loop

A `while` loop in C is a control flow statement that allows code to be executed repeatedly based on a given boolean (`true`/`false`) condition. The loop continues to execute as long as the condition remains true.

## Syntax

```c
while (condition) {
    // Loop Body
}
```

## Parts of a `while` Loop

1. **Condition**
    - Checked before each iteration.
    - If `true`, execute the body. If `false`, terminate the loop
2. **Loop Body**
    - The block of code that is executed while `condition` is true.

## Example: Basic Loop

```c
#include <stdio.h>

int main() {
    int i = 0;
    while (i < 5) {
        printf("%d\n", i);
        i++;
    }
    return 0;
}
// Prints:
// 0
// 1
// 2
// 3
// 4
```

## Key Points

- The condition is evaluated _before_ the execution of the loop body.
- If the condition is `false` initially, the loop body will never even start.
- If the condition never becomes `false`, you will get an infinite loop.

## Assignment

Implement the `print_numbers_reverse` prototyped in `exercise.h`. It takes a starting number (higher) and an ending number (lower) and prints all the numbers in that range from highest to lowest **inclusive** (this time, using a while-loop).

```c
#include <stdio.h>

void print_numbers_reverse(int start, int end) {
  int i = start;
  while (i >= end) {
    printf("%d\n", i);
    i--;
  }
}
```

# Do While Loop

A `do while` loop in C is a control flow statement that allows code to be executed repeatedly based on a given boolean condition.

Unlike the `while` loop, the `do while` loop checks the condition after executing the loop body, so the loop body is **always** executed at least once.

## Syntax

```c
do {
    // Loop Body
} while (condition);
```

## Parts of a `do while` Loop

1. **Loop Body**
    - The block of code that is executed _before_ checking the condition, and then repeatedly as long as the condition is true.
2. **Condition:**
    - Checked _after_ each iteration.
    - If `true`, execute the body again.
    - If `false`, terminate the loop

## Examples

```c
#include <stdio.h>

int main() {
    int i = 0;
    do {
        printf("i = %d\n", i);
        i++;
    } while (i < 5);
    return 0;
}
// Prints:
// i = 0
// i = 1
// i = 2
// i = 3
// i = 4
```

```c
#include <stdio.h>

int main() {
    int i = 100;
    do {
        printf("i = %d\n", i);
        i++;
    } while (i < 5);
    return 0;
}
// Prints:
// i = 100
```

## Key Points

The `do while` loop guarantees that the loop body is executed at least once, even if the condition is false initially.

The most common scenario you will see a do-while loop used is in [C macros](https://gcc.gnu.org/onlinedocs/cpp/Macros.html) – they let you define a block of code and execute it exactly once in a way that is safe across different compilers, and ensures that the variables created/referenced within the macro do not leak to the surrounding environment.

If you end up looking at any source code for macros, you will probably see a few do-while loops. For example, here's a simplified version from our `munit` testing library we're using:

```c
#define munit_assert_type_full(T, fmt, a, op, b, msg)                          \
  do {                                                                         \
    T munit_tmp_a_ = (a);                                                      \
    T munit_tmp_b_ = (b);                                                      \
    if (!(munit_tmp_a_ op munit_tmp_b_)) {                                     \
      munit_errorf("assertion failed: %s %s %s (" prefix "%" fmt suffix        \
                   " %s " "%" fmt "): %s",                                     \
                   #a, #op, #b, munit_tmp_a_, #op, munit_tmp_b_, msg);         \
    }                                                                          \
  } while (0)
```

It creates a do-while loop, creates a few new variables and then checks that the assertion is valid. If it is not, then it errors and formats a (complicated) error message (If this code doesn't make any sense, that's fine too! I just wanted to show you where they most often occur).

There is no semi-colon after `while(0)` in the loop above. This lets the macro be used in a block of code without causing syntax errors.

When writing a normal do-while loop in your C code (not in a macro), you must include the semicolon after the loop.

## Assignment

Run the code. Notice that it prints numbers from `5` to `1` in descending order. However, when the starting number is less than the ending number, it doesn't print anything because the condition of the `while` loop is never `true`. Modify the `print_numbers_reverse` function to use a do-while loop so that it always prints the starting number at least once, even if the condition is initially false

```c
#include <stdio.h>

void print_numbers_reverse(int start, int end) {
  do{
    printf("%d\n", start);
    start--;
  }while(start>=end);
}

```

# Pragma Once and Header Guards

We saw how `.h` header files are used in a previous lesson, but before we go further let's talk about a potential issue you might run into: multiple inclusions. If the same header file gets included more than once, you can end up with some nasty errors caused by redefining things like functions or structs.

## Pragma Once

One simple solution (and the one we'll use for the rest of this course) is `#pragma once`. Adding this line to the top of a header file tells the compiler to include the file only once, even if it's referenced multiple times across your program.

```c
// my_header.h

#pragma once

struct Point {
    int x;
    int y;
};
```

## Header Guards

Another common way to avoid multiple inclusions is with include guards, which use preprocessor directives like this:

```c
#ifndef MY_HEADER_H
#define MY_HEADER_H

// some cool code

#endif
```

This method works by defining a unique [macro](https://gcc.gnu.org/onlinedocs/cpp/Macros.html) for the header file. If it's already been included, the guard prevents it from being processed again.

	Throughout this course, you'll see `#pragma once` in our header files. It's quicker and less error-prone than traditional include guards, and it works well with most modern compilers.

# Structs

Click to hide video

Your browser does not support playing HTML5 video. You can instead. Here is a description of the content: what are structs

So far all we've seen are the _simple_ (non-collection) types in C. However, stuff like this can get really annoying:

```c
int main() {
    int x_1 = 1;
    int y_1 = 2;
    int z_1 = 3;
    int x_2 = 4;
    int y_2 = 5;
    int z_2 = 6;

    int dist = distance(x_1, y_1, z_1, x_2, y_2, z_2);
    printf("Distance: %d", dist);
}
```

Because our distance function starts to look... ridiculous.

```c
int distance(int x_1, int y_1, int z_1,
             int x_2, int y_2, int z_2)
{
    // a lot of numbers
}
```

We also run into a new problem: _In C, we're only allowed to return a single value from a function_. This doesn't work:

```c
int int int scale_coordinate(int x, int y, int z, int scale) {
    return x * scale, y * scale, z * scale;
    // Error! Too many values to return
}
```

_[Structs](https://en.cppreference.com/w/c/language/struct) solve this._ Here's an example of the syntax:

```c
struct Human {
    int age;
    char *name;
    int is_alive;
};
```

## Assignment

Sneklang has built-in support for graphics programming (and vows to never gouge game devs...).

Define a new struct called `Coordinate` in `coord.h`. Remember, `.h` files are for declarations of types and function prototypes. The `Coordinate` struct should have three fields:

1. [ ] `x`: an integer
2. [ ] `y`: an integer
3. [ ] `z`: an integer

```c
#pragma once

struct Coordinate {
  int x;
  int y;
  int z;
};
```


# Initializers

So now you're probably wondering: "Hey TJ, so... how do we actually _make an instance of_ a struct"? You may have noticed in the previous lesson all we did was _define the struct type_.

Unfortunately, there are a few different ways to [initialize a struct](https://en.cppreference.com/w/c/language/struct_initialization), I'll give you an example of each using this struct:

```c
struct City {
  char *name;
  int lat;
  int lon;
};
```

## Zero Initializer

```c
int main() {
  struct City c = {0};
}
```

This sets all the fields to `0` values.

## Positional Initializer

```c
int main() {
  struct City c = {"San Francisco", 37, -122};
}
```

## Designated Initializer

**This is my (generally) preferred way to initialize a struct.** Why?

- It's easier to read (has the field names)
- If the fields change, you don't have to worry about breaking the ordering

```c
int main() {
  struct City c = {
    .name = "San Francisco",
    .lat = 37,
    .lon = -122
  };
}
```

Remember, it's `.name` not `name`. If this trips you up, just remember it's `.name` and not `name` because that's how you access the field, e.g. `c.name`.

## Accessing Fields

Accessing a field in a struct is done using the `.` operator. For example:

```c
struct City c;
c.lat = 41; // Set the latitude
printf("Latitude: %d", c.lat); // Print the latitude
```

There's another way to do this for pointers that we'll get to later.

## Assignment

Complete the `new_coord` function. It accepts 3 integers and returns a `Coordinate`.

_Use the "designated initializer" syntax... because I said so._

## Tip

The easiest way to return a struct is to initialize it in a variable first. If you want to skip the variable assignment, you can write something like this:

```c
struct City new_city(char *name, int lat, int lon) {
    return (struct City){.name = name, .lat = lat, .lon = lon};
}
```


```c
#include "coord.h"

struct Coordinate new_coord(int x, int y, int z) {
  struct Coordinate coord = {.x = x, .y = y, .z = z};
  return coord;
}

```
# Scaling Coordinate

Remember how we can **not** return multiple values from a function in C? We can't do this:

```c
int, char * become_older(int age, char *name) {
  return age + 1, name;
}
```

However, we _can_ accomplish effectively the same thing by returning a `struct`:

```c
struct Human become_older(int age, char *name) {
  struct Human h = {.age = age, .name = name};
  h.age++;
  return h;
}
```

## Assignment

1. [ ] Open `coord.h` and add a declaration for the `scale_coordinate` function as defined in the `coord.c` file.
2. [ ] Complete the `scale_coordinate` function in `coord.c`. It should return a new `Coordinate` where each field is scaled up (multiplied) by the `factor` parameter.
```c
#include "coord.h"

struct Coordinate new_coord(int x, int y, int z) {
  struct Coordinate coord = {.x = x, .y = y, .z = z};
  return coord;
}

struct Coordinate scale_coordinate(struct Coordinate coord, int factor) {
  coord.x *= factor;
  coord.y *= factor;
  coord.z *= factor;
  return coord;
}

```

`exercise.h`
```c
#pragma once

struct Coordinate {
  int x;
  int y;
  int z;
};

struct Coordinate new_coord(int x, int y, int z);

struct Coordinate scale_coordinate(struct Coordinate, int factor);

```

# Typedef

By now, you're probably tired of typing `struct Coordinate` over and over again, and you're wondering "How can I make my struct types easier to write, like `int`?"

Good news! C can do this with the [`typedef` keyword](https://en.cppreference.com/w/c/language/typedef).

```c
struct Pastry {
    char *name;
    float weight;
};
```

This can also be written as:

```c
typedef struct Pastry {
    char *name;
    float weight;
} pastry_t;
```

Now, you can use `pastry_t` wherever before you would have used `struct Pastry`.

The `_t` at the end is a common convention to indicate a type.

In fact, you can optionally skip giving the struct a name:

```c
typedef struct {
    char *name;
    float weight;
} pastry_t;

pastry_t muffin = {"Muffin", 0.3};
```

In this case you'd only be able to refer to the type as `pastry_t`. In general, I _do_ give the struct an actual name (e.g. `Pastry`), but I only use the `typedef`'d type. _We'll be using this convention in this course._

## Assignment

1. [ ] Update the `Coordinate` declaration in `coord.h` to use `typedef` to create a new type called `coordinate_t`.
2. [ ] Update the `new_coord` and `scale_coordinate` function declarations in `coord.h` and their definitions in `coord.c` to use the `coordinate_t` type instead of `struct Coordinate`.

coord.h
```c
#pragma once

typedef struct Coordinate {
  int x;
  int y;
  int z;
} coordinate_t ;

coordinate_t new_coord(int x, int y, int z);
coordinate_t scale_coordinate(struct Coordinate coord, int factor);

```

coord.c
```c
#include "coord.h"

coordinate_t new_coord(int x, int y, int z) {
  struct Coordinate coord = {.x = x, .y = y, .z = z};

  return coord;
}

coordinate_t scale_coordinate(struct Coordinate coord, int factor) {
  struct Coordinate scaled = coord;
  scaled.x *= factor;
  scaled.y *= factor;
  scaled.z *= factor;

  return scaled;
}

```

# Sizeof

As we saw earlier, [`sizeof`](https://en.cppreference.com/w/c/language/sizeof) can be used to view the size of a type (for once, programmers thought of a name that was actually helpful). But this isn't just true of builtin types like `int` or `float`, you can also use it to find out the size of `struct`s!

```c
printf("Size of coordinate_t: %zu bytes\n", sizeof(coordinate_t));
```

## Memory Layout

Structs are stored contiguously in memory one field after another. Take this struct:

```c
typedef struct Coordinate {
    int x;
    int y;
    int z;
} coordinate_t;
```

Assuming `int` is 4 bytes, the memory layout for `coordinate_t` would look like:

## Mixed Type Structs

```c
typedef struct Human{
    char first_initial;
    int age;
    double height;
} human_t;
```

Assuming `char` is 1 byte, `int` is 4 bytes, and `double` is 8 bytes, the memory layout for `human_t` might look like this:

**Wait**! What is that `padding` doing here?

It turns out that CPUs don't like accessing data that isn't [aligned](https://en.wikipedia.org/wiki/Data_structure_alignment) (incredible oversimplification alert, since obviously CPUs don't have feelings (yet)), so C inserts padding to maintain alignment (e.g. every 4 bytes in this example).

_Huge caveat: these layouts can vary depending on the compiler and system architecture._


# What is Alignment 
Alignment means the CPU wants a variable's memory address to be a multiple of its own size (a 4-byte `int` wants to start at an address divisible by 4, an 8-byte `double` divisible by 8, etc). If a field doesn't naturally land there, the compiler inserts padding bytes to push it forward.

For `human_t`:

```c
typedef struct Human {
    char first_initial;  // 1 byte
    int age;              // 4 bytes
    double height;         // 8 bytes
} human_t;
```

Byte-by-byte layout:

```
Offset:   0    1    2    3    4    5    6    7    8    9   10   11   12   13   14   15
        [ c ][ P ][ P ][ P ][------ age ------][-------------- height --------------]
          |    └──┴──┴── padding (3 bytes) so 'age' starts at offset 4 (multiple of 4)
          first_initial
```

Why: `age` is an `int` (4 bytes), so it needs to start at an offset divisible by 4. After `first_initial` at offset 0, the next free offset is 1 — not divisible by 4 — so the compiler inserts 3 padding bytes to bump `age` to offset 4.

`height` is a `double` (8 bytes), needing an offset divisible by 8. After `age` ends at offset 8, that's already divisible by 8, so no padding needed there.

Total size: 16 bytes, even though the fields themselves only add up to 1 + 4 + 8 = 13 bytes.

Compare with `coordinate_t` (three `int`s, all 4-byte-aligned already):

```
Offset:  0    1    2    3    4    5    6    7    8    9   10   11
       [-------- x --------][-------- y --------][-------- z --------]
```

No padding needed — every field is the same size, so each one naturally lands on a 4-byte boundary. Total: 12 bytes, matching the fields exactly.

Real-world consequence: field order affects struct size. If you reordered `human_t` as `double height; int age; char first_initial;`, you'd get:

```
Offset:  0-7: height (8 bytes, no padding needed)
Offset:  8-11: age (4 bytes, offset 8 is div by 4, no padding)
Offset: 12: first_initial (1 byte)
Offset: 13-15: 3 bytes trailing padding (to make the whole struct's size a multiple of the largest alignment, 8, so arrays of this struct stay aligned)
```

Still 16 bytes here, but with different structs the ordering can save real space — a common trick is "biggest fields first" to minimize wasted padding.

lets look at good and bad strut positioning 
```c
struct Bad {
    char a;   // 1 byte
    int b;    // 4 bytes
    char c;   // 1 byte
};
// layout: a(1) + pad(3) + b(4) + c(1) + pad(3) = 12 bytes
```

```c
struct Good {
    int b;    // 4 bytes
    char a;   // 1 byte
    char c;   // 1 byte
};
// layout: b(4) + a(1) + c(1) + pad(2) = 8 bytes
```

# Struct Padding

There are a bunch of complicated rules and heuristics that different compilers use to determine how to lay out your structs. But to oversimplify:

1. The fields of a struct are laid out in memory contiguously (next to each other).
2. Structs can vary in size depending on how they are laid out.

C is a language that aims to give tight control over memory, so the fact that you can control the layout of your structs is a feature, not a bug.

Compilers + modern hardware + optimizations + skill issues means that sometimes what you _think_ the computer is going to do isn't exactly what it actually _does_. That said, C is designed to get you close to the machine and allows you to dig in and figure out what's going on if you want to for a specific compiler or architecture.

As a _rule of thumb_, ordering your fields from largest to smallest will help the compiler minimize padding:

```c
typedef struct {
  char* a;
  double b;
  char c;
  char d;
  long e;
  char f;
} poorly_aligned_t;

typedef struct {
  double b;
  long e;
  char* a;
  char c;
  char d;
  char f;
} better_t;
```

## Assignment

Re-arrange the fields in `sneklang_var_t` so that the padding is optimal and the tests in `main.c` pass.

```c
#pragma once

typedef struct SneklangVar {
  double weight;
  int value;
  int scope_level;
  char *name;
  char type;
  char is_constant;
} sneklang_var_t;

```

# Memory

Before we talk about pointers, we should talk about variables and memory in general. Here are some useful (albeit hand-wavy) mental models:

> Variables are human readable names that refer to some data in memory.

> Memory is a big array of bytes, and data is stored in the array.

A variable is a human readable name that refers to an address in memory, which is an index into the big array of bytes. Here's a diagram:

## Getting a Variable's Address

[%p format specifier](https://en.cppreference.com/w/c/io/fprintf#:~:text=The%20following%20format%20specifiers%20are%20available%3A)
## Assignment

The `size_of_addr` function accepts a [`long long`](https://en.wikipedia.org/wiki/C_data_types) (a potentially very large integer) as input and returns the _size_ of its _address_.

_There's a bug_! Memory addresses in Sneklang should always be `4` bytes long...

Fix the function so that it returns the size of `i`'s _address_, not value.
```c
#include "snek.h"

unsigned long size_of_addr(long long i) {
  unsigned long sizeof_snek_version = sizeof(&i);
  return sizeof_snek_version;
}

```

# What Is an Address?

So I mentioned in the last lesson that memory can be thought of as a big array of bytes, and each byte has an address.

That's true, and the beauty is that each address is _literally just a number_. It's not some _mortal_ address like "1234 Elm St." or "1600 Pennsylvania Ave." It's **just a number**.

You might be thinking, "Hey, if it's just a number, why does it look all disgusting like `0xfff8`?"

That's because `0xfff8` _is_ just a number. But:

1. It's written in [`hexadecimal`](https://www.wikipedia.org/wiki/Hexadecimal) (base 16) instead of decimal (base 10).
2. It's a pretty big number, so it's not very human readable. `0xfff8` is the same as `65,528` in decimal.
# Pointers

You've probably heard of pointers. You may have also seen jokes about how they are impossible to learn... Well, that's _wrong_.

In fact, now that you understand how memory is laid out in an array, a lot of the mystery behind pointers should be gone. Put simply: **a pointer is just a variable that stores a memory address**. It's called a pointer, because it "points" to the address of a variable, which stores the actual data held in that variable.

Click to hide video

Your browser does not support playing HTML5 video. You can instead. Here is a description of the content: pointers are easy

## Syntax

A pointer is declared with an asterisk (`*`) after the type. For example, `int *`.

```c
int age = 37;
int *pointer_to_age = &age;
```

Remember, to get the address of a variable so that we can store it _in_ a pointer variable, we can use the address-of operator (`&`).


# Why Pointers?

To illustrate the usefulness of pointers, let's pretend we want to pass a collection of data into a function. Within that function, we want to modify the data. In Python, we could use a class to store the data, and pass an instance of that class into the function:

```python
class Coordinate:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


def update_coordinate_x(coord, new_x):
    coord.x = new_x


c = Coordinate(1, 2, 3)
print(c.x)  # 1
update_coordinate_x(c, 4)
print(c.x)  # 4
```

## Assignment

Now let's do the same thing, but using a struct in C.

**Complete the `coordinate_update_x` and `coordinate_update_and_return_x` functions.**

1. [ ] `coordinate_update_x` should update the `x` field with the provided `new_x` value. It returns `void` and should not update the caller's struct.
2. [ ] `coordinate_update_and_return_x` should update the `x` field with the provided `new_x` value, and then return the updated coordinate struct.

Remember, you can access the field of a struct with a `.` operator, like so:

```c
car.tires = 4;
```

## What Happened?

After passing the assignment, open up `main.c` and take a look at the test cases. You'll notice that `coordinate_update_x` doesn't update anything, but `coordinate_update_and_return_x` does because it returns a new copy of the struct.

- In C, structs are passed by _value_. That's why updating a field in the struct does _not_ change the original struct from the `main` function.
- To get the change to "persist", we needed to return the updated struct from the function (a new copy).
- The memory address of the struct that went _in_ to `coordinate_update_and_return_x` was not the same as the address of the struct that was returned. Again, because we created a copy.


# Pointer Basics

Remember, pointers are just an address (read: value) that tells the computer where to look for _other_ values. Just like how the address to your house is not actually your house, but points you to where your house **is**.

## Syntax Review

Declare a pointer to an integer:

```c
// declares `pointer_to_something` as a pointer to an int
int *pointer_to_something;
```

Get the address of a variable:

```c
int meaning_of_life = 42;
int *pointer_to_mol = &meaning_of_life;
// pointer_to_mol now holds the address of meaning_of_life
```

## New: Dereferencing Pointers

Oftentimes we have a pointer, but we want to get access to the data that it points to. Not the address itself, but the value stored at _that_ address.

We can use an asterisk (`*`) to do it. The `*` operator dereferences a pointer.

```c
int meaning_of_life = 42;
int *pointer_to_mol = &meaning_of_life;
int value_at_pointer = *pointer_to_mol;
// value_at_pointer = 42
```

_It can be a touch confusing, but remember that the asterisk symbol is used for two different things:_

1. Declaring a pointer type: `int *pointer_to_thing;`
2. Dereferencing a pointer value: `int value = *pointer_to_thing;` (retrieving the value) or `*pointer_to_thing = 20;` (modifying the value)

## Assignment

Fix the `change_filetype` function (both in the `.c` and `.h` files). It should copy the struct from the pointer, update the copy, and leave the original unchanged.

1. [ ] Accept _a pointer_ to a `codefile_t`, instead of a struct value
2. [ ] Dereference the pointer into the `new_f` `codefile_t` struct
3. [ ] The `filetype` field should still be changed to the provided `new_filetype` value
4. [ ] Still return the updated `new_f` `codefile_t` struct

`exercise.h`
```c
typedef struct CodeFile {
  int lines;
  int filetype;
} codefile_t;

codefile_t change_filetype(codefile_t *f, int new_filetype);
```

`exercise.c`
```c
#include "exercise.h"

codefile_t change_filetype(codefile_t *f, int new_filetype) {
  codefile_t new_f = *f;
  new_f.filetype = new_filetype;
  return new_f;
}

```

# Pointers to Structs

As you know, when you have a struct, you can access the fields with the dot (`.`) operator:

```c
coordinate_t point = {10, 20, 30};
printf("X: %d\n", point.x); // X: 10
```

However, when you're working with a _pointer to a struct_, you need to use the arrow (`->`) operator:

```c
coordinate_t point = {10, 20, 30};
coordinate_t *ptrToPoint = &point;
printf("X: %d\n", ptrToPoint->x); // X: 10
```

It effectively dereferences the pointer and accesses the field in one step. To be fair, you can also use the dereference and dot operator (`*` and `.`) to achieve the same result (it's just more verbose and less common):

```c
coordinate_t point = {10, 20, 30};
coordinate_t *ptrToPoint = &point;
printf("X: %d\n", (*ptrToPoint).x); // X: 10
```

## Order of Operations

The `.` operator has a higher precedence than the `*` operator, so parentheses are _necessary_ when using `*` to dereference a pointer before accessing a member... which is another reason why the arrow operator is so much more common.

# C Arrays

If you're used to [Lists in Python](https://docs.python.org/3/tutorial/datastructures.html), [Arrays in C](https://en.cppreference.com/w/c/language/array) are _similar_, but a bit lower level.

An array is a _fixed-size_, ordered collection of elements. Like Python lists, they are indexed by integers, starting at zero. Unlike Python lists, they can only hold elements of the same type. They are stored in contiguous memory, like structs.

## Integer Array

```c
int numbers[5] = {1, 2, 3, 4, 5};
```

### Iterating Over an Array

In C, there is no `for x in list:` syntax. Instead, you must iterate over them using a `for` loop with an index (or some other conditional loop)

```c
#include <stdio.h>

int main() {
    int numbers[5] = {1, 2, 3, 4, 5};

    // Iterate and print each element
    for (int i = 0; i < 5; i++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");

    return 0;
}
```

Output:

```text
1 2 3 4 5
```

### Updating Values in an Array

The syntax for updating values in an array is the same as how you access them:

`arr[index] = value`

Using our `numbers` example:

```c
#include <stdio.h>

int main() {
    int numbers[5] = {1, 2, 3, 4, 5};

    // Update some values
    numbers[1] = 20;
    numbers[3] = 40;

    // Print updated array
    for (int i = 0; i < 5; i++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");

    return 0;
}
```

Output:

```text
1 20 3 40 5
```

## Assignment

Complete the `update_file` function. The `filedata` array is a large 200-integer array representing a Sneklang source file. Each integer in the array represents a special piece of data.

- Index `1` is the number of lines
- Index `2` is the filetype
- Index `199` is always `0`

Update the function so that it:

1. [ ] overwrites indexes 1 and 2 with the provided values
2. [ ] ensures that index 199 is always `0`

By modifying the array within your function, you're changing the values of the **original array**, not just a copy. More on that later.

```c
#include "exercise.h"

void update_file(int filedata[200], int new_filetype, int new_num_lines) {
  filedata[2] = new_filetype;
  filedata[1] = new_num_lines;

  if (filedata[199] != 0){
    filedata[199] = 0;
  }
}

```
# Arrays As Pointers in C

In C, arrays and pointers are closely related. An array name acts as a pointer to the first element of the array. That means array indexing and pointer arithmetic can be used interchangeably to access array elements. Let's go through this step-by-step to understand how this works.

## Step-by-Step Walkthrough

1. **Array Declaration:**
    
    ```c
    int numbers[5] = {1, 2, 3, 4, 5};
    ```
    
    Here, `numbers` is an array of 5 integers.
    
2. **Array as Pointer:**
    
    The name `numbers` acts as a pointer to the first element of the array.
    
    ```c
    int *numbers_ptr = numbers;
    ```
    
    `numbers_ptr` is a pointer to the same place as `numbers`.
    
3. **Accessing Elements via Indexing:**
    
    ```c
    // Access the third element (index 2)
    int value = numbers[2];
    ```
    
    Which is the same as:
    
    ```c
    int value = *(numbers + 2);
    ```
    
    Here, `numbers + 2` computes the address of the third element, and `*` dereferences it to get the value.
    
4. **Pointer Arithmetic:**
    
    When you add an integer to a pointer, the resulting pointer is offset by that integer times the size of the data type.
    
    ```c
    int *p = numbers + 2;  // p points to the third element
    int value = *p;        // value is 3
    ```

## Diagram Explanation

Let's assume `numbers` is stored starting at memory address `0x1000`. An integer is typically 4 bytes in C. Here's how the array elements are laid out in memory:

|Address|Element|Value|
|---|---|---|
|0x1000|numbers[0]|1|
|0x1004|numbers[1]|2|
|0x1008|numbers[2]|3|
|0x100C|numbers[3]|4|
|0x1010|numbers[4]|5|

Try it out! Change the base address, operator, and offset to see how pointer arithmetic selects different memory cells:

Base Address 0x1008

Offset 

0x1008+8=0x1028→0

## Accessing Elements Using Pointers

- `numbers + 0` or `&numbers[0]` points to `0x1000`
- `numbers + 1` or `&numbers[1]` points to `0x1004`
- `numbers + 2` or `&numbers[2]` points to `0x1008`
- `numbers + 3` or `&numbers[3]` points to `0x100C`
- `numbers + 4` or `&numbers[4]` points to `0x1010`

## Example Code

```c
#include <stdio.h>

int main() {
  int numbers[5] = {1, 2, 3, 4, 5};

  // Accessing elements using array indexing
  printf("numbers[2] = %d\n", numbers[2]);  // Output: 3

  // Accessing elements using pointers
  printf("*(numbers + 2) = %d\n", *(numbers + 2));  // Output: 3

  // Pointer arithmetic
  int *ptr = numbers;
  printf("Pointer ptr points to numbers[0]: %d\n", *ptr);  // Output: 1
  ptr += 2;
  printf("Pointer ptr points to numbers[2]: %d\n", *ptr);  // Output: 3

  return 0;
}
```