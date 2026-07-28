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
