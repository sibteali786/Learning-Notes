# Learn Go

![golang gopher](https://go.dev/blog/gopher/header.jpg)

Go is one of the fastest-growing languages in the world, and it's the language Boot.dev's own backend is written in! In this course, you'll learn it by building parts of a make-believe [SaaS](https://www.salesforce.com/saas/) app: **Textio**, which programmatically sends SMS (text messages) to customers.

The code on the right is a complete program:

1. `package main` tells the Go compiler this code is a standalone program, not a library for other programs to import.
2. `import "fmt"` pulls in the [`fmt` package](https://pkg.go.dev/fmt) from the [standard library](https://pkg.go.dev/std) so we can print to the console.
3. `func main()` is the entry point.

This course assumes you're already familiar with programming basics in at least one other language. If you're _brand brand new_ to coding, start with [Python for beginners](https://boot.dev/courses/learn-python-beginners) instead.

## Assignment

**Edit the code to print `starting server...` to the console instead of `edit me`.**

Capitalization and punctuation matter!

```go
package main

import "fmt"

func main() {
	fmt.Println("starting server...")
}

```

# Declaring a Variable

The [`var`](https://go.dev/ref/spec#Variable_declarations) keyword is used to declare a variable ~~the sad way~~. For example, to declare an integer variable called `mySkillIssues` and assign it the value `42`:

```go
// create a new variable, it defaults to 0
// (the "zero value" for ints)
var mySkillIssues int

// overwrite the zero value with 42
mySkillIssues = 42
```

## Assignment

The code _should_ print the user's sending limit... _but there's a syntax bug_!

**Fix the syntax error on line 6**.

Don't worry, we'll talk about a _better_ way to declare variables soon.

```go
package main

import "fmt"

func main() {
	var smsSendingLimit int
	smsSendingLimit = 1000
	fmt.Println("Your SMS sending limit is", smsSendingLimit)
}

```

# Basic Variables

Some of Go's most common variable [types](https://go.dev/ref/spec#Types) are:

- `int`: a signed integer
- `bool`: a boolean value, either `true` or `false`
- `string`: a sequence of characters
- `float64`: a floating-point number
- `byte`: exactly what it sounds like: 8 bits of data

And to use them, their values are set like this:

```go
var health int
health = 100

var isAwesome bool
isAwesome = true

var greeting string
greeting = "Hello, world!"

var pi float64
pi = 3.14159

var data byte
data = 0xFF
```

Don't worry, we'll talk about a better way to declare variables in the next lesson.

## Assignment

Run (but don't submit yet!) the code. Notice that the `username` is blank!

**Set the `username` variable to the value "eddie_cabot"**. Then submit the fixed code.
```go
package main

import "fmt"

func main() {
	var username string
	username = "eddie_cabot"

	var isAdmin bool
	isAdmin = true

	var permissions int
	permissions = 0x1F

	var costPerSMS float64
	costPerSMS = 0.05

	fmt.Println("username:", username)
	fmt.Println("isAdmin:", isAdmin)
	fmt.Println("permissions:", permissions)
	fmt.Println("costPerSMS:", costPerSMS)
}

```

# Short Variable Declaration

Sad variable declaration:

```go
var mySkillIssues int
mySkillIssues = 42
```

GOATed variable declaration:

```go
mySkillIssues := 42
```

The walrus operator, `:=`, declares a new variable and assigns a value to it in one line. Go can infer that `mySkillIssues` is an `int` because of the `42` value. Yay [type inference](https://en.wikipedia.org/wiki/Type_inference)!

## When to Use the Walrus Operator

The `:=`, (walrus operator) should be used instead of [var](https://go.dev/tour/basics/9) style declarations basically anywhere possible. The limitation is that `:=` can't be used outside of a function (in the [global/package scope](https://dave.cheney.net/2017/06/11/go-without-package-scoped-variables) which we'll talk about later).

Type inference is based on the value being assigned.

An `int`:

```go
mySkillIssues := 42
```

A `float64`:

```go
pi := 3.14159
```

A `string`:

```go
message := "Hello, world!"
```

A `bool`:

```go
isGoat := true
```

## Assignment

A common use case for Textio is to send birthday messages.

1. [ ] Complete the `main` function. It should print: "Happy birthday! You are now 21 years old!".
    - [ ] Create a string variable `messageStart` with the text "Happy birthday! You are now"
    - [ ] Create an integer variable `age` set to `21`
    - [ ] Create another string variable `messageEnd` with the text "years old!"
2. [ ] The provided `fmt.Println` statement will print the full message on a single line separated by spaces.


# Short Variable Declaration

Sad variable declaration:

```go
var mySkillIssues int
mySkillIssues = 42
```

GOATed variable declaration:

```go
mySkillIssues := 42
```

The walrus operator, `:=`, declares a new variable and assigns a value to it in one line. Go can infer that `mySkillIssues` is an `int` because of the `42` value. Yay [type inference](https://en.wikipedia.org/wiki/Type_inference)!

## When to Use the Walrus Operator

The `:=`, (walrus operator) should be used instead of [var](https://go.dev/tour/basics/9) style declarations basically anywhere possible. The limitation is that `:=` can't be used outside of a function (in the [global/package scope](https://dave.cheney.net/2017/06/11/go-without-package-scoped-variables) which we'll talk about later).

Type inference is based on the value being assigned.

An `int`:

```go
mySkillIssues := 42
```

A `float64`:

```go
pi := 3.14159
```

A `string`:

```go
message := "Hello, world!"
```

A `bool`:

```go
isGoat := true
```

## Assignment

A common use case for Textio is to send birthday messages.

1. [ ] Complete the `main` function. It should print: "Happy birthday! You are now 21 years old!".
    - [ ] Create a string variable `messageStart` with the text "Happy birthday! You are now"
    - [ ] Create an integer variable `age` set to `21`
    - [ ] Create another string variable `messageEnd` with the text "years old!"
2. [ ] The provided `fmt.Println` statement will print the full message on a single line separated by spaces.
```go
package main

import "fmt"

func main() {
	messageStart := "Happy birthday! You are now"
	age := 21
	messageEnd := "years old!"
	fmt.Println(messageStart, age, messageEnd)
}

```

# Why Go?

Go is my favorite programming language by a good margin.

![go features](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/RxCpanC-1280x720.png)

- **It's fast.** Go compiles to a single native binary, and it compiles _fast_.
- **It's simple.** It's a small language without a ton of feature bloat.
- **It's statically typed.** The compiler catches type bugs before your code even runs.
- **Concurrency is built in.** Goroutines are very powerful, which is a big reason tools like Docker and Kubernetes are written in Go.

We'll dig into all of that later. For now, _let's whet your appetite with some more code._

## Assignment

**Critical bug!**

Textio users reported that we're billing them for _wildly inaccurate amounts_. They're _supposed_ to be billed `.02` dollars (2 cents) for each text message sent.

Without changing any of the other lines, **fix the math bug in the `totalCost` calculation.**

`float64(numMessagesFromDoris)` converts the integer to a `float64` so it can be used in math with `costPerMessage`. Go won't mix number types silently. More on that soon.

```go
package main

import "fmt"

func main() {
	numMessagesFromDoris := 72
	costPerMessage := .02
	totalCost := costPerMessage * float64(numMessagesFromDoris)
	fmt.Printf("Doris spent %.2f on text messages today\n", totalCost)
}

```

# Comments

Go has two styles of comments:

```go
// This is a single line comment

/*
  This is a multi-line comment
  neither of these comments will execute
  as code
*/
```

## Assignment

The new intern on the team screwed up their documentation comment.

Fix the issue.

```go
package main

import "fmt"

func main() {
	/*
		We are increasing the maximum message length from 140 to 280 characters.
		Very reluctantly, I might add.
		Users actually want to write more than 140 characters?!? Madness.
	*/
	maxMessageLength := 140
	newMaxMessageLength := 280
	fmt.Println("Textio is increasing the maximum message length from", maxMessageLength, "to", newMaxMessageLength, "characters.")
}

```

# The Compilation Process

Computers need machine code, they don't understand English or even Go. We need to convert our high-level (Go) code into machine language, which is really just a set of instructions that some specific hardware can understand. In your case, your CPU.

The Go compiler's job is to take Go code and produce machine code, an `.exe` file on Windows or a standard executable on Mac/Linux.

![compiler](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/clmYRJv-1130x480.png)

## Two Kinds of Errors

Loosely speaking, there are two kinds of errors in programming:

1. **Compilation errors** happen when the code is compiled. They're the good kind: a program with a compiler error won't build, so it can't ship to production.
2. **Runtime errors** happen while the program is running. They're worse because they can crash a program that's already in use.

In the browser we compile and run in one step, so you'll see both kinds in the same output panel.

## Assignment

1. [ ] Run the code. Notice the compilation error? It's due to invalid syntax.
2. [ ] Fix the compilation error in the code.

```go
package main

import "fmt"

func main() {
	fmt.Println("The compiled textio server is starting")
}

```

# Fast and Compiled

Generally speaking, languages that [compile](https://en.wikipedia.org/wiki/Compiled_language) directly to [machine code](https://simple.wikipedia.org/wiki/Machine_code) produce programs that are faster than [interpreted](https://en.wikipedia.org/wiki/Interpreter_\(computing\)) programs.

_Go is one of the fastest programming languages_, beating JavaScript, Python, and Ruby handily in most benchmarks.

However, Go programs don't run quite as fast as its compiled Rust, Zig, and C counterparts. That said, it _compiles_ much faster than they do, which makes the developer experience super productive. Unfortunately, there are no swordfights on Go teams...

![xkcd compiling](https://imgs.xkcd.com/comics/compiling.png)

_- comic by [xkcd](https://xkcd.com/303/)_

# Type Sizes

Integers, [uints](https://www.cs.utah.edu/~germain/PPS/Topics/unsigned_integer.html#:~:text=Unsigned%20Integers,negative%20\(zero%20or%20positive\).), [floats](https://techterms.com/definition/floatingpoint), and [complex](https://byjus.com/maths/complex-numbers/) numbers all have type sizes.

- **Signed integers** (no decimal)

```go
int  int8  int16  int32  int64
```

- **Unsigned integers** (non-negative numbers/no decimal)

```go
uint uint8 uint16 uint32 uint64 uintptr
```

- **Signed decimal numbers**

```go
float32 float64
```

- **Complex numbers** (a complex number has a real and imaginary part)

```go
complex64 complex128
```

## What's the Deal With the Sizes?

The size (8, 16, 32, 64, 128, etc.) represents how many [bits](https://en.wikipedia.org/wiki/Bit) in memory will be used to store the variable. The "default" `int` and `uint` types refer to their respective 32 or 64-bit sizes depending on the environment of the user.

The "standard" types that should be used unless you have a specific performance need (e.g. using less memory) are:

- `int`
- `uint`
- `float64`
- `complex128`

## Converting Between Types

Some types can be easily converted like this:

```go
temperatureFloat := 88.26
temperatureInt := int(temperatureFloat)
```

Casting a float to an integer in this way [truncates](https://techterms.com/definition/truncate) the floating point portion.

## Assignment

Our Textio customers want to know how long they have had accounts with us.

On line 7, create an `accountAgeInt` variable and assign it the value of `accountAgeFloat` truncated to an integer.

```go
package main

import "fmt"

func main() {
	accountAgeFloat := 2.6
	accountAgeInt := int(accountAgeFloat)
	fmt.Println("Your account has existed for", accountAgeInt, "years")
}

```


# Which Type Should I Use?

With so many types for what is essentially just a number, developers coming from languages that only have one kind of `Number` type (like JavaScript) may find the choices daunting.

## Prefer “Default” Types

A problem arises when we have a `uint16`, and the function we are trying to pass it into takes an `int`. We're forced to write code riddled with type conversions like:

```go
var myAge uint16 = 25
myAgeInt := int(myAge)
```

This style of code can be slow and annoying to read. When Go developers stray from the "default" type for any given type family, the code can get messy quickly. Unless you have a good _performance related_ reason, you'll typically just want to use the "default" types:

- `bool`
- `string`
- `int`
- `uint`
- `byte`
- `rune`
- `float64`
- `complex128`

## When Should I Use a More Specific Type?

When you're super concerned about performance and memory usage.

That's about it. The only reason to deviate from the defaults is to squeeze out every last bit of performance when you are writing an application that is resource-constrained. (Or, in the special case of `uint64`, you need an absurd range of unsigned integers).


# Go Is Statically Typed

Go enforces [static typing](https://developer.mozilla.org/en-US/docs/Glossary/Static_typing) meaning variable types are known _before_ the code runs. That means your editor and the compiler can display type errors before the code is ever run, making development easier and faster.

Contrast this with most dynamically typed languages like JavaScript and Python... Dynamic typing often leads to subtle bugs that are hard to detect. The code _must_ be run to catch syntax and type errors. (sometimes in production if you're unlucky 😨)

Languages also have [strong or weak typing](https://en.wikipedia.org/wiki/Strong_and_weak_typing), meaning stricter or weaker type checking rules.

## Concatenating Strings

Two strings can be [concatenated](https://en.wikipedia.org/wiki/Concatenation) with the `+` operator. But the compiler will not allow you to concatenate a `string` variable with an `int` or a `float64`.

## Assignment

Textio uses [basic authentication](https://en.wikipedia.org/wiki/Basic_access_authentication) to log users in.

The code on the right has a type error. Change the assignment statement on line 7 to use a string value for `password` instead of an integer (but don't use a different password) so that it can be concatenated with the `username` variable.

```go
package main

import "fmt"

func main() {
	var username string = "presidentSkroob"
	var password string = "12345"

	// don't edit below this line
	fmt.Println("Authorization: Basic", username+":"+password)
}

```

# Compiled vs. Interpreted

You can run a compiled program _without_ the original source code. You don't need the compiler anymore after it's done its job. That's how most video games are distributed! Players don't need to install the correct version of `Go` to run a PC game: they just download the executable game and run it.

![compiler vs interpreter](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/l3iv7KS-999x722.png)

With interpreted languages like Python and Ruby, the code is interpreted at [runtime](https://en.wikipedia.org/wiki/Runtime_\(program_lifecycle_phase\)) by a separate program known as the "interpreter". Distributing code for users to run can be a pain because they need to have an interpreter installed, and they need access to the source code.

## Examples of Compiled Languages

- Go
- C
- C++
- Rust

## Examples of Interpreted Languages

- JavaScript (sometimes JIT-compiled, but a similar concept)
- Python
- Ruby

## Why Build Textio in a Compiled Language?

One of the most convenient things about using a compiled language like Go for Textio is that when we deploy our server we don't need to include any runtime language dependencies like Node or a Python interpreter. We just add the pre-compiled binary to the server and start it up!

# Same Line Declarations

You can declare multiple variables on the same line:

```go
mileage, company := 80276, "Toyota"
```

The above is the same as:

```go
mileage := 80276
company := "Toyota"
```

## Assignment

At the top of the `main` function, declare a float called `averageOpenRate` and string called `displayMessage` _on the same line._

Initialize them to values:

- `.23`
- `is the average open rate of your messages`

before they're printed.

```go
package main

import "fmt"

func main() {
	averageOpenRate := .23
	displayMessage := "is the average open rate of your messages"
	fmt.Println(averageOpenRate, displayMessage)
}

```

# Small Memory Footprint

Go programs are fairly lightweight. Each program includes a small amount of extra code that's included in the executable binary called the [Go Runtime](https://go.dev/doc/faq#runtime). One of the purposes of the Go runtime is to clean up unused memory at runtime. It includes a [garbage collector](https://en.wikipedia.org/wiki/Garbage_collection_\(computer_science\)) that automatically frees up memory that's no longer in use.

## Comparison

As a general rule, Java programs use _more_ memory than comparable Go programs. There are several reasons for this, but one of them is that Java uses a virtual machine to interpret bytecode at runtime and typically allocates more on the [heap](https://courses.grainger.illinois.edu/cs225/fa2022/resources/stack-heap/).

On the other hand, Rust and C programs use slightly _less_ memory than Go programs because more control is given to the developer to optimize the memory usage of the program. The Go runtime just handles it for us automatically.

## Idle Memory Usage

![idle memory](https://miro.medium.com/max/1400/1*Ggs-bJxobwZmrbfuoWGpFw.png)

In the chart above, [Dexter Darwich compares the memory usage](https://medium.com/@dexterdarwich/comparison-between-java-go-and-rust-fdb21bd5fb7c) of three _very_ simple programs written in Java, Go, and Rust. As you can see, Go and Rust use _very_ little memory when compared to Java.

Click to hide video

Your browser does not support playing HTML5 video. You can instead. Here is a description of the content: go vs rust

