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

# Multibyte Arrays

If we create an array of structs it gets crazy because we can access and manipulate the elements using either indexing _or_ pointer arithmetic. Let's see how multi-byte width structures are managed in memory.

First, let's say we're working with our familiar Coordinate struct:

```c
typedef struct Coordinate {
  int x;
  int y;
  int z;
} coordinate_t;
```

We can declare an array of 3 `Coordinate` structs like so:

```c
coordinate_t points[3] = {
  {1, 2, 3},
  {4, 5, 6},
  {7, 8, 9}
};
```

Then we can print out the values of the second element in the array:

```c
printf("points[1].x = %d, points[1].y = %d, points[1].z = %d\n",
  points[1].x, points[1].y, points[1].z
);
// points[1].x = 4, points[1].y = 5, points[1].z = 6
```

Or we can use a pointer:

```c
coordinate_t *ptr = points;
printf("ptr[1].x = %d, ptr[1].y = %d, ptr[1].z = %d\n",
  (ptr + 1)->x, (ptr + 1)->y, (ptr + 1)->z
);
// ptr[1].x = 4, ptr[1].y = 5, ptr[1].z = 6
```

## Memory Layout

Assuming each `int` is 4 bytes, the `Coordinate` structure will be 12 bytes (`3 * 4` bytes). Let's assume the `points` array starts at memory address `0x2000`.

Here is the memory layout:

|Address|Element|Value|Offset (bytes)|
|---|---|---|---|
|`0x2000`|`points[0].x`|1|0|
|`0x2004`|`points[0].y`|2|4|
|`0x2008`|`points[0].z`|3|8|
|`0x200C`|`points[1].x`|4|12|
|`0x2010`|`points[1].y`|5|16|
|`0x2014`|`points[1].z`|6|20|
|`0x2018`|`points[2].x`|7|24|
|`0x201C`|`points[2].y`|8|28|
|`0x2020`|`points[2].z`|9|32|

## Accessing Elements Using Pointers

- `points + 0` or `&points[0]` points to `0x2000`
- `points + 1` or `&points[1]` points to `0x200C` (next structure, offset by 12 bytes)
- `points + 2` or `&points[2]` points to `0x2018`

A struct stores 8 integers in its ordered fields:  
A through H.  
An array stores 10 of these structs.  
What will be the offset in bytes from **the start** of the array to **the 5th element's `C` field**?

indexes 0 
- 5th element so one array of 8 values takes 4 * 8 = 32 bytes
- so 4 * 32* = 128 bytes
- 3rd element offset in struct so 2 * 4 = 8 bytes 
- total offset = 136 bytes
# Array Casting

Let's explore a special kind of psychopathy that's possible in C. Let's assume we have this array of 3 structs where each struct holds 3 integers:

```c
coordinate_t points[3] = {
  {5, 4, 1},
  {7, 3, 2},
  {9, 6, 8}
};
```

Because arrays are basically just pointers (in most cases; more on that later), and we know that structs are contiguous in memory, we can cast the array of structs to an array of integers:

```c
int *points_start = (int *)points;
```

The cast tells C to treat the same starting address as an `int *`, so each index walks one `int` at a time through the contiguous struct fields.

Then we can iterate over the known number of integers in the array of structs:

```c
for (int i = 0; i < 9; i++) {
  printf("points_start[%d] = %d\n", i, points_start[i]);
}
/*
points_start[0] = 5
points_start[1] = 4
points_start[2] = 1
points_start[3] = 7
points_start[4] = 3
points_start[5] = 2
points_start[6] = 9
points_start[7] = 6
points_start[8] = 8
*/
```

## Assignment

Take a look at the `dump_graphics` function. It works similarly to the example above.

Go ahead and run it in its current state. You should notice that after all the values specified in `main.c` are printed... all hell breaks loose. That's because we've ventured out of the bounds of our array! We're going rogue! We're in the weeds! We're in undefined territory. This is something you _do not_ want to do. It's one of the things that makes C powerful but dangerous. Other languages stop you from going out of bounds, but C will let you fly off the edge of the world.

**Fix the loop to only print the values that are actually in the array of structs**. Take a look at the `graphics_t` struct in `exercise.h` to figure out how large each struct is.

```c
#include "exercise.h"
#include <stdio.h>

void dump_graphics(graphics_t gsettings[10]) {
  int *ptr = (int *)gsettings;
  for (int i = 0; i < 30; i++) {
    printf("settings[%d] = %d\n", i, ptr[i]);
  }
}

```

# Pointer Size

The size of an array depends on both the number of elements and the size of each element. An array is a contiguous block of memory where each element has a specific type, and therefore, a specific size.

In C, pointers are always the same size because they just represent memory addresses. The size of a pointer is determined by the architecture of the system (e.g., 32-bit or 64-bit). A pointer's size doesn't depend on the type of data it points to; it just holds the address of a memory location.

## Pointer Example

```c
int *intPtr;
char *charPtr;
double *doublePtr;
printf("Size of int pointer: %zu bytes\n", sizeof(intPtr));
printf("Size of char pointer: %zu bytes\n", sizeof(charPtr));
printf("Size of double pointer: %zu bytes\n", sizeof(doublePtr));
// Size of int pointer: 4 bytes
// Size of char pointer: 4 bytes
// Size of double pointer: 4 bytes
```

In Boot.dev's 32-bit [WASM](https://webassembly.org/) environment, they're all the same [size](https://port70.net/~nsz/c/c11/n1570.html#6.5.3.4), because they're all just 32-bit memory addresses: it doesn't matter how much memory the value at that address takes up.

## Array Example

```c
int intArray[10];
char charArray[10];
double doubleArray[10];
printf("Size of int array: %zu bytes\n", sizeof(intArray));
printf("Size of char array: %zu bytes\n", sizeof(charArray));
printf("Size of double array: %zu bytes\n", sizeof(doubleArray));
// Size of int array: 40 bytes
// Size of char array: 10 bytes
// Size of double array: 80 bytes
```

Now the sizes are different because the array type keeps track of the size of each element and the number of elements. Although an array is a pointer to the first element, it's not _just_ a pointer: it's a block of memory that holds all the elements.

Boot.dev runs C in the browser using [WASM](https://webassembly.org/), which is typically a 32-bit system. If you run this code on a 64-bit system, the size of the pointers will be 8 bytes.```
# Arrays Decay to Pointers

So we know that arrays are _like_ pointers, but they're not exactly the same. Arrays allocate memory for all their elements, whereas pointers just hold the address of a memory location. In many contexts, [arrays **decay** to pointers](https://port70.net/~nsz/c/c11/n1570.html#6.3.2.1), meaning the array name _becomes_ "just" a pointer to the first element of the array.

## When Arrays Decay

Arrays decay when used in expressions containing pointers:

```c
int arr[5];

// 'arr' decays to 'int*' because that's the type of 'ptr'
int *ptr = arr;

// 'arr' decays to 'int*' to perform pointer arithmetic
int value = *(arr + 2);
```

And also when they're passed to functions... so they actually decay quite often in practice. That's why you can't pass an array to a function by value like you do with a struct; instead, the array name decays to a pointer.

### When Arrays Don't Decay

- **`sizeof` Operator:** Returns the size of the entire array (e.g., sizeof(arr)), not just the size of a pointer.
- **`&` Operator:** Taking the address of an array with `&arr` gives you a pointer to the whole array, not just the first element. The type of `&arr` is a pointer to the array type, e.g., `int (*)[5]` for an `int` array with 5 elements.
- **Initialization:** When an array is declared and initialized, it is fully allocated in memory and does not decay to a pointer.

## Assignment

Take a look at the `main` function. It declares an array of numbers `core_utilization` that represents the CPU utilization of each core on a system running the Sneklang interpreter. The array has 8 elements. On lines 12 and 13 it prints the size of the array and the length of the array.

Complete the `core_utils_func` function to print:

```text
sizeof core_utilization in core_utils_func: X
```

Where `X` is the size of the array calculated using the `sizeof` operator.

**Once you've completed the function, run it and take a look at the output. You'll notice that due to the array decaying to a pointer, the reported size is the size of a pointer, not the size of the actual array.**

```c
#include <stdio.h>

void core_utils_func(int core_utilization[]) {
  printf("sizeof core_utilization in core_utils_func: %zu", sizeof(core_utilization));
}

// don't touch below this line

int main() {
  int core_utilization[] = {43, 67, 89, 92, 71, 43, 56, 12};
  int len = sizeof(core_utilization) / sizeof(core_utilization[0]);
  printf("sizeof core_utilization in main: %zu\n", sizeof(core_utilization));
  printf("len of core_utilization: %d\n", len);
  core_utils_func(core_utilization);
  return 0;
}

```


# C Strings

Since the beginning of the course we've been doing these shenanigans to be able to print strings:

```c
char *msg = "ssh terminal.shop for the best coffee";
```

I told you not to worry about the weird `char *` syntax, but now that we understand a bit about pointers, let's dive into it. In the example above, `msg` is a pointer to the first character of the string `"ssh terminal.shop for the best coffee"`, which is a [C string](https://en.wikipedia.org/wiki/C_string_handling). C strings are:

- How we represent text in C programs
- Any number of characters (`char`s) terminated by a null character (`'\0'`).
- A pointer to the first element of a character array.

It's important to understand that most string manipulation in C is done using pointers to move around the array and the null terminator is critical for determining the end of the string. In the example above, the string `"ssh terminal.shop for the best coffee"` is stored in memory as an array of characters, and the null terminator `'\0'` is automatically added at the end.

## C Strings Are Simple

- Unlike other programming languages, C strings do _not_ store their length.
- The length of a C string is determined by the position of the null terminator (`'\0'`).
- Functions like [`strlen`](https://en.cppreference.com/w/c/string/byte/strlen) calculate the length of a string by iterating through the characters until the null terminator is encountered.
- This lack of length storage requires careful management to avoid issues such as buffer overflows and off-by-one errors during string operations.

## Pointers vs. Arrays

You can declare strings in C using either arrays or pointers:

```c
char str1[] = "Hi";
char *str2 = "Snek";
printf("%s %s\n", str1, str2);
// Output: Hi Snek
```

The output is the same. Let's break down the memory of this example:

```c
// notice we aren't using all 50 characters
char first[50] = "Snek";
char *second = "lang!";
strcat(first, second);
printf("Hello, %s\n", first);
// Output: Hello, Sneklang!
```

The [`strcat`](https://en.cppreference.com/w/c/string/byte/strcat) function appends its second argument to the first argument. In this case, it appends `"lang!"` to `"Snek"`, resulting in the output `Hello, Sneklang!`.

Here's what `first` might look like in memory:

The **\0** is a `\` followed by the **number zero**. Do not confuse it with the **O** letter.

|'S'|'n'|'e'|'k'|'\0'|????|...|????|
|---|---|---|---|---|---|---|---|
|0x3000|0x3001|0x3002|0x3003|0x3004|0x3005|...|0x3031|

_NOTE! There is a bunch of garbage memory after the end of the string_.

Here's what `second` might look like in memory:

|'l'|'a'|'n'|'g'|'!'|'\0'|
|---|---|---|---|---|---|
|0x4000|0x4001|0x4002|0x4003|0x4004|0x4005|

And `first` after `strcat`:

|'S'|'n'|'e'|'k'|'l'|'a'|'n'|'g'|'!'|'\0'|????|...|????|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|0x3000|0x3001|0x3002|0x3003|0x3004|0x3005|0x3006|0x3007|0x3008|0x3009|0x300A|...|0x3031|

The `strcat` function appends the string `"lang!"` to the end of the string `"Snek"`, but smartly uses the null terminator to know where to start appending. It doesn't know the length of the string, but it knows where it ends.

## Assignment

At Sneklang, we have a bit of ["not invented here"](https://en.wikipedia.org/wiki/Not_invented_here) culture. As such, we've decided to implement our own string concatenation function.

Complete the `concat_strings` function. It should append `str2` to the end of `str1` _in place_. Here are the steps:

1. [ ] Find the null terminator ('\0') of `str1`
2. [ ] Iterate over `str2` and copy each character to the memory locations at the end of `str1`.
3. [ ] Add a null terminator at the end of the concatenated string.

_Don't cheat and use `strcat`!_

`str1` is already allocated with enough memory to hold the concatenated string, so don't worry about that.

## Tips

- Use a while loop and a pointer dereference to see when you reach a null terminator.
- Increment your pointer with the `++` operator to move to the next character.
- You can copy a character by dereferencing and assigning the value of one pointer to another.

```c
#include "exercise.h"
#include <stdio.h>

void concat_strings(char *str1, const char *str2) {
  char *start = str1;
  while(*str1 != '\0'){
    str1++;
  }
  const char *p = str2;
  while(*p != '\0'){
    *str1 = *p;
    p++;
    str1++;
  }
  *str1 = '\0';
}

```

# C String Library

The C standard library provides a comprehensive set of functions to manipulate strings in the `<string.h>` header file. Here are some of the most commonly used functions:

- [`strcpy`](https://en.cppreference.com/w/c/string/byte/strcpy): Copies a string to another.
    
    ```c
    char src[] = "Hello";
    char dest[6];
    strcpy(dest, src);
    // dest now contains "Hello"
    ```
    
- [`strncpy`](https://en.cppreference.com/w/c/string/byte/strncpy): Copies a _specified number of characters_ from one string to another.
    
    ```c
    char src[] = "Hello";
    char dest[6];
    strncpy(dest, src, 3);
    // dest now contains "Hel"
    dest[3] = '\0';
    // ensure null termination
    ```
    
- [`strcat`](https://en.cppreference.com/w/c/string/byte/strcat): Concatenates (appends) one string to another.
    
    ```c
    char dest[12] = "Hello";
    char src[] = " World";
    strcat(dest, src);
    // dest now contains "Hello World"
    ```
    
- [`strncat`](https://en.cppreference.com/w/c/string/byte/strncat): Concatenates a _specified number of characters_ from one string to another.
    
    ```c
    char dest[12] = "Hello";
    char src[] = " World";
    strncat(dest, src, 3);
    // dest now contains "Hello Wo"
    ```
    
- [`strlen`](https://en.cppreference.com/w/c/string/byte/strlen): Returns the length of a string (excluding the null terminator).
    
    ```c
    char str[] = "Hello";
    size_t len = strlen(str);
    // len is 5
    ```
    
- [`strcmp`](https://en.cppreference.com/w/c/string/byte/strcmp): Compares two strings lexicographically.
    
    ```c
    char str1[] = "Hello";
    char str2[] = "World";
    int result = strcmp(str1, str2);
    // result is negative since "Hello" < "World"
    ```
    
- [`strchr`](https://en.cppreference.com/w/c/string/byte/strchr): Finds the first occurrence of a character in a string.
    
    ```c
    char str[] = "Hello";
    char *pos = strchr(str, 'l');
    // pos points to the first 'l' in "Hello"
    ```
    
- [`strstr`](https://en.cppreference.com/w/c/string/byte/strstr): Finds the first occurrence of a substring in a string.
    
    ```c
    char str[] = "Hello World";
    char *pos = strstr(str, "World");
    // pos points to "World" in "Hello World"
    ```
    

## Assignment

Complete the `smart_append` function. It appends a `src` string to the `buffer` field inside the `dest` `TextBuffer` _struct_.

The `TextBuffer` struct tracks both the buffer and its current length. It's called a "smart" append because the destination buffer is a fixed `64` bytes, and it:

- Checks for available space before appending.
- Appends as much as possible if there's not enough space.
- Always ensures the buffer remains null-terminated.
- Returns a status indicating whether the full append was possible.

Here are the steps:

1. [ ] If either the `dest` or `src` input is `NULL`, return `1` (failure). The input pointer checks can be done with `ptr == NULL` or `!ptr`.
    
    In C, `NULL` represents a [null pointer](https://en.wikipedia.org/wiki/Null_pointer), which does not point to a value.
    
2. [ ] Create a constant to represent the max buffer size of 64.
3. [ ] Get the length of the src string using `strlen`.
4. [ ] Calculate the remaining space in the dest buffer. Notice that it stores its own length. The 64-byte buffer can hold 63 characters plus the null terminator.
5. [ ] If the src string is larger than the remaining space:
    1. [ ] Copy as much of the src string as possible to the dest buffer using `strncat`.
    2. [ ] Update the dest buffer length to the max size, accounting for the null terminator.
    3. [ ] Return `1` (failure) to indicate the full append wasn't possible.
6. [ ] Otherwise, if there's enough space:
    1. [ ] Append the entire src string to the dest buffer using `strcat`.
    2. [ ] Update the dest buffer length.
    3. [ ] Return `0` (success) to indicate the full append was possible.


```c
#include "exercise.h"
#include <string.h>
#include <stdio.h>

int smart_append(TextBuffer *dest, const char *src) {
  if (dest == NULL || src == NULL ) {
    return 1;
  }
  const int max_buffer = 64;
  size_t src_len = strlen(src);
  printf("\nSrc Length: %zu\n",src_len);
  size_t remaining_length = max_buffer - dest->length - 1;
  printf("\nRemaining Length: %zu\n",remaining_length);
  if (src_len > remaining_length) {
    strncat(dest->buffer, src, remaining_length);
    dest->length = max_buffer - 1;
    return 1;
  }else {
    strcat(dest->buffer, src);
    dest->length += src_len;
    return 0;
  }
}
```

# Forward Declaration

Sometimes you have a struct that may need to reference itself, or be used recursively.

For example, consider a `Node` struct that can contain other `Node`s. This might be useful for building a linked list or a tree:

```c
typedef struct Node {
  int value;
  node_t *next;
} node_t;
```

The problem here is that `node_t` is not defined yet, so the compiler will complain. To fix this, we can add a forward declaration. A forward declaration lets the compiler know about the existence of a struct type before it's fully defined:

```c
typedef struct Node node_t;

typedef struct Node {
  int value;
  node_t *next;
} node_t;
```

Note that the forward declaration must match the eventual definition, so you can't do something like this:

```c
typedef struct Node node_t;

typedef struct BadName {
  int value;
  node_t *next;
} node_t;
```

## Assignment

Sneklang, like Python, is built on the idea of dynamic objects, and objects need to be able to store other objects.

Run the code in its current state. Notice that the `.h` file is producing an error because the `Object` struct references itself. Fix it with a forward declaration.

```c
typedef struct SnekObject snekobject_t;
typedef struct SnekObject {
  char *name;
  snekobject_t *child;
} snekobject_t;

snekobject_t new_node(char *name);

```

# Mutual Structs

Forward declarations can also be used when two structs reference each other (a circular reference). For example, a `Person` has a `Computer` and a `Computer` has a `Person`:

```c
typedef struct Computer computer_t;
typedef struct Person person_t;

struct Person {
  char *name;
  computer_t *computer;
};

struct Computer {
  char *brand;
  person_t *owner;
};
```

Notice that the struct definitions end with just `};` rather than `} person_t;`. Since we already created the typedef aliases in the forward declarations, we don't need to repeat them, though both styles are valid in C.

Note that when you use forward declarations, you must use pointers to incomplete types (`Computer *computer;`), not full values (`Computer computer;`). This is because the size of the struct is unknown.

## Assignment

Complete the definitions of the `Employee` and `Department` structs. Take a look at the implementations in the `.c` file to understand how they should be defined.

## Tip

_A manager is just another `employee_t`._

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Employee employee_t;
typedef struct Department department_t;

struct Employee {
  int id;
  char *name;
  department_t *department;
};

struct Department {
  char *name;
  employee_t *manager;
};

employee_t create_employee(int id, char *name);
department_t create_department(char *name);

void assign_employee(employee_t *emp, department_t *department);
void assign_manager(department_t *dept, employee_t *manager);
```

# Enums

Unlike [Golang](https://www.boot.dev/courses/learn-golang) (a language living in 1970), C has explicit support for `enum`s (enumerations) with the [`enum` keyword](https://en.cppreference.com/w/c/language/enum).

TJ is salty because Go is a simple, modern language that companies ackshually use to ship products. Not all programming languages can be academic thought-experiments like OCaml.

You can define a new enum type like this:

```c
typedef enum DaysOfWeek {
  MONDAY,
  TACO_TUESDAY,
  WEDNESDAY,
  THURSDAY,
  FRIDAY,
  SATURDAY,
  FUNDAY,
} days_of_week_t;
```

The `typedef` and its alias `days_of_week_t` are optional, but like with structs, they make the enum easier to use.

In the example above, `days_of_week_t` is a new type that can _only_ have one of the values defined in the `enum`:

- `MONDAY`, which is 0
- `TACO_TUESDAY`, which is 1
- `WEDNESDAY`, which is 2
- `THURSDAY`, which is 3
- `FRIDAY`, which is 4
- `SATURDAY`, which is 5
- `FUNDAY`, which is 6

You can use the `enum` type like this:

```c
typedef struct Event {
  char *title;
  days_of_week_t day;
} event_t;

// Or if you don't want to use the alias:

typedef struct Event {
  char *title;
  enum DaysOfWeek day;
} event_t;
```

An `enum` is _not_ a collection type like a struct or an array. It's just a list of integers constrained to a new type, where each is given an explicit name.

## Assignment

The Sneklang graphics library needs to represent colors.

Create a `Color` enum (and the `color_t` typedef) with `RED`, `GREEN`, and `BLUE` values, in that order.

```c
typedef enum Color {
  RED,
  GREEN,
  BLUE,
} color_t;
```


# Switch Case

One of the best features of `enums` is that it can be used in [`switch` statements](https://en.cppreference.com/w/c/language/switch). Enums + switch statements:

- Avoid "[magic numbers](https://en.wikipedia.org/wiki/Magic_number_\(programming\))"
- Use descriptive names
- With modern tooling, will give you an error/warning that you haven't handled all the cases in your switch

Here's an example:

```c
switch (logLevel) {
  case LOG_DEBUG:
    printf("Debug logging enabled\n");
    break;
  case LOG_INFO:
    printf("Info logging enabled\n");
    break;
  case LOG_WARN:
    printf("Warning logging enabled\n");
    break;
  case LOG_ERROR:
    printf("Error logging enabled\n");
    break;
  default:
    printf("Unknown log level: %d\n", logLevel);
    break;
}
```

You'll notice that we have a `break` after each case. If you do **not** have a `break` (or `return`), the next case will _still execute_: it "falls through" to the next case. Many devs have written bugs when using switch statements, because they forgot to add `break`.

In some rare cases, you might want the fallthrough:

```c
switch (errorCode) {
  case 1:
  case 2:
  case 3:
    // 1, 2, and 3 are all minor errors
    printf("Minor error occurred. Please try again.\n");
    break;
  case 4:
  case 5:
    // 4 and 5 are major errors
    printf("Major error occurred. Restart required.\n");
    break;
  default:
    printf("Unknown error.\n");
    break;
}
```

But usually, it's a footgun. You'll almost always want a `break` at the end of each case statement.

## Assignment

Complete the `http_to_str` function. Given the enum defined in `http.h`, it should return a hard-coded string (`char *`) with the human-readable version of the HTTP status code:

1. [ ] `HTTP_BAD_REQUEST`: "400 Bad Request"
2. [ ] `HTTP_UNAUTHORIZED`: "401 Unauthorized"
3. [ ] `HTTP_NOT_FOUND`: "404 Not Found"
4. [ ] `HTTP_TEAPOT`: "418 I AM A TEAPOT!"
5. [ ] `HTTP_INTERNAL_SERVER_ERROR`: "500 Internal Server Error"
6. [ ] Default case: "Unknown HTTP status code"

```c
#include "http.h"
char *http_to_str(http_error_code_t code) {
  char *readable_str = "";
  switch (code){
    case HTTP_BAD_REQUEST:
      readable_str = "400 Bad Request";
      break;
    case HTTP_UNAUTHORIZED:
      readable_str = "401 Unauthorized";
      break;
    case HTTP_NOT_FOUND:
      readable_str = "404 Not Found";
      break;
    case HTTP_TEAPOT:
      readable_str = "418 I AM A TEAPOT!";
      break;
    case HTTP_INTERNAL_SERVER_ERROR:
      readable_str = "500 Internal Server Error";
      break;
    default:
      readable_str = "Unknown HTTP status code";
      break;
  }
  return readable_str;
}

```

# Sizeof Enum

The same [`sizeof`](https://en.cppreference.com/w/c/language/sizeof) operator that we've talked about works on enums.

Generally, enums in C are the same size as an `int`. However, if an enum value exceeds the range of an `int`, the C compiler will use a [larger integer type](https://en.cppreference.com/w/c/language/type) to accommodate the value, such as an `unsigned int` or a `long`.

- [`unsigned int`](https://en.wikipedia.org/wiki/C_data_types#:~:text=unsigned-,unsigned%20int,-Basic%20unsigned%20integer) doesn't represent negative numbers, so it can represent larger positive numbers.
- [`long`](https://en.wikipedia.org/wiki/C_data_types#:~:text=%5B8%5D-,long,-long%20int) is just a larger integer type than `int`, so it can represent larger numbers.

## Just Fancy Integers

Enums are often used to represent the possibilities in a set. For example:

- `SMALL` = 0
- `MEDIUM` = 1
- `LARGE` = 2
- `EXTRA_LARGE` = 3

Your code probably cares a lot about _which size_ a variable represents, but it probably doesn't care that `SMALL` happens to be `0` under the hood. From the compiler's perspective, enums are just fancy integers.

## Assignment

At the start of `main()`, print the size of the two enums already defined for you, in the format:

```text
The size of BigNumbers is Y bytes
The size of HttpErrorCode is X bytes
```

_Remember that `%zu` is the format specifier for `size_t`_.

```c
#include <stdio.h>

typedef enum {
  BIG = 123412341234,
  BIGGER,
  BIGGEST,
} BigNumbers;

typedef enum {
  HTTP_BAD_REQUEST = 400,
  HTTP_UNAUTHORIZED = 401,
  HTTP_NOT_FOUND = 404,
  HTTP_I_AM_A_TEAPOT = 418,
  HTTP_INTERNAL_SERVER_ERROR = 500
} HttpErrorCode;

int main() {
  printf("The size of BigNumbers is %zu bytes\n",sizeof(BigNumbers));
  printf("The size of HttpErrorCode is %zu bytes\n",sizeof(HttpErrorCode));
  return 0;
}

```


# Union

Now that we understand `struct`s and `enum`s, we can learn about `union`s: a combination of the two concepts.

This is not the kind of union that $300k-earning Google employees fight for because they "don't have enough oat milk in the office kitchen." No, this feature is one that even Golang doesn't have (probably because they were worried about getting fired from Google for just mentioning the word!).

Unions in C can hold one of several types. They're like a less-strict [sum type](https://en.wikipedia.org/wiki/Algebraic_data_type) from the world of functional programming. Here's an example union:

```c
typedef union AgeOrName {
  int age;
  char *name;
} age_or_name_t;
```

The `age_or_name_t` type can hold _either_ an `int` or a `char *`, but not both at the same time (that would be a struct). We provide the list of possible types so that the C compiler knows the _maximum_ potential memory requirement, and can account for that. This is how the union is used:

```c
age_or_name_t lane = { .age = 29 };
printf("age: %d\n", lane.age);
// age: 29
```

Here's where it gets interesting. What happens if we try to access the `name` field (even though we _set_ the `age` field)?

```c
printf("name: %s\n", lane.name);
// name:
```

We get... nothing? To be more specific, we get undefined behavior. A `union` only reserves enough space to hold the largest type in the union and then _all_ of the fields **use the same memory**. So when we set `.age` to 29, we are writing the integer representation of `29` to the memory of the `lane` union:

```text
0000 0000 0000 0000 0000 0000 0001 1101
```

Then if we try to _access_ `.name`, we read from the **same block of memory** but try to interpret the bytes as a `char *`, which is why we get garbage (which is interpreted as nothing in this case). **Put simply, setting the value of `.age` overwrites the value of `.name` and vice versa, and you should only access the field that you set**.

## Assignment

`Sneklang` is going to need objects. We'll hand-code those objects, and Sneklang developers will use them to store dynamic variables, kinda like Python. Everything is an object, even simple integers and strings!

Take a look at the `SnekObject` struct in `exercise.h`. It has a `kind` field that stores the type of the object (like `INTEGER` or `STRING`) and a `data` field that stores the actual data.

1. [ ] Create a `snek_object_kind_t` enum type in `exercise.h`. It's the one used as the `kind` field of the provided `SnekObject`. It's an enum that can be an `INTEGER` (`0`) or a `STRING` (`1`).
2. [ ] Complete the `format_object` function in `exercise.c` that uses a `switch` on the `.kind` of a `snek_object_t` and writes a formatted string to the associated buffer.
    1. [ ] For an integer, write the string `int:N` to the buffer, replacing `N` with the integer value
    2. [ ] For a string, write the string `string:STR` to the buffer, replacing `STR` with the string value

You can use [`sprintf`](https://en.cppreference.com/w/c/io/fprintf#sprintf) to write the formatted string to the buffer. For example:

```c
char buffer[100];
sprintf(buffer, "There are %d lights!", 4); // There are 4 lights!
```

```c
#include "exercise.h"
#include <stdio.h>

void format_object(snek_object_t obj, char *buffer) {
  switch(obj.kind){
    case INTEGER:
      sprintf(buffer, "int:%d", obj.data.v_int);
      break;
    case STRING:
      sprintf(buffer, "string:%s", obj.data.v_string);
      break;
    default:
      printf("Nothing");
      break;
  }
}

// don't touch below this line

snek_object_t new_integer(int i) {
  return (snek_object_t){
      .kind = INTEGER,
      .data = {.v_int = i},
  };
}

snek_object_t new_string(char *str) {
  // NOTE: We will learn how to copy this data later.
  return (snek_object_t){
      .kind = STRING,
      .data = {.v_string = str},
  };
}

```


# Memory Layout

Unions store their value in the same memory location, no matter which field or type is actively being used. That means that accessing any field apart from the one you set is generally a **bad idea**.

## Assignment

Take a look at the `val_or_err_t` union. It represents either an integer value _or_ an unsigned (non-negative) integer error code.

1. Run the code in its current state.
    
    Notice that the `.value` field is set to `-420`, then the data in each field is printed. The `.value` field works as you'd expect, printing `-420`. However, the `.err` field prints `4294966876`! It's trying to interpret the bytes of `-420` as an unsigned integer, which results in a very large number.
    
2. Uncomment the next block of code, and run it without submitting.
    
    Notice that now we set the `.err` field (an unsigned integer) to `UINT_MAX`, which is a constant representing the largest possible unsigned integer (`4294967295` in my case). As expected, the `.err` field prints `4294967295`. However, the `.value` field prints `-1`! It's reading the bytes for `4294967295` as a signed integer instead of an unsigned one, which turns it into `-1`.
    

**Submit the fully uncommented code.**

```c
#include "limits.h"
#include "munit.h"
#include <stdio.h>

typedef union {
  int value;
  unsigned int err;
} val_or_err_t;

int main() {
  val_or_err_t lanes_score = {.value = -420};
  printf("value (set): %d\n", lanes_score.value);
  printf("err (unset): %u\n", lanes_score.err);

  val_or_err_t teejs_score = {
    .err = UINT_MAX
  };
  printf("value (unset): %d\n", teejs_score.value);
  printf("err (set): %u\n", teejs_score.err);
}

```


# Union Size

A downside of unions is that the size of the union is the size of the _largest_ field in the union. Take this example:

```c
typedef union IntOrErrMessage {
  int data;
  char err[256];
} int_or_err_message_t;
```

This `IntOrErrMessage` union is designed to hold an `int` 99% of the time. However, when the program encounters an error, instead of storing an integer here, it will store an error message. The trouble is that it's incredibly inefficient because it allocates 256 bytes for every `int` that it stores!

Imagine an array of 1000 `int_or_err_message_t` objects. Even if none of them make use of the `.err` field, the array will take up `256 * 1000 = 256,000` bytes of memory! An array of `int`s would have only taken `4,000` bytes (assuming 32-bit integers).

## Quiz Examples

_Assume the following_:

- `sizeof(int) = 4`
- `sizeof(char) = 1`
- `sizeof(long int) = 8`

```c
union SensorData {
  long int temperature;
  long int humidity;
  long int pressure;
};
```

```c
union PacketPayload {
  char text[256];
  unsigned char binary[256];
  struct ImageData {
    int width;
    int height;
    unsigned char data[1024];
  } image;
};
```

```c
union Item {
  struct {
    int damage;
    int range;
    int size;
  } weapon;
  struct {
    int healingAmount;
    int duration;
  } potion;
  struct {
    int doorID;
  } key;
};
```

# Helper Fields

One interesting (albeit not commonly used) trick is to use unions to create "helpers" for accessing different parts of a piece of memory. Consider the following:

```c
typedef union Color {
  struct {
    uint8_t r;
    uint8_t g;
    uint8_t b;
    uint8_t a;
  } components;
  uint32_t rgba;
} color_t;
```

It results in a memory layout like this:

Only 4 bytes are used. And, unlike in 99% of scenarios, it makes sense to both set _and_ get values from this union through both the `components` and `rgba` fields! Both fields in the union are exactly 32 bits in size, which means that we can "safely" (?) access the entire set of colors through the `.rgba` field, or get a single color component through the `.components` field.

The convenience of additional fields, with the efficiency of a single memory location!

and the fragility of C...

## Assignment

Sneklang has support for networking!

Complete the `PacketHeader` union. It should have two potential fields:

1. [ ] `tcp_header`: A struct:
    1. [ ] The first 2 bytes are the `src_port`.
    2. [ ] The next 2 bytes are the `dest_port`.
    3. [ ] The last 4 bytes are the `seq_num`.
2. [ ] `raw`: An array of 8 integers that are each 1 byte in size.

_Use `uint8_t`, `uint16_t`, and `uint32_t` for the types of the fields, based on the number of bytes needed. Remember, 8 bits = 1 byte._

```c
#include <stdint.h>

typedef union PacketHeader {
  struct {
    uint16_t src_port;
    uint16_t dest_port;
    uint32_t seq_num;
  } tcp_header;
  char raw[8];
} packet_header_t;

```
# The Stack

Remember how I told you that memory is basically just a giant array of bytes with addresses at various offsets?

That's true, but it also has some additional structure. In particular, memory is divided into two main regions: the **stack** and the **heap**. We'll cover the heap later.

The stack is where local variables are stored. When a function is called, a new **stack frame** is created in memory to store the function's parameters and local variables. When the function returns, its entire stack frame is deallocated.

The stack is aptly named: it is a **stack** (the "Last In, First Out" data structure) of memory frames. Each time a function is called, a new frame is pushed onto the stack. When the function returns, its frame is popped off the stack.

Take a look at this example function:

```c
void create_typist(int uses_nvim) {
  int wpm = 150;
  char name[4] = {'t', 'e', 'e', 'j'};
}
```

Say we call `create_typist(1)`. Before the call, our stack memory might look like this, with the next memory address to be used `0x0004`:

Once called, the [stack pointer](https://en.wikipedia.org/wiki/Stack_pointer) is moved to make room for:

- The [return address](https://en.wikipedia.org/wiki/Return_statement) (to pick up execution after the function returns)
- Arguments to the function
- Local variables in the function body

and the local variables are stored in the stack frame:

When the function returns, the stack frame is deallocated by resetting the stack pointer to where the frame began.

## Assignment

1. Run the code in its current state.
    
    See how with each successive nested function call (`printMessageOne`, which calls `printMessageTwo`, which calls `printMessageThree`) the memory addresses allocate more and more space?
    
2. Update _where_ `printMessageTwo` and `printMessageThree` are called from so that all three of the functions use the same stack space.
    
    The offsets printed by `printStackPointerDiff` should now be different from before. The `printStackPointerDiff()` calls should remain at the start of each function.
    

## Tip

The print message functions should _not_ call each other because that creates a new stack frame on top of the existing one. They should be called sequentially from the main function.
![[Pasted image 20260813141935.png]]
![[Pasted image 20260813141939.png]]
![[Pasted image 20260813141945.png]]

```c
#include "exercise.h"
#include <stdio.h>

int main() {
  printMessageOne();
  printMessageTwo();
  printMessageThree();
  return 0;
}

// __attribute__((noinline)) helps the compiler behave; don't worry about it
__attribute__((noinline)) void printMessageOne(void) {
  const char *message = "Dark mode?\n";
  printStackPointerDiff();
  printf("%s\n", message);
}

__attribute__((noinline)) void printMessageTwo(void) {
  const char *message = "More like...\n";
  printStackPointerDiff();
  printf("%s\n", message);
}

__attribute__((noinline)) void printMessageThree(void) {
  const char *message = "dark roast.\n";
  printStackPointerDiff();
  printf("%s\n", message);
}

// don't touch below this line

void printStackPointerDiff(void) {
  static void *last_sp = NULL;
  void *current_sp;
  current_sp = __builtin_frame_address(0);
  long diff;
  if (last_sp == NULL) {
    last_sp = current_sp;
    diff = 0;
  } else {
    diff = (char *)last_sp - (char *)current_sp;
  }
  printf("---------------------------------\n");
  printf("Stack pointer offset: %ld bytes\n", diff);
  printf("---------------------------------\n");
}

```

# Why a Stack?

Allocating memory on the stack is preferred when possible because the stack is faster and simpler than the heap (which we'll get to, be patient):

- **Efficient Pointer Management:** Stack "allocation" is just a quick increment or decrement of the stack pointer, which is extremely fast. Heap allocations require more complex bookkeeping.
- **Cache-Friendly Memory Access:** Stack memory is stored in a contiguous block, enhancing cache performance due to spatial locality. Related values live next to each other in memory, so the CPU can load and access them more quickly.
- **Automatic Memory Management:** Stack memory is managed automatically as functions are called and as they return.
- **Inherent Thread Safety:** Each thread has its own stack. Heap allocations require synchronization mechanisms when used concurrently, potentially introducing overhead.

One reason Go programs are efficient is that Go uses stack allocation for variables when possible, much like C. The Go compiler performs escape analysis to decide whether a variable can be allocated on the stack. On the other hand, languages like Python allocate most objects on the heap, which can impact performance.

# Stack Overflow

So the stack is great and all, but one of the downsides is that it has a limited size. If you keep pushing frames onto the stack without popping them off, you'll eventually run out of memory and get a [**stack overflow**](https://en.wikipedia.org/wiki/Stack_overflow). (yes, that's what the [famous site](https://stackoverflow.com/) is named after)

That's one of the reasons recursion without [tail-call optimization](https://en.wikipedia.org/wiki/Tail_call) can be dangerous. Each recursive call pushes a new frame onto the stack, and if you have too many recursive calls, you'll run out of stack space.

## Assignment

Sneklang is admittedly a fairly inefficient language (don't tell the VC investors!). Sometimes, rather than carefully managing memory, the Sneklang interpreter allocates a big chunk of stack data – simply because the creators (us) are too lazy to allocate the right amount.

Anyhow, the BDFL of Sneklang has allowed this laziness, but only to a maximum amount of 10 kibibytes. A single kibibyte is 1024 bytes.

1. [ ] Run the starting code in its current state. You should get a stack overflow which will cause a [segmentation fault](https://en.wikipedia.org/wiki/Segmentation_fault).
2. [ ] Fix the `pool_size` so that it allocates exactly 10 kibibytes.
```c
#include <stdio.h>

int main() {
  const int pool_size = 1024 * 10;
  char snek_pool[pool_size];
  snek_pool[0] = 's';
  snek_pool[1] = 'n';
  snek_pool[2] = 'e';
  snek_pool[3] = 'k';
  snek_pool[4] = '\0';

  printf("Size of pool: %d\n", pool_size);
  printf("Initial string: %s\n", snek_pool);
  return 0;
}

```


# Pointers to the Stack

So we know that stack frames are always getting pushed and popped, and as a result, memory addresses on the stack are always changing and getting reused.

_Remember: the stack is only safe to use within the context of the current function!_

## Assignment

Let's get back to Sneklang's built in 2D graphics library. Take a look at the `new_coord` function. It accepts an `x` and `y` value and creates a new pointer to a stack-allocated `coord_t` struct.

1. Run the code in its current state. You should see something... weird. Why don't the `x` and `y` values match the ones passed in on lines 20–22???
    
    Because we're accessing stack memory (the pointer created on line 16) outside of the function that created it, the memory has been deallocated and is no longer safe to use. Technically the behavior is undefined, but it's likely that in this specific scenario you're just seeing it get overwritten by the next function call (thus `50` and `60` always print).
    
1. Fix the `new_coord` function so that it returns a struct, not a pointer to a struct. This will force the compiler to copy the struct to the `main` function's stack frame, and the memory will be safe to use. You'll have to update syntax in a few places to accommodate the change.


```c
#include <stdio.h>

typedef struct {
  int x;
  int y;
} coord_t;

__attribute__((noinline))

// Don't touch above this line

coord_t new_coord(int x, int y) {
  coord_t c;
  c.x = x;
  c.y = y;
  return c;
}

int main() {
  coord_t c1 = new_coord(10, 20);
  coord_t c2 = new_coord(30, 40);
  coord_t c3 = new_coord(50, 60);

  printf("c1: %d, %d\n", c1.x, c1.y);
  printf("c2: %d, %d\n", c2.x, c2.y);
  printf("c3: %d, %d\n", c3.x, c3.y);
}
```

# The Heap

Click to show video

Your browser does not support playing HTML5 video. You can instead. Here is a description of the content: best place to store in memory data

["The heap"](https://en.wikipedia.org/wiki/Memory_management#Dynamic_memory_allocation), as opposed to "the stack", is a pool of long-lived memory shared across the entire program. Stack memory is automatically allocated and deallocated as functions are called and returned, but heap memory is allocated and deallocated as-needed, independent of the burdensome shackles of function calls.

When you need to store data that outlives the function that created it, you'll send it to the heap. The heap is called "dynamic memory" because it's allocated and deallocated as needed. Take a look at `new_int_array`:

```c
int *new_int_array(int size) {
  int *new_arr = malloc(size * sizeof(int)); // Allocate memory
  if (new_arr == NULL) {
    fprintf(stderr, "Memory allocation failed\n");
    exit(1); // Exit if allocation fails
  }
  return new_arr;
}
```

Because the size of the array isn't known at compile time, we can't put it on the stack. Instead, we allocate memory on the heap using the `<stdlib.h>`'s [`malloc`](https://en.cppreference.com/w/c/memory/malloc) function. It takes a number of bytes to allocate as an argument (`size * sizeof(int)`) and returns a pointer to the allocated memory (a `void *` that is automatically converted to an `int *` when assigned). Here's a diagram of what happened in memory:

The `new_int_array` function's `size` argument is just an integer, it's pushed onto the stack. Assuming `size` is `6`, when `malloc` is called we're given enough memory to store 6 integers on the heap, and we're given the address of the start of that newly allocated memory. We store it in a new local variable called `new_arr`. The address is stored on the stack, but the data it points to is in the heap.

Let's look at some code that uses `new_int_array`:

```c
int* arr_of_6 = new_int_array(6);
arr_of_6[0] = 69;
arr_of_6[1] = 42;
arr_of_6[2] = 420;
arr_of_6[3] = 1337;
arr_of_6[4] = 7;
arr_of_6[5] = 0;
```

The data is stored in the heap:

When we're done with the memory, we need to manually deallocate it using the `<stdlib.h>`'s [`free`](https://en.cppreference.com/w/c/memory/free) function:

```c
free(arr_of_6);
```

The `free` function returns (deallocates) that memory for use elsewhere. It's important to note that the pointer (`arr_of_6`) still exists, but shouldn't be used. It's a "dangling pointer", pointing to deallocated memory.

## Assignment

1. [ ] Run the `get_full_greeting` function in its current state. If you take a look at the `main.c` file, you'll notice that it's testing to ensure that a pointer to stack memory isn't returned (which you never should do, because it's undefined behavior).
2. [ ] Fix the `get_full_greeting` function so that it allocates memory on the heap and returns a pointer to _that_ memory. Use the provided `size` parameter to allocate enough space for the resulting string, be sure to account for the size of each `char`.

Use [snprintf](https://cplusplus.com/reference/cstdio/snprintf/) to write the formatted output to a buffer. Remember to pass in the `size` rather than the hard-coded `100`.
![[Pasted image 20260813172704.png]]![[Pasted image 20260813172709.png]]
![[Pasted image 20260813172716.png]]
```c
#include "exercise.h"
#include <stdio.h>
#include <stdlib.h>

char *get_full_greeting(char *greeting, char *name, int size) {
  char *full_greeting = malloc(size * sizeof(char));
  snprintf(full_greeting, size, "%s %s", greeting, name);
  return full_greeting;
}

```

# Malloc

The [`malloc` function](https://en.cppreference.com/w/c/memory/malloc) (`m`emory `alloc`ation) is a standard library function in C that allocates a specified number of bytes of memory on the heap and returns a pointer to the allocated memory.

This new memory is **uninitialized**, which means:

- It contains whatever data was previously at that location.
- It is the programmer's responsibility to ensure that the allocated memory is properly initialized and eventually freed using [`free`](https://en.cppreference.com/w/c/memory/free) to avoid memory leaks.

If you want to make sure that the memory is properly initialized, you can use the `calloc` function, which allocates the specified number of bytes of memory on the heap and returns a pointer to the allocated memory. This memory is initialized to zero (meaning it contains all zeroes).

## Function Signature

```c
void* malloc(size_t size);
```

- `size`: The number of bytes to allocate.
- Returns: A pointer to the allocated memory or `NULL` if the allocation fails.

## Example Usage

```c
// Allocates memory for an array of 4 integers
int *ptr = malloc(4 * sizeof(int));
if (ptr == NULL) {
  // Handle memory allocation failure
  printf("Memory allocation failed\n");
  exit(1);
}
// use the memory here
// ...
free(ptr);
```

## Manual Memory Management

This idea of manually calling `malloc` and `free` is what puts the "manual" in "manually managing memory":

- The programmer must remember to eventually free the allocated memory using `free(ptr)` to avoid memory leaks.
- Otherwise, that allocated memory is never returned to the operating system for use by other programs. (Until the program exits, at which point the operating system will clean up after it, but that's not ideal.)

Manually managing memory can be error-prone and tedious, but languages that automatically manage memory (like Python, Java, and C#) have their own trade-offs, usually in terms of performance.

## Assignment

We're working on some of the dynamic memory management tooling that we'll eventually need to build a garbage collector for Sneklang.

Complete the `allocate_scalar_array` function. It should:

1. [ ] Accept `size` and `multiplier` parameters and should allocate an array of `size` integers on the heap.
2. [ ] Gracefully return `NULL` if the allocation fails.
3. [ ] Initialize each element in the array to the `index * multiplier`. (e.g. a multiplier of 2 would result in `[0, 2, 4, 6, ...]`)
4. [ ] Return a pointer to the allocated memory.

_Assume that the calling code will eventually call `free` on the returned pointer._

```c
#include "exercise.h"
#include <stdio.h>
#include <stdlib.h>

int *allocate_scalar_array(int size, int multiplier) {
  int *arr = malloc(size * sizeof(int));
  if (arr == NULL){
    printf("Memory allocation failed");
    exit(1);
  }
  for (int i = 0; i < size; i++){
    arr[i] = i * multiplier;
  }
  return arr;
}

```

# Free

The [`free`](https://en.cppreference.com/w/c/memory/free) function deallocates memory that was previously allocated by [`malloc`](https://en.cppreference.com/w/c/memory/malloc), [`calloc`](https://en.cppreference.com/w/c/memory/calloc), or [`realloc`](https://en.cppreference.com/w/c/memory/realloc).

```c
int *ptr = malloc(4 * sizeof(int));
free(ptr);
```

**IMPORTANT:** `free` does not change the **value** stored in the memory, and it doesn't even change the address stored in the pointer. Instead, it simply informs the operating system that the memory can be used again.

## Forgetting to free

Forgetting to call `free` leads to a memory leak. This means that the allocated memory remains occupied and cannot be reused, even though the program no longer needs it. Over time, if a program continues to allocate memory without freeing it, the program may run out of memory and crash.

Memory leaks are one of the most common bugs in C programs, and they can be difficult to track down because the memory is still allocated and accessible, even though it is no longer needed.

## Assignment

We may be inefficient here at Sneklang, but we don't want outright memory leaks!

1. Run the code in its current state. After a number of successful allocations you should get a failure. The program is running out of memory due to a leak.
    
    See how it's calling the `allocate_scalar_list` function in a loop? Well, the lists aren't needed from loop to loop, so they should be freed at the end of each iteration. If we do that, we should be able to allocate as many lists as we want (because we return the memory in between iterations).
    
1. Fix the code by freeing the allocated list at the end of each loop.
```c
#include "exercise.h"
#include <stdio.h>
#include <stdlib.h>

int main() {
  const int num_lists = 500;
  for (int i = 0; i < num_lists; i++) {
    int *lst = allocate_scalar_list(50000, 2);
    if (lst == NULL) {
      printf("Failed to allocate list\n");
      return 1;
    } else {
      printf("Allocated list %d\n", i);
    }
    free(lst);
  }
  return 0;
}
```

# Big Endian and Little Endian

While we are on the topic of memory, it's worth knowing about "endianness". Endianness is the order in which bytes are stored in memory. The two most common formats are big endian and little endian.

## Big Endian

In a big-endian system, the most significant byte is stored first, at the lowest memory address. The "most significant byte" is just a fancy way of saying "the biggest part of the number".

Let's say you have the hexadecimal number `0x12345678`. Here's how it would be stored in big-endian format:

  
The most significant byte (`0x12`) is stored at the lowest memory address.

## Little Endian

In a little-endian system, the least significant byte (the "smallest" part of the number) is stored first, at the lowest memory address. This is the format used by most modern computers.

Using the same number `0x12345678`, here's how it would be stored in little-endian format:

  
Here, the least significant byte (`0x78`) is stored first.

For the most part, you won't have to worry about endianness when writing programs. The way data is read from memory automatically handles this, so we can spend our valuable time building e-commerce shops for the terminal instead. Endianness becomes important in certain scenarios, like networking and working with binary files.

For now, just know that most modern systems use little-endian, and the compiler takes care of how data is stored and accessed.
![[Pasted image 20260813204427.png]]![[Pasted image 20260813204431.png]]

# Pointer-Pointers

Ok, so... now we know what pointers are. So let's learn it over again! A pointer-to-pointer in C is just a pointer variable that holds the address of another pointer.

Click to show video

Your browser does not support playing HTML5 video. You can instead. Here is a description of the content: Pointer pointers are easy

This allows you to create complex data structures like arrays of pointers, and to modify pointers indirectly. The syntax is exactly what you would expect:

```c
int value;
int *pointer;
int **pointer_pointer;
```

Pointers to pointers (or pointers to pointers to pointers to pointers... you get the idea) are like a treasure map or a scavenger hunt. You start at one pointer and keep following the chain of addresses until you get to the final value. Each `*` follows one address: `*pointer_pointer` gets the inner `int *`, and `**pointer_pointer` gets the final `int`.

### Pointers in Memory

A pointer is a variable whose stored value is another variable's address.

ptr_to_ptr selected — choose an outlined int * cell.

|Variable|Type|Memory address|Value|
|---|---|---|---|
|Variable name for age|Type for age|0x10004096|Value for age|
|Variable name for score|Type for score|0x10084104|Value for score|
|Variable name for ptr_to_age|Type for ptr_to_age|0x10184120|Value for ptr_to_age|
|Variable name for ptr_to_score|Type for ptr_to_score|0x10204128|Value for ptr_to_score|
|Variable name for ptr_to_ptr|Type for ptr_to_ptr|0x10284136|Value for ptr_to_ptr|

## Assignment

Complete the `allocate_int` function. It accepts a pointer to a pointer to an integer called `pointer_pointer`, and a raw value. Update the pointer that `pointer_pointer` points to so it stores the address of newly allocated memory containing `value`.

1. [ ] Allocate memory for a single integer on the heap, and save its address into a new pointer.
2. [ ] Update the pointer that pointer_pointer is pointing at to hold the newly allocated memory address.
3. [ ] Set the raw value of the integer that `pointer_pointer` now points to (well, that it points to through 2 address hops) to the value passed in.

_Observe: If you take a look at `test_does_not_overwrite` in the `main.c` file, you'll notice that while `pointer_pointer` does indeed unravel and point to the new value, the original value still exists at its spot in memory. We just don't point to it anymore._

```c
#include "exercise.h
#include "stdlib.h"

void allocate_int(int **pointer_pointer, int value) {
  int *ptr = malloc(sizeof(int));
  *pointer_pointer = ptr;
  **pointer_pointer = value;
}

```

note
```
`&` is only needed to get the address of a variable that already exists (like `&meaning_of_life`). `malloc` doesn't work that way — it directly _returns_ an address (of newly allocated heap memory), not a variable you then need to take the address of.
```

# Array of Pointers

Making an array of integers on the heap is pretty simple:

```c
int *int_array = malloc(sizeof(int) * 3);
int_array[0] = 1;
int_array[1] = 2;
int_array[2] = 3;
```

But we can also make an array of pointers! It's quite common to do this in C, especially considering that strings are just pointers to `char`s:

```c
char **string_array = malloc(sizeof(char *) * 3);
string_array[0] = "foo";
string_array[1] = "bar";
string_array[2] = "baz";
```

## Assignment

Sneklang, being a super-robust programming language toolchain, needs to represent "Tokens" – strings of text that represent Sneklang syntax, things like `if`, `else` and `def`. They're represented as structs, you can see the struct in `exercise.h`.

Take a look at `create_token_pointer_array`. It correctly allocates an array of token pointers on the heap, but notice that the addresses it's adding to each index are the addresses of the stack-allocated inputs.

1. [ ] Update the `create_token_pointer_array`'s loop to allocate _new_ space for each token on the heap.
2. [ ] Store the address of the new space in the array instead of the stack address.
3. [ ] Copy the members of the input struct into the newly allocated one.
```c
#include "exercise.h"
#include <stdlib.h>

token_t **create_token_pointer_array(token_t *tokens, size_t count) {
  token_t **token_pointers = malloc(count * sizeof(token_t *));
  if (token_pointers == NULL) {
    exit(1);
  }
  for (size_t i = 0; i < count; ++i) {
    token_t *new_ptr = malloc(sizeof(token_t));
    token_pointers[i] = new_ptr;
    *new_ptr = tokens[i];
  }
  return token_pointers;
}

```

indivdual copy to new allocated heap space
```c
#include "exercise.h"
#include <stdlib.h>

token_t **create_token_pointer_array(token_t *tokens, size_t count) {
  token_t **token_pointers = malloc(count * sizeof(token_t *));
  if (token_pointers == NULL) {
    exit(1);
  }
  for (size_t i = 0; i < count; ++i) {
    token_t *new_ptr = malloc(sizeof(token_t));
    token_pointers[i] = new_ptr;
    new_ptr->literal = tokens[i].literal;
    new_ptr-> line = tokens[i].line;
    new_ptr -> column = tokens[i].column;
  }
  return token_pointers;
}

```

# Void Pointers

We've already discussed `void`, which essentially means "nothing" in C. It's used in a few different contexts:

- `void update_soldier(soldier_t *s)`: means the function returns nothing
- `soldier_t new_soldier(void)`: means the function takes no arguments.

And, because C likes re-using ideas but with slightly different meanings (the genius of the design can't be understood by us mere mortals) `void` also has another use!

A `void *` "void pointer" tells the compiler that this pointer could point to **anything**. This is why void pointers are also known as a "generic pointer". Since void pointers do not have a specific data type, they cannot be directly dereferenced or used in pointer arithmetic without casting them to another pointer type first.

## Casting to Void Pointers

Casting to and from void pointers in C is unique because void pointers are type-agnostic. When casting a specific type pointer to a void pointer, no type information is retained, allowing the void pointer to point to any data type. However, you **must** cast a void pointer back to its original type before dereferencing it, as direct dereferencing is not possible.

```c
int number = 42;
void *generic_ptr = &number;

// This doesn't work
printf("Value of number: %d\n", *generic_ptr);

// This works: Cast to appropriate type before dereferencing
printf("Value of number: %d\n", *(int*)generic_ptr);
```

A common pattern is to store generic data in one variable, and the type of that data in another variable. This is useful when you need to pass data around without knowing its type at compile time.

```c
typedef enum DATA_TYPE {
  INT,
  FLOAT
} data_type_t;

void printValue(void *ptr, data_type_t type) {
  if (type == INT) {
    printf("Value: %d\n", *(int*)ptr);
  } else if (type == FLOAT) {
    printf("Value: %f\n", *(float*)ptr);
  }
}

int number = 42;
printValue(&number, INT);

float decimal = 3.14;
printValue(&decimal, FLOAT);
```

## Assignment

In Sneklang, we have to dynamically interpret Snek code and store the values in memory. The `snek_object_kind_t` enum defines the different types of objects that can be stored in memory.

Complete the `snek_zero_out` function. It accepts a generic pointer to one of:

- `snek_int_t`
- `snek_float_t`
- `snek_bool_t`

It should "zero out" the `.value` field of the struct by setting it to the zero value of its type. Use the `kind` parameter to figure out which type of struct you are working with.

When working with pointers and dereferencing them, parentheses usage is essential. Consider the following examples:

- `((some_struct_t*)ptr)->field` means casting is applied to `ptr` and then the field is obtained.
- `(some_struct_t*)ptr->field` means casting is applied to `ptr->field`.
```c
#include "exercise.h"

void snek_zero_out(void *ptr, snek_object_kind_t kind) {
  if (kind == INTEGER){
    ((snek_int_t*)ptr)->value = 0;
  }else if (kind == FLOAT) {
    ((snek_float_t*)ptr)->value = 0.0;
  }else {
    ((snek_bool_t*)ptr)->value=0;
  }
}

```
```c
typedef enum SnekObjectKind {
  INTEGER,
  FLOAT,
  BOOL,
} snek_object_kind_t;

typedef struct SnekInt {
  char *name;
  int value;
} snek_int_t;

typedef struct SnekFloat {
  char *name;
  long _pad;
  float value;
} snek_float_t;

typedef struct SnekBool {
  char *name;
  long _pad;
  unsigned int value;
} snek_bool_t;

void snek_zero_out(void *ptr, snek_object_kind_t kind);

```

# Swapping Integers

Sneklang makes it easy to swap two values:

```py
cool_person = "Lane"
uncool_person = "TJ"
cool_person, uncool_person = uncool_person, cool_person
print(cool_person)  # TJ
print(uncool_person)  # Lane
# (get rekt lane)
```

## Assignment

Before we do something more tricky, let's start with just swapping some integers. Complete the `swap_ints` function. It accepts two pointers to integers, and should swap the values of the integers they point to.

_You'll need to use a temporary variable to store one of the values while you swap them_.

```c
void swap_ints(int *a, int *b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}


```

# Swapping Strings

Let's take it up a notch. (okay, a half-notch, but still).

## Assignment

Complete the `swap_strings` function. It swaps the values stored in the string pointers.

Remember, `char **` is a `pointer` to a `char pointer`, which means we can simply switch the "address" that we're referencing in our `swap` function.

_You won't need to use any `str_` specific functions for this swap implementation._


```c
void swap_strings(char **a, char **b) {
  char *temp = *a;
  *a = *b;
  *b = temp;
}

```

# Generic Swap

For the previous `swap` implementations we've known the type of the data we want to swap. Because we knew the type, the compiler knew the sizes of the data we want to swap.

However, to make a generic swap, we will need to provide the C compiler with the size of the data that we are swapping because `void *` loses that type info. Our new interface for `swap` will include the size:

```c
void swap(void *vp1, void *vp2, size_t size);
```

The other problem we're going to have is that directly assigning pointer values does not work the same way with `void *`. Instead of using `*ptr1 = *ptr2`, we will use [`memcpy`](https://en.cppreference.com/w/c/string/byte/memcpy), which is included in the `string.h` library:

```c
void *memcpy(void *destination, void* source, size_t size);
```

So to move the data from `ptr2` to `ptr1`, we will use the following:

```c
memcpy(ptr1, ptr2, size);
```

## Assignment

Implement the generic `swap()` function.

1. [ ] Allocate memory for a temporary buffer to store the data using [`malloc`](https://en.cppreference.com/w/c/memory/malloc).
2. [ ] If the allocation fails (if it's `NULL`) return immediately.
3. [ ] Use `memcpy` to shuffle the data around.
4. [ ] Don't forget to [`free`](https://en.cppreference.com/w/c/memory/free) the temporary buffer.

```c
#include <stdlib.h>
#include <string.h>

void swap(void *vp1, void *vp2, size_t size) {
  void *mem_ptr = malloc(size);
  if (mem_ptr == NULL){
    return;
  }
  memcpy(mem_ptr, vp1, size);
  memcpy(vp1, vp2, size);
  memcpy(vp2, mem_ptr, size);
  free(mem_ptr);
}

```

# Low Level Stack

If you've taken our data structures course, you've already implemented a [stack](https://en.wikipedia.org/wiki/Stack_\(abstract_data_type\)). We're going to implement a stack again, but this time we're going to do it while manually managing the memory of generic pointers!

We'll get to have our first deeper exploration of "generics" in C (remember, that just means `void *`) as well as creating a data structure we will later use in our mark-and-sweep garbage collector.

## Assignment

Take a look at `snekstack.h`, specifically the `Stack` struct.

- `count` is the number of elements in the stack.
- `capacity` is the number of elements the stack can hold before it needs to be resized in memory.
- `data` is a pointer to all the generic data.

Implement the `stack_new` function:

1. [ ] Allocate memory for a new `Stack` struct on the heap.
2. [ ] If allocation fails, return `NULL`.
3. [ ] Initialize the `count` to `0`.
4. [ ] Initialize the `capacity` to the given value.
5. [ ] Allocate enough memory for `capacity` number of `void *` pointers and assign it to the `data` field.
6. [ ] If the `data` allocation fails, free the `Stack` struct and return `NULL`.
7. [ ] Return the `Stack` struct pointer.
```c
#include "snekstack.h"
#include <stdlib.h>

stack_t *stack_new(size_t capacity) {
  stack_t *new_ptr = malloc(sizeof(stack_t));
  if (new_ptr == NULL){
    return NULL;
  }
  new_ptr->count = 0;
  new_ptr->capacity = capacity;
  new_ptr->data = malloc(capacity * sizeof(void*));
  if (new_ptr->data == NULL){
    free(new_ptr);
    return NULL;
  }
  return new_ptr;
}


```
``
```c
#include <stddef.h>

typedef struct Stack {
  size_t count;
  size_t capacity;
  void **data;
} stack_t;

stack_t *stack_new(size_t capacity);

```
# Stack Push

Ok, so let's actually store some data instead of just allocating memory for no practical purpose (a.k.a "haskell programming").

## Making Room

As you know, our stack has a `count` and a `capacity`... but what happens when the `count` is equal to the `capacity`? We need to make room for more data!

We'll take a simple approach: whenever we run out of capacity, we'll double it. That way we don't have to reallocate memory on every push. For example:

|Count|Capacity|Data|
|---|---|---|
|0|4|[-, -, -, -]|
|1|4|[1, -, -, -]|
|2|4|[1, 2, -, -]|
|3|4|[1, 2, 3, -]|
|4|4|[1, 2, 3, 4]|
|5|8|[1, 2, 3, 4, 5, -, -, -]|

## Assignment

Complete the `stack_push` function. It safe(ish)ly adds a new object to the top of the stack. Remember: the size of the `data` array is the `capacity` of the stack, and the number of elements that are actually in the stack is the `count` (which is less than or equal to the `capacity`).

1. [ ] If the stack's `count` is equal to the stack's `capacity`:
    1. [ ] Double the stack's `capacity`
    2. [ ] Reallocate enough memory for the stack's data using the new `capacity` (tip below on how to do this)
    3. [ ] If `realloc` fails, set the stack's capacity back and return from the function. The old data is still valid.
    4. [ ] If it succeeds, update the stack's `data` field to point to the new memory
2. [ ] Add the new object to the top of the stack (the `count`-th element in the array)
3. [ ] Increment the stack's `count`

## Tip

The [`realloc`](https://en.cppreference.com/w/c/memory/realloc) function is used to resize memory that was previously allocated with `malloc` or `calloc`. It takes a **pointer to the old memory** and the new size, and returns a pointer to the new memory:

```c
void *realloc(void *ptr, size_t size);
```

```c
int *smol_boi = malloc(10 * sizeof(int));
int *large_boi = realloc(smol_boi, 20 * sizeof(int));
```


```c
#include "snekstack.h"
#include <assert.h>
#include <stddef.h>
#include <stdlib.h>

void stack_push(stack_t *stack, void *obj) {
  if (stack->count == stack->capacity){
    size_t orig_capacity = stack->capacity;
    stack->capacity = stack->capacity * 2;
    void *new_mem = realloc(stack->data,stack->capacity * sizeof(void *));
    if (new_mem == NULL){
      stack->capacity = orig_capacity;
      return ;
    }
    stack->data = new_mem;
  }
  stack->data[stack->count] = obj;
  stack->count++;
  
}

// don't touch below this line

stack_t *stack_new(size_t capacity) {
  stack_t *stack = malloc(sizeof(stack_t));
  if (stack == NULL) {
    return NULL;
  }

  stack->count = 0;
  stack->capacity = capacity;
  stack->data = malloc(stack->capacity * sizeof(void *));
  if (stack->data == NULL) {
    free(stack);
    return NULL;
  }

  return stack;
}

```

# Stack Pop

As you _should_ know by now, items go on and off the stack from the same end. (last in, first out).

Don't worry, the pop method is much simpler than the push method in our case, because we don't have to worry about resizing the stack.

## Assignment

Complete the `stack_pop` function.

1. [ ] If the stack has no elements, return `NULL`.
2. [ ] Decrement the stack's `count`.
3. [ ] Return the top element of the stack (the `count`-th element in the array).

```c
#include "snekstack.h"
#include <assert.h>
#include <stddef.h>
#include <stdlib.h>

void *stack_pop(stack_t *stack) {
  if (stack->count == 0){
    return NULL;
  }
  stack->count--;
  return stack->data[stack->count];
  
}

// don't touch below this line'

void stack_push(stack_t *stack, void *obj) {
  if (stack->count == stack->capacity) {
    stack->capacity *= 2;
    void **temp = realloc(stack->data, stack->capacity * sizeof(void *));
    if (temp == NULL) {
      stack->capacity /= 2;

      exit(1);
    }
    stack->data = temp;
  }
  stack->data[stack->count] = obj;
  stack->count++;
  return;
}

stack_t *stack_new(size_t capacity) {
  stack_t *stack = malloc(sizeof(stack_t));
  if (stack == NULL) {
    return NULL;
  }

  stack->count = 0;
  stack->capacity = capacity;
  stack->data = malloc(stack->capacity * sizeof(void *));
  if (stack->data == NULL) {
    free(stack);
    return NULL;
  }

  return stack;
}

```
# Stack free

In C, we don't have a lot of abstractions at our disposal. There are no classes, destructors, functors, monads, made-up-category-theory-words, etc.

We've got _data_. And we've got _functions_. Just the way ~~God~~ Dennis Ritchie intended.

So, to make it easier to work with our `Stack`, we're going to build our own little `free` function that will clean up all the memory that we've allocated for our stack.

## Assignment

Complete the `stack_free` function.

1. [ ] If the stack is `NULL`, return immediately.
2. [ ] If the stack data is not `NULL`, free the stack data.
3. [ ] Free the stack itself.

You can assume all the elements inside the stack are already freed. That's not _our_ problem.

```c
#include "snekstack.h"
#include <assert.h>
#include <stddef.h>
#include <stdlib.h>

void stack_free(stack_t *stack) {
  if (stack == NULL){
    return;
  }
  free(stack->data);
  free(stack);
}

// don't touch below this line

void *stack_pop(stack_t *stack) {
  if (stack->count == 0) {
    return NULL;
  }

  stack->count--;
  return stack->data[stack->count];
}

void stack_push(stack_t *stack, void *obj) {
  if (stack->count == stack->capacity) {
    stack->capacity *= 2;
    void **temp = realloc(stack->data, stack->capacity * sizeof(void *));
    if (temp == NULL) {
      stack->capacity /= 2;
      exit(1);
    }
    stack->data = temp;
  }
  stack->data[stack->count] = obj;
  stack->count++;
  return;
}

stack_t *stack_new(size_t capacity) {
  stack_t *stack = malloc(sizeof(stack_t));
  if (stack == NULL) {
    return NULL;
  }

  stack->count = 0;
  stack->capacity = capacity;
  stack->data = malloc(stack->capacity * sizeof(void *));
  if (stack->data == NULL) {
    free(stack);
    return NULL;
  }

  return stack;
}

```


# Dangerous Push

Up until now, even though we made our stack with `void *`, you'll notice that we've only stored plain old `int` pointers. I want to show you that you can actually store _anything_ in the stack, even heterogeneous lists! That being said, this is usually a bad idea.

TJ likes to use words like "heterogeneous" to keep kids-who-don't-read-good at bay. He meant to say, "you can actually store _anything_ in the stack, even lists of different types of data!"

Now, we're going to do something _pretty gross_ to demonstrate the wise words of one of the philosophers of our time:

> With great power comes great responsibility.
> 
> -- Uncle Ben

I'm going to have you push an `int *` and a regular old `int` directly onto the stack (a bad idea). I just want to show you that you can store _anything_ in a `void *`, even values that aren't pointers at all.

## Assignment

Complete the `scary_double_push` function.

1. [ ] Push the value `1337` directly onto the stack using the `stack_push` function. You'll need to [cast](https://en.cppreference.com/w/c/language/cast) the value to a `void *`.
2. [ ] Allocate memory for a new `int` on the heap
3. [ ] Set the value to which the address points to `1024`
4. [ ] Push the int pointer onto the stack using the `stack_push` function

```c
#include "snekstack.h"
#include "stdlib.h"

void scary_double_push(stack_t *s) {
  stack_push(s,(void *)1337);
  int *new_ptr = malloc(sizeof(int));
  int val = 1024;
  *new_ptr = val;
  stack_push(s, (void *)new_ptr);
}

```


# Multiple Types

So we saw that we _can_ push both `int` and `int *` types into the same stack (again, a **bad idea**).

In this example, we'll see that not only can you push values and pointers into the same stack, but you can also push different types of values into the same stack.

This is once again a terrible idea, but the thrust of what we're getting at here is:

**C doesn't care what you put in memory, it's bytes all the way down.**

Fortunately, C doesn't let you do these conversions automatically... but it still lets you do them. When you're working with `void *`, you're working with raw memory addresses, and you can cast them to whatever you want.

## Assignment

Complete the `stack_push_multiple_types` function.

1. [ ] Allocate memory on the heap for a `float` and set the value to which it's pointed to `3.14`.
2. [ ] Push the `float *` onto the stack using `stack_push`.
3. [ ] Create a `char *` constant that points to the value: `Sneklang is blazingly slow!`
4. [ ] Get the length of the string for memory allocation.
    
    Remember to leave room for the null terminator (`\0`)!
    
5. [ ] Allocate memory for a `char *`.
6. [ ] Copy the value to the memory.
7. [ ] Push the pointer to the memory onto the stack using `stack_push`.

## Tip

Don't forget to use the `string.h` library when working with `char *` types.

```c
#include "snekstack.h"
#include "stdlib.h"
#include <string.h>

void stack_push_multiple_types(stack_t *s) {
  float *new_ptr = malloc(sizeof(float));
  *new_ptr = 3.14;
  stack_push(s, (void *)new_ptr);
  char *new_str = "Sneklang is blazingly slow!";
  size_t len_str = strlen(new_str) + 1;
  char *new_str_ptr = malloc(len_str);
  strcpy(new_str_ptr, new_str);
  stack_push(s, (void *)new_str_ptr);
}

```


# SnekObjects

Objects in C?!? No. Way.

_However_, Sneklang is built in C, and everything in Sneklang is an "object". To be clear, not a _class_ or _object-oriented programming_ object, but a higher-level data structure that _holds some metadata about itself_. For example, it will store:

- What type of data it holds (int, float, string, etc.)
- The size of the data it holds
- The data itself
- How many _references_ to itself exist (at least later, when we build our own garbage collector!)

That last point is critical! Because Sneklang is a garbage-collected language, we need to know how many references to an object exist so we can free it when it's no longer needed.

## Assignment

**Complete the missing definitions in `snekobject.h`** Here's a breakdown of all that this file should define:

1. [ ] An [enum](https://devdocs.io/c/language/enum) called `snek_object_kind_t` with a single value, `INTEGER`.
2. [ ] A [union](https://devdocs.io/c/language/union) called `snek_object_data_t` with a single member, an integer named `v_int`.
3. [ ] A [struct](https://devdocs.io/c/language/struct) declaration called `snek_object_t` with two members:
    1. [ ] A member of type `snek_object_kind_t` named `kind`.
    2. [ ] A member of type `snek_object_data_t` named `data`.

```c
typedef enum {
  INTEGER
} snek_object_kind_t;

typedef union {
  int v_int;
} snek_object_data_t;

typedef struct {
  snek_object_kind_t kind;
  snek_object_data_t data;
} snek_object_t;

```

# Integer

Let's start simple with a single integer object. The difference between a "snek integer" and a regular C integer is that the Snek integer:

1. Is allocated on the heap
2. Can store additional metadata about itself (for now, just its type)

## Assignment

**Complete the `new_snek_integer` function** in `snekobject.c`. It should:

1. [ ] Use [`malloc`](https://en.cppreference.com/w/c/memory/malloc) to allocate heap memory for a new pointer to a `snek_object_t`.
2. [ ] If the allocation fails, return `NULL`.
3. [ ] Set the `kind` field of the new snek object to the `INTEGER` enum value (defined in `snekobject.h`).
4. [ ] Set the `v_int` field of the new snek object to the integer value passed in.
5. [ ] Return the pointer to the new snek object.

If you're curious how this will be used, take a look at the `main.c` file (where the tests are). You'll see some code that looks like this:

```c
snek_object_t *int_object = new_snek_integer(42);
```


```c
#include "snekobject.h"
#include <stdlib.h>

snek_object_t *new_snek_integer(int value) {
  snek_object_t *new_ptr = malloc(sizeof(snek_object_t));
  if (new_ptr == NULL){
    return NULL;
  }

  new_ptr->kind = INTEGER;
  new_ptr->data.v_int = value;
  return new_ptr;
}

```

# Float

Sneklang needs floats (obviously). How else will all the crypto bros write weird floating-point bugs into their smart contracts?

So how do we store both floats and ints into the same type?

We're going to use the `union` and `enum` features in C to be able to do this, just like we discussed in previous chapters. You will need to extend the existing `snek_object_kind_t` and `snek_object_data_t` types to be able to include both `int`s and `float`s (and we will continue to add more types in the following chapters to exercise your newfound mastery of memory management).

## Assignment

You will need to edit _2 files_ in this lesson! `snekobject.c` and `snekobject.h`.

1. [ ] In `snekobject.h`:
    1. [ ] Add a new enum value to the `snek_object_kind_t` enum called `FLOAT`.
    2. [ ] Add a new `float` field to `snek_object_data_t` called `v_float`.
    3. [ ] Declare the `new_snek_float` function.
2. [ ] In `snekobject.c`, complete the `new_snek_float` function. It should:
    1. [ ] Allocate memory for a new pointer to a `snek_object_t`.
    2. [ ] If the allocation fails, return `NULL`.
    3. [ ] Set the `kind` field to the appropriate enum.
    4. [ ] Store the float value in the object.
    5. [ ] Return the pointer to the new snek object.


```c
#include "snekobject.h"
#include <stdlib.h>

snek_object_t *new_snek_float(float value) {
  snek_object_t *new_ptr = malloc(sizeof(snek_object_t));
  if (new_ptr == NULL){
    return NULL;
  }

  new_ptr->kind = FLOAT;
  new_ptr->data.v_float = value;
  return new_ptr;
}

// don't touch below this line

snek_object_t *new_snek_integer(int value) {
  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = INTEGER;
  obj->data.v_int = value;
  return obj;
}

```

```c
typedef enum SnekObjectKind { INTEGER, FLOAT } snek_object_kind_t;

typedef union SnekObjectData {
  int v_int;
  float v_float;
} snek_object_data_t;

typedef struct SnekObject {
  snek_object_kind_t kind;
  snek_object_data_t data;
} snek_object_t;

snek_object_t *new_snek_integer(int value);
snek_object_t *new_snek_float(float value);
```

# String

Now we're going to do our first object that has something... _additional_ allocated. When we allocate memory for a "snek object", that reserves memory for the object itself. Small data types like integers and floats are stored directly in the object, so there's no need for additional memory allocation.

Strings, however, are a different story. Strings in C are just arrays of characters, and because they can be any length, we need to dynamically allocate memory for the string data separately from the object itself.

```c
char *my_string = "hello world";
```

In the example above, `my_string` is a pointer to a character array. The character array contains:

```text
h
e
l
l
o

w
o
r
l
d
\0
```

The extra spot at the end with the `\0` is the null terminator. It's how C knows where the string ends.

## Assignment

1. [ ] In `snekobject.h`:
    1. [ ] Add a new enum value to the `snek_object_kind_t` enum called `STRING`.
    2. [ ] Add a new string (`char *`) field to `snek_object_data_t` called `v_string`
    3. [ ] Declare the `new_snek_string` function.
2. [ ] In `snekobject.c`, complete the `new_snek_string` function. It should:
    1. [ ] Allocate memory for a new pointer to a `snek_object_t`.
    2. [ ] If the allocation fails, return `NULL`.
    3. [ ] Calculate the length (in bytes using [`strlen`](https://devdocs.io/c/string/byte/strlen)) of the string passed in.
    4. [ ] Allocate memory in a `char *` field equal to the length of the string plus one (for the null terminator).
    5. [ ] If the allocation fails, [`free`](https://devdocs.io/c/memory/free) the memory allocated for the snek object, then return `NULL`.
    6. [ ] Copy the data from the input value into the new string field you just allocated using [`strcpy`](https://devdocs.io/c/string/byte/strcpy).
    7. [ ] Set the `kind` field to the appropriate enum.
    8. [ ] Store the newly allocated string in the object.
    9. [ ] Return the pointer to the new snek object.
```c
#include "snekobject.h"
#include <stdlib.h>
#include <string.h>

snek_object_t *new_snek_string(char *value) {
  snek_object_t *new_ptr = malloc(sizeof(snek_object_t));
  if (new_ptr == NULL){
    return NULL;
  }

  size_t str_len = strlen(value);
  char *str_ptr = malloc(str_len+1);
  if (str_ptr == NULL){
    free(new_ptr);
    return NULL;
  }
  strcpy(str_ptr, value);

  new_ptr->kind = STRING;
  new_ptr->data.v_string = str_ptr;
  return new_ptr;
}

// don't touch below this line
snek_object_t *new_snek_integer(int value) {
  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = INTEGER;
  obj->data.v_int = value;
  return obj;
}

snek_object_t *new_snek_float(float value) {
  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = FLOAT;
  obj->data.v_float = value;
  return obj;
}

```

```c
typedef enum SnekObjectKind {
  INTEGER,
  FLOAT,
  STRING
} snek_object_kind_t;

typedef union SnekObjectData {
  int v_int;
  float v_float;
  char *v_string;
} snek_object_data_t;

typedef struct SnekObject {
  snek_object_kind_t kind;
  snek_object_data_t data;
} snek_object_t;

snek_object_t *new_snek_integer(int value);
snek_object_t *new_snek_float(float value);
snek_object_t *new_snek_string(char *value);
```


# Vector3

`Vector3` is going to be the first Snek Object that can hold a reference to another Snek Object. It's a collection type: a type that holds other types.

Arrays, lists, dictionaries, and sets are all examples of collection types. We won't implement all of those types in this course, but they each will follow the same pattern that we're establishing here with `Vector3`.

`Vector3` is similar to a Python tuple that contains _exactly_ 3 "SnekObject" elements.

## Assignment

1. In `snekobject.h`:
    
    1. [ ] Forward declare the `snek_object_t` struct at the top of the file. It will need to be used in a circular dependency between `snek_object_t -> snek_object_data_t -> snek_vector_t`.
    2. [ ] Create a new [struct](https://devdocs.io/c/language/struct) called `snek_vector_t` that has three fields. Name the fields `x`, `y`, and `z`. Each field should be a Sneklang Object pointer (`snek_object_t *`).
    3. [ ] Add a new enum value to the `snek_object_kind_t` enum called `VECTOR3`.
    4. [ ] Add a new `snek_vector_t` field (the struct type you just created) to `snek_object_data_t` called `v_vector3`.
    5. [ ] Declare the `new_snek_vector3` function.
    
    The `v_vector3` field is not a pointer to a `vector3`; it's directly allocated inside the struct. We can do this because we know the size of the vector (it's only 3 pointers wide) in advance.
    
2. In `snekobject.c`, complete the `new_snek_vector3` function:
    
    1. [ ] If any of the inputs are `NULL`, return `NULL`.
    2. [ ] Allocate memory for a new pointer to a `snek_object_t`, and if the allocation fails return `NULL`.
    3. [ ] Set the `kind` field to the appropriate enum.
    4. [ ] Initialize the `v_vector3` field of the new snek object so that its `x`, `y`, and `z` members point to the input objects (for example, by creating a `snek_vector_t` with those fields and assigning it to `v_vector3`).
    5. [ ] Return the pointer to the new snek object.

```c
#include "snekobject.h"
#include <stdlib.h>
#include <string.h>

snek_object_t *new_snek_vector3(snek_object_t *x, snek_object_t *y,
                                snek_object_t *z) {
  if (x == NULL || y == NULL || z == NULL) {
    return NULL;
  }
  snek_object_t *new_ptr = malloc(sizeof(snek_object_t));
  if (new_ptr == NULL){
    return NULL;
  }
  new_ptr->kind = VECTOR3;
  new_ptr->data.v_vector3.x = x;
  new_ptr->data.v_vector3.y = y;
  new_ptr->data.v_vector3.z = z;

  return new_ptr;
}

// don't touch below this line

snek_object_t *new_snek_integer(int value) {
  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = INTEGER;
  obj->data.v_int = value;
  return obj;
}

snek_object_t *new_snek_float(float value) {
  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = FLOAT;
  obj->data.v_float = value;
  return obj;
}

snek_object_t *new_snek_string(char *value) {
  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  int len = strlen(value);
  char *dst = malloc(len + 1);
  if (dst == NULL) {
    free(obj);
    return NULL;
  }

  strcpy(dst, value);

  obj->kind = STRING;
  obj->data.v_string = dst;
  return obj;
}

```

```c
typedef struct SnekObject snek_object_t;
typedef enum SnekObjectKind {
  INTEGER,
  FLOAT,
  STRING,
  VECTOR3,
} snek_object_kind_t;

typedef struct SnekVector {
  snek_object_t *x;
  snek_object_t *y;
  snek_object_t *z;
} snek_vector_t;

typedef union SnekObjectData {
  int v_int;
  float v_float;
  char *v_string;
  snek_vector_t v_vector3;
} snek_object_data_t;


typedef struct SnekObject {
  snek_object_kind_t kind;
  snek_object_data_t data;
} snek_object_t;

snek_object_t *new_snek_integer(int value);
snek_object_t *new_snek_float(float value);
snek_object_t *new_snek_string(char *value);
snek_object_t *new_snek_vector3(snek_object_t *x, snek_object_t *y, snek_object_t *z);

```

`v_vector3` is stored **by value**, embedded directly inside the union — not as a `snek_vector_t *` pointing somewhere else on the heap.

Concretely:

c

```c
typedef union SnekObjectData {
  int v_int;
  snek_vector_t v_vector3;   // <-- the actual struct lives here, inline
} snek_object_data_t;
```

vs. what it's _not_:

c

```c
typedef union SnekObjectData {
  int v_int;
  snek_vector_t *v_vector3;  // <-- this would be a pointer needing its own malloc
} snek_object_data_t;
```

**Why this is possible:** `snek_vector_t` is just three pointers (`x`, `y`, `z` — each `snek_object_t *`). That's a small, fixed size known at compile time. So the compiler can reserve exactly that much space inside the union/struct itself — no separate heap allocation needed for the vector struct.

This is why the union already grew big enough to hold it once you added `v_vector3` as a field type (not a field pointer-type) — `sizeof(snek_object_data_t)` just became `max(existing members, sizeof(snek_vector_t))`.

**Contrast with the pointers _inside_ the vector:** `x`, `y`, `z` themselves are still pointers to separately-heap-allocated `snek_object_t`s (e.g. integers) — that part _is_ a reference. Only the _container_ (the 3-pointer-wide struct) is inline; what it points _to_ is not.


# Array

Let's add a dynamically sized array to Sneklang. We'll do it in multiple parts. First, we'll just create an empty array. In later lessons, we'll make it useful.

## Assignment

1. [ ] In `snekobject.h`:
    1. [ ] Add a new enum value to the `snek_object_kind_t` enum called `ARRAY`.
    2. [ ] Create a new [struct](https://devdocs.io/c/language/struct) called `snek_array_t` that has two fields:
        1. [ ] `size` – the number of elements in the array, a [size_t](https://devdocs.io/c/types/size_t)
        2. [ ] `elements` – a pointer to an array of snek object pointers, a `snek_object_t **`
    3. [ ] Add a new `snek_array_t` field (the struct type you just created) to `snek_object_data_t` called `v_array`.
    4. [ ] Declare the `new_snek_array` function.
2. [ ] In `snekobject.c`, complete the `new_snek_array` function. It should:
    1. [ ] Accept a `size` parameter.
    2. [ ] Allocate memory for a new pointer to a `snek_object_t`, and if the allocation fails return `NULL`.
    3. [ ] Allocate memory for a new pointer to an array of snek objects (`snek_object_t **`).
        1. [ ] How much memory should you allocate? Think about it: probably the `sizeof` a pointer for each element in the array. We're not storing the actual snek objects in the array, just pointers to them.
        2. [ ] If the allocation fails, `free` the first snek object allocation and return `NULL`.
        3. [ ] Use [`calloc`](https://en.cppreference.com/w/c/memory/calloc) instead of `malloc` so there is no "junk" in our array to start, we want beautiful, pristine `NULL`s. Note that `calloc` takes two arguments: number of objects and the size of each object.
    4. [ ] Set the `kind` field to the appropriate enum.
    5. [ ] Create a new `snek_array_t` struct and set the `size` and `elements` fields.
    6. [ ] Set the `v_array` field of the new snek object to the newly created `snek_array_t`.
    7. [ ] Return the pointer to the new snek objec

```c
#include "snekobject.h"
#include <stdlib.h>
#include <string.h>

snek_object_t *new_snek_array(size_t size) {
  snek_object_t *new_ptr = malloc(sizeof(snek_object_t));
  if (new_ptr == NULL){
    return NULL;
  }
  snek_object_t **new_arr_ptr = calloc(size, sizeof(new_ptr));
  if (new_arr_ptr == NULL){
    free(new_ptr);
    return NULL;
  }

  new_ptr->kind = ARRAY;
  snek_array_t arr = {
    .size = size,
    .elements = new_arr_ptr,
  };
  new_ptr->data.v_array = arr;
  return new_ptr;
}

// don't touch below this line

snek_object_t *new_snek_vector3(snek_object_t *x, snek_object_t *y,
                                snek_object_t *z) {
  if (x == NULL || y == NULL || z == NULL) {
    return NULL;
  }

  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = VECTOR3;
  obj->data.v_vector3 = (snek_vector_t){.x = x, .y = y, .z = z};

  return obj;
}

snek_object_t *new_snek_integer(int value) {
  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = INTEGER;
  obj->data.v_int = value;
  return obj;
}

snek_object_t *new_snek_float(float value) {
  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = FLOAT;
  obj->data.v_float = value;
  return obj;
}

snek_object_t *new_snek_string(char *value) {
  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  int len = strlen(value);
  char *dst = malloc(len + 1);
  if (dst == NULL) {
    free(obj);
    return NULL;
  }

  strcpy(dst, value);

  obj->kind = STRING;
  obj->data.v_string = dst;
  return obj;
}

```

```c
#include <stddef.h>

typedef struct SnekObject snek_object_t;

typedef struct {
  snek_object_t *x;
  snek_object_t *y;
  snek_object_t *z;
} snek_vector_t;

typedef struct {
  size_t size;
  snek_object_t **elements;
} snek_array_t;

typedef enum SnekObjectKind {
  INTEGER,
  FLOAT,
  STRING,
  VECTOR3,
  ARRAY,
} snek_object_kind_t;

typedef union SnekObjectData {
  int v_int;
  float v_float;
  char *v_string;
  snek_vector_t v_vector3;
  snek_array_t v_array;
} snek_object_data_t;

typedef struct SnekObject {
  snek_object_kind_t kind;
  snek_object_data_t data;
} snek_object_t;

snek_object_t *new_snek_integer(int value);
snek_object_t *new_snek_float(float value);
snek_object_t *new_snek_string(char *value);
snek_object_t *new_snek_vector3(snek_object_t *x, snek_object_t *y,
                                snek_object_t *z);
snek_object_t *new_snek_array(size_t size);

```

# Set

We can make empty arrays! ... which is kinda pointless, but at least the bones are there. Let's make our arrays useful by allowing us to _store values_ in them.

`snek_array_set` sets a value at a specific index in the array. The equivalent in Python would be:

```py
array[3] = new_value
```

## Assignment

Complete the `snek_array_set` function:

1. [ ] If the object _or_ the new value is `NULL`, return `false`.
2. [ ] If the object's `kind` is not `ARRAY`, return `false`.
3. [ ] If the index is out of bounds, return `false`. _Remember, the `v_array` field has a `size` field._
4. [ ] Set the value in the `elements` array at the specified index to the new value.
5. [ ] Return `true`. _The return value is a boolean that indicates success._

```c
#include "snekobject.h"
#include <stdlib.h>
#include <string.h>

bool snek_array_set(snek_object_t *snek_obj, size_t index,
                    snek_object_t *value) {
  if (snek_obj == NULL || value == NULL){
    return false;
  }
  if (snek_obj->kind != ARRAY) {return false;}
  if (index >= snek_obj->data.v_array.size){
    return false;
  }
  snek_obj->data.v_array.elements[index] = value;
  return true;
}

// don't touch below this line

snek_object_t *new_snek_array(size_t size) {
  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  snek_object_t **elements = calloc(size, sizeof(snek_object_t *));
  if (elements == NULL) {
    free(obj);
    return NULL;
  }

  obj->kind = ARRAY;
  obj->data.v_array = (snek_array_t){.size = size, .elements = elements};
  return obj;
}

snek_object_t *new_snek_vector3(snek_object_t *x, snek_object_t *y,
                                snek_object_t *z) {
  if (x == NULL || y == NULL || z == NULL) {
    return NULL;
  }

  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = VECTOR3;
  obj->data.v_vector3 = (snek_vector_t){.x = x, .y = y, .z = z};

  return obj;
}

snek_object_t *new_snek_integer(int value) {
  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = INTEGER;
  obj->data.v_int = value;
  return obj;
}

snek_object_t *new_snek_float(float value) {
  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = FLOAT;
  obj->data.v_float = value;
  return obj;
}

snek_object_t *new_snek_string(char *value) {
  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  int len = strlen(value);
  char *dst = malloc(len + 1);
  if (dst == NULL) {
    free(obj);
    return NULL;
  }

  strcpy(dst, value);

  obj->kind = STRING;
  obj->data.v_string = dst;
  return obj;
}

```

```c
#include <stdbool.h>
#include <stddef.h>

typedef struct SnekObject snek_object_t;

typedef struct {
  size_t size;
  snek_object_t **elements;
} snek_array_t;

typedef struct {
  snek_object_t *x;
  snek_object_t *y;
  snek_object_t *z;
} snek_vector_t;

typedef enum SnekObjectKind {
  INTEGER,
  FLOAT,
  STRING,
  VECTOR3,
  ARRAY,
} snek_object_kind_t;

typedef union SnekObjectData {
  int v_int;
  float v_float;
  char *v_string;
  snek_vector_t v_vector3;
  snek_array_t v_array;
} snek_object_data_t;

typedef struct SnekObject {
  snek_object_kind_t kind;
  snek_object_data_t data;
} snek_object_t;

snek_object_t *new_snek_integer(int value);
snek_object_t *new_snek_float(float value);
snek_object_t *new_snek_string(char *value);
snek_object_t *new_snek_vector3(snek_object_t *x, snek_object_t *y,
                                snek_object_t *z);
snek_object_t *new_snek_array(size_t size);
bool snek_array_set(snek_object_t *array, size_t index, snek_object_t *value);

```

# Get

Now that we can store values in arrays, we need a way to _retrieve_ them. `snek_array_get` returns the value at a specific index in the array. The equivalent in Python would be:

```py
array[7]
```

## Assignment

Complete the `snek_array_get` function:

1. [ ] If the object is `NULL`, return `NULL`.
2. [ ] If the object's `kind` is not `ARRAY`, return `NULL`.
3. [ ] If the index is out of bounds, return `NULL`.
4. [ ] Return the value in the `elements` array at the specified index.

```c
#include "snekobject.h"
#include <stdlib.h>
#include <string.h>

snek_object_t *snek_array_get(snek_object_t *snek_obj, size_t index) {
  if (snek_obj == NULL){
    return NULL;
  }
  if (snek_obj->kind != ARRAY){
    return NULL;
  }
  if (index >= snek_obj->data.v_array.size){
    return NULL;
  }
  
  return snek_obj->data.v_array.elements[index];
}
```
# Length

Now that we have all sorts of Snek Objects (integers, floats, strings, arrays, etc.), we need a convenient way to get the `length` of _any_ Snek Object. In Python (Sneklang's dreaded competitor) it's as easy as:

```python
print(len(x))
```

As a Python dev, you don't have to know the value of `x` ahead of time because Python keeps track of it under-the-hood for you. We want the same capability in Sneklang.

## Assignment

In `snekobject.c`, complete the `snek_length` function:

1. [ ] If the input is `NULL` return `-1` (which we've chosen to indicate failure).
2. [ ] If the input is an integer, its size is always `1`.
3. [ ] If the input is a float, its size is always `1`.
4. [ ] If the input is a string, its size is the [length of the string in bytes](https://devdocs.io/c/string/byte/strlen).
5. [ ] If the input is a `VECTOR3`, its size is always `3`.
6. [ ] If the input is an array, its size is stored in the `v_array.size` field.
7. [ ] If the input is none of the above, return `-1`.

```c
#include "snekobject.h"
#include <stdlib.h>
#include <string.h>

int snek_length(snek_object_t *obj) {
  if (obj == NULL){
    return -1;
  }

  if (obj->kind == INTEGER || obj->kind == FLOAT){
    return 1;
  }

  if (obj->kind == STRING){
    return strlen(obj->data.v_string);
  }

  if (obj->kind == VECTOR3){
    return 3;
  }

  if (obj->kind == ARRAY){
    return obj->data.v_array.size;
  }

  return -1;
  
}
```

# Add

If you're familiar with Python, you'll be familiar with how Python objects can have an `__add__` method. It allows developers to specify custom logic for different types of objects. For example, adding two integers we want to behave like this:

```py
3 + 5
# 8
```

But with an array, we probably want it to work like this:

```py
[3] + [5]
# [3, 5]
```

## Assignment

_This is the final lesson on objects, and it's a big one. Take your time – you'll be using a lot of the functions that you wrote in past chapters to complete this one_.

Complete the `snek_add` function. It accepts two pointers to `snek_object_t` objects ("a" and "b") and returns a pointer to a new `snek_object_t` object (the result of the sum):

1. [ ] If either input is `NULL`, return `NULL`.
2. [ ] If "a" is an integer:
    1. [ ] If "b" is an integer, return a `new_snek_integer` with the sum of the two integers.
    2. [ ] If "b" is a float, return a `new_snek_float` with the sum of the integer and float.
    3. [ ] Anything else, invalid operation, return `NULL`.
3. [ ] If "a" is a float:
    1. [ ] If "b" is an integer, return a `new_snek_float` with the sum of the float and integer.
    2. [ ] If "b" is a float, return a `new_snek_float` with the sum of the two floats.
    3. [ ] Anything else, invalid operation, return `NULL`.
4. [ ] If "a" is a string:
    1. [ ] If "b" is not a string, invalid operation, return `NULL`.
    2. [ ] Otherwise:
        1. [ ] Calculate the length of the new string by combining the length of the two strings (properly handling the null terminator)
        2. [ ] Allocate memory for a new temporary string using [calloc](https://devdocs.io/c/memory/calloc)
        3. [ ] Use [strcat](https://devdocs.io/c/string/byte/strcat) to append the data from a and then b to the temporary string.
        4. [ ] Create a `new_snek_string` and pass in the temporary string.
        5. [ ] Free the memory for the temporary string and return the new string object.
5. [ ] If "a" is a vector3:
    1. [ ] If "b" is not a `VECTOR3`, invalid operation, return `NULL`.
    2. [ ] Otherwise:
        1. [ ] Create a `new_snek_vector3`.
        2. [ ] Recursively call `snek_add` for each of the x, y, and z fields. For example, a vector [1,2,3]+[4,5,6] should result in a new vector [5,7,9].
        3. [ ] Return the new vector struct.
6. [ ] If "a" is an array:
    1. [ ] If "b" is not an array, invalid operation, return `NULL`.
    2. [ ] Otherwise:
        1. [ ] Create a `new_snek_array` with the combined length of the two arrays.
        2. [ ] Iterate over each index in "a" and use `snek_array_set` and `snek_array_get` to copy the values from "a" to the new array.
        3. [ ] Do the same for "b".
        4. [ ] Return the new array object.
7. [ ] If "a" is none of the above, invalid operation, return `NULL`.

_We won't implement `subtract`, `multiply`, or `divide` but each of these would follow the same pattern_. This is how arithmetic operations work in Sneklang!


```c
#include "snekobject.h"
#include <stdlib.h>
#include <string.h>

snek_object_t *snek_add(snek_object_t *a, snek_object_t *b) {
  if (a == NULL || b == NULL){
    return NULL;
  }
  if (a->kind == INTEGER){
    if (b->kind == INTEGER){
      int result = b->data.v_int + a->data.v_int;
      return new_snek_integer(result);
    }else if (b->kind == FLOAT){
      float result = a->data.v_int + b->data.v_float;
      return new_snek_float(result);
    }else {
      return NULL;
    }
  }
  
  if (a->kind == FLOAT){
    if (b->kind == INTEGER){
      int result = a->data.v_float + b->data.v_int;
      return new_snek_float(result);
    }else if (b->kind == FLOAT){
      float result = a->data.v_float + b->data.v_float;
      return new_snek_float(result);
    }else {
      return NULL;
    }
  }

  if (a->kind == STRING){
    if (b->kind != STRING) {
      return NULL;
    }else {
      size_t new_str_len = strlen(a->data.v_string) + strlen(b->data.v_string) + 1 + 1; // 1+1 for two null terminators
      char *new_ptr = calloc(new_str_len,sizeof(char));
      if (new_ptr == NULL){
        return NULL;
      }
      strcat(new_ptr, a->data.v_string);
      strcat(new_ptr, b->data.v_string);
      snek_object_t *str = new_snek_string(new_ptr);
      free(new_ptr);
      return str;
    }    
  }

  if (a->kind == VECTOR3){
    if(b->kind != VECTOR3){
      return NULL;
    }else {
      snek_object_t *x = snek_add(a->data.v_vector3.x, b->data.v_vector3.x);  
      snek_object_t *y = snek_add(a->data.v_vector3.y, b->data.v_vector3.y);  
      snek_object_t *z = snek_add(a->data.v_vector3.z, b->data.v_vector3.z);  
      return new_snek_vector3(x, y, z);
    }
  }

  if (a->kind == ARRAY){
    if (b->kind != ARRAY){
      return NULL;
    }else {
      size_t a_len = a->data.v_array.size;
      size_t b_len = b->data.v_array.size;
      snek_object_t *new_arr = new_snek_array(a_len+b_len);
      if(new_arr == NULL){
        return NULL;
      }
      // copy values from a to new_arr
      for (size_t i = 0; i < a_len; i++){
        snek_object_t *val = snek_array_get(a, i);
        snek_array_set(new_arr, i, val);
      }

      // copy values from b to new_arr
      for (size_t i = 0; i < b_len; i++){
        snek_object_t *val = snek_array_get(b, i);
        snek_array_set(new_arr, a_len+i, val);
      }

      return new_arr;
    }
  }
  return NULL;
  
}

// don't touch below this line

int snek_length(snek_object_t *obj) {
  if (obj == NULL) {
    return -1;
  }

  switch (obj->kind) {
  case INTEGER:
    return 1;
  case FLOAT:
    return 1;
  case STRING:
    return strlen(obj->data.v_string);
  case VECTOR3:
    return 3;
  case ARRAY:
    return obj->data.v_array.size;
  default:
    return -1;
  }
}

snek_object_t *new_snek_array(size_t size) {
  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  snek_object_t **elements = calloc(size, sizeof(snek_object_t *));
  if (elements == NULL) {
    free(obj);
    return NULL;
  }

  obj->kind = ARRAY;
  obj->data.v_array = (snek_array_t){.size = size, .elements = elements};
  return obj;
}

bool snek_array_set(snek_object_t *array, size_t index, snek_object_t *value) {
  if (array == NULL || value == NULL) {
    return false;
  }

  if (array->kind != ARRAY) {
    return false;
  }

  if (index >= array->data.v_array.size) {
    return false;
  }

  array->data.v_array.elements[index] = value;
  return true;
}

snek_object_t *snek_array_get(snek_object_t *array, size_t index) {
  if (array == NULL) {
    return NULL;
  }

  if (array->kind != ARRAY) {
    return NULL;
  }

  if (index >= array->data.v_array.size) {
    return NULL;
  }

  return array->data.v_array.elements[index];
}

snek_object_t *new_snek_vector3(snek_object_t *x, snek_object_t *y,
                                snek_object_t *z) {
  if (x == NULL || y == NULL || z == NULL) {
    return NULL;
  }

  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = VECTOR3;
  obj->data.v_vector3 = (snek_vector_t){.x = x, .y = y, .z = z};

  return obj;
}

snek_object_t *new_snek_integer(int value) {
  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = INTEGER;
  obj->data.v_int = value;
  return obj;
}

snek_object_t *new_snek_float(float value) {
  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = FLOAT;
  obj->data.v_float = value;
  return obj;
}

snek_object_t *new_snek_string(char *value) {
  snek_object_t *obj = malloc(sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  int len = strlen(value);
  char *dst = malloc(len + 1);
  if (dst == NULL) {
    free(obj);
    return NULL;
  }

  strcpy(dst, value);

  obj->kind = STRING;
  obj->data.v_string = dst;
  return obj;
}

```

# Garbage Collector

Click to hide video

Your browser does not support playing HTML5 video. You can instead. Here is a description of the content: garbage collection video

As you're painfully aware, we've been manually managing memory throughout this course with our C code. However, Sneklang, the language we're building, has _automatic memory management_. Specifically, it makes use of a [garbage collector](https://en.wikipedia.org/wiki/Garbage_collection_\(computer_science\)).

- In C and C++, management of heap memory is done manually with `malloc` and `free` (and `new` and `delete` in C++).
- Rust has a compile-time system that ensures memory safety.
- Zig gives the programmer access to "allocators" to manage memory.

These are all examples of "manual memory management" – the programmer has to write code that keeps track of and frees memory.

## So What's a Garbage Collector?

A garbage collector is a program (or part of a program) that automatically frees memory that is no longer in use. Languages like Python, Java, JavaScript, OCaml, and even Go use garbage collectors _as the code is running_ to manage memory. It's "automatic memory management". Automatic memory management can be a huge productivity boost for developers (less code, and sometimes fewer memory-related bugs) but it typically comes with a performance cost because, like Forrest Gump, the garbage collector is always running.

It's no coincidence that C, C++, Rust, and Zig are all great choices when you need to squeeze every last drop of performance out of your code.

# Refcounting

One of the simplest ways to implement a garbage collector is to use a [reference counting](https://en.wikipedia.org/wiki/Garbage_collection_\(computer_science\)#Reference_counting) algorithm. It goes something like this:

- All objects keep track of a `reference_count` integer.
- When that object is referenced, its reference count is incremented.
- When an object is garbage collected, the reference count of any object it references is decremented.
- When any object's reference count reaches zero, the object is garbage collected.

## Assignment

1. [ ] In `snekobject.h`: add a new integer field named `refcount` to `snek_object_t`.
2. [ ] In `snekobject.c`: complete the `_new_snek_object` function:
    1. [ ] Allocate a `snek_object_t` on the heap using `calloc` so its memory is zero-initialized.
    2. [ ] If the allocation fails, return `NULL`.
    3. [ ] Set the `refcount` to `1`.
    4. [ ] Return the pointer to the new object.

```c
#include "snekobject.h"
#include <stdlib.h>
#include <string.h>

snek_object_t *_new_snek_object(void) {
  snek_object_t *new_obj = calloc(1,sizeof(snek_object_t));
  if (new_obj == NULL){
    return NULL;
  }

  new_obj->refcount = 1;
  return new_obj;
}
```

```c
typedef struct SnekObject {
  snek_object_kind_t kind;
  snek_object_data_t data;
  int refcount;
} snek_object_t;
```

# Increment

We need to be able to increment the reference count of a `SnekObject` any time a new reference to it is created.

## Assignment

Complete the `refcount_inc` function. It should increment the `refcount` of a `SnekObject`. If the object is `NULL`, it should do nothing (but safely).

```c
#include "snekobject.h"
#include "assert.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void refcount_inc(snek_object_t *obj) {
  if (obj == NULL){
    return;
  }
  obj->refcount++;
}

```

# Decrement and free

Now things are going to get a touch more complicated. In a refcounting GC, the interesting stuff happens when the refcount equals `0`. That's when the garbage gets collected.

When the refcount reaches 0, there are no references to this object anymore! So, we need to `free` the memory _automagically_ -- that's the whole point of a garbage collector.

For our first pass at this, we will only handle integers, floats and strings to keep things simple. As we go a little further, we'll implement it for the rest of the SnekObject types.

## Assignment

1. [ ] Complete the `refcount_dec` function:
    1. [ ] Handle `NULL` objects gracefully.
    2. [ ] Decrement the `refcount`
    3. [ ] Then check if the `refcount` has reached 0, and if so, call `refcount_free` on the object.
2. [ ] Complete the `refcount_free` function:
    1. [ ] If the object is an `INTEGER` or a `FLOAT`, free the object itself (we don't need to worry about the data inside the object because it's stored directly in the object).
    2. [ ] If the object is a `STRING`, free the `char*` data inside the object, then free the object itself.
    3. [ ] If it's any other type, do nothing for now.



**INTEGER/FLOAT** — the value is stored directly inside the object (`obj->data.v_int` / `obj->data.v_float`). One `malloc`, one block of memory. Freeing `obj` frees everything:

```c
free(obj);
```

**STRING** — `obj->data.v_string` is a `char*`, a separate heap allocation:

```c
char *dst = malloc(len + 1);   // separate malloc, in new_snek_string
...
obj->data.v_string = dst;
```

So a string object is **two** allocations: the `snek_object_t` struct itself, and the string buffer it points to. `free(obj)` alone only frees the struct — the buffer becomes a memory leak (nothing else references it, so it can never be freed).

So order matters: free the inner pointer first, then the struct that held it.

```c
free(obj->data.v_string);
free(obj);
```

(Reversed order would also work here technically — `free(obj)` doesn't erase the pointer value — but freeing outer-before-inner is generally unsafe practice since you'd lose access to `obj->data.v_string` after freeing `obj`. Free inner first, always.)

```c
#include "snekobject.h"
#include "assert.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void refcount_dec(snek_object_t *obj) {
  if (obj == NULL){
    return;
  }
  obj->refcount--;
  if(obj->refcount == 0){
    refcount_free(obj);
  }
}

void refcount_free(snek_object_t *obj) {
  if (obj->kind == INTEGER || obj->kind == FLOAT){
    free(obj);
  }else if (obj->kind == STRING){
    free(obj->data.v_string);
    free(obj);
  }
}
```


# Vectors

We have arrived at our first container type! What makes `VECTOR3` not like the other types is that it _holds other snek objects_. That is, it "references" them. They are contained in its `x`, `y`, and `z` fields.

When we create a vector and place objects in those fields, we need to `increment` the refcount of each of those objects! Otherwise, we might accidentally free its contents and be left with a vector holding garbage memory.

## Assignment

1. [ ] Update the `new_snek_vector3` function. It should `refcount_inc` _each of its 3 objects_.
2. [ ] Update the `refcount_free` function to handle vectors. It should `refcount_dec` each of its 3 objects (which will automatically free them if they hit 0).
```c
#include "snekobject.h"
#include "assert.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

snek_object_t *_new_snek_object(void);

snek_object_t *new_snek_vector3(snek_object_t *x, snek_object_t *y,
                                snek_object_t *z) {
  if (x == NULL || y == NULL || z == NULL) {
    return NULL;
  }
  snek_object_t *obj = _new_snek_object();
  if (obj == NULL) {
    return NULL;
  }
  obj->kind = VECTOR3;
  obj->data.v_vector3 = (snek_vector_t){.x = x, .y = y, .z = z};
  refcount_inc(obj->data.v_vector3.x);
  refcount_inc(obj->data.v_vector3.y);
  refcount_inc(obj->data.v_vector3.z);
  return obj;
}

void refcount_free(snek_object_t *obj) {
  switch (obj->kind) {
  case INTEGER:
  case FLOAT:
    break;
  case STRING:
    free(obj->data.v_string);
    break;
  case VECTOR3: {
    refcount_dec(obj->data.v_vector3.x);
    refcount_dec(obj->data.v_vector3.y);
    refcount_dec(obj->data.v_vector3.z);
    break;
  }
  default:
    assert(false);
  }

  free(obj);
}

// don't touch below this line

void refcount_inc(snek_object_t *obj) {
  if (obj == NULL) {
    return;
  }

  obj->refcount++;
  return;
}

void refcount_dec(snek_object_t *obj) {
  if (obj == NULL) {
    return;
  }
  obj->refcount--;
  if (obj->refcount == 0) {
    refcount_free(obj);
    return;
  }
  return;
}

snek_object_t *_new_snek_object(void) {
  snek_object_t *obj = calloc(1, sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  obj->refcount = 1;

  return obj;
}

snek_object_t *new_snek_array(size_t size) {
  snek_object_t *obj = _new_snek_object();
  if (obj == NULL) {
    return NULL;
  }

  snek_object_t **elements = calloc(size, sizeof(snek_object_t *));
  if (elements == NULL) {
    free(obj);
    return NULL;
  }

  obj->kind = ARRAY;
  obj->data.v_array = (snek_array_t){.size = size, .elements = elements};

  return obj;
}

snek_object_t *new_snek_integer(int value) {
  snek_object_t *obj = _new_snek_object();
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = INTEGER;
  obj->data.v_int = value;
  return obj;
}

snek_object_t *new_snek_float(float value) {
  snek_object_t *obj = _new_snek_object();
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = FLOAT;
  obj->data.v_float = value;
  return obj;
}

snek_object_t *new_snek_string(char *value) {
  snek_object_t *obj = _new_snek_object();
  if (obj == NULL) {
    return NULL;
  }

  int len = strlen(value);
  char *dst = malloc(len + 1);
  if (dst == NULL) {
    free(obj);
    return NULL;
  }

  strcpy(dst, value);

  obj->kind = STRING;
  obj->data.v_string = dst;
  return obj;
}

```

# Arrays

Refcounting for an array is similar to the `VECTOR3` kind. However, an `ARRAY` has a dynamic size, which will add complexity.

## Assignment

1. [ ] Update the `snek_array_set` function:
    1. [ ] Increment the refcount of the object being assigned to the index.
    2. [ ] If there was already an object stored at that index, decrement the refcount of that object.
2. [ ] Update the `refcount_free` function to handle arrays. If it's an array:
    1. [ ] Iterate over each element (from `0` to `size - 1`) and decrement the refcount of each object.
    2. [ ] Free the array itself (the `elements` field).
```c
#include "snekobject.h"
#include "assert.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool snek_array_set(snek_object_t *snek_obj, size_t index,
                    snek_object_t *value) {
  if (snek_obj == NULL || value == NULL) {
    return false;
  }
  if (snek_obj->kind != ARRAY) {
    return false;
  }
  if (index >= snek_obj->data.v_array.size) {
    return false;
  }

  refcount_inc(value);
  if (snek_obj->data.v_array.elements[index] != NULL){
    refcount_dec(snek_obj->data.v_array.elements[index]);
  }
  snek_obj->data.v_array.elements[index] = value;
  return true;
}

void refcount_free(snek_object_t *obj) {
  switch (obj->kind) {
  case INTEGER:
  case FLOAT:
    break;
  case STRING:
    free(obj->data.v_string);
    break;
  case VECTOR3: {
    snek_vector_t vec = obj->data.v_vector3;
    refcount_dec(vec.x);
    refcount_dec(vec.y);
    refcount_dec(vec.z);
    break;
  }
  case ARRAY: {
    for (size_t i = 0; i < obj->data.v_array.size; i++){
      refcount_dec(obj->data.v_array.elements[i]);
    }
    free(obj->data.v_array.elements);
    break;
  }
  default:
    assert(false);
  }
  free(obj);
}

// don't touch below this line

snek_object_t *snek_array_get(snek_object_t *snek_obj, size_t index) {
  if (snek_obj == NULL) {
    return NULL;
  }

  if (snek_obj->kind != ARRAY) {
    return NULL;
  }

  if (index >= snek_obj->data.v_array.size) {
    return NULL;
  }

  return snek_obj->data.v_array.elements[index];
}

void refcount_inc(snek_object_t *obj) {
  if (obj == NULL) {
    return;
  }

  obj->refcount++;
  return;
}

void refcount_dec(snek_object_t *obj) {
  if (obj == NULL) {
    return;
  }
  obj->refcount--;
  if (obj->refcount == 0) {
    refcount_free(obj);
    return;
  }
  return;
}

snek_object_t *_new_snek_object(void) {
  snek_object_t *obj = calloc(1, sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }

  obj->refcount = 1;

  return obj;
}

snek_object_t *new_snek_array(size_t size) {
  snek_object_t *obj = _new_snek_object();
  if (obj == NULL) {
    return NULL;
  }

  snek_object_t **elements = calloc(size, sizeof(snek_object_t *));
  if (elements == NULL) {
    free(obj);
    return NULL;
  }

  obj->kind = ARRAY;
  obj->data.v_array = (snek_array_t){.size = size, .elements = elements};

  return obj;
}

snek_object_t *new_snek_integer(int value) {
  snek_object_t *obj = _new_snek_object();
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = INTEGER;
  obj->data.v_int = value;
  return obj;
}

snek_object_t *new_snek_float(float value) {
  snek_object_t *obj = _new_snek_object();
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = FLOAT;
  obj->data.v_float = value;
  return obj;
}

snek_object_t *new_snek_string(char *value) {
  snek_object_t *obj = _new_snek_object();
  if (obj == NULL) {
    return NULL;
  }

  int len = strlen(value);
  char *dst = malloc(len + 1);
  if (dst == NULL) {
    free(obj);
    return NULL;
  }

  strcpy(dst, value);

  obj->kind = STRING;
  obj->data.v_string = dst;
  return obj;
}

snek_object_t *new_snek_vector3(snek_object_t *x, snek_object_t *y,
                                snek_object_t *z) {
  if (x == NULL || y == NULL || z == NULL) {
    return NULL;
  }
  snek_object_t *obj = _new_snek_object();
  if (obj == NULL) {
    return NULL;
  }
  obj->kind = VECTOR3;
  obj->data.v_vector3 = (snek_vector_t){.x = x, .y = y, .z = z};
  refcount_inc(x);
  refcount_inc(y);
  refcount_inc(z);
  return obj;
}

```


# Handling Cycles

We built a simple reference counting garbage collector. It can handle:

- Simple types, like `INT` and `FLOAT`
- Dynamically allocated types, like `STRING`
- Static container types, like `VECTOR3`
- Dynamic container types, like `ARRAY`

However, there's one little problem with our implementation. Take a look at this code:

```c
snek_object_t *first = new_snek_array(1);
snek_object_t *second = new_snek_array(1);
// refcounts: first = 1, second = 1
snek_array_set(first, 0, second);
// refcounts: first = 1, second = 2
refcount_dec(first);
// refcounts: first = 0, second = 1
refcount_dec(second);
// refcounts: first = 0, second = 0
// all free!
```

We create a `first` array, and shove the `second` array inside of it. Everything here works as expected. The trouble arises when we introduce a cycle: for example, `first` contains `second`, but `second` also contains `first`...

## Assignment

Run the code in its current state. Notice that the assertions in `main.c` _fail_. Even though we decremented both the `first` and `second` arrays' refcounts, neither was freed: the refcounts are not `0`!

**Fix the _assertions_ to pass by updating them to match the sad reality of our current implementation.**

You'll still see a [memory leak](https://en.wikipedia.org/wiki/Memory_leak) warning after you get the tests passing. That's expected! We're _proving_ that refcounting is broken for cycles, and we'll fix it in upcoming lessons.

## Observe

The reason both refcounts are stuck at `1` after being decremented is that, when `first` has its refcount decremented, it already has `2`. So it only drops to `1`, which does _not_ trigger a "free" of the `second` array:

```c
void refcount_dec(snek_object_t *obj) {
  if (obj == NULL) {
    return;
  }
  obj->refcount--;
  if (obj->refcount == 0) {
    // this doesn't happen when refcount is 1
    return refcount_free(obj);
  }
  return;
}
```

And because `second` still has `2` refcounts, it also only drops to `1`, which fails to trigger a "free" of the `first` array.

In other words, we have a **cycle**, and our simple reference counting garbage collector can't handle it.


```c
#include "bootlib.h"
#include "munit.h"
#include "snekobject.h"
#include <stdio.h>
#include <stdlib.h>

munit_case(RUN, correctly_free, {
  snek_object_t *first = new_snek_array(1);
  snek_object_t *second = new_snek_array(1);
  // refcounts: first = 1, second = 1
  snek_array_set(first, 0, second);
  // refcounts: first = 1, second = 2
  snek_array_set(second, 0, first);
  // refcounts: first = 2, second = 2
  refcount_dec(first);
  refcount_dec(second);
  assert_int(first->refcount, ==, 1, "Refcount first should be ?");
  assert_int(second->refcount, ==, 1, "Refcount second should be ?");
});

// Don't touch below this line

int main() {
  MunitTest tests[] = {
      munit_test("/correctly_free", correctly_free),
      munit_null_test,
  };

  MunitSuite suite = munit_suite("refcount", tests);

  int result = munit_suite_main(&suite, NULL, 0, NULL);

  printf("*** NOTE: A memory leak warning is EXPECTED here ***\n");
  printf("*** We'll fix the circular reference problem soon ***\n");

  return result;
}

```
# Pros and Cons

To solve our cyclic reference issue (and to force you to implement another GC algorithm, HA!) we're going to implement a [Mark and Sweep](https://en.wikipedia.org/wiki/Tracing_garbage_collection#Na%C3%AFve_mark-and-sweep) garbage collector.

## Pros of MaS

- Can detect cycles, and thus prevent memory leaks in certain cases
- Less on-demand bookkeeping (Remember: all work done by the GC is "wasted" – it doesn't make your ~~GPT-4 wrapper~~ custom AI product run any faster)
- Reduces potential performance degradation in highly multithreaded programs (refcounting requires atomic updates for thread safety)

## Cons of MaS

- More complex to implement (heh, you'll see)
- Can cause "stop-the-world" pauses when lots of objects exist and must be freed (resulting in poor performance)
- Higher memory overhead
- Less predictable performance

## Assignment

We'll be using a `vm_t` struct which stands for `Virtual Machine Type`. This `vm_t` simulates what would normally be tracked if Sneklang were a fully functional interpreted language (it's not). This virtual machine is much simpler than a real one because all we care about is demonstrating the garbage collection aspects.

You can spam Lane if you want a full "write your own programming language" course on boot.dev

Please don't. I have a wife and kids.

Open `vm.h` and take a look at the `vm_t` struct. The `frames` field holds a stack of frames, which are pushed and popped as we enter and exit new scopes. For example:

```python
msg1 = "This is in scope 1"


def outer_func():
    msg2 = "This is in scope 2"

    def inner_func():
        msg3 = "This is in scope 3"
        return

    return
```

At each of the `scope` entrances (in this case function calls), a new stack frame is pushed onto the `frames` stack. When we exit a scope (a function returns), we pop the stack frame off the `frames` stack. Because we use `void *` to work with generics in C, you can't actually tell what the data type held by the `stack_t` is for each field. We'll write some wrapper functions later to help us make sure that we don't accidentally push the wrong kinds of data into our stacks (yay, C!).

The `objects` field is also a stack, but it holds `snek_object_t` pointers.

1. [ ] In `vm.c` complete the `vm_new` function. It should:
    1. [ ] allocate space for a `vm_t` struct on the heap
    2. [ ] initialize the `frames` stack with a capacity of `8` and the `objects` stack with a capacity of `8` using the `stack_new` function
    3. [ ] return the pointer to our new `vm_t` struct
2. [ ] Complete the `vm_free` function. It should:
    1. [ ] free the `frames` and `objects` stacks (remember, we wrote a special `stack_free` function for this)
    2. [ ] free the `vm_t` struct itself
`vm.c`
```c
#include "vm.h"

vm_t *vm_new(void) {
  vm_t *new_ptr = malloc(sizeof(vm_t));
  if (new_ptr == NULL){
    return NULL;
  }
  new_ptr->frames = stack_new(8);
  new_ptr->objects = stack_new(8);
  return new_ptr;
}

void vm_free(vm_t *vm) {
  stack_free(vm->frames);
  stack_free(vm->objects);
  free(vm);
}
```

`vm.h`
```c
#include "stack.h"

typedef struct VirtualMachine {
  stack_t *frames;
  stack_t *objects;
} vm_t;

vm_t *vm_new(void);
void vm_free(vm_t *vm);


```
stack.h
```c
#include <stddef.h>
#include <stdlib.h>

typedef struct Stack {
  size_t count;
  size_t capacity;
  void **data;
} stack_t;

stack_t *stack_new(size_t capacity);

void stack_push(stack_t *stack, void *obj);
void *stack_pop(stack_t *stack);

void stack_free(stack_t *stack);
void stack_remove_nulls(stack_t *stack);

```

stack.h
```c
#include "stack.h"
#include "munit.h"
#include <stdio.h>

void stack_push(stack_t *stack, void *obj) {
  if (stack->count == stack->capacity) {
    // Double stack capacity to avoid reallocing often
    stack->capacity *= 2;
    stack->data = realloc(stack->data, stack->capacity * sizeof(void *));
    if (stack->data == NULL) {
      // Unable to realloc, just exit :) get gud
      exit(1);
    }
  }

  stack->data[stack->count] = obj;
  stack->count++;

  return;
}

void *stack_pop(stack_t *stack) {
  if (stack->count == 0) {
    return NULL;
  }

  stack->count--;
  return stack->data[stack->count];
}

void stack_free(stack_t *stack) {
  if (stack == NULL) {
    return;
  }

  if (stack->data != NULL) {
    free(stack->data);
  }

  free(stack);
}

void stack_remove_nulls(stack_t *stack) {
  size_t new_count = 0;

  // Iterate through the stack and compact non-NULL pointers.
  for (size_t i = 0; i < stack->count; ++i) {
    if (stack->data[i] != NULL) {
      stack->data[new_count++] = stack->data[i];
    }
  }

  // Update the count to reflect the new number of elements.
  stack->count = new_count;

  // Optionally, you might want to zero out the remaining slots.
  for (size_t i = new_count; i < stack->capacity; ++i) {
    stack->data[i] = NULL;
  }
}

stack_t *stack_new(size_t capacity) {
  stack_t *stack = malloc(sizeof(stack_t));
  if (stack == NULL) {
    return NULL;
  }

  stack->count = 0;
  stack->capacity = capacity;
  stack->data = malloc(stack->capacity * sizeof(void *));
  if (stack->data == NULL) {
    free(stack);
    return NULL;
  }

  return stack;
}

```


# Stack Frames

Think back to the warnings I gave you about working with `void*` data types. It's easy to push the wrong kinds of data onto our `stack_t` because, like Starbucks Wi-Fi, it will let _anything_ in.

So, to prevent us from shooting ourselves in the foot, we will create some functions that are more type safe and make it much more difficult to do the wrong thing when interacting with our `vm_t`. Wrong things like:

```c
// The C compiler won't stop us :'(
stack_push(vm->frames, (void *)7);
stack_push(vm->frames, (void *)"uh oh");
```

But we want to make it easier on ourselves to only push `frame_t *` types onto `vm->frames`, so we'll write some wrapper functions to help us out.

## Assignment

Take a look at the `frame_t` type in `vm.h`. It's a simple struct that holds a `stack_t` of `snek_object_t *` pointers that represent the object references in the frame.

1. [ ] Complete the `vm_frame_push` function in `vm.c`. It should `stack_push` a `frame_t *` onto the `vm->frames` stack.
2. [ ] Complete the `vm_new_frame` function in `vm.c`. It should:
    1. [ ] Allocate a new `frame_t` on the heap.
    2. [ ] Initialize the frame's references with a `stack_new` of capacity `8`.
    3. [ ] Push the newly allocated frame onto the `vm->frames` stack.
    4. [ ] Return the newly allocated frame.
3. [ ] Complete the `frame_free` function in `vm.c`. It should:
    1. [ ] Free the `frame_t`'s `references` stack (we have a special function for this)
    2. [ ] Free the `frame_t` struct.

```c
#include "vm.h"

void vm_frame_push(vm_t *vm, frame_t *frame) {
  stack_push(vm->frames, frame);
}

frame_t *vm_new_frame(vm_t *vm) {
  frame_t *new_ptr = malloc(sizeof(frame_t));
  if (new_ptr == NULL){
    return NULL;
  }

  new_ptr->references = stack_new(8);
  stack_push(vm->frames, new_ptr);
  return new_ptr;
}

void frame_free(frame_t *frame) {
  stack_free(frame->references);
  free(frame);
}

// don't touch below this line

vm_t *vm_new(void) {
  vm_t *vm = malloc(sizeof(vm_t));
  if (vm == NULL) {
    return NULL;
  }

  vm->frames = stack_new(8);
  vm->objects = stack_new(8);
  return vm;
}

void vm_free(vm_t *vm) {
  for (size_t i = 0; i < vm->frames->count; i++) {
    frame_free(vm->frames->data[i]);
  }
  stack_free(vm->frames);
  stack_free(vm->objects);
  free(vm);
}

```

```c
#include "vm.h"

void vm_frame_push(vm_t *vm, frame_t *frame) {
  stack_push(vm->frames, frame);
}

frame_t *vm_new_frame(vm_t *vm) {
  frame_t *new_ptr = malloc(sizeof(frame_t));
  if (new_ptr == NULL){
    return NULL;
  }

  new_ptr->references = stack_new(8);
  stack_push(vm->frames, new_ptr);
  return new_ptr;
}

void frame_free(frame_t *frame) {
  stack_free(frame->references);
  free(frame);
}

// don't touch below this line

vm_t *vm_new(void) {
  vm_t *vm = malloc(sizeof(vm_t));
  if (vm == NULL) {
    return NULL;
  }

  vm->frames = stack_new(8);
  vm->objects = stack_new(8);
  return vm;
}

void vm_free(vm_t *vm) {
  for (size_t i = 0; i < vm->frames->count; i++) {
    frame_free(vm->frames->data[i]);
  }
  stack_free(vm->frames);
  stack_free(vm->objects);
  free(vm);
}

```
# Tracking Objects

Our virtual machine needs to track _every Snek object_ that gets created.

We are no longer going to track how many times an object is referenced, but instead check _at garbage collection time_ if each object is still referenced **at all**. If it is, keep it. If not, free it.

## Assignment

If a file tab is out of view, scroll the file tabs horizontally.

1. [ ] In `vm.c` complete the `vm_track_object`, which adds an object to our `vm->objects` stack in a more type-safe way.
2. [ ] In `sneknew.c` update the `_new_snek_object` function. Before returning the newly allocated object, it should ensure it's tracked by the VM.
```c
#include "sneknew.h"
#include "snekobject.h"
#include "vm.h"
#include <stdlib.h>
#include <string.h>

snek_object_t *_new_snek_object(vm_t *vm) {
  snek_object_t *obj = calloc(1, sizeof(snek_object_t));
  if (obj == NULL) {
    return NULL;
  }
  vm_track_object(vm, obj);
  return obj;
}

// don't touch below this line

snek_object_t *new_snek_array(vm_t *vm, size_t size) {
  snek_object_t *obj = _new_snek_object(vm);
  if (obj == NULL) {
    return NULL;
  }

  snek_object_t **elements = calloc(size, sizeof(snek_object_t *));
  if (elements == NULL) {
    free(obj);
    return NULL;
  }

  obj->kind = ARRAY;
  obj->data.v_array = (snek_array_t){.size = size, .elements = elements};

  return obj;
}

snek_object_t *new_snek_vector3(vm_t *vm, snek_object_t *x, snek_object_t *y,
                                snek_object_t *z) {
  if (x == NULL || y == NULL || z == NULL) {
    return NULL;
  }

  snek_object_t *obj = _new_snek_object(vm);
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = VECTOR3;
  obj->data.v_vector3 = (snek_vector_t){.x = x, .y = y, .z = z};

  return obj;
}

snek_object_t *new_snek_integer(vm_t *vm, int value) {
  snek_object_t *obj = _new_snek_object(vm);
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = INTEGER;
  obj->data.v_int = value;

  return obj;
}

snek_object_t *new_snek_float(vm_t *vm, float value) {
  snek_object_t *obj = _new_snek_object(vm);
  if (obj == NULL) {
    return NULL;
  }

  obj->kind = FLOAT;
  obj->data.v_float = value;
  return obj;
}

snek_object_t *new_snek_string(vm_t *vm, char *value) {
  snek_object_t *obj = _new_snek_object(vm);
  if (obj == NULL) {
    return NULL;
  }

  int len = strlen(value);
  char *dst = malloc(len + 1);
  if (dst == NULL) {
    free(obj);
    return NULL;
  }

  strcpy(dst, value);

  obj->kind = STRING;
  obj->data.v_string = dst;
  return obj;
}

```

```c
#include "vm.h"
#include "snekobject.h"
#include "stack.h"

void vm_track_object(vm_t *vm, snek_object_t *obj) {
  stack_push(vm->objects, obj);
}

// don't touch below this line

vm_t *vm_new(void) {
  vm_t *vm = malloc(sizeof(vm_t));
  if (vm == NULL) {
    return NULL;
  }

  vm->frames = stack_new(8);
  vm->objects = stack_new(8);
  return vm;
}

void vm_free(vm_t *vm) {
  for (size_t i = 0; i < vm->frames->count; i++) {
    frame_free(vm->frames->data[i]);
  }
  stack_free(vm->frames);
  stack_free(vm->objects);
  free(vm);
}

void vm_frame_push(vm_t *vm, frame_t *frame) { stack_push(vm->frames, frame); }

frame_t *vm_new_frame(vm_t *vm) {
  frame_t *frame = malloc(sizeof(frame_t));
  frame->references = stack_new(8);

  vm_frame_push(vm, frame);
  return frame;
}

void frame_free(frame_t *frame) {
  stack_free(frame->references);
  free(frame);
}

```

# Free

Recall the `refcount_free` function that you wrote in the previous chapter. It should have looked something like this:

```c
void refcount_free(snek_object_t *obj) {
  switch (obj->kind) {
    case INTEGER:
    case FLOAT:
      break;
    case STRING:
      free(obj->data.v_string);
      break;
    case VECTOR3: {
      snek_vector_t vec = obj->data.v_vector3;
      refcount_dec(vec.x);
      refcount_dec(vec.y);
      refcount_dec(vec.z);
      break;
    }
    case ARRAY: {
      snek_array_t *array = &obj->data.v_array;
      for (size_t i = 0; i < array->size; i++) {
        refcount_dec(array->elements[i]);
      }
      free(array->elements);
      break;
    }
  }
  free(obj);
}
```

## Assignment

Let's rewrite our free-ing logic for mark-and-sweep. Because the virtual machine is the one tracking objects, all of the `refcount_dec` work can be removed! There's some very cool tricks coming up for mark-and-sweep to manage this, but for now you can just trust me that we'll correctly free any of the contained elements if they are no longer alive.

1. [ ] In `snekobject.c` complete the `snek_object_free` function.
    1. [ ] `INTEGER`, `FLOAT`, and `STRING` objects should all work the same as the refcount version (non container types).
    2. [ ] `VECTOR3` doesn't need to do _anything_ before freeing the object, because the mark-and-sweep will handle the contained objects.
    3. [ ] `ARRAY` should free the `elements` array, but not the objects themselves because the mark-and-sweep will handle that.
2. [ ] In `vm.c` complete the `vm_free` function.
    1. [ ] Iterate over all the VM's frames and free them using `frame_free`.
    2. [ ] Free the `frames` stack itself using `stack_free`.
    3. [ ] Iterate over all the VM's objects and free them using `snek_object_free`.
    4. [ ] Free the `objects` stack itself using `stack_free`.
    5. [ ] Free the VM struct itself.

```c
#include "vm.h"
#include "stack.h"

void vm_free(vm_t *vm) {
  stack_t *frames = vm->frames;
  for (size_t i = 0; i < frames->count; i++){
    frame_free((frame_t*)frames->data[i]);
  }
  stack_free(frames);

  stack_t *objects = vm->objects;
  for (size_t i = 0; i < objects->count; i++){
    snek_object_free((snek_object_t*)objects->data[i]);
  }
  stack_free(vm->objects);
  free(vm);
}

// don't touch below this line

vm_t *vm_new(void) {
  vm_t *vm = malloc(sizeof(vm_t));
  if (vm == NULL) {
    return NULL;
  }

  vm->frames = stack_new(8);
  vm->objects = stack_new(8);
  return vm;
}

void vm_track_object(vm_t *vm, snek_object_t *obj) {
  stack_push(vm->objects, obj);
}

void vm_frame_push(vm_t *vm, frame_t *frame) { stack_push(vm->frames, frame); }

frame_t *vm_new_frame(vm_t *vm) {
  frame_t *frame = malloc(sizeof(frame_t));
  frame->references = stack_new(8);

  vm_frame_push(vm, frame);
  return frame;
}

void frame_free(frame_t *frame) {
  stack_free(frame->references);
  free(frame);
}

```