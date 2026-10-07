```table-of-contents
```
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

# Constants

Constants are declared with the `const` keyword. They can't use the `:=` short declaration syntax.

```go
const pi = 3.14159
```

Constants can be primitive types like strings, integers, booleans and floats. They _cannot_ be more complex types like slices, maps and structs, which are types we will explain later.

As the name implies, the value of a constant can't be changed after it has been declared.

## Use Two Separate Constants

Something weird is happening in this code.

What _should_ be happening is that we create 2 separate constants: `premiumPlanName` and `basicPlanName`. Right now it looks like we're trying to overwrite one of them.

## Assignment

Complete the code to remove the bug and create the constant `basicPlanName`.

```go
package main

import "fmt"

func main() {
	const premiumPlanName = "Premium Plan"
	basicPlanName := "Basic Plan"

	// don't edit below this line

	fmt.Println("plan:", premiumPlanName)
	fmt.Println("plan:", basicPlanName)
}

```

# Computed Constants

Constants must be known at compile time. They are _usually_ declared with a static value:

```go
const myInt = 15
```

However, constants _can be computed_ as long as the computation can happen at _compile time_.

For example, this is valid:

```go
const firstName = "Lane"
const lastName = "Wagner"
const fullName = firstName + " " + lastName
```

That said, you _cannot_ declare a constant that can only be computed at run-time like you can in JavaScript. This breaks:

```go
// the current time can only be known when the program is running
const currentTime = time.Now()
```

## Assignment

Keeping track of time in a message-sending application is _critical_. Imagine getting an appointment reminder an hour **after** your doctor's visit.

Complete the code using a computed constant to print the number of seconds in an hour.

```go
package main

import "fmt"

func main() {
	const secondsInMinute = 60
	const minutesInHour = 60
	const secondsInHour = minutesInHour * secondsInMinute

	// don't edit below this line
	fmt.Println("number of seconds in an hour:", secondsInHour)
}
```


# Comparing Go's Speed

Go is _generally_ faster and more lightweight than interpreted or VM-powered languages like:

- Python
- JavaScript
- PHP
- Ruby
- Java

However, in terms of execution speed, Go does lag behind some other compiled languages like:

- C
- C++
- Rust

Go is a bit slower mostly due to its automated memory management, also known as the "Go runtime". Slightly slower speed is the price we pay for memory safety and simple syntax!

![speed comparison](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/tUIWLob-705x400.png)

Textio is an amazing candidate for a Go project. We'll be able to quickly process large amounts of text all while using a language that is safe and simple to write.

# Formatting Strings in Go

Go follows the [printf tradition](https://cplusplus.com/reference/cstdio/printf/) from the C language. In my opinion, string formatting/interpolation in Go is _less_ elegant than Python's f-strings, unfortunately.

- [fmt.Printf()](https://pkg.go.dev/fmt#Printf) - Prints a formatted string to [standard out](https://stackoverflow.com/questions/3385201/confused-about-stdin-stdout-and-stderr).
- [fmt.Sprintf()](https://pkg.go.dev/fmt#Sprintf) - Returns the formatted string

These following "formatting verbs" work with the formatting functions above:

## Default Representation

The `%v` variant prints any value in a default format. It can be used as a catchall.

```go
s := fmt.Sprintf("I am %v years old", 10)
// I am 10 years old

s := fmt.Sprintf("I am %v years old", "way too many")
// I am way too many years old
```

If you want to print in a more specific way, you can use the following formatting verbs:

## String

```go
s := fmt.Sprintf("I am %s years old", "way too many")
// I am way too many years old
```
## Integer

```go
s := fmt.Sprintf("I am %d years old", 10)
// I am 10 years old
```

## Float

```go
s := fmt.Sprintf("I am %f years old", 10.523)
// I am 10.523000 years old

// The ".2" rounds the number to 2 decimal places
s := fmt.Sprintf("I am %.2f years old", 10.523)
// I am 10.52 years old
```

If you're interested in all the formatting options, you can look at the `fmt` package's [docs](https://pkg.go.dev/fmt#hdr-Printing).

## Assignment

Create a new variable called `msg` on line 11 and use the appropriate formatting function to return a string that contains the following:

```text
Hi NAME, your open rate is OPENRATE percentNEWLINE
```

- Replace `NAME` with the variable `name`,
- Replace `OPENRATE` with the variable `openRate` rounded to the nearest "tenths" place, e.g `10.523` should be rounded down to `10.5`
- The word percent should appear as part of the string following the open rate value
- Replace `NEWLINE` with the newline [`\n`](https://en.wikipedia.org/wiki/Newline) escape sequence.

For example, with the inputs `"Jimmy McGill"` and `2.5`, the expected output would be:

```text
Hi Jimmy McGill, your open rate is 2.5 percent
```

```go
package main

import "fmt"

func main() {
	const name = "Saul Goodman"
	const openRate = 30.54

	// don't edit above this line

	msg := fmt.Sprintf("Hi %s, your open rate is %.1f percent\n", name, openRate)

	// don't edit below this line

	fmt.Print(msg)
}

```

# Runes and String Encoding

In many programming languages (cough, C, cough), a "character" is a single byte. Using [ASCII](https://www.asciitable.com/) encoding, the standard for the C programming language, we can represent 128 characters with 7 bits. This is enough for the English alphabet, numbers, and some special characters.

In Go, strings are just sequences of bytes: they can hold arbitrary data. However, Go also has a special type, [`rune`](https://go.dev/blog/strings), which is an alias for `int32`. This means that a `rune` is a 32-bit integer, which is large enough to hold any [Unicode](https://home.unicode.org/) code point.

When you're working with strings, you need to be aware of the encoding (bytes -> representation). Go uses [UTF-8](https://en.wikipedia.org/wiki/UTF-8) encoding, which is a variable-length encoding.

### UTF-8 Text

Type text to see its code points and bytes. Joining adjacent emoji inserts a [zero width joiner](https://en.wikipedia.org/wiki/Zero-width_joiner) (U+200D).

boots🐻é👨‍👩密碼

6 code points· 9 bytes

bU+0062

0x62

oU+006F

0x6F

oU+006F

0x6F

tU+0074

0x74

sU+0073

0x73

🐻U+1F43B

0xF00x9F0x900xBB

## What Does This Mean?

There are 2 main takeaways:

1. When you need to work with individual characters in a string, you should use the `rune` type. It breaks strings up into their individual characters, which can be more than one byte long.
2. We can include a wide variety of Unicode characters in our strings, such as emojis and Chinese characters, and Go will handle them just fine.

## Assignment

Boots is a _bear_. (Not a dog, haters).

1. [ ] Run the code as-is. Notice that the simple string "boots" has 5 bytes, and 5 runes (characters).
2. [ ] Update the `name` constant to be the [bear emoji](https://emojipedia.org/bear) instead of the word "boots".

```text
🐻
```

If you've got it right, you should notice that the emoji is only one rune, but it takes up 4 bytes.

```go
package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {
	const name = "🐻"
	fmt.Printf("constant 'name' byte length: %d\n", len(name))
	fmt.Printf("constant 'name' rune length: %d\n", utf8.RuneCountInString(name))
	fmt.Println("=====================================")
	fmt.Printf("Hi %s, so good to have you back in the arcanum\n", name)
}

```

# Format Practice

You've been asked to improve the logs to include information about individual users and their recent messages.

## Assignment

Create a `userLog` variable on line 15. It should contain:

```text
Name: FNAME LNAME, Age: AGE, Rate: MESSAGERATE, Is Subscribed: ISSUBSCRIBED, Message: MESSAGE
```

Where `FNAME` `LNAME` `AGE` `MESSAGERATE` `ISSUBSCRIBED` and `MESSAGE` correspond to the variables above.

`MESSAGERATE` should be rounded to the `tenths` place.

## Tips

- [fmt.Sprintf](https://golang.org/pkg/fmt/#Sprintf) can be used to format strings.
- `%.1f` rounds a float to the tenths place, `%.2f` rounds to the hundredths place, etc.
- `%t` formats a boolean value.
- `%v` can be used to format any value in its default representation.
- `%s` can be used to format a string.
- `%d` can be used to format an integer.

```go
package main

import "fmt"

func main() {
	fname := "Dalinar"
	lname := "Kholin"
	age := 45
	messageRate := 0.5
	isSubscribed := false
	message := "Sometimes a hypocrite is nothing more than a man in the process of changing."

	// Don't touch above this line

	userLog := fmt.Sprintf("Name: %s %s, Age: %d, Rate: %.1f, Is Subscribed: %t, Message: %s", fname, lname, age, messageRate, isSubscribed, message)

	// Don't touch below this line

	fmt.Println(userLog)
}

```

# Conditionals

`if` statements in Go do not use parentheses around the condition:

```go
if height > 4 {
    fmt.Println("You are tall enough!")
}
```

`else if` and `else` are supported as you might expect:

```go
if height > 6 {
    fmt.Println("You are super tall!")
} else if height > 4 {
    fmt.Println("You are tall enough!")
} else {
    fmt.Println("You are not tall enough!")
}
```

Unlike other languages, you _must_ put the opening brace on the same line as the condition and not on a new line.

## Assignment

Fix the bug on line `12`. If `messageLen` is less than or equal to the `maxMessageLen` the program should print "Message sent", else it should print "Message not sent".

## Tips

Here are some of the comparison operators in Go:

- `==` equal to
- `!=` not equal to
- `<` less than
- `>` greater than
- `<=` less than or equal to
- `>=` greater than or equal to


```go
package main

import "fmt"

func main() {
	messageLen := 10
	maxMessageLen := 20
	fmt.Println("Trying to send a message of length:", messageLen, "and a max length of:", maxMessageLen)

	// don't touch above this line

	if messageLen <= maxMessageLen {
		fmt.Println("Message sent")
	} else {
		fmt.Println("Message not sent")
	}
}

```

# The Initial Statement of an If Block

An `if` conditional can have an "initial" statement. The variable(s) created in the initial statement are _only_ defined within the scope of the `if`, `else if`, and `else` blocks.

```go
if INITIAL_STATEMENT; CONDITION {
}
```

## Why Would I Use This?

It has two valuable purposes:

1. It's a bit shorter
2. It limits the scope of the initialized variable(s) to the `if` statement

For example, instead of writing:

```go
length := getLength(email)
if length < 10 {
    fmt.Printf("Email must be at least 10 characters, is %d\n", length)
}
```

We can do:

```go
if length := getLength(email); length < 10 {
    fmt.Printf("Email must be at least 10 characters, is %d\n", length)
}
```

In the example above, `length` isn't available in the parent scope, which is nice because we don't need it there - we won't accidentally use it elsewhere in the function. It would still be available in any `else if` or `else` blocks attached to that `if`.

# Switch

Switch statements are a way to compare a value against multiple options. They are similar to if-else statements but are more concise and readable when the number of options is more than 2.

```go
func getCreator(os string) string {
    var creator string
    switch os {
    case "linux":
        creator = "Linus Torvalds"
    case "windows":
        creator = "Bill Gates"
    case "mac":
        creator = "A Steve"
    default:
        creator = "Unknown"
    }
    return creator
}
```

Notice that in Go, the `break` statement is not required at the end of a `case` to stop it from falling through to the next `case`. The `break` statement is implicit in Go.

If you _do_ want a `case` to fall through to the next `case`, you can use the `fallthrough` keyword.

```go
func getCreator(os string) string {
    var creator string
    switch os {
    case "linux":
        creator = "Linus Torvalds"
    case "windows":
        creator = "Bill Gates"

    // all three of these cases will set creator to "A Steve"
    case "macOS":
        fallthrough
    case "Mac OS X":
        fallthrough
    case "mac":
        creator = "A Steve"

    default:
        creator = "Unknown"
    }
    return creator
}
```

The `default` case does what you'd expect: it's the case that runs if none of the other cases match.

## Assignment

I know we haven't covered function syntax in depth yet, but _bear_ with me.

Fix the bug in the `billingCost` function. The "basic" plan is set correctly, but we need matches for the "pro" and "enterprise" plans too. If the `plan` is:

- "pro", the cost should be `20.0`
- "enterprise", the cost should be `50.0`

```go
package main

import "fmt"

func billingCost(plan string) float64 {
	switch plan {
	case "basic":
		return 10.0
	case "pro":
		return 20.0
	case "enterprise":
		return 50.0
	default:
		return 0.0
	}
}

// don't touch below this line

func main() {
	plan := "basic"
	fmt.Printf("The cost for a %s plan is $%.2f\n", plan, billingCost(plan))
	plan = "pro"
	fmt.Printf("The cost for a %s plan is $%.2f\n", plan, billingCost(plan))
	plan = "enterprise"
	fmt.Printf("The cost for a %s plan is $%.2f\n", plan, billingCost(plan))
	plan = "free"
	fmt.Printf("The cost for a %s plan is $%.2f\n", plan, billingCost(plan))
	plan = "unknown"
	fmt.Printf("The cost for a %s plan is $%.2f\n", plan, billingCost(plan))
}

```

# Calculate Balance

We need to calculate the total cost for a batch of messages, and update the user's balance if they have enough money.

## Assignment

Using the given variables, write conditional statements to calculate and update the variables.

1. [ ] Set `finalCost` to the `bulkMessageCost`.
2. [ ] If the user is a premium user, apply the `discountRate` to the `finalCost`.
    - For example, a `discountRate` of 0.10 means the discounted price per message would be 90% of the original price.
3. [ ] If the user has enough money in their `accountBalance`:
    - [ ] Deduct `finalCost` from their `accountBalance`.
    - [ ] Print the `purchaseSuccessMessage`
4. [ ] If not, just print the `insufficientFundMessage`.

```go
package main

import "fmt"

func main() {
	var insufficientFundMessage string = "Purchase failed. Insufficient funds."
	var purchaseSuccessMessage string = "Purchase successful."
	var accountBalance float64 = 100.0
	var bulkMessageCost float64 = 75.0
	var isPremiumUser bool = true
	var discountRate float64 = 0.10
	var finalCost float64

	// don't edit above this line

	finalCost = bulkMessageCost
	if isPremiumUser {
		finalCost -= finalCost * discountRate
	}

	if finalCost <= accountBalance {
		accountBalance -= finalCost
		fmt.Println(purchaseSuccessMessage)
	}else {
		fmt.Println(insufficientFundMessage)
	}


	// don't edit below this line

	fmt.Println("Account balance:", accountBalance)
}

```

# Functions

Functions in Go can take zero or more arguments.

To make code easier to read, the variable type comes _after_ the variable name.

For example, the following function:

```go
func sub(x int, y int) int {
    return x-y
}
```

Accepts two integer parameters and returns another integer.

Here, `func sub(x int, y int) int` is known as the "function signature".

Go doesn't care where in a file a function is defined: you can call a function that's declared later, even below `main`.

## Assignment

We often will need to manipulate strings in our messaging app. For example, adding some personalization by using a customer's name within a template. The `concat` function should take two strings and smash them together.

- `hello` + `world` = `helloworld`

Fix the [function signature](https://en.wikipedia.org/wiki/Type_signature) of `concat` to reflect its behavior.

```go
package main

import "fmt"

func concat(s1 string, s2 string) string {
	return s1 + s2
}

// don't touch below this line

func main() {
	test("Lane,", " happy birthday!")
	test("Zuck,", " hope that Metaverse thing works out")
	test("Go", " is fantastic")
}

func test(s1 string, s2 string) {
	fmt.Println(concat(s1, s2))
}

```
# Multiple Parameters

When multiple arguments are of the same type, and are next to each other in the function signature, the type only needs to be declared after the last argument.

Here are some examples:

```go
func addToDatabase(hp, damage int) {
  // ...
}
```

```go
func addToDatabase(hp, damage int, name string) {
  // ?
}
```

```go
func addToDatabase(hp, damage int, name string, level int) {
  // ?
}
```

# Unit Test Lessons

Up until now, all the coding lessons in this course have been testing you based on your code's _console output_ (what's printed). For example, a lesson might expect your code (in conjunction with the code we provide) to `print` something like:

```text
Price: 0.2
NumMessages: 18
```

If your code prints that _exact_ output, you pass. If it doesn't, you fail.

## A New Type of Lesson

Going forward, you'll also encounter a new type of lesson: [unit tests](https://en.wikipedia.org/wiki/Unit_testing). If you've taken a course with us before, you'll know what we are referring to. But in case you haven't, a unit test is just an automated program that tests a small "unit" of code. Usually just a function or two. The editor will have tabs: the "main.go" file containing your code, and the "main_test.go" file containing the unit tests.

These new unit-test-style lessons will test your code's _functionality_ rather than its output. Our tests will call functions in your code with different arguments, and expect specific `return` values. If your code returns the correct values, you pass. If it doesn't, you fail.

There are two reasons for this change:

1. It's more realistic. In the real world, you'll be writing unit tests and running them against your code to make sure it works as expected.
2. You can run and debug your code with `fmt.Println` statements, and leave those print statements in when you submit. Unlike the output-based lessons, you won't have to remove your `fmt.Println` statements to pass.

## Assignment

Complete the `getMonthlyPrice` function. It accepts a `tier` (string) as input and returns the monthly price for that tier in pennies. Here are the prices in dollars:

- "basic" - $100.00
- "premium" - $150.00
- "enterprise" - $500.00

Convert the prices from dollars to pennies. If the given tier doesn't match any of the above, return 0 pennies.

To avoid pesky [floating-point errors](https://en.wikipedia.org/wiki/Floating-point_arithmetic#Accuracy_problems), we often store prices in the currency's **base unit**. In this case, we are storing the prices in pennies, and **a dollar consists of 100 pennies.**

```go
package main
import "fmt"
func getMonthlyPrice(tier string) int {
	fmt.Println("String ---> ",tier)
	switch tier  {
	case "basic":
		return 100 * 100
	case "premium":
		return 150 * 100
	case "enterprise":
		return 500 * 100
	default:
		return 0		
	}
}

```

# Declaration Syntax

Developers often wonder why the declaration syntax in Go is different from the tradition established in the C family of languages.

## C-Style Syntax

The C language describes types with an expression including the name to be declared, and states what type that expression will have.

```c
int y;
```

The code above declares `y` as an `int`. In general, the type goes on the left and the expression on the right.

Interestingly, the creators of the Go language agreed that the C-style of declaring types in signatures gets confusing really fast - take a look at this nightmare.

```c
int (*fp)(int (*ff)(int x, int y), int b)
```
## Go-Style Syntax

Go's declarations are clear, you just read them left to right, just like you would in English.

```go
x int
p *int
a [3]int
```

It's nice for more complex signatures, it makes them easier to read.

Don't worry if you haven't seen functions stored in variables yet – we'll cover that later. For now, just notice how you can still read the type from left to right.

```go
f func(func(int,int) int, int) int
```

## Reference

The [following post on the Go blog](https://blog.golang.org/declaration-syntax) is a great resource for further reading on declaration syntax.

# Passing Variables by Value

Variables in Go are passed by value (except for a few data types we haven't covered yet). "Pass by value" means that when a variable is passed into a function, that function receives a _copy_ of the variable. The function is unable to mutate the caller's original data.

```go
func main() {
    x := 5
    increment(x)

    fmt.Println(x)
    // still prints 5,
    // because the increment function
    // received a copy of x
}

func increment(x int) {
    x++
}
```

## Assignment

- `monthlyBillIncrease`: Should return the increase in the bill from the previous to the current month. If the bill decreased, return a negative number.
- `getBillForMonth`: Should return the total cost for the number of messages sent.

Fix the bugs in the `monthlyBillIncrease` and `getBillForMonth` functions. Looks like whoever wrote the functions didn't know the `getBillForMonth` function's `bill` parameter would be passed by value. It's not actually updating the `lastMonthBill` and `thisMonthBill` variables as intended so `monthlyBillIncrease` isn't returning the right result.

1. [ ] Drop the `bill` parameter from `getBillForMonth`, so it only takes 2 parameters.
2. [ ] Instead, simply _return_ the total cost of the messages.
3. [ ] `monthlyBillIncrease` should use the result of calling `getBillForMonth` to calculate the increase between months.
```go
package main

func monthlyBillIncrease(costPerSend, numLastMonth, numThisMonth int) int {
	var lastMonthBill int
	var thisMonthBill int
	lastMonthBill = getBillForMonth( costPerSend, numLastMonth)
	thisMonthBill = getBillForMonth( costPerSend, numThisMonth)
	return thisMonthBill - lastMonthBill
}

func getBillForMonth(costPerSend, messagesSent int) int {
	return costPerSend * messagesSent
}

```

# Ignoring Return Values

A function can return a value that the caller doesn't care about. We can explicitly ignore variables by using an underscore, or more precisely, the [blank identifier `_`](https://go.dev/doc/effective_go#blank).

For example:

```go
func getPoint() (x int, y int) {
    return 3, 4
}

// ignore y value
x, _ := getPoint()
```

Even though `getPoint()` returns two values, we can capture the first one and ignore the second. In Go, the blank identifier isn't just a convention; it's a real language feature that completely discards the value.

## Why Might You Ignore a Return Value?

Maybe a function called `getCircle` returns the center point and the radius, but you only need the radius for your calculation. In that case, you can ignore the center point variable.

The Go compiler will **return an error** if you have any unused variable declarations in your code, so you _need_ to ignore anything you don't intend to use.

## Assignment

1. [ ] Run the code as-is. You should get a compiler error.
2. [ ] Fix `getProductMessage` to ignore the unused return value.

```go
package main

func getProductMessage(tier string) string {
	quantityMsg, priceMsg, _ := getProductInfo(tier)
	return "You get " + quantityMsg + " for " + priceMsg + "."
}

// don't touch below this line

func getProductInfo(tier string) (string, string, string) {
	if tier == "basic" {
		return "1,000 texts per month", "$30 per month", "most popular"
	} else if tier == "premium" {
		return "50,000 texts per month", "$60 per month", "best value"
	} else if tier == "enterprise" {
		return "unlimited texts per month", "$100 per month", "customizable"
	} else {
		return "", "", ""
	}
}

```

# Named Return Values

Return values may be given names, and if they are, then they are treated the same as if they were new variables defined at the top of the function.

Named return values are best thought of as a way to document the purpose of the returned values.

According to the [tour of go](https://tour.golang.org/):

> A return statement without arguments returns the named return values. This is known as a "naked" return. Naked return statements should be used only in short functions. They can harm readability in longer functions.

Named return values are what enable naked returns. Use naked returns only in short functions where the purpose of the returned values is obvious.

```go
func getCoords() (x, y int) {
	// x and y are initialized with zero values

	return // automatically returns x and y
}

```

Is the same as:

```go
func getCoords() (int, int) {
	var x int
	var y int
	return x, y
}
```

In the first example, `x` and `y` are the return values. At the end of the function, we could simply write `return` to return the values of those two variables, rather than writing `return x,y`.

## Assignment

One of our clients likes us to send text messages reminding users of life events coming up.

Fix the bug by adding named return values to the _function signature_ – the bare `return` at the end is already a naked return that will return them. The variables need to be automatically initialized. Order them as they appear in the code. _Do not alter the body of the function_.

```go
package main

func yearsUntilEvents(age int) (yearsUntilAdult int, yearsUntilDrinking int, yearsUntilCarRental int) {
	// don't touch below this line

	yearsUntilAdult = 18 - age
	if yearsUntilAdult < 0 {
		yearsUntilAdult = 0
	}
	yearsUntilDrinking = 21 - age
	if yearsUntilDrinking < 0 {
		yearsUntilDrinking = 0
	}
	yearsUntilCarRental = 25 - age
	if yearsUntilCarRental < 0 {
		yearsUntilCarRental = 0
	}
	return
}

```
# The Benefits of Named Returns

## Good for Documentation (Understanding)

Named return parameters are great for documenting a function. We know what the function is returning directly from its signature, no need for a comment.

Named return parameters are particularly important in longer functions with many return values.

```go
func calculator(a, b int) (mul, div int, err error) {
    if b == 0 {
      return 0, 0, errors.New("can't divide by zero")
    }
    mul = a * b
    div = a / b
    return mul, div, nil
}
```

Which is easier to understand than:

```go
func calculator(a, b int) (int, int, error) {
    if b == 0 {
      return 0, 0, errors.New("can't divide by zero")
    }
    mul := a * b
    div := a / b
    return mul, div, nil
}
```

We know _the meaning_ of each return value just by looking at the function signature: `func calculator(a, b int) (mul, div int, err error)`

`nil` is the zero value of an error. More on this later.

## Less Code (Sometimes)

If there are multiple return statements in a function, you don't need to write all the return values each time, though you _probably_ should.

When you choose to omit return values, it's called a _naked_ return. Naked returns should only be used in short and simple functions.

# Explicit Returns

Even though a function has named return values, we can still explicitly return values if we want to.

```go
func getCoords() (x, y int) {
	return x, y // this is explicit
}
```

Using this explicit pattern we can even overwrite the return values:

```go
func getCoords() (x, y int) {
    return 5, 6 // this is explicit, x and y are NOT returned
}
```

Otherwise, if we want to return the values defined in the function signature we can just use a naked `return` (blank return):

```go
func getCoords() (x, y int) {
    return // implicitly returns x and y
}
```

## Assignment

Fix the bug in the code so that it returns the named values _explicitly_.

```go
package main

func yearsUntilEvents(age int) (yearsUntilAdult, yearsUntilDrinking, yearsUntilCarRental int) {
	yearsUntilAdult = 18 - age
	if yearsUntilAdult < 0 {
		yearsUntilAdult = 0
	}
	yearsUntilDrinking = 21 - age
	if yearsUntilDrinking < 0 {
		yearsUntilDrinking = 0
	}
	yearsUntilCarRental = 25 - age
	if yearsUntilCarRental < 0 {
		yearsUntilCarRental = 0
	}
	return yearsUntilAdult, yearsUntilDrinking, yearsUntilCarRental
}

```

# Early Returns

Go supports the ability to return early from a function. This is a powerful feature that can clean up code, especially when used as guard clauses.

Guard Clauses leverage the ability to `return` early from a function (or `continue` through a loop) to make nested conditionals one-dimensional. Instead of using if/else chains, we just return early from the function at the end of each conditional block.

```go
func divide(dividend, divisor int) (int, error) {
	if divisor == 0 {
		return 0, errors.New("can't divide by zero")
	}
	return dividend/divisor, nil
}
```

Error handling in Go naturally encourages developers to make use of guard clauses and early returns. JavaScript can use the same pattern, but many real-world JS codebases still lean heavily on nested conditionals. When I started writing more JavaScript, I noticed how much more deeply nested many of those functions were compared to their Go equivalents.

Let's take a look at an exaggerated example of nested conditional logic:

```go
func getInsuranceAmount(status insuranceStatus) int {
  amount := 0
  if !status.hasInsurance(){
    amount = 1
  } else {
    if status.isTotaled(){
      amount = 10000
    } else {
      if status.isDented(){
        amount = 160
        if status.isBigDent(){
          amount = 270
        }
      } else {
        amount = 0
      }
    }
  }
  return amount
}
```

This could be written with guard clauses instead:

```go
func getInsuranceAmount(status insuranceStatus) int {
  if !status.hasInsurance(){
    return 1
  }
  if status.isTotaled(){
    return 10000
  }
  if !status.isDented(){
    return 0
  }
  if status.isBigDent(){
    return 270
  }
  return 160
}
```

The example above is _much_ easier to read and understand. When writing code, it's important to try to reduce the cognitive load on the reader by reducing the number of entities they need to think about at any given time.

In the first example, if the developer is trying to figure out when `270` is returned, they need to think about each branch in the logic tree and try to remember which cases matter and which cases don't. With the one-dimensional structure offered by guard clauses, it's as simple as stepping through each case in order.

# Functions As Values

Go supports [first-class](https://developer.mozilla.org/en-US/docs/Glossary/First-class_Function) and higher-order functions, which are just fancy ways of saying "functions as values". Functions are just another type -- like `int`s and `string`s and `bool`s.

Let's assume we have two simple functions:

```go
func add(x, y int) int {
	return x + y
}

func mul(x, y int) int {
	return x * y
}
```

We can create a new `aggregate` function that accepts a function as its 4th argument:

```go
func aggregate(a, b, c int, arithmetic func(int, int) int) int {
  firstResult := arithmetic(a, b)
  secondResult := arithmetic(firstResult, c)
  return secondResult
}
```

It calls the given `arithmetic` function (which could be `add` or `mul`, or any other function that accepts two `int`s and returns an `int`) and applies it to three inputs instead of two. It can be used like this:

```go
func main() {
	sum := aggregate(2, 3, 4, add)
	// sum is 9
	product := aggregate(2, 3, 4, mul)
	// product is 24
}
```

## Assignment

Complete the `reformat` function. It takes a `message` string and a `formatter` function as input:

1. [ ] Apply the given `formatter` _three times_ to the `message`
2. [ ] Add a prefix of `TEXTIO:` to the result
3. [ ] Return the final string

For example, if the `message` is "General Kenobi" and the given `formatter` adds a period to the end of the string, the final result should be

```text
TEXTIO: General Kenobi...
```

```go
package main

func reformat(message string, formatter func(string) string) string {
	for i:= 0;  i < 3; i++ {
		message = formatter(message)
	}
	return "TEXTIO: "+message
}

```

# Anonymous Functions

Anonymous functions are true to form in that they have _no name_. They're useful when defining a function that will only be used once or to create a quick [closure](https://en.wikipedia.org/wiki/Closure_\(computer_programming\)).

Let's say we have a function `conversions` that accepts another function, `converter` as input:

```go
func conversions(converter func(int) int, x, y, z int) (int, int, int) {
	convertedX := converter(x)
	convertedY := converter(y)
	convertedZ := converter(z)
	return convertedX, convertedY, convertedZ
}
```

We _could_ define a function normally and then pass it in by name... but it's usually easier to just define it anonymously:

```go
func double(a int) int {
    return a + a
}

func main() {
    // using a named function
	newX, newY, newZ := conversions(double, 1, 2, 3)
	// newX is 2, newY is 4, newZ is 6

    // using an anonymous function
	newX, newY, newZ = conversions(func(a int) int {
	    return a + a
	}, 1, 2, 3)
	// newX is 2, newY is 4, newZ is 6
}
```

## Assignment

Complete the `printReports` function. It takes as input a sequence of messages, `intro`, `body`, `outro`. It should call `printCostReport` once for each message by making three separate calls (you don't need to use loops or arrays for this).

For each call of `printCostReport`, give it an anonymous function that returns the `cost` of a message as an integer. Here are the costs:

- Intro: 2x the message length
- Body: 3x the message length
- Outro: 4x the message length

Use the built-in [`len()` function](https://pkg.go.dev/builtin#len) to get the length of a string:

```go
helloLen := len("hello")
// helloLen = 5
```

```go
package main

import "fmt"

func printReports(intro, body, outro string) {
	printCostReport(func(s string) int {
		return 2 * len(s)
	}, intro)
	
	printCostReport(func(s string) int {
		return 3 * len(s)
	}, body)
	printCostReport(func(s string) int {
		return 4 * len(s)
	}, outro)
}

// don't touch below this line

func main() {
	printReports(
		"Welcome to the Hotel California",
		"Such a lovely place",
		"Plenty of room at the Hotel California",
	)
}

func printCostReport(costCalculator func(string) int, message string) {
	cost := costCalculator(message)
	fmt.Printf(`Message: "%s" Cost: %v cents`, message, cost)
	fmt.Println()
}

```

# Defer

The `defer` keyword is a fairly unique feature of Go. It allows a function to be executed automatically _just before_ its enclosing function returns. The deferred call's arguments are evaluated immediately, but the function call is not executed until the surrounding function returns.

Deferred functions are typically used to clean up resources that are no longer being used. Often to close database connections, file handlers and the like.

For example:

```go
func GetUsername(dstName, srcName string) (username string, err error) {
	// Open a connection to a database
	conn, _ := db.Open(srcName)

	// Close the connection *anywhere* the GetUsername function returns
	defer conn.Close()

	username, err = db.FetchUser()
	if err != nil {
		// The defer statement is auto-executed if we return here
		return "", err
	}

	// The defer statement is auto-executed if we return here
	return username, nil
}
```

In the above example, the `conn.Close()` function is not called here:

```go
defer conn.Close()
```

It's called:

```go
// here
return "", err
// or here
return username, nil
```

Depending on whether the `FetchUser` function errored. (We'll cover errors later).

Defer is a great way to **make sure** that something happens before a function exits, even if there are multiple return statements, a common occurrence in Go.

## Multiple Defers

The location of a `defer` statement inside a function matters. The deferred call is registered at the point where `defer` is executed, and it will run when the function returns. If you have multiple `defer` statements in a single function, they are executed in **last-in, first-out** order (the last deferred call runs first).

For example, you'd want to close a file before trying to remove it:

```go
func CreateTempFile() {
	f, _ := os.Create("temp-42.txt")
	defer os.Remove(f.Name()) // executed second
	defer f.Close()           // executed first

	fmt.Fprintln(f, "How many roads must a man walk down?")
}
```

## Assignment

Complete the `bootup` function.

1. Be sure to print the following string _just before_ the `bootup` function returns:
    
    ```text
    TEXTIO BOOTUP DONE
    ```
    
1. Use `defer` so that you only have to write this message once instead of before each `return` statement. The message should be printed on its own newline.
```go
package main

import (
	"fmt"
)

func bootup() {
	defer fmt.Println("TEXTIO BOOTUP DONE")
	ok := connectToDB()
	if !ok {
		return
	}
	ok = connectToPaymentProvider()
	if !ok {
		return
	}
	fmt.Println("All systems ready!")
}

// don't touch below this line

var shouldConnectToDB = true

func connectToDB() bool {
	fmt.Println("Connecting to database...")
	if shouldConnectToDB {
		fmt.Println("Connected!")
		return true
	}
	fmt.Println("Connection failed")
	return false
}

var shouldConnectToPaymentProvider = true

func connectToPaymentProvider() bool {
	fmt.Println("Connecting to payment provider...")
	if shouldConnectToPaymentProvider {
		fmt.Println("Connected!")
		return true
	}
	fmt.Println("Connection failed")
	return false
}

func test(dbSuccess, paymentSuccess bool) {
	shouldConnectToDB = dbSuccess
	shouldConnectToPaymentProvider = paymentSuccess
	bootup()
	fmt.Println("====================================")
}

func main() {
	test(true, true)
	test(false, true)
	test(true, false)
	test(false, false)
}

```

# Block Scope

Unlike Python, Go is _not_ function-scoped, it's [block-scoped](https://go.dev/ref/spec#Declarations_and_scope). Variables declared inside a block are only accessible within that block (and its nested blocks). There's also the package scope. We'll talk about packages later, but for now, you can think of it as the outermost, nearly global scope.

```go
package main

// scoped to the entire "main" package (basically global)
var age = 19

func sendEmail() {
    // scoped to the "sendEmail" function
    name := "Jon Snow"

    for i := 0; i < 5; i++ {
        // scoped to the "for" body
        email := "snow@winterfell.net"
    }
}
```

Blocks are defined by curly braces `{}`. New blocks are created for:

- Functions
- Loops
- If statements
- Switch statements
- Select statements
- Explicit blocks

It's a bit unusual, but occasionally you'll see a plain old explicit block. It exists for no other reason than to create a new scope.

```go
package main

import "fmt"

func main() {
    {
        age := 19
        // this is okay
        fmt.Println(age)
    }

    // this is not okay
    // the age variable is out of scope
    fmt.Println(age)
}
```

## Assignment

1. [ ] Run the code without changing anything: you should see a compilation error.
2. [ ] Fix the scoping issue in the function so that it runs as you'd expect.

```go
package main

func splitEmail(email string) (string, string) {
	username, domain := "", ""
	for i, r := range email {
		if r == '@' {
			username = email[:i]
			domain = email[i+1:]
			break
		}
	}
	return username, domain
}

```

# Processing Orders

Management thinks our branding is so creative that our SaaS customers will pay for Textio merch.

## Assignment

Complete the `placeOrder` function.

It returns a `bool` indicating whether the order was successful (`true` is a success) and a `float64` representing the user's balance after the order. The `placeOrder` function should always return the account balance regardless of whether it was adjusted.

The `amountInStock` and `calcPrice` functions can be used to look up the current stock and price of an item.

- If the quantity is greater than the amount in stock, the order should be rejected.
- If the user doesn't have enough money in their account, the order should be rejected.
- Otherwise, the order should be accepted and you should return the new balance.

```go
package main

func placeOrder(productID string, quantity int, accountBalance float64) (bool, float64) {
	if quantity > amountInStock(productID) {
		return false, accountBalance
	}
	price := calcPrice(productID, quantity)
	if price > accountBalance {
		return false, accountBalance
	}
	accountBalance -= price
	return true, accountBalance
}

// Don't touch below this line

func calcPrice(productID string, quantity int) float64 {
	return priceList(productID) * float64(quantity)
}

func priceList(productID string) float64 {
	if productID == "1" {
		return 1.50
	} else if productID == "2" {
		return 2.25
	} else if productID == "3" {
		return 3.00
	} else if productID == "4" {
		return 1.00
	} else if productID == "5" {
		return 2.50
	} else if productID == "6" {
		return 8.99
	} else if productID == "7" {
		return 22.50
	} else if productID == "8" {
		return 50.00
	} else if productID == "9" {
		return 999.99
	} else {
		return 0.00
	}
}

func amountInStock(productID string) int {
	if productID == "1" {
		return 11
	} else if productID == "2" {
		return 25
	} else if productID == "3" {
		return 4
	} else if productID == "4" {
		return 6
	} else if productID == "5" {
		return 50
	} else if productID == "6" {
		return 2
	} else if productID == "7" {
		return 0
	} else if productID == "8" {
		return 99
	} else if productID == "9" {
		return 1
	} else {
		return 0
	}
}

```

# Closures

A [closure](https://en.wikipedia.org/wiki/Closure_\(computer_programming\)) is a function that references variables from outside its own function body. The function may access and _assign_ to the referenced variables.

In this example, the `concatter()` function returns a function that has reference to an _enclosed_ `doc` value. Each successive call to `harryPotterAggregator` mutates that same `doc` variable.

```go
func concatter() func(string) string {
	doc := ""
	return func(word string) string {
		doc += word + " "
		return doc
	}
}

func main() {
	harryPotterAggregator := concatter()
	harryPotterAggregator("Mr.")
	harryPotterAggregator("and")
	harryPotterAggregator("Mrs.")
	harryPotterAggregator("Dursley")
	harryPotterAggregator("of")
	harryPotterAggregator("number")
	harryPotterAggregator("four,")
	harryPotterAggregator("Privet")

	fmt.Println(harryPotterAggregator("Drive"))
	// Mr. and Mrs. Dursley of number four, Privet Drive
}
```

## Assignment

Keeping track of how many texts we send is mission-critical at Textio. Complete the `adder()` [enclosing function](https://en.wikipedia.org/wiki/Nested_function).

1. [ ] Create an enclosed `sum` value inside the `adder()` function.
2. [ ] Return a function from the `adder()` function that adds its input (an `int`) to the `sum` and returns the new value of `sum`. (In other words, it keeps a running total of the `sum` variable within a closure.)
```go
package main

func adder() func(int) int {
	sum := 0
	return func(val int) int {
		sum += val
		return sum
	}
}

```
# Currying

Function [currying](https://en.wikipedia.org/wiki/Currying) is a concept from functional programming and involves [partial application](https://en.wikipedia.org/wiki/Partial_application) of functions. It allows a function with multiple arguments to be transformed into a sequence of functions, each taking a single argument.

Let's simulate this behavior. For example:

```go
func main() {
  squareFunc := selfMath(multiply)
  doubleFunc := selfMath(add)

  fmt.Println(squareFunc(5))
  // prints 25

  fmt.Println(doubleFunc(5))
  // prints 10
}

func multiply(x, y int) int {
  return x * y
}

func add(x, y int) int {
  return x + y
}

func selfMath(mathFunc func(int, int) int) func (int) int {
  return func(x int) int {
    return mathFunc(x, x)
  }
}
```

In the example above:

- `selfMath(multiply)` returns a new function and stores it in `squareFunc`; it doesn't run `multiply` yet.
- `squareFunc(5)` runs the returned function, which calls `multiply(5, 5)`.

## Assignment

The Textio API needs a very robust error-logging system so we can see when things are going awry in the back-end system. We need a function that can create a custom "logger" (a function that prints to the console) given a specific formatter.

These errors are test data, not runtime failures.

Complete the `getLogger` function. It should take as input a `formatter` function and `return` _a new function_. The new logger function takes as input two strings and passes them to the `formatter`, then prints the result. Keep the order of the strings.

```go
package main

import (
	"errors"
	"fmt"
)

// getLogger takes a function that formats two strings into
// a single string and returns a function that formats two strings but prints
// the result instead of returning it
func getLogger(formatter func(string, string) string) func(string, string) {
	return func(str1 , str2 string){
		res := formatter(str1, str2)
		fmt.Println(res)
	}
}

// don't touch below this line

func test(first string, errors []error, formatter func(string, string) string) {
	defer fmt.Println("====================================")
	logger := getLogger(formatter)
	fmt.Println("Logs:")
	for _, err := range errors {
		logger(first, err.Error())
	}
}

func colonDelimit(first, second string) string {
	return first + ": " + second
}

func commaDelimit(first, second string) string {
	return first + ", " + second
}

func main() {
	dbErrors := []error{
		errors.New("out of memory"),
		errors.New("cpu is pegged"),
		errors.New("networking issue"),
		errors.New("invalid syntax"),
	}
	test("Error on database server", dbErrors, colonDelimit)

	mailErrors := []error{
		errors.New("email too large"),
		errors.New("non alphanumeric symbols found"),
	}
	test("Error on mail server", mailErrors, commaDelimit)
}

```
# Structs in Go

We use [structs](https://go.dev/ref/spec#Struct_types) in Go to represent structured data. It's often convenient to group different types of variables together. For example, if we want to represent a car we could do the following:

```go
type car struct {
	brand      string
	model      string
	doors      int
	mileage    int
}
```

This creates a new struct type called `car`. All cars have a `brand`, `model`, `doors` and `mileage`.

To create a `car`, use a struct literal:

```go
myCar := car{
	brand:   "Toyota",
	model:   "Camry",
	doors:   4,
	mileage: 5000,
}
```

Structs in Go are often used to represent data that you might use a dictionary or object for in other languages.

## Assignment

Complete the definition of the `messageToSend` struct. It needs two fields:

- `phoneNumber` - an integer
- `message` - a string.

```go
package main

type messageToSend struct {
	phoneNumber int
	message string
}

```

# Nested Structs in Go

Structs can be nested to represent more complex entities:

```go
type car struct {
  brand string
  model string
  doors int
  mileage int
  frontWheel wheel
  backWheel wheel
}

type wheel struct {
  radius int
  material string
}
```

The fields of a struct can be accessed using the dot `.` operator.

```go
myCar := car{}
myCar.frontWheel.radius = 5
```

## Assignment

Textio has a bug, we've been sending texts that are missing critical bits of information! Before we send text messages in Textio, we must check to make sure the required fields have non-[zero values](https://go.dev/tour/basics/12).

Notice that the `user` struct is a nested struct within the `messageToSend` struct. Both `sender` and `recipient` are `user` struct types.

Complete the `canSendMessage` function. It should return `true` only if the `sender` and `recipient` fields each contain a `name` and a `number`. If any of the default zero values are present, return `false` instead.

## Tip

Zero values:

- int: `0`
- bool: `false`
- string: `""`

```go
package main

type messageToSend struct {
	message   string
	sender    user
	recipient user
}

type user struct {
	name   string
	number int
}

func canSendMessage(mToSend messageToSend) bool {
	if mToSend.sender.name != "" && mToSend.sender.number != 0 && mToSend.recipient.name != "" && mToSend.recipient.number != 0 {
		return true
	}
	return false
}

```

# Anonymous Structs in Go

An anonymous struct is just like a normal struct, but it is defined without a name and therefore cannot be referenced elsewhere in the code.

To create an anonymous struct, just instantiate the instance immediately using a second pair of brackets after declaring the type:

```go
myCar := struct {
  brand string
  model string
} {
  brand: "Toyota",
  model: "Camry",
}
```

You can even nest anonymous structs as fields within other structs:

```go
type car struct {
  brand string
  model string
  doors int
  mileage int
  // wheel is a field containing an anonymous struct
  wheel struct {
    radius int
    material string
  }
}

var myCar = car{
  brand:   "Rezvani",
  model:   "Vengeance",
  doors:   4,
  mileage: 35000,
  wheel: struct {
    radius   int
    material string
  }{
    radius:   35,
    material: "alloy",
  },
}
```

## When Should You Use an Anonymous Struct?

In general, _prefer named structs_. Named structs make it easier to read and understand your code, and they have the nice side-effect of being reusable. I sometimes use anonymous structs when I _know_ I won't ever need to use a struct again. For example, sometimes I'll use one to create the shape of some JSON data in HTTP handlers.

If a struct is only meant to be used once, then it makes sense to declare it in such a way that developers down the road won't be tempted to accidentally use it again.

# Embedded Structs

Go is not an [object-oriented](https://en.wikipedia.org/wiki/Object-oriented_programming) language. However, embedded structs provide a kind of _data-only_ inheritance that can be useful at times. Keep in mind, Go doesn't support classes or inheritance in the _complete_ sense, but embedded structs are a way to elevate and **share fields between struct definitions.**

```go
type car struct {
  brand string
  model string
}

type truck struct {
  // "car" is embedded, so the definition of a
  // "truck" now also additionally contains all
  // of the fields of the car struct
  car
  bedSize int
}
```

## Embedded vs. Nested

- Unlike nested structs, an embedded struct's fields are accessed at the top level like normal fields.
- Like nested structs, you assign the promoted fields with the embedded struct in a [composite literal](https://golang.org/ref/spec#Composite_literals).

```go
lanesTruck := truck{
  bedSize: 10,
  car: car{
    brand: "Toyota",
    model: "Tundra",
  },
}

fmt.Println(lanesTruck.brand) // Toyota
fmt.Println(lanesTruck.model) // Tundra
```

In the example above, `car` is an embedded struct within `truck`. You can see that both `brand` and `model` are accessible from the top-level, while the nested equivalent to this object would require you to access these fields via a nested `car` struct: `lanesTruck.car.brand` or `lanesTruck.car.model`.

## Assignment

At Textio, a "user" struct represents an account holder, and a "sender" is just a "user" with some additional "sender" specific data. A "sender" is a user that has a `rateLimit` field that tells us how many messages they are allowed to send.

Fix the bug by embedding the proper struct in the other

```go
package main

type sender struct {
	user
	rateLimit int
}

type user struct {
	name   string
	number int
}
```

# Struct Methods in Go

While Go is **not** object-oriented, it does support methods that can be defined on structs. Methods are just functions that have a receiver. A receiver is a special parameter that syntactically goes _before_ the name of the function.

```go
type rect struct {
  width int
  height int
}

// area has a receiver of (r rect)
// rect is the struct
// r is the placeholder
func (r rect) area() int {
  return r.width * r.height
}

var r = rect{
  width: 5,
  height: 10,
}

fmt.Println(r.area())
// prints 50
```

A receiver is just a special kind of function parameter. In the example above, the `r` in `(r rect)` could just as easily have been `rec` or even `x`, `y` or `z`. By convention, Go code will often use the first letter of the struct's name.

Receivers are important because they will, as you'll learn in the exercises to come, allow us to define interfaces that our structs (and other types) can implement.

## Assignment

Let's clean up Textio's authentication logic. We store our user's authentication data inside an `authenticationInfo` struct. We need a method that can take that data and return a basic authorization string.

The format of the string should be:

```text
Authorization: Basic USERNAME:PASSWORD
```

Create a method on the `authenticationInfo` struct called `getBasicAuth` that returns the formatted string.

```go
package main
import "fmt"
type authenticationInfo struct {
	username string
	password string
}

// create the method below
func (a authenticationInfo) getBasicAuth() string {
	auth_str := fmt.Sprintf("Authorization: Basic %s:%s", a.username, a.password)
	return  auth_str
}
```


# Memory Layout

In Go, structs sit in memory in a contiguous block, with fields placed one after another as defined in the struct. For example this struct:

```go
type stats struct {
	Reach    uint16
	NumPosts uint8
	NumLikes uint8
}
```

Looks like this in memory:

![struct layout](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/qFsTyxI-980x550.png)

## Field ordering... Matters?

the order of fields in a struct can have a big impact on memory usage. This is the same struct as above, but _poorly_ designed:

```go
type stats struct {
	NumPosts uint8
	Reach    uint16
	NumLikes uint8
}
```

It looks like this in memory:

![struct layout](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/qcX53j6-1180x550.png)

Notice that Go has "aligned" the fields, meaning that it has added some padding (wasted space) to make up for the size difference between the `uint16` and `uint8` types. It's done for execution speed, but it can lead to increased memory usage.

## Should I Panic?

To be honest, you _should not stress_ about [memory layout](https://go101.org/article/memory-layout.html). However, if you have a specific reason to be concerned about memory usage, aligning the fields by size (largest to smallest) can help. You can also use the [reflect package](https://pkg.go.dev/reflect) to debug the memory layout of a struct:

```go
typ := reflect.TypeOf(stats{})
fmt.Printf("Struct is %d bytes\n", typ.Size())
```

## Real Story

I once had a server in production that held _a lot_ of structs in memory. Like _hundreds of thousands_ in a list. When I re-ordered the fields in the struct, the memory usage of the program dropped by over 2 gigabytes! It was a _huge_ performance win.

## Assignment

Our over-engineering boss is at it again. He's heard about memory layout and wants to squeeze every last byte out of our structs.

Run the tests to see the current size of the structs, then update the struct definitions to minimize memory usage.

```go
package main

type contact struct {
	sendingLimit int32
	age          int32
	userID       string
}

type perms struct {
	permissionLevel int
	canSend         bool
	canReceive      bool
	canManage       bool
}

```

# Empty Struct

[Empty structs](https://dave.cheney.net/2014/03/25/the-empty-struct) are used in Go as a [unary](https://en.wikipedia.org/wiki/Unary_operation) value.

```go

// anonymous empty struct type
empty := struct{}{}

// named empty struct type
type emptyStruct struct{}
empty := emptyStruct{}
```

Later in this course, you'll see how and when they're used: it's surprisingly often! Mostly with maps and channels.

# Empty Struct Memory

Empty structs are Go's smallest possible type: they take up **zero bytes of memory**.

Compare their size with the other types below:

![memory usage](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/hXAvfvS-1280x448.png)

# Update Users

We need a way to differentiate between standard and premium users. When a new user is created, they need a membership type, and that type will determine the message character limit.

## Assignment

1. [ ] Create a new struct called `Membership`, it should have:
    - [ ] A `Type` string field
    - [ ] A `MessageCharLimit` integer field
2. [ ] Update the `User` struct to [embed](https://gobyexample.com/struct-embedding) a `Membership`.
3. [ ] Complete the `newUser` function. It should return a new `User` with all the fields set as you would expect based on the inputs. If the user is a `"premium"` member, the `MessageCharLimit` should be `1000`, otherwise, it should only be `100`.

```go
package main

type Membership struct {
	Type string
	MessageCharLimit int
}
type User struct {
	Membership
	Name string
}

func newUser(name string, membershipType string) User {
	if membershipType == "premium" {
		return User{
			Name: name,
			Membership: Membership{
				Type: membershipType,
				MessageCharLimit: 1000,
			},
		}
	} 
	return User{
		Name: name,
		Membership: Membership{
			Type: membershipType,
			MessageCharLimit: 100,
		},
	}
}

```
# Send Message

## Assignment

Create a `SendMessage` method for the `User` struct.

It should take a `message` string and `messageLength` int as inputs.

If the `messageLength` is within the user's `MessageCharLimit`, return the original `message` and `true` (indicating the message can be sent), otherwise, return an empty string and `false`.

```go
package main

func (u User) SendMessage(message string, messageLength int) (string, bool) {
	if messageLength <= u.MessageCharLimit {
		return message, true
	}
	return "", false
}

// don't touch below this line

type User struct {
	Name string
	Membership
}

type Membership struct {
	Type             string
	MessageCharLimit int
}

func newUser(name string, membershipType string) User {
	membership := Membership{Type: membershipType}
	if membershipType == "premium" {
		membership.MessageCharLimit = 1000
	} else {
		membership.Type = "standard"
		membership.MessageCharLimit = 100
	}
	return User{Name: name, Membership: membership}
}

```

# Interfaces in Go

[Interfaces](https://go.dev/tour/methods/9) allow you to focus on what a type does rather than how it's built. They can help you write more flexible and reusable code by defining behaviors (like methods) that different types can share. This makes it easy to swap out or update parts of your code without changing everything else.

Interfaces are just collections of method signatures. A type "implements" an interface if it has methods that match the interface's method signatures.

In the following example, a "shape" must be able to return its area and perimeter. Both `rect` and `circle` fulfill the interface.

```go
type shape interface {
  area() float64
  perimeter() float64
}

type rect struct {
    width, height float64
}
func (r rect) area() float64 {
    return r.width * r.height
}
func (r rect) perimeter() float64 {
    return 2*r.width + 2*r.height
}

type circle struct {
    radius float64
}
func (c circle) area() float64 {
    return math.Pi * c.radius * c.radius
}
func (c circle) perimeter() float64 {
    return 2 * math.Pi * c.radius
}
```

When a type implements an interface, it can then be used as that interface type.

```go
func printShapeData(s shape) {
	fmt.Printf("Area: %v - Perimeter: %v\n", s.area(), s.perimeter())
}
```

Because we say the input is of type `shape`, we know that any argument must implement the `.area()` and `.perimeter()` methods.

As an example, because [the empty interface](https://go.dev/tour/methods/14) doesn't require a type to have any methods at all, every type automatically implements the empty interface, written as:

```go
interface{}
```

## Assignment

The `birthdayMessage` and `sendingReport` structs already have implementations of the `getMessage` method. The `getMessage` method returns a string, and any type that implements the method can be considered a `message` (meaning it implements the `message` interface).

1. [ ] Add the `getMessage()` method signature as a requirement on the message interface.
2. [ ] Complete the `sendMessage` function. It should return:
    1. [ ] The content of the message.
    2. [ ] The cost of the message, which is the length of the message multiplied by 3.

_Notice that your code doesn't care at all about whether a specific message is a `birthdayMessage` or a `sendingReport`!_

## Tip

The length of a string can be obtained using the `len` function, which [returns the number of bytes](https://pkg.go.dev/builtin#len).

```go
s := "Hello, World!"
fmt.Println(len(s))
// 13
```

```go
package main

import (
	"fmt"
	"time"
)

func sendMessage(msg message) (string, int) {
	message := msg.getMessage()
	cost := len(message) * 3
	return message, cost
}

type message interface {
	getMessage() string
}

// don't edit below this line

type birthdayMessage struct {
	birthdayTime  time.Time
	recipientName string
}

func (bm birthdayMessage) getMessage() string {
	return fmt.Sprintf("Hi %s, it is your birthday on %s", bm.recipientName, bm.birthdayTime.Format(time.RFC3339))
}

type sendingReport struct {
	reportName    string
	numberOfSends int
}

func (sr sendingReport) getMessage() string {
	return fmt.Sprintf(`Your "%s" report is ready. You've sent %v messages.`, sr.reportName, sr.numberOfSends)
}

```

# Interface Implementation

Interfaces are implemented _implicitly_.

A type never declares that it implements a given interface. If an interface exists and a type has the proper methods defined, then the type automatically fulfills that interface.

A quick way of checking whether a struct implements an interface is to declare a function that takes an interface as an argument. If the function can take the struct as an argument, then the struct implements the interface.

## Assignment

At Textio we have full-time employees and contract employees. We have been tasked with making a more general `employee` interface so that dealing with different employee types is simpler.

1. [ ] Run the code. You should see an error indicating the `contractor` type does not fulfill the `employee` interface.
2. [ ] Implement the missing `getSalary` method for the `contractor` type so that it fulfills the `employee` interface.
    - A contractor's salary is their hourly pay multiplied by how many hours they work per year.

```go
package main

type employee interface {
	getName() string
	getSalary() int
}

type contractor struct {
	name         string
	hourlyPay    int
	hoursPerYear int
}

func (c contractor) getName() string {
	return c.name
}

func (c contractor) getSalary() int {
	return c.hourlyPay * c.hoursPerYear
}

type fullTime struct {
	name   string
	salary int
}

func (ft fullTime) getSalary() int {
	return ft.salary
}

func (ft fullTime) getName() string {
	return ft.name
}

```

# Interfaces Are Implemented Implicitly

A type implements an interface by implementing its methods. Unlike in many other languages, there is no explicit declaration of intent, there is no "implements" keyword.

Implicit interfaces _decouple_ the definition of an interface from its implementation. You may add methods to a type and in the process be unknowingly implementing various interfaces, and _that's okay_.

# Interfaces Quiz

Remember, interfaces are collections of method signatures. A type "implements" an interface if it has all of the methods of the given interface defined on it.

```go
type shape interface {
  area() float64
}
```

If a type in your code implements an `area` method, with the same signature (e.g. accepts nothing and returns a `float64`), then that object is said to _implement_ the `shape` interface.

```go
type circle struct{
	radius float64
}

func (c circle) area() float64 {
  return 3.14 * c.radius * c.radius
}
```

This is _different from most other languages_, where you have to _explicitly_ assign an interface type to an object, like with Java:

```java
class Circle implements Shape
```

# Multiple Interfaces

A type can implement any number of interfaces in Go. For example, the [empty interface](https://go.dev/tour/methods/14), `interface{}`, is _always_ implemented by every type because it has no requirements.

## Assignment

Complete the required methods so that the `email` type implements both the `expense` and `formatter` interfaces.

Complete the `cost()` method:

1. [ ] If the email is _not_ "subscribed", then the cost is `5` cents for each character in the body.
2. [ ] If it _is_, then the cost is `2` cents per character.
3. [ ] Return the _total_ cost of the entire email in cents.

Complete the `format()` method.

1. It should return a string in this format:
    
    ```text
    'CONTENT' | Subscribed
    ```
    
2. If the email is not subscribed, change the second part to "Not Subscribed":
    
    ```text
    'CONTENT' | Not Subscribed
    ```
    
    The single quotes are included in the string, and `CONTENT` is the email's body. For example:
    
    ```text
    'Hello, World!' | Subscribed
    ```
    

You may want to import the `fmt` package and use [`Sprintf`](https://pkg.go.dev/fmt#Sprintf).

```go
package main
import "fmt"

func (e email) cost() int {
	if e.isSubscribed == false {
		return 5 * len(e.body)
	}
	return 2 * len(e.body)
}

func (e email) format() string {
	if e.isSubscribed == false {
		return fmt.Sprintf("'%s' | Not Subscribed", e.body)
	}
	return fmt.Sprintf("'%s' | Subscribed", e.body)
}

type expense interface {
	cost() int
}

type formatter interface {
	format() string
}

type email struct {
	isSubscribed bool
	body         string
}

```

# Name Your Interface Parameters

Consider the following interface:

```go
type Copier interface {
  Copy(string, string) int
}
```

This is a valid interface, but based on the code alone, can you deduce what _kinds_ of strings you should pass into the `Copy` function?

We know the function signature expects 2 string types, but what are they? Filenames? URLs? Raw string data? For that matter, what the heck is that `int` that's being returned?

Let's add some named parameters and return data to make it more clear.

```go
type Copier interface {
  Copy(sourceFile string, destinationFile string) (bytesCopied int)
}
```

Much better. We can see what the expectations are now. The first parameter is the `sourceFile`, the second parameter is the `destinationFile`, and `bytesCopied`, an integer, is returned.

# Type Assertions in Go

When working with interfaces in Go, every once-in-awhile you'll need access to the underlying type of an interface value. You can cast an interface to its underlying type using a [type assertion](https://go.dev/tour/methods/15).

The example below shows how to safely access the `radius` field of `s` when it is not known that `s` is a `circle`:

```go
type shape interface {
	area() float64
}

type circle struct {
	radius float64
}

func (c circle) area() float64 {
	// ...
}

func printShapeInfo(s shape) {
	c, ok := s.(circle)
	if ok {
		radius := c.radius
		fmt.Printf("s is a circle, radius: %v\n", radius)
		return
	}
}
```

In `printShapeInfo`:

- We want to check if `s` is a `circle` in order to cast it into its underlying concrete type
- We know (from the function signature) that `s` is an instance of the `shape` interface, but we do not know if it's also a `circle`
- `c` is a new `circle` struct cast from `s`
- `ok` is `true` if `s` is indeed a `circle`, or `false` if `s` is NOT a `circle`

`c` and `ok` aren't duplicates: the assertion returns the concrete `circle` value and a separate boolean that says whether the assertion succeeded.

## Assignment

Implement the `getExpenseReport` function.

1. [ ] If the `expense` is an `email`, return the email's `toAddress` and the `cost` of the email.
2. [ ] If the `expense` is an `sms`, return the sms's `toPhoneNumber` and its `cost`.
3. [ ] If the `expense` has any other underlying type, return an empty string and `0.0` for the cost.

```go
package main

func getExpenseReport(e expense) (string, float64) {
	switch v := e.(type) {
	case email:
		return v.toAddress, v.cost()
	case sms:
		return v.toPhoneNumber, v.cost()
	default:
		return "",0.0
	}
}

// don't touch below this line

type expense interface {
	cost() float64
}

type email struct {
	isSubscribed bool
	body         string
	toAddress    string
}

type sms struct {
	isSubscribed  bool
	body          string
	toPhoneNumber string
}

type invalid struct{}

func (em email) cost() float64 {
	if !em.isSubscribed {
		return float64(len(em.body)) * .05
	}
	return float64(len(em.body)) * .01
}

func (sm sms) cost() float64 {
	if !sm.isSubscribed {
		return float64(len(sm.body)) * .1
	}
	return float64(len(sm.body)) * .03
}

func (inv invalid) cost() float64 {
	return 0.0
}

```