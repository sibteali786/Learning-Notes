---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
Promise.all ^KAypAjjT

first some theoretical study of how Promises work ^nZ5zsal0

- Promise is an object representing the eventual completion or failure of an asynchronous operation. ^kvkY79er

Example ^FBJfZ4sZ

Essentially, a promise is a returned object to which you attach callbacks, instead of passing callbacks into a function. Imagine a function, createAudioFileAsync(), which asynchronously generates a sound file given a configuration record and two callback functions: one called if the audio file is successfully created, and the other called if an error occurs. ^8yrOgFG5

function successCallback(result) {
  console.log(`Audio file ready at URL: ${result}`);
}

function failureCallback(error) {
  console.error(`Error generating audio file: ${error}`);
}

createAudioFileAsync(audioSettings, successCallback, failureCallback); ^vwfbDWNe

Chaining ^kQ1tXIHY

- Execute two or more asynchronous operations back to back where subsequent 
operation starts when previous operation succeeds with result from previous step.
- in old days this lead to `Callback Hell` problem. ^7eZ9iQZj

doSomething(function (result) {
  doSomethingElse(result, function (newResult) {
    doThirdThing(newResult, function (finalResult) {
      console.log(`Got the final result: ${finalResult}`);
    }, failureCallback);
  }, failureCallback);
}, failureCallback); ^oujw3EvE

- With promise we accomplish this by creating a promise chain.
- The API design of promise has feature that callbacks are attached to returned 
promise object instead of being passed into a function.
- the .then() returns a new promise different from the original ^4CQlfth0

const promise = doSomething();
const promise2 = promise.then(successCallback, failureCallback); ^rsDHAKoY

This second promise (promise2) represents the completion not just of doSomething(), but also of the successCallback or failureCallback you passed in — which can be other asynchronous functions returning a promise. When that's the case, any callbacks added to promise2 get queued behind the promise returned by either successCallback or failureCallback ^PAR7KaXO

For details visit ^10t19NKb

Promise States ^9knFLS5r

A Promise is in one of these states:
- pending: initial state, neither fulfilled nor rejected.
- fulfilled: meaning that the operation was completed successfully.
- rejected: meaning that the operation failed. ^VUmr4R2B

- A promise is said to be settled if it is either fulfilled or rejected, but not pending. ^wWQg3lkP

Promise.resolve() ^tTA2TKiT

The Promise.resolve() static method "resolves" a given value to a Promise. If the value is a promise, that promise is returned; if the value is a thenable, Promise.resolve() will call the then() method with two callbacks it prepared; otherwise the returned promise will be fulfilled with the value. ^6BpVcot7

Attempt 1 to write pseudocode ^KY2QAal5

export default function promiseAll(iterable) {
  return new Promise((resolve, reject) => {
    const results = new Array(iterable.length);
    let unresolved = iterable.length;

    if (unresolved === 0) {
      resolve(results);
      return;
    }

    iterable.forEach((item, index) => {
      Promise.resolve(item).then(
        (value) => {
          results[index] = value;
          unresolved -= 1;

          if (unresolved === 0) {
            resolve(results);
          }
        },
        (reason) => {
          reject(reason);
        },
      );
    });
  });
} ^m3vOm4Hd

With Async Await ^QtoKLsjA

/**
 * @param {Array} iterable
 * @return {Promise<Array>}
 */
export default function promiseAll(iterable) {
  return new Promise((resolve, reject) => {
    const results = new Array(iterable.length);
    let unresolved = iterable.length;

    if (unresolved === 0) {
      resolve(results);
      return;
    }

    iterable.forEach(async (item, index) => {
      try {
        const value = await item;
        results[index] = value;
        unresolved -= 1;

        if (unresolved === 0) {
          resolve(results);
        }
      } catch (err) {
        reject(err);
      }
    });
  });
}
 ^ii9kzHvU

this is called Executor Function. It runs immediately and synchronously when we call new Promise() ^w55O7Teu

new Promise((resolve, reject) => {
    // this Promise is currently "Pending"
    // it's just sitting there, waiting...
    
    resolve(42)
    // NOW it moves from Pending → Fulfilled with value 42
}) ^A6Dd9Rdx

resolve and reject are callbacks injected by the JS engine that act like a door — calling them closes the Promise and announces the result. ^DyTDWMQp

new Promise((resolve, reject) => {
    // ...
}) ^aTNsmFQg

Tell me what state the Promise is in at each comment: ^7cejHSHG

const p = new Promise((resolve, reject) => {
    // State here?
    
    setTimeout(() => {
        resolve("done")
        // State here?
    }, 1000)
    
    // State here? (after setTimeout is registered but before 1s passes)
})

// State here? (outside, immediately after new Promise()) ^WyjkkmJI

my answer  ^nZwyvkYd

const p = new Promise((resolve, reject) => {
    // pending maybe ?
    
    setTimeout(() => {
        resolve("done")
        //fulfilled
    }, 1000)
    
    //pending
})

// pending ^8biew60X

what's happening under the hood at that second // pending:

The executor ran synchronously
setTimeout was registered but not executed yet
The Promise is sitting in pending, waiting for someone to call resolve or reject ^7YChIsHT

const p = new Promise((resolve, reject) => {
    // never call resolve or reject
})

p.then(v => console.log("fulfilled:", v))
p.catch(e => console.log("rejected:", e)) ^nzodlOWi

What do you think happens if you never call resolve or reject? ^yQwXA8z7

Nothing gets logged. The Promise stays pending forever — .then and .catch never fire.
Think of it like: ^WRxyJWUH

Promise = a box that will eventually have a value
.then   = "when the box opens with a value, do this"
.catch  = "when the box opens with an error, do this" ^f2omEWz0

As for now 

- Promise has 3 states
- resolve/reject settle it
- .then/.catch are listeners ^JZEKn2aF

const p = new Promise((resolve) => resolve(1))

const result = p.then(v => v + 1)

// What is `result`?
// Is it 2?
// Is it a Promise?
// Something else? ^bqY2n0Kt

what do you think .then returns? ^RQoIxAkp


`.then` always returns a **new Promise** that resolves with whatever you return inside it:

```
p.then(v => v + 1)        // returns Promise<2>
 .then(v => v + 1)        // returns Promise<3>
 .then(v => console.log(v)) // logs 3
```

This is why chaining works. Each `.then` hands off to the next one.

---

## Now `.catch` Makes More Sense Too

Since every `.then` returns a Promise, errors bubble down the chain until something catches them:

```
p.then(v => throw new Error("oops"))
 .then(v => console.log("never runs"))
 .catch(e => console.log("caught:", e))  ← lands here
``` ^p96Pkr7h

What gets logged and in what order? ^W8dyDp7M

Promise.resolve(1)
    .then(v => v + 1)
    .then(v => {
        throw new Error("boom")
    })
    .then(v => console.log("A:", v))
    .catch(e => console.log("B:", e.message))
    .then(v => console.log("C:", v)) ^l9E9EsCO

B: boom
C: undefined ^wwpffEN9

Why C is undefined
Remember — .catch is just .then in disguise. It returns a new Promise too.

.catch(e => console.log("B:", e.message))

console.log returns undefined. So .catch returns Promise<undefined>. That's what C receives. ^aQoNk0vH

The Mental Model To Lock In ^9UD60CkU

error thrown    → skips all .then until first .catch
after .catch    → chain RESUMES normally as fulfilled ^bvRIGt3G

So after .catch handles an error, the chain continues as if nothing happened — unless you throw again inside .catch ^gywb2FnX

what wll be logged here  ^isd61aL6

Promise.resolve(1)
    .then(v => { throw new Error("oops") })
    .catch(e => { throw new Error("oops again") })
    .then(v => console.log("A:", v))
    .catch(e => console.log("B:", e.message)) ^FInB6CNq

B: oops again ^MzvWz4jk

error → skips .then → lands in .catch
error inside .catch → skips .then → lands in NEXT .catch
.catch that doesn't throw → chain resumes as fulfilled ^1ebiz7Bm

.finally ^Sy5R0Dza

.finally(() => ...)        // no parameter — receives nothing
.finally does NOT modify the value passing through the chain
.finally runs on BOTH fulfilled and rejected ^GJl4zAvE

Promise.resolve(42)
    .finally(() => console.log("cleanup"))
    .then(v => console.log(v))

// logs:
// cleanup
// 42  ← value passed through untouched ^rQTfFFjp

function fetchWithFallback(primaryUrl, fallbackUrl) {
    resultPrimary = new Promise((resolve, reject) => {
        const response = fetch(primaryUrl)
        response
        .then((v) => resolve(v))
        .catch((e) => reject(e))
    })
    resultPrimary
    .then()
    .catch((e) => fetch(fallbackUrl))
    .then()
    .catch((e) => console.log("Both requests failed"))
    .finally(() => console.log("request complete"))
} ^S9XawA4U

Implement a small function:
fetchWithFallback(primaryUrl, fallbackUrl)

Try fetching primaryUrl first
If it fails, try fallbackUrl
If that also fails, reject with "Both requests failed"
Always log "request complete" regardless of outcome ^DgAZZkr3

Attempt 2 ^U7jRoznz

function fetchWithFallback(primaryUrl, fallbackUrl) {
    return fetch(primaryUrl)
    .then(v => v)
    .catch((e) => fetch(fallbackUrl))
    .then(v => v)
    .catch((e) => console.log("Both requests failed"))
    .finally(() => console.log("request complete"))
} ^HZqUR70S

Final Attempt ^7JBfa81D

function fetchWithFallback(primaryUrl, fallbackUrl):
    return fetch(primaryUrl)
        .catch(() => fetch(fallbackUrl))
        .catch(() => Promise.reject("Both requests failed"))
        .finally(() => console.log("request complete")) ^yzruUhiu

What's the difference between these two:
.catch(() => throw new Error("Both requests failed"))
.catch(() => Promise.reject("Both requests failed")) ^RwTZD7Ft

Are they identical or is there a subtle difference? ^25OK0csw

What .catch Does With Your Return Value ^BuQi18Ti

// case 1
.catch(() => { throw new Error("failed") })
// .catch sees a throw → wraps it into Promise.reject("failed")

// case 2  
.catch(() => Promise.reject("failed"))
// .catch sees a rejected Promise → passes it through as-is ^SC2HPzZx

catch returns a promise in first case 
in second it already returns a promise so as per what i learned it becomes 2 promises ? ^Dz5WUSXo

About "2 Promises"
.catch doesn't stack Promises on top of each other. It unwraps them automatically. So: ^L9wvffcf

.catch(() => Promise.reject("failed"))
// NOT Promise<Promise<rejected>>
// just → Promise<rejected>  ✅ ^834dFASJ

In strict environments, throw inside a callback can sometimes behave unexpectedly. Promise.reject() is more explicit and intentional — which is why it's preferred in interviews. ^jPGWrFMC

## Two Ways To Handle Fulfillment + Rejection

```
// Way 1 — .then(onFulfilled, onRejected)
Promise.resolve(item).then(
    (value) => resolve(value),
    (reason) => reject(reason)
)

// Way 2 — .then(onFulfilled).catch(onRejected)
Promise.resolve(item)
    .then((value) => resolve(value))
    .catch((reason) => reject(reason))
```

---

## The Subtle Difference 🎯

Way 2 has a bug in this context:

```
Promise.resolve(item)
    .then((value) => {
        results[index] = value  
        // if THIS line threw an error...
    })
    .catch((reason) => reject(reason))
    // ← .catch would catch errors from .then too!
```

`.catch` catches errors from **both** the original Promise **and** the `.then` handler above it.

Way 1's `onRejected` only catches errors from the **original Promise**, not from inside `onFulfilled`.

---

## In `promiseAll` Context

You don't want accidental errors inside your `.then` handler to trigger `reject()`. So using:

```
.then(onFulfilled, onRejected)
```

Is more **precise and safe** here. ✅

Makes sense? 🎯 ^pdKpsDLP

inside .then for Promise.resolve why did we not use catch here after then instead we used resolve and reject with value and reason as values ? ^lLr6V7HJ

can you explain this line 
Promises are meant to be chained, so the function needs to return a Promise.
for Promise.all() challenge context and with an example ^VRQhpJjv


## What It Means

When you call `promiseAll()`, the caller needs to **wait for all promises to finish**. The only way to "wait" in JS is to have a Promise to attach `.then`/`await` on.

So if you don't return a Promise:

```
// caller does this
const results = await promiseAll([p1, p2, p3])
```

`await` only works on Promises. If `promiseAll` returns `undefined` or a plain array — `await` has nothing to wait on.

---

## Concrete Example

```
// without returning a Promise
function promiseAll(iterable) {
    const results = []
    iterable.forEach(item => {
        Promise.resolve(item).then(v => results.push(v))
    })
    return results  // ← returns empty [] immediately!
}

const results = await promiseAll([p1, p2, p3])
console.log(results)  // [] ← empty, async work not done yet!
```

vs

```
// returning a Promise
function promiseAll(iterable) {
    return new Promise((resolve) => {
        // ... logic
        resolve(results)  // ← caller waits until THIS fires
    })
}

const results = await promiseAll([p1, p2, p3])
console.log(results)  // [v1, v2, v3] ✅ waits correctly
```

---

## One Line Summary

> Returning a Promise lets the **caller decide** when to continue — either with `await` or `.then`. Without it, async work runs but nobody can wait for it. 🎯 ^aH3v0qyV

Promise.resolve(p1).then(value => results[0] = value)  // p1 resolved ✅
Promise.resolve(p2).then(value => results[1] = value)  // p2 resolved ✅
Promise.resolve(p3).then(value => results[2] = value)  // p3 resolved ✅

// but caller is awaiting promiseAll() — a completely separate Promise
// nobody told IT that results is ready
// until...
resolve(results)  // ← "hey caller, everything is done, here's your array" ✅ ^FecmgXyi

but isnt each value we get in onFulfilled already resolved ? thn we are are resolvog results array again ? ^smmCF8Bb

Think About This
When each item resolves, where does its value go?
(value) => {
    results[index] = value  // ← stored in an array
}
The individual items resolve into results[]. But who knows that results[] is ready?
The caller is doing:
await promiseAll([p1, p2, p3])
They're not waiting for p1, p2, p3 individually. They're waiting for one thing — what is that one thing? 🎯 ^wdIY4DBD

One Line Summary
Individual Promises resolving fills the data. resolve(results) settles the outer Promise that the caller is actually waiting on.
They're two separate things:

Items resolving = collecting ingredients
resolve(results) = serving the finished meal 🍽️ ^PjbuzrSi

## Element Links
10t19NKb: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises

tTA2TKiT: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve

%%
## Drawing
```compressed-json
N4KAkARALgngDgUwgLgAQQQDwMYEMA2AlgCYBOuA7hADTgQBuCpAzoQPYB2KqATLZMzYBXUtiRoIACyhQ4zZAHoFAc0JRJQgEYA6bGwC2CgF7N6hbEcK4OCtptbErHALRY8RMpWdx8Q1TdIEfARcZgRmBShcZQUebQBGAE5tHho6IIR9BA4oZm4AbXAwUDBSiBJuCABpAEF4GoArBoAVNNLIWERKqCwoNrLMbmcAFgBmZIA2RLHhgHZRgA54gFZE

+IX+MpghngWJhMTRnkSABln4k+HhxL4iyAoSdW542eSFtZukxNmzk9HNyCSBCEZTSbjDZYAiDWZTBbgnKHMKCkNgAawQAGE2Pg2KRKgBieIIIlE/qQTS4bCo5QooQcYhYnF4iTI6zMOC4QI5MkQABmhHw+AAyrA4RJBB4eUiUeiAOqPSTcW7tCDStEIEUwMXoCUVKG00EccJ5NDxKFsDnYNTbU0nBF3CA04RwACSxBNqHyAF0obzyFk3dwOEJBVD

CPSsJVcCcebT6UbmB7g6GHWEEMRngtlktlvFhusoYwWOwuGh84WmKxOAA5ThibizRtjF4LZVlQjMAAiGR6GbQvIIYShmmE9IAosEsjkPd6oUI4MRcL3no3lid1hDs4soTiqenuAP8EOHT1MH0JAAFFH6DsIbQEfCxyjNXqVK8GW/3wU83mcKBCwgjHEVBRgmX0/wAMVwG98BtVBIRPXoaiIZRS3QYJeT6CtSCgcwCGQkE0OgC0eT0HJcHDJhAzQZ

N8HNUgQXDAgXzPN9r0/B8eVwIQoDYAAlcJAOA5EhAQHdKIACWBUFz1QeIUgQlVJFCFioAAGXDVED0HMSHSIDgtJokN8CKABfTYSnbPt0A4AAtZYTAIGMoU6YDoFfKFBjQEZhgWBJlkbUY12WYYeGWCYzQdODnCSUZtFbb41h4UZRjtCZtwdB5iCeMtvni14pm+X5RniMKoSBEEwTQMqHRhbV7RVNV0UZXECRJYkkGHSlqTjBlsVallyA4dlOWyLC

HX5QVNW1VVsT1VNkXVeVssVarEUW9Fprc3UM31YRDWNZ5zUta1njtKEnXnN0Zx9Cb/QQajUFosMIy89BcHiWNR2IBMk2MxEEH3U1s0Oa4QrbSAiyrNCLkilUoZLWsOHrNAfnGNczmGMMux7IHUEPY8VRHOliAnTIxpuucFyXPGXlmNceHXWZGb+Hc2D3ayCd0lVT1kvlCBYKBUEELJUHUBBcQQXD3GFqAhGIGBUDYXlUEkNgKFQd8bzCZhUAoXEt

P1Z9XwkflBeFgwEDFoFJelghZflxXldV9XNfYnW9YNn8/wAoClQaspfxyKCYLgxSyl5gjUMqDDxvhpg7fwKOiN4uBSL/CijVIR7nodXFGI4ZiTfQM2kQt0XxdtvD8AdhWlZVtWNa129df10hDdqnj+MEv20BE7myn0hApMq2T5JqpSVN6DSDO0o8B8gfTDKe4yzIsh0KgkVF6FRABNV4mB5Vzug8h03pGNdtEWUZrjC+ms12WYoWivNx6Ck4FjGZ

m1mzCGICynKqBGzJCCoceI4wJi+TGBsB0FUZL+yhHVYCAcBAbUxP1Zk6BCQdVJF1Kkl16QtUwdAIaI0uRx0DgKYUoptpzV2gtGUCBlqAL/k1DUNDKg7S+n4SQv0jp5xOrAM6KDHS0ldO6Aot0VR+mgg9ayucVThmIJGCQuBUh7RJnwoyKZGqA2snmCYswFithvn/BGnBnjLH+A6cxHAkYoyAcME4YVvhrmxt2YIy5+w6WHN9MmU5ciSKpouLxclV

zOKZizaxKpdzok5j4xCrEJDODdh+MIqAOyoGsErTQDQEDYCFoEOAgQwg5HDMoa2VsECMByEIe2eh9A+CliWJWpB8YUV8IEeuWSOBZOYDAZGkgUQcGELrC0TAlwlm0E+CgqlKgpObukzJ2S7B5IKagIpJSxrlMqagapY06k1waU03CnBWntIFCIK2ztsmhAGdgIZnBRlK0QOQU5HBpngRyL7YC8QwITUgtBAUYcXJIRQkRWOPIiyJ2Tt0EiUIyJRE

otneR/084MX8EXJJ6AFnuytss3pqz8mFIQMU8I2yOAVPFnsmpct6kGBOS03EFzOnXJVrc/pgzhnPPGW8qZXEu4CVYL3MWpBRLiSNCPeBpoFLlSnmeGey8uYSuXrRNeRRLKQE3ugCCAAhAAUryWywxmC2SPvANyvMeTnwhPJB+JxEgTHeFcd40SthDBuNoCYUwJgnCsYkAKqwUpQgAatIB+wSqJEdSsOYWYVj/KUtJKqvBw6QCQfCdajCiFtRwZ1B

0FJ8G9WzYNNkHJyE/ioVtThdCpRoOYWG1haCq3ihrRog6iZ+EqgtJSU6toRGXXEZTO6sic5osUa9KMoxuHxkOtouiqY9HPCCrmCYuYjHYWhiuDdiM6y/Ida8eYLZ3G43ifPXxJN/EUyCQ6ecITabhMZi8KJbMOZz0JhHYuEAxyYGgk0mZcyJDft/XCL5/4hIIIBcHIFsFuCpvcmeWFEhIXYRheCuFacEUZ2RaOnRZR86YvwAB9AQHGkgc7rxIV4G

+5ioXhAIeUrk3jzg8pZgqlFVvto0vIMq9SjmQ1RvayEAFgwFIAAeWUBBAA4ssc1XQWSnxVDauY2hwpOuzAFdKfyYEqmissZYKnUolQWHaaYq65hwdDQ2Yz2hLhnFU9MIxwwE1lDgcm4ziDKX1UzeqYtWD2q4Pzd1AhfUmTdFIWWsaFapocJbZKbzcoFRKni+wrUtC4sOgNLw2dcljo9qEX2i6YjrrXukfdHD87x3KLetCYY06frZYUWUNM+ieBTB

4HmZx26LGmguF1uxu7ngQkgbsY4cN2w408XjZV+a/GTivWgWcN7qahLpiFZYrXTgQkSC+uJHHQXYq/YmbZD4YDUCyagYpaT8W61wBsqWIgjTEByWsoWvE9aSHMJIVAMBhBZJkJSL77h8AFtRMwM74YkQhCe87DkiZykAB1kYPhB7rcMb3bu8jpAUqZqAXT6GiJRc7mPkbvLO9gQINMajy3YBBAUCAaicuwAACgAJRnYoB9h5fT7mPJGUIZgsFEfK

GyBMnoN2LYk3xnT1AqgannbIvyZQIhJlnMCHoUgT3rBPagPrVAQOQf4yx+8+QSsjR64fOmDJKtxaI+4o4NgUvggZN1swIQ2AxCJkx4KRW5OQi9jO1r3ZbBxZtKB5bwg7LelMBRG09m2ARDME+Rl42B2xxHbKSdgPF28XO/O4EOWpBHvPeJWLB3HPPvfd+0uKIXP9fdTBxk4aPRcDQ5VrD1glLzeChR439HhuSc47xwTs3GOjcljJxTnoVP7e0+CA

z+5rP2ec6+3crlTz+ewRlyLt54RzuCEl5NK2svsjy84Ir5X7y7vq81/SMWuu69Un79jzgJvOBWzD09iPuy7fsEd9d4WbuHuzAXum+vuNMxAAet+1KweQIoeFun+keeypAMeSs7uCeSe0iPsVGckzmkAQcUAIcwKsG+2UAiG6ECAmEUKCc1cZBxEGGDoiKmcVEqKuGkA+GTEhGn6aepSuEme52l22s/+t2+eD2luRK6yb25eXOP2Qgf2NegOyO9e4

OTeUO3S7eOyD+oOveDuo+A+nA2guO+O/gVsuhz+HAE+fu9O1ObAs+9OjOi+72Feq+Dy3KG+iswuWcNM4u++t+h+MuhAcut2CuIIF+LSauuIN+2u9+ihj+xOZhr+ZuH+Vu3+1hf+ueru7uxoIBPuk+6YkB2uQISsIeXewQCBPSSBKBce6BAqFGPcwE02MSkkSaY8sqsC8q6kmke2eknRc66qpQmq5Qgm9AFAvImgnYso1YeaPMFqJ8rEnkQwtq8UA

aPwCwQUoUwCz84IkwpUSw3q4Cuwa42mZQlmaAEU+mUaawm4ZwSwE8LmzRmYIi6aaAIibCvmEA+Iwwi4mgvIswPIIOwWbxrIw0EW3IvolaMWOoraDCS0iWa00Jm0EJs06WKomWWiOWAieWcEFw/aRWEiC2UigcZWLBFW7YE6qiMmGiM6Hac6AMtMPAvk7WKw2YfWzwuBDAlYO6yMvyWY6UPwxwRxWqE2UsU2CSRMs25M04JWZQt64BK49MEST6dob

qi87Mu23iZ6iSfMcRl+GRQBGIMRqITOJSIYUALOqAwAiOqAeuL+2Id4OIygTOAABtPr/n4RTnXEuKgAAKp8RqRoAAAkwAxp+AUApkjpLOAA3IjqZIjojtqS0gOJcoEPqd3t1EztHriGaRab0tacNLadoBmaQE6WOMgcyh4aLjsj/g7ofgGcAIWWGZGdGbGcjLkS6TYXTvPsjEzlWUKFLLhJSg3rqcaCmcDt1GdomayiOSDpGf+p+vGWckOYmFOWm

cGaaeaZabmRKHaWwA6c6akW6VDorJ6T6X6agIGauQ2VGRwDGRwHGWPmchOVcsuVSOmaWaQFmRuWRFuQWW+cWW+Vvp4f2RUlWX/rWfWeGVeTeYjmAVPtYbYZ2czj2X2eUoOYAcOQaeOR0k+QaTOaBj8qyaBoQTBmgAKfBqQWhkhhQRQpDNQe4LQanOnORNhsSfRAXFilqfeb0oucwM+YaauR+TmV+fmfaU6W2Wke6UeULCebWReRBU2beRwPOb0o+

cmQaa+THgJVaUJcED+THn+SgeWXyp3iBTWWeXWW+ZefJdBa2XBR2fYUhTIChWdtxbxZhUmZiDhRGTUd3MKsJDRhKsPPcTKrcYCO0exuqe+ovD0SvIKH0cUAJpUKiAAIrxBQAAAaLoEku8smlqCmAwCx1wNmKw8QJVTq/Jrwmx1UYwKm62aweYn8qwrYIasJckH8KQ9MhwUa+YTiEwIVUgQVIEcGTxqALxaCbx2C7UfxQWRaGCYWpao0oJE04JqW1

ayJTWdaLVjajCzakJa1kAqJ2WY2bBgiWJ50DoA6xW+JvoRJ3GrB5QZJ70EwdWaJjWAgi6po3qjYfwPAPwLJaAQUfW9iwExmlwswTmvVx6k2p6kVEAxM44c2kpV1S2d6+iD6kSSpO2IpGpPMn6GIyk4Y5Ss5B2eNmchNeF2BuwhF0GIKmptByGNitF+EFF6ADFmGTFWc5WrFBGRGEAJNBNlK3llGIq/cAVDGLRfVLGbG0VDRg80VaqvG68iigmswC

AtkiQhASVtkDQOVsx1FEASm5xAaN8AaYUW4emlVIEfwCQpUa2Cw5w5wJUzVK03AkCww7VeYyUKUiQn8GUiao8LtjxnmyCyW41/mUxZQ/xM1oWJawJC1etk01CK1sW80jUG1ztcJqd21iJXCbaWW1J6JXaJ1wihWzol1noBJeBN1NJG8D10IvxlJ9W+dr1qo71ckoEdm9MENDNxY3WIE4wgNA2/1awqUhwpFHYHiwp0NtGcNpMCNgSSNKoMpK2aNi

prMekqpWNMNVqySqA36+SPEVsOuDuzK+gks3Oa+fOYyryKuw0qABub2BuHOTAVsru9gCAAAjqJDkKgIjryjfbLJyLkO9ifmSmYDytfTqWhemK3GoF9qufjNeNntUuwPzrLKStoIjikuGErPgE9ouDALrOoJksEC3qXqgI6bxagFJIKI6dnnYJOBgWUOQLMp+iknvfHj0HfsfW0qfV0s4bzuAxWS/nfd1GQ4/bAS/VoGEJ/WND/SMhAy0kiIA63EC

L0qAyg1fUI1xVA+6HrLA3dq7iGQgwYEg2A6g5DnABgy4I3jg3g7gAQ9bMQ6oW9hQwaVQ0EPgLQ5dpoAw97N8tgX8lTaHMQbTczXRlRVQThDQWE6zQwVhhzSxeimxZwQdmw5gPvZw0fecrwyYYzgI6g3/cbiI4/g/aI0/V0q/dI1/ULL/QowuVEDhCoyA4EGY5o3yguTozA+oAYyacY/oKYxo2g5Y5gzY9iHYw40Q7rCQ9rg7q46mY/tQ543Qz45k

Iw2moKnUdwCLd0ZKgNUxnKqxtPNLaKbLbPL0QrfxkrZUMIA0BQKMGOPQGODrfJnMWfAVbMCkNMDsfmKBPMBbYsPJClEkOtr5OFHmE/JlC1bmCcFfFGqNnC+sPTOVHs04h5rCMHfCegtHX5t8PENgOooFoWt9ICeFnHVFonTNDnZi/WklpiztUiSnUw/tHnR6EdRAN2laPlq1TiaXXieXddSOok5Viou9AsM9Q1mOk1q3acF80kKFH9agNtt3dDED

c8GFOArsScGyePSel0WKRenPUOovctvevKY+szBjeva+hFbRtvegMQGwEKJbEQ5SkzkpagEaeECaZpagA6061kC68oBOGEJ64Y1AOOZxR60aBQEKt6+uTmVaQ680B9hrsm+UkztG7GyGRG3ob0m6xwVm2udmVaSW5ucJTuU6ZJsHrsvyIXDXKubWbWwQIW5ZQm6gOZCythfM6iI2TmR2ypR5d272/21hapUO15UbCwwdn686x9q6+66G3G8W7646

7O+UsGwgIu9m0/pfhmwgDG16yGT64m2wGm6m3Ow6Zm4e+Gzuy0vm3W4W8eyW9pdubuVW69oUU2/W9e42wW9e626WyO+5bxb21aUB5OZ5dGW5RB+O342BiKoE5BgQdTdwKRZHGE/TfHFE3RTE/CnE+zcwbdSSWwRihwTzTOwGxe265G1u0WxuRR1LBexu7Rzm2YVG/u4+/G6W0mym8QGm661e2G6x7u1+5x8u6Wy+9oCJY6e+zWxwT0yGb+w+/+3J

W2+B126OVSKB+29Bxp9OZBbp2O5pz2xO+Rj5dgds40bs/7cFcxmFcc9jac6qjxmAHxv0QlRIMMBiElfgJhJIM5CeDMS83rTarmAcJcKumcK8PmH/GHE4toGax/McLsEqyqCcagJAskKFDfBFJcVqxLQNe5rVEHRmpi6HbmlNUSyTCS/NeWmCdFknbtYy6gowjSxnetVnY1wy/Qiicy2iWyxy72tyyXVdHy4tqVoK0Ry9FVlGIkOK03ZK29bTK2B/

Hpg6qRbYtwEFMqeyT3f1lyWdO1hCDwCNpDZPXqxHeKQEka9KSa6jYl6vTt7Epvba6w6gPKN0wIbeHrCYe7gykQMwF9pM3fTkX7pWXQ4IXrvjR8iM8m1bDUBeC6L64JKhGoTnixvjH7lctbJ6ZoTdnw/9g8pbm9iIYXpbojl9+kuIULBDs3q3nfcCJ3u3uHjkDobe/oSM9StoOLBwKzndgXrfbdtGxD9944LyLyM/d/X6CY9AaR3W0TXzCkh919pT

1bBQL98cgD0Dx9rrJoKD5MsZSL+kg8pnFYyknD6gAj0j8oqwKjzDuj6EJj0uNj+oLjwafjyYYT0CDM/z6IU9hTzntT43pDqQ87JoIzxUsz5/qz0TpxWb7stz6o3z6T4L09Pu0b1bGLxL+Qn00HnLwQHB/hR9UE0QWgHBuh4RDHBEyhtE5XyyHhyqIwcxVN0k9zW98rxnz91kn96Rh2Nr5knr3rpPuD6r1D6b7D4UVb8j7b4Sm3g77rBL8710q70L

Hj1kgT/IcTw7in+TxwKP0H7T6oWHxHxdqEGENH33kpfH1zzz8n/doXuLsL6P1n5L0LNL/07L8k4LZs9RuKjs4FTZzkitFJ4hzBVA5xhpcZzmrnRWlZEqAsBOwEkGoFUDYDZUXIQXFmnlUgChd9MH8XqrmGMyzBV0n8C2pAjiiZdQYxmG4O1ghZpcoW6UA4J8DtrMYBqqLYrui1K6Z0fMs1CQISFxb4tKuPUYltwJZqks6uS1BrpSyhKcCEs6dXgM

lnpZUteuPCfrrlk5anUeWo3G7pXUm7V1hW1WXAJ2Hm5/Q7qzWbgI6jtDGZjgWMZViWDMED0Du1Ub2iFHSjysN4QpUJDLXJBXd5s/LZGrKVNAr0LWa9GJBvSnokFKgX5IWKPwAC8K7f1ox3Ta9tIhGfHgKgFiGq9E+2QJnC5QwqdsjO+nBXhEJfxRCc8sQhjoG1ZxXlkhqvVIekLxSZDeeOQ7toZ0HbGdcKSHIvjgRL7EVUAaHMFHX3IKUEa+OHAY

XQUYpIoEmLfLtPnxSZ8xqhpQuIWu1dZJDihKQtIRnwaHZC0KS5XIQOxA6mcVQ3EWor5S2b+V/+YtZ4MAJcz2czm7SRzlFVuHy1oBlzWAZeBqB8RZgVQXAGlVEzPMMBrzRTAsRCgJAswfwJzKcFWJOYSBeUNdOsFShTAb4owGgccRarpR9MEUdKI6m9rtY7QyIwEHszOqHCSuzxEOsIPeJh0BBAJMkUCTISRZ6uFLNLM11VBp0WE8g7OlIKZbKDDq

qgobtiRG6DopS2ggMEK1JIzdVETzBui9UW4t08YLMDcJGmsFYdN01URmPYIcTFVcwjqX1H/B1ZQ0LuXgg1hKXnq+DjWKNOUgzHRrBDB4oQ/UWRUqBpsXc+STgE9lH5M4ahZpTZOSmnC7JNezSM5CMiFgNB+cQsZWIjnKFUc2cd9HiFkiPDH1rchRJocZ3OR7C3GMhU/kdmj6I5AAKASOFa82ScPkUVgLn0XC6+BfpxV1gp8R+9Q97qoxx5QAAA5M

wERzUo8AQ4HpD7nd5ZJiAyiH3jUK3xCwZGokJ7OHznYFErYqvRHDv2HGKxgQxRRMQbmZQpju2hQiQA6OFhOjb8ro90XdjJQ8FCGhRX0ZfgDGoAgxZcZ2OGMSFnZNA0YwcHGN2TzjRGi40dq0INxpio+NjHMVIQUK9ICxMBJgMWPyZljc2FY+/hwCrFXYDCsoWsSv0bE+jQgYkdsSUR7wt4exZDPscLgHGiQhxDPUcbslH5TiQeeyWBv+IfGP4nxw

HA0oXwCZsl8CRFGmjjQQwYdq+3dVDKMNiaN94mhHXQXhhmE801xYQMiC6Jzxui8UPAD0aSi2TeiWx/3P0b0mPGniQxKsC8csKvE3jYx3SalKRNRDJjnxlDN8WfxZ6oBPxy+c3D+OuTFF+GrhICfEV96F5wJghSCdBOUgNj9x7+eCZAQ7Hdsbs3YrfmsIwmoBBxluEcUojwk54CJg/WcUWK0k6SKJy4xBBsxOE2tRaezK4aFVAEdFbhngujHLRc5u

d4qVzCQBcCgBJBqwVQTQH8LtHzFvIQ2bQDcFSh7AtwVwRsBbSWBxRVg9VP5BCMMRsl0uNtK+I1XSi7AbayLQAaqLYFeYyuZIiah1EpFR0BoIg2rnSPEEMjVqTIthG1zkF0t2Re1CAAdXzoDci6BWc6riS0F8gq6MVYjvdTFHvQIIRgqYVK1piXAtspULVgq2OBqi90AUB1EyTHruCXu56eGkaNOlL1TWFox7iqkqDSBZA8gJQMokYA4hXk2gU+pY

EFC4BtAuIGINkGcBekhQCgB1tgAiCygEAmgBQPqlwD0BcAQocnIQDgBQAFAkmIQCQAQAKAvSHeZQAAH1VeeQTGmEM1KVAIIzKZREiiPCoAzArAPWswx5oCy2kQsjpLrDFlqAqJCHGiYCmCZl8SCdNZiVh1YnRx6+9BDiQRxRT3SSOyTKWYLKlhyzRZHYRWfFOOEWczhVnAAdKiAES0bhSqHSHFQGLaoIAiQVEBwAghqQhQywPEGgLkz/CQuCxb1L

VMMRDS/gpwdbADSiiodWwCQJxIsDChTBIkTtFhA6m0BOZXgFwQgd6nXDhQRpzsxOUSPYEkjJp2LckRVzwSCDqu1I0QUtOkTLVJBO09aZtTZFddFBnI9tKyx5Fcs+Rx03lqdJkTCjjZV0kVtCEkx3TuJS3ayLGlKhGJvUb0jbhyRrCD14IZwdKL6lOBncPBJzA0YDOu6CiIAIM+7mDKCFPcbRSUvmZeBzwigvCK49AIsitjPyxcSs4CJTSQ50SQmD

E8iqMMw5lBoUtfXWSzQb5lAm+kwheey14mfp35qAT+eEG/6JTRUf/R2RcNs4HMpamU4+dlMeG5SYBWqQTAADUvS+gUgMMD4g8BdUFUq1FVNQAXxkgJVfAaBB+ouILaoMBIEYj0wWswoQUUiul16rJA0oOXQKFGmIGwJCugdKuSNVJG1zppAWImNNSEG1yaRIJeOu3MZE9cOuMJWQVtXVAKCOR+1PrtyIxJqDi6o8zQefInlyIp5SiGebgAkjzyLp

tJVGj1SsTgwFW0wD6Uun2KEDzgIiXUed3vn6tT5Pg8brdzNEBCHuN8nmbaLtYQAagqSSHpkmwZv4NJQIdJEozFzIARmiAekOUjQAE1eCNcPJQhKNDES2kXuBOpbhGRtJAgL2dMPHzqVUJ0waALINYB2Qr8g8dTXpBQEd6HjLc3FbIvH2aXEpOlqAbpWBM7x9LoCAyllK0tfkpK0l33DJYSjNzOxxYuSqIPksKXZBHAlKUpWBPKUAMegZ2apcUXaW

CgGlzKSZQUlaUjNblpRLpSEDmVUpnJ/SrRnrGGUyTewABTIp7mMgwAJlCAFpcQHeU9L5l3yxZb8onIrLyays7ofRI/SMTgFWs0BYzSTi4d9Z0CziUbLgXsE62PNVJUgs2Wm42UlSPZV4QKXWMilxy5QKcrUBWAKl+yqpZFP/GvL7lTSiFVMuIBtKQw9SqFTMo+W9K4VhRQpi0iGW6wRlT2MZaCvBWQroVnyusT8vabKUOkSKszkLXqIEL6MKU12e

lPCp3CIBOU2Khc3c4FT0AFAWUElWUCjB8AqIC8AwswH61I58kP1L8Ci57BHUio91LaGqq2oNWTAuYOAmzlhpfUfkLVu8AdRNSTuqwMucmlYGVyJp0grFvNLrmTUG5VIjRS3MWptyJBui2tK127lbTe5pi3aeYv2lDz1B/IsutEqFEOK4FTi/QS6DcXN1TBpoNYtcFChrybBvdR2oOv27qiIozidKOt0Pn/SZshos+QvRiX+Cwk8S59FazVJmrXuq

TS3p30yTMAKIPvAsWEBkClFkiagXPFytqXCqOl0OPlZCtUlCwAxFPI5eUjWa7SU8ivbdaP13X7qxGL9Psieq/xnrMkF6w3L52vXnJHl/uKMQ+uraMqX138gin/JQ7qzQmmKoYSxPAUpwoFkAGBVxPcWt8yOb3VJV+pdw/qH6f649eHhVhAbdYIGnlTerux3roNT0WDc+spSvqjh5nEVFlMNWAD9mbRE1eAM4wWqTIVq/Ka8JZrNAagPAZoFUEICt

BQ5uVAEflWqm9V4oWrAKLDBjkFQLapVSYH6j2CgRDE3wOYJGtZJxQtsxiJzGMD0ymaZFo0oasSIUU1ys1yi8OuSDUVNz81i0wtZQmLWrS9FLXAxayIrUdymRe0weZYt5GEiygF1MbncDTQNBZgSVasCcAaCdg2A7M/VA0GYCgh6AzgWyLZCqDVgIAdwCumdJ0H4a9BUYF0GQs7XSju1bdRsJAk/h7AFW8afxacRuKXAY0063mREtnpAzz5l880RE

npJ/IoROzZeFIBkByBFAeM/ZAjKYBIy2AKM/AGjIxkKAsZOMvGezEJnEzSZ5MymdTNpkKABI2fbIGIHpk4gKQ+AdmaJlyTEoIg78hQCUmxCMAeQz3freir5jvztAb2/AIwFZyrK/tAOoHSzgQ3VQREtE5DfBA1lMT0N2szDehnGFMEiVVWniabMQX1Cwdm7CHbbK41+VMFpzJ2YxlSlSA3ZHGT2R53QATBdUcAMhXoCgD11AuYcyqW81U1+Q8wQi

3yMuiREVzA1ckRmG7X51zAjgq3I4HiP/ioiraxmL4KFDtrRpUudxQAUVzTUYsM15XHNYS0bmEJm5Pm7Rf5uTqBbmRZawxT3LC0m6ItnaPDIdOG42KBRC2BLdCCS0pa0tGWrLTlry0FaitJWsrQK0nmtra6uAfVPVpMGt0VgrWCKDMAVZBQ2WtiVVmXwdS7BrgbWtwRPSPn3DYa3gxGiaMXXL1Eu42yBGyS+1JLP0FvUHeEHe146Ll5gMVeoDYD+9

dpVewHeEHhwQBzsx+XpBTN8CH02ef2xHC6HjFWwe9okXPLdlV5nY+lJG2yY9gjLJFqUo+oQpUkLgrNqAiOSvRKHB16NBQJRXZLfzNKUdG9ejbplkzX5nqyUEWYgFeT/GkAHg6SalARNH4PBd9BY+jSfu14j6CAokV9ZLPL2FFN91evnnkrr1H6m9uOpsR3tuxd7RZ3+vvedj+245h9sB3vePoz5T7vlM+qcfPq/yL64DaBnnrgDX3rKwg/2lvdvp

f1HIHw++pPofsY7H6Hgp+6Il5IyQlDSUo0a/YWKYD37D6hRJ/TnkoMM9QNIqj/bsiX2vr8CnQxDpgSgxqy4dqGiBeE0R3YrsOTNNidhogC4b0dzdElexXtEAGcd5BmvSAewD161Y4Bow5Ac70BET8S+shrdkQND6xD+B5ZOgfVVYHQJ6YHA8gbsOuHCDxBwA63r56CGgcNBrIXQYb1PZGDQPZg8Z1RxsGr98+2/Twd2T8GrsO+muG/qvV3Koj+jP

A73o40JTsCPGponxvJ2S0jm+CrPZAIunU6bVEAMhR2GIBwBJMaVW6YprgHEp00TCkYJ/BSCbgIEkCEqsYl015g3a2YT+OuCcTAIVgZm04mFxChCK9grwYzBFGTVjxfU1tRmCd0MSLAtwf8YaqNSzRTSKRuauacQk0Vkt6RJizuSyIbQW6S1udFQVFuHkxbIAcWmcM7twCu7Ut6WzLdlty2SB8thW4raVvaDlb7FnNGutdOhBVA3FmqDoOgNGB3A8

pi8swX8FeD7oREm3FUVLoT3bzjEjqEqM4L622iZ6l6XPU2ovl3dRt2x/MMXohlwLS94S64YJqqNhA6jEmiACcAQBpUagCwNKvqlQGs63IauKICVx6Op7apPVDTWbWGlJySK9A6PY/Dtp+ppgFmFqj8C9XBRFgvkH4PTDZauZZI9JGNe8BuBg01wvVL4Gi3TX6LmoJx+uTrrzVZrLjYgotStON2lrgt9x0LY8Yyw1rIthdTEtYpVAfG7F505um2qj

AABZeE87uPj/UUTHi/2CZrTnroR1DYPE5vNHU/z5gfqBEQGsFIZ6Z1A2ik8aKpMja4lFo+kj1qe4ibElLJtKXgvdnzxOTpCmOHAFW3VgKA0Z4U9MTZ1inujHO5hdcBhZHBwEJVZxNQO9SFmIAcEZKH5BuAMwwapUDVgGjmNAISqtU5mE4jqorGo06xgOm7WZj87koyXc4I5vkVHGuBSi0406fONzVY6bpvzR6aa4m6u55u30wFu4QDybdx1YM0dN

DMnTwzlWyM8HpK2SjssCJ6AEiaTMLpZRpUeOSVDzDtb2snWnAoQPBFHp09urRs9nrnVRLytlZ5ddfNXVWdnOd1ZkxutwWVGWzHJsTV7MEwQRlAbAasLqnoD4BPoHRiQIOYlPDmRg3tPOWLpMyvBswfyNktFBxHxRSouwSY8LtzAbnP4cQfAYzFWLRqjgO3I0+CGUzRqtMoEFsMZkvO2mgt9p2846dUVVc9d3mp863JfM3G1pdx2lhmvstW6Azf59

lnbpHlAWx5IFwPRjq1TB7fhkF/OtBYTMgQ4LuiWmOGt+Ymb2t64dC+sGShi7Vgs50JZnphrknDWw2mk1WYVLhQ1wyuh4RRculUWspFRsAeyYQBtnBilQKoLvB4BJUagBACkiKd1rWoFiqxFIGqdktasIQuA3TfmCy51VjNJiVYjt3S56Z5IjYdYMFCzCHAkW9m52RCBtMa67Tma4hG5tmnqKXTBaw3a+e65emZBIW5y9tPC1uXTQdakM7FuAsLrm

1UJ6raoldXBXjBl0xreqzWwGIFWfzEdYnqF3jBDguwX2uNmLPfaT5g2+dXnsgDEXVsESK4KDVvnWtqLD89ADUBkCZBaZckMhhQAYicM5ACAeWOzEb3ua31U7PmKjZ6CNIhY8QLGzjfHFhACbegZRJDpAgqzZDpfeQ4As1nKGaKqh3FeofxU4bCV91zHW3wOzk30bVNmm2oDpv438ZRNtBfbOJ0PDSd4tOzmybovCaiFlq54daq5P6BRg9AUTPoGG

ASQTdYV9nYCOqmvAliqp2zIYkPS6bNRCQSNGplXQ/VZz6XH5ipi6qtYNsVieU37WdkhQ5Fxl03Tedc13mLLuukLDtYN3ksXLh1phOWpOuVqdp1ui6y8frUO7G1EJiM9KKjOqIkqYe16xHo1YXA9gnWDM2gFBjoWjER3I4AfJwt6i8LmVobbdepOxKSLzifncFD/ilWCFySrAJ2ZwjI8BwvTd1qr2Qj4Amc0t8gCsx9Yp80+TcPFEzlDbV6zskGs0

tEIAB8XHZ9qsNXK6xYhwvGoMgXsYz2egc9nSsEEpTqBtOVpTxKgDpC46nssQ2e0QevvZBlA6gK8huStJf4mcz9ow6/eiGxCTgT7K0rjto7MB77JbFPleUA7NlS279lZtoF/CkAxwAOVe9Lf0DKEqsW93e+JxLaBGgdODlnJsL/ulsPWS+gh3vaodwPr2zAfIG2q9DrCl9CD+hyWyAdb7LczgWIfEF/ttt6HAD7h9XpAdgOIHnDqB4fdgf0ObynDn

TpQ9LaetQgnAWh0Q/oeQaVHggDgLI5LbmQlHqAWB6ZG04mPIKqyoe7iCFjKIx7RjCe3iinsX2Jk89ve4veF7vzV7uOje/yoKTqPKHyQw++sJPtn2YATjq+3aS/t32OHD9qWE/Y4Av31hKDz+7fckCCPkHKsQB/E+AdpDQHI1SR9I8Yd6P4HlDqCm2ySd3h0HmDh5Ng4pt4OsAfjoRyQbvBQOyHFDxp1aSZw0O0hhDwx6W0PvMPXorD2Iew96dcOs

nPDp7Hw7khpOFHyRTJwk9AcSO6Hszgp2GxgfRPOH8jzZ+vvacesKcOjhp7M8Y3EptHajjZ4Bx2f0PjHpj4dszekOBxVZ7NvoRisUMgKebOsrDQLc0NC2RRJs0W3zEscj2bH3EOx5G0nuCgwnH9hAAvdAlL2mnnjow945eyHP97TeBTkA2Pvp9T75AUJ+U6k6RPJAsDx+6I9b2v3WDzj5J9/dSdIOS2Ij8Z2I5ydLONHBjIAzI/Oez6NnpT5B5fah

doPcQVTyQDU8yB1PMAKL0tiQ83atPb+ozzp3AbFdSPGHAzqrEM5QOiR2XpbEl4wEmf8OZnCjulws9yfgPlnCj1ZyaXWejOwOozgx7s9Oe6Punxrqh1o/2dnOrXlzqh9c44dmPoyCt4Wg7JJ3YKXZat5s7aJqNPC8pjFyoElV4hVA1IzABoDUDdXKasBCxQS+sDWCvAwovtnMBbXawlQ85xmoFq6il3pdkoEaOYKcDjn5dmBgAgXWmic3XnTLEd8y

xHU81WXY7Nl3zXgR0XfnksG0oxQiVTtnWuRtazO1dfeM3XIbFWvy2BZhO4A+Ixd5Mx9TOAN3wab0nbviYcE4E7au551KSZbs57yzRFnK13eSjzBjMk2kIYjaynJKO+CFS3kMptnJ5SblQW94znvcUR46WBEVL/JkPIc5D5ffoa86xXvPkdes1Hc32JUIKDsr7+5O+8feHCijvrpW4QpVuXDjVwbvC6G+IUvD2zEgQgIQF9lGAJI9AL0om4jnVTTg

XqJxCVRKoBpnBcGec+sHkgrBgElwcKOcGkW0DZBXt1YNMF9tTB/bBXQAb6hDurWTL61nNNrqjvOmLju1+O6dffOOX2u4nhO08YsVBmrFgF66z5fbuQnfn08/QdzP9OaIJW4e2mN6gCiOp2sG8vbi7QStIihpYwPxU3bCVI3SzWV9u9DYfT86kRzJNdSWZ+2VAFAAAKmC+WlgvqAAAAJlpoI5pbF/Y1Mjkvwn4XqL4veADvyAAPPF5gDb35HwXhQI

jkBfWOKCILt/mC4ccQvynMLgXnC48dr3W9SL4lPK4CeMOgnWLkJ5C9Qc32qXRL2J5q8txv2eXXXgl7q7mf9fxHeTh16a5DLmvGnxTtTjS//tDedKlTrB84Q9Y4ORX8rq0siEVjMutKqwuw7EMoAfvyX+gdV+i6YcsO2HcBi7+N+YU6vFvVD/V9k8WeTf9vDDnh9A70eWvGniXvAFAC5zqVJHkDnx1AGB/sutnYHG55BURyrKQvYX3pBF+i+chYvw

AbL4l/KcpfIvaXzL9l9y/heCvRoTAMPeK+2OyvubDPo46q+uPYX7jle/V8YCNffH9rohy17WdteNY2Xzr5S6ieUPiX9L0l4k+W8ROUno3l7xM8ZfvfDH033IEU9AmcunveL1b9U/W9OPcHjefB6z8Me7eHXB3tF0d6yQPuaeFNi7/0+u/DPbvoz+71M4EdPf0nHre7296NcffQfX3tl1a8Mf/elwQP6PCD+OcFIIfXvkpzD/kp3PWbf7p5/DrQ16

0wFIwxQ+xIJWGzhbfzwjQdgR/Y+Yv/TdHyE8x8i/sfuPvFFl5CcE+kfRPor6PdK/s81GFX6ezT+XZuP0+dXrxwH7XI73ln7Ps15z8t4de8X3Xvn22wF8LOkvvL/v9S4UoO/5nr3w1/k6MPff2X83xBxP9pci++XGDtb2+/V9bftfjT3Xx9+SGG+TvQG036M/N+DObvveu74L61cPfpn9v2lxk6d8z+9fn31l4U4u9Q/9H5uQH19mB8v+tHfvpD4h

+nrsOxw+BOnqqnCyHrxrOy/GiAIYebnk5xEc1Vt7KzAUAKhBek0ZokDv0FUrxbsCTCjsYfMViF/DMwmJr6hS6umMYgqYfyI2DnAoUIsbCKLVClD7A27i4KpQiap3SHmQatbRRoTMDFzc6O3IcaKKTblJ4tulljHYbWCAIkD5IFBPJ6DuinmbrHWa1qp7Gev5hnYae0WhoKO6k7np6OKwekIBxm7QIiZhyyJu0ComMovohOo5wEyRwYOJnJDvA6Fq

ugvAViIFB7uCAWDZlmnxoYEImRgUprUUXJrgDNA1YMwD6AEEA6pgmpgf7p+CBemthzARiD8CFWhCsVYNmbgRTrq2VOgxY060IIEHBBoQcoBke7VribKWiIo2A/UpwGQEW0zgKph5y4UK2C9U5wIcADqXHiwhqa62DQEOo5gvNbVuzsr6grWHAmtZa6M0mcbbWEgVIFiAvILIGW6idn24PGPbioEss7loNyvGmgTnYB6Lav5YGeUYEIBzyz1lPKNa

OxFMZMB67tmbPApUOha+QqxLsBRcrgVlKt2ENhWbHuq2BCCxBqpgkH92Weskr0+V2Ai48OzPm349ObbEoCoA2gMCHRk+Ok+480nwYITfB69q37yugIcCFWMJjuH6oqACj9pc2sfjiq0EN4N2JkYBshMJ4aEAKgHoBmAdgFc0afnzCQht4NCENesITv6ls8ISCHXkYIQh52ySHpraoeOCgJrwBJRlraiaOtuJq4etqnpiiYswC+D6B3FuHIFBvAK1

gfMsMO8D7yYwGsYKmI5psYhQ7wNmDXAFpgFAbmTUnnJOCTqP9bFyf8FpZlgonn0HieAwSoqiB0djVwdue1soEZq0wV+aemaniO7qBSwQ2pjcudqBb52wevQALu8FhYGGIKVlqzx6xwf9QOo6Fj9QfwLHn1RpWAXu4Eeek7l570wTwY2AvByQde6fowPJkhJE7DF3BtIEEHHy44hSHSCo4+gFkCOANMJvha4iOHkxWSm+E/SDKbkrvqUhIbMyFMM7

6t0A68ueHmHpMHDMyhFhubAYQugpYbfSEAFYemBWAPQDWG349YaWKNhtYurx76bYXjrIhSGv+7R+QHtza7cHzijps0+IdobSiuhrMLdhGSnKrwEu9P2EFhqAEOFmEI4WOHlhlYdOFBAR5HOE84DYYrBNhXfKEarhwOuAE/8KQdAFk66HrRYhuImsgGCYDQPqRCAMABQB7wOAV0Z8WlttKGrACXOAh12hwKBBaiFQeMAwsAnt8A/AkCMHalykLNx5

GIztpm4vAZmOqycBy6rVJAs62FmB209JEZZieYdo24bWkdtaEyeBIGIDEAnxLgATBfpo6HJ2SgQp4/m8wWoG26AFvbreWtirp552d1AXbvQVADsFoAoVrBamBi7nJCnAJ3LHIJBtgX8g2B2Zr9a+QvJFmDfWiiH9Kg2+FpEqUmCWt4EwWbOowoJagoSkoTAnYMQCJAfEMQCDACWqZCRBpokuqPBIUOmHxBjJusFvBMNOVYZSGtpBGVANQJ5HeRvk

YMAShFtiprShkCOhFIiCUEwE4Ryoc4BIiU1lYLiKa6KsQ6h2YAlxRo4UH6hOYTAnREdYvQdXKa6DpiIEeaYgbaG0inbvzBG6b5lMFiRKnhJGuhgZjJGaeckdp4KR2gUpGXSKkdCBpRxnlSQvWOkeAgBQEIJ/CGIqFlmZ7cv1tmAGmexNcEEKtwYRbBIIUauBphcQZGH+etkR8FN+DPi36b2dISWyAhwPBSpyqIgOQib47eheBsaygO3qUOgIWoCw

SCksLBqAQFJUiBA7OB+4vqjIaWyUOUDqFAs4AMQoCoA1YKJiygrBjMpsAjAAvyIMP0cUqd4gAEmEt4dkYnq0Rqq5WwoUKCGrKf4Yz4ISj0e35EOL0T2FvReuB9FjQX0RAD4xTKv9EAhKMUDG6wIMeLLgxIeAhLG+MMVYxwxbbAjFiSyMajHoxmMafQ4xufNzE7IxMUWFgaORqIZ2GVMUyHrhv7v/IoanNgjoYhvNliEkAxALiFJ+h4Y9AQA0EdxB

wRCEWSGkqn6LTEPRYPnCEoxr0Tni5h7MTkCcxqsZSi8x9IfzEuSJ4sGKgxjlLCrP0UMayrsasMSWzwxc/ojFyxaMRjFnqSsbvjv8msL9GoA6saTGW45MTrE8A1MQBHoKlnP65GqQbmBGYeEERkH1GnYDADNA4xNGZJUXzubauRKETsb6Y+YA7R+ok1kwEVBSQHEBOYWrIiLfUJUH1QTWziNJYruqxEzA3wdET0HjS7Ea8RtRgwfebDBfEemCCRwk

bMGiRn5inaTBI0QsGeWbxqIg6e00T6HKRwetsDqR6wXsHBQB6KsTbRyom3RmIpkdvL7BYNOGpS68YbZHHRlJke6d2oUc8ERR10WXoHYuOj0hPYkGuvwthcRo3iQqhEtSj6oQoHsiUohOCvy246yEQDog52A6zMoOYkDgSqmQHrg4gHsNShIKgeNYB84XJE2I5AfBtey/6XYTxZGGMCa37wJSEvXhIJAqigmFEaCRgnGE6qpSBCweCSYQrsRCSUSk

J/TNgAUJu+FQk54NCRwB0JHuKkbMJ+sQ85s2PQgB4vOEKMB67hoHpApfOWhin7wKWOlAnsJgeHAmjQ3CVSCo4HAMgmD8qCeglf2WCd8qiJqAOIkEJbAFIkkJ0cbInyJrkk04cJtCaOBqJj+hollxxRgaqlGMAeUaU6tcbyEJREgLMBiADQBJBCgEkNsGtWwXFKHdxtUgFAyhUaHXZ+oFQVGi1SXzEqRYRREcW4tU/alfBqWapl9KTxXQcmhjS6uu

aEcREnjwLcRHUTaFTSkgdIHjB1xsNHUsg0d0kOh/clJEF0Y0RoGeh48jNHTczikYABhkVvoh8e3OriwKsfnkqKckDiEYiUCXVAkH/xZJge7AyDwedFhRl0a8F3yKQckovgu+qLAc4npJUq7IrMdgyekIQLXgGAASMgCrKjyTXDPJ3ym8mKJ6RpSpfJAONaSThOQP8nIqvyBH6GxHNmiEmxkTHuFgeB4WjpmJJ4XxIeMYqu9ivJHKu8k+xDiX9h7I

UKQ0h/JPrkTrshAbrAGsm3IbEnJJ9cVybJQptqloUA5UulG4BVscm4qi2Uc4ghQ1AS6jgsFQVHK9URAt8C+o+8ocA6hfRqmHqmhiIiw+0dEdGHNRzmq1FmW7UbDStu4gQSBDJYwXvEuh4yYfHiRcgZJHPG7oVnbyRWgVSY6BQejCaaA64AYH9mwECYFiaaJh9ROeL8dqFV2rVDZ4qs28qDBXAVwLKkue6VtPTnJBQI5FuRzkb4FkgXJrKAwADQKi

Cog+gPqgdqAUUFH56oMhdEZhU2lPLRRtGLFGmqXMCknoASaSmlppGafkH4BG2DZhhQ9Jj/FLAdmjphDAEUF6itYIMIQJas7QeNb1JvkF6jow27t3ZfwbScabLxnSS1H9B68VaH9JvETwIGpMgaMnmpvbhMlsIUyWYrDuo0f+bjRXlpNG2p3odO6+hjqc4hrJD0tZC+ox3NlyvxtgqcRhhO0dvKECuYAyRlJ4aQmF2R4NidFRBuadcn5pl7uupZhB

2NULd+zfoi60hjMXLEoKqsM/QAA/JQ6UOR6s0AThEsDxCr223q/5BG7eg6xGg7ekjG7OgIdBkSM8GWpxnY2JOA4IZfMcgpEpxGR6y4AmECRJSwyGVkDCANPCBKqAkOIEDDiPEIjjh86DlbDxAusMzwwOoIc2SEZNGXBkesrGQ4AISE4c+HVhR5AxltIf4Szgdh+1KwnoAIGZi7L2XwXTG/BnsdRk0wMGYEAkZUsaWxIZKGaxnoZT0Zo5z+2GW/h4

ZozuJlGZxGSU5kZdoBRltsUGRJkmZdGUpnriUAMxmoZbGXdgcZl9kFLRifGWfSCZ6YjrD4ZJjmJkoxRGZJlM40mUzLg4k4VWEzhimZfa1eK9qpmaJeBI846JW4fok7hcfmoaKG2IZbHE2piYJhspxABylcpBGi7HAZqwnACgZ90eBkMx/wSHGGZnDK5leZbbBZksZaGXzyQZuzlA72ZuGRAD4ZCjs5kDZcGW5ncsnmWZnPRSWT5kIAsGX5m5ZI2c

Fm54gQGFnP03GULBRZXSDFnCZ8WfhmI4C2VbC0ZqWTxAyZGWfJnZZWSP5kqZamdCCIeNKclJlGoERVYa2kUWG4kKNVhIB2QFADAA7wu8GbboCGUXynSh5wPFDGIqUPMAMkqmDm4pQCkDMA/ArQaFBss6XH0bluoMG1jpySwKqlmh06RaGzpxNpHRbxi6aMHLpy0pundJToUfEiR0yZalzJHodnZehqwWYlzRTqVOj3xXaq3SxoqwFYhXReyb3SbR

P1kGmp66rKuiHRWeoAmHup0dEF5p4CQBkfpySvoBvhzAOrxtIqyrrk9I+uf+KFZfIMVloqHQIB5lZpseinGJ4HrArrBOKZ+jG5bIAbnoA0SWyG/Z8Sf9lxR4Ecyn8hEbhIDEAywI1aogowIQCGC3KUhF4Bw5jsaTAFwdu6NpIUDm6roXVgiyOoxmClCp5ZEYAixo/UliJJQbCt7Sqpv1CvFdJa8Vqkbx0ng+b05wyUan9Ra6aalDRq6XMGc5u6fM

k85iydfGzRtdE6ktWSgktHcAmkcYERWF6eZqvwSFu1qnBsuZu60eewKFA/MSuRlZRpTul4GxpHcZgJcmCwJoCEA+7L6hpU4QbxjZpUNpcmphf6ZrmIBTJncllWiSRurlpQmHvkH5JwEfnpRncZlEncYNF6hJ5YNCnmzm85tZiMwmeU6h/AaxBuamICXEFCWBptHNazmJobwCpqZQIIEuaXEc27zpdeVghLpIyUzljJB8YoGt5x8e3nqeXOdakHpK

wcOjHpN8aelPUwuQ1oR60eiFBEmJkbZ6mgdtOhZmmWYPmC+p1kSDZnJBFkAlq5v6WAmS51ole4D2n6Fpl5Zume7HIuNmagCAhcGp3j44MAAWKmZiccNlMZlmWNkYZbvkAbTZCAI5kEZCgPRrLZ5GXNkaFIcUoV/RTIYlkXYv0aspSFbsd1kex8hYoW5xKhWoWUZ5mVoWjZ4PuNm9ZCrl94GFRhfNkmFBccQBmFHmRYVWkyMdYWiZClO4UExeQfCm

IaBsbDq6JQCtuF25RiRADVZvKd87J+gmKHnh5kedHktZehhIBOFd0TIUuFchRNl9Z1hTMr2MXhUNk+FgWdoX+FuhSy5YZEADhmGFs2U5nhFmsaURRFdoDEVyMVhb9EJFN2SjHWF1KZAG0pVcTRYA5AecVaP5swLvB40LoMwASQCmrkmShdaUsCfMzMJ7TnAyUFaKQAYcB2l6YSlu1J/5YaU0FRqW5u1gxBsMOFBCeMAefEoFmqcIE15PEZgXvE2B

Y3kHWzeQQWTJeBRzkkFnedzk2pFBRNxUFfeaeks6Q+Y3TLRgYZYhdUccucA7JAafsnA0JUL6pvpvBbhYpBKuRckgJVySIW3J4he8GfoLyWHHKQcAEUo7IJMP+LUoasMfqekfSgJLOiChXMW/R9KojgW8WABkwPK2SPOGX0guMNC+F+2bKqhZHYOFknZLGkLCilHDJbgwAUsMKUGG4KS7hgxOyNgzWFsceDHoO5cBLBm4b2KEbQJDymD6rKDJbBJM

lLJZ3hslbSByW+JmuB+yvJG4k9hJFTKkKUcAIpdeG8QTShKUfhC4TAB1hspaxl/K7GYqXHZzGseJqlB9E9ialUANqVWwrMcLEGlajL9HGlOyKaUiw5pfAZWl7CTaUvY5uTDqbhChrblopuRYn6C2RRVPIu5B2PaW6wjpdkCslEYK6WFEnJR6XqqvJbfi+lJSs2SBlYpSGVcUYZVKURlMpR0V+FMZQqWcZEWTBqqlQZRqValAZTqXpKepVHEVIhpb

mV/KccRUgFllsFkqWl1BtaW3qxKAsW/8SxX9nVxqxUknrFLKe5GkAywJoA1AomJ2BkKpIQcXN6BSEOZdxrWHFCtgNQfSQlQTUhbSBQ0ln6ipQPzGDRd0TxbBjzAKQNfDERLHshaNRqoRtgRcg0g5hS6PxTOnV5c6TqmdRgyQzk4F7pszkfm4JRumQlW6aoGzJMJWQXjul8XalLJ0JjPJOpYrPfGj5bqePmepQuqsTbuSan6krAeJVvLz5mXDfDHc

cGKcn7uAheWYxphgT4FtWAIFyYcARgI3r4A6MYQDH5rnKfkd2Z0RfnUlQOdKJFpKxf7k2sj+RpVaVOlbWnx5rWH5AgVZVM2AQVyodFw2Y8wNiIWm4wKBAQFoUFAU1BzMLcUpWjUR0nIF9bkIFoF2qbTlearmsCUrpRBfgU+mbOfvFQlboaQVjuF8VNFsVvecsnVYTqXNx0FZnvojCWgirMaiVohTzaBp8+SjnTG3tGyxyVZJWvnJh5+TEHhRVVXR

i35EhW1louHWdpnwuemRBmBFVpICFGgRYHvoXlrfjMV78mwvQD2uknCJTt69GgUo0AosqpkU8ugD76CuVsO36LVFbO3qQanSu3pnY0Lp9l/6vVWXD9V0hVCFDVPWcs5jV+yHAS76U1ZBozVljLfzzVe1TaTX2B1XyARFq1Wdj0AG1bNUA+1TrtW72+1Q6SHVYPsdVrVZ1RWWW5qIdbl6JVfOVmYhYTPkW1ZPznAJvlH5V+U/l0whYlzC7WZ1m1FP

wcNUPVKMeNX/iJZTw4QaYPu9VzVC1T9WvsTOMtUA1J1etX4ZljGDU7VLNXmS/V0Nc3oqqXNQjVe5P2ecLLFXITXFARdcUHmZBMAElQUAfJgsBGAKJRHCw5H+fDk7G+wLuYncu5uQKQViwLCz+ooEBLnGIDAdx4pyAaEbTYRHWHgLk56qQ249JfmOgUkVAyUooJVuBW3nJVTlmalJV6VTukeWskfuksVOVUelrBM7pxUnACbsVUl2dJLGogw9gaJW

9Yc+Q4i5uDntMBZgK+ZGkKVFJUZXtVNyZmE9VfMFBKekDrJXiyELrNpLtl44SrBpiNNc9Xfs9NWWXEosGasrl11jg7hpiNdarC4AzJdkCo4Ddb9hN1k1aWWXlBSB3WpFxfBuHs2mReiG1l8fp86O5eGjoZQeZdd8qV1vdXOy11A9UUrD1VdWnwTVdNdXoM1L2NPW6qgERXHK2dKQklpBj5UgHPloORWl8QmADAD6osoF6SuK7+e6pvQCeVAUnc3t

OcGPo3ClYjxQViEiIBoLgilwbmhiH5C5gr8EFB/56wKRQIFSBXW5XmUVZJ7/FGBXTlYF5FSCV9y4nqzkB17OfRUzJB0qHXnxYZopF5VHFQVUnA9CvHUrRVwO1iHAa4Lem90NwAlarGOeUYgnJNkfwX2RquT+lXyGuZ1XmVyNhAC1ggbP2JTMO5MLiCqqABXo54SjA4xNF/GRNU5iDQhwlbVP/sfXcqAsHeDalmkN0hnq4iXCnghn6LI0Xs8jV4mK

NrSio2bl33Oo1CZucVo3/iOjTzx6NfNYY21KxjVYz8c2ks7AWNhAOiBWNv7lIaIpGRaVlo1ORcvX7h+HDbH6ezZXzC2NOyBhIKNygEo0GEqjekZuN9hckX4wksNo1AhPjYHj6NXOGPVmwJjRuVmNoTWInhNCAJE3IF32YsU+5IEfeWWVctYHnhumQbyA8ABgGOCygRgAFyupqlQ5X0Chlv6hWIewHbQ7ccEBcQ1UxwClAwVRwDqErAheblwO1nxc

miTpEVVg2oFODcRWxVbbiMEN5iVeQ0s566U2h0V1atumnx1DcsG85lBVHUnpMdRiDnpAlRNoWeIaSwVvxuySoY1VDiGMCXBN6bnUAyX6YIViN5ohI00lgGaXVsQ6Rsd530bAJgDqqghvsi1IJ2P3WMA52EvqI4ujVaSxC7et+HUoI4Bi3jIt9OTG3YS+mdiV1kzLzFVNX2OsJktTklbCUtLyEPWiG2SIWQMtDuEy0QAIOgsK3YXLX0pYttKIcib4

ykPi10tcBkS0+NJLT/T/wHLWi1UtB9by0UxArY4yQGRLX41stqrSfgUt6Ldy00t+jHy1vkOrUK2I12iVblkUi9cMKVZK9ZikQezuRvXItkPKi3it3ypK0HIuLbK0SJhLR8hKthreS2FEXLdS1dMK+Nq0rsurcy0GtpLUa29IJrRq08ttLVHhWtcbTa0S1HTVLV3lFlaWlMpT5QrX1G+qLZBjgVQBwA8AuAO0a/l2tR6r8pbtBibANwSutiQIumg6

hxQLMI/BLmLgnUmGK2UZiJfUnDTcTjparGxGV5Y1NTlbWcVRc2GpVzWlUkNtzZ1yB1FDR3kh1e6TQ0TuuVYiX5VlQE6nlFqJVKIlVLtDfAvATgkcGsFvQuJU5mJwU4iTW1wJC2zqIjQXXq5l+ZI3dVdJWLYL8zKCMgawzZLijpGGPKMAXKbetYy46r2mD4BZUAE7hqAIzA0IKALLVwkA8PQFnBGeKJBpkpKv7cpmuwgHSEkgdYHQwkpIkHXAlHqs

Hfihpl1jIh3Idtiah3b4GHVonwcP8tDpI1RsSikx+S9c61JNeIVimpNHrRIAM4JTbh0AdClEB2Q8hHZUrEdPRYwBQdL2DB1wdVHSkg0dfjXR1xl6HdeUYKt5b7ndNRbdUby1/TfUZ8QSVGwAugmADUCog7cVrV/1SoL7ZeodmPVIfwoEKRRYkYUH5Deog0hcDHJ/dHnkNoVUWPFGILwKTkB2Kus7LhVmDaHZV5fxac26p41N7WUV9zdRUpVZDUu0

PNDFVQ1btLzT3l7tDDQe0nAdbce2meCdfojOBa4PSZXtb8aXnp1vyLsBTAiLMGjvpACS1X3BlJcZUdVrwfWYQJeFskoMlcbTvVmNujSnzMAl9Zh3PuEgL13b1v2H3WDdoEsN22tkfiVnVl8TVx182CfhoZ1ZTZQJ22qW9T3VTdu9eU21iQ3SN1tNrIZLVYK0tXAGy1Zac/XeyZCsQC7wSVGQrLAxAM1kTNbCf+XIRn+XfBXw1mu8AvSu8rpqjY1Q

X1bcFcrM1K+d4IGFzRh+XOaZqWbJAgUzWKmH8CroBpvKEjGFeZTndJloTTmxdZFZc0+1a7Tc0t5EJb7VB1TzZl0LJvlu83UFMdTkmFdIVvGZaRHqeYGwY+ZnbQvA7Wq2nAt+JYNhPS6co1VCN8la+3RpG+cpVxpkzWL3eymgO/T1WHACcBVAfQFmngmQheI0ftHXbyEl1WeiWlCaj+dL2y98vXrRb5Sbo21ZRcQDly+QSULiISWS6JcBdW6UA3Yl

UYLfjmMBaEXHIxycaB8XjtS7s7XYNvSe7VnNeqfXkLtBPdc1Jd/tYQXXN6doxWbtXeXCWvNCJdT1IlMdT/WLRaJbsGt0pAq/B2gALXekZcD6SC0/yGrClAQIslYL3NV+ddlatdRdf+liFiLd+0k1fVWTW3VuOrQ5QO8QCDXQUB9tezrCH1UnxfVu9vNUAA1HJDXZNgCjFd1ueI6SrkjpCRmAhOxZjE8As/SjHz9Z6g4Z4oS/cgpLCFSEEBhAx3ep

ljdmmaTUDVYGTw6t9c/u32j9nfkYzpCzNe35D9I/XYUT9mSFP3XsM/bMW448RrwAb9K/ULBr9V2Bv3xCcjTv1bZ83UikL1qKU62rdREFjWr16Og0b3dj3c92vdItuSFFCjfcf1dZp/fa5t9HfcjBd9YbD3239A/agDD97fY/3fKz/dP3f9n/Yv3v9P/Qgbr97/YAN2NwA3v1fZp3Xm3ndBbTLUPlvTSW2GdXJnACOoF4KiCkAswIqC/1xvf/V2dJ

plcBBQ42rV2O2jMBA3MwKwNnUo9Gptx7p5zYFmDSVj6P3F0RGMD73HNfvTFW49XtYQ2LtxqX7XKeJPYT1R9GXbH3kF8fYST0ND1ugBOpHaiw0YlqMKFCOVGlu1o8F3PRJUOIaInvJiVz7e55t2rVVX1zNuYOjB92X7VvSfoiOI6QNCtDAQBDKDjEN3nYoXquGhe6qhAaI45MQyVPVR9YvYQ4TMqwb+ljpLUObVn1fa7397fWEWz6usJl48A29paR

EDosiQMj9LQzkOZeowJ0O9I3Q1DWdOqmfyUONygLrCjAqQ3UMKUa4pkgc4PuNDw7IbcKDgGEAruQzpD/dfSBjI4vGQw24Kib0BUqVjJgzOAzgM2T4g+IKjGuwaQ3zW0M0ZrgDogusNGZn0vZDKUqNvic2QAQXJDShMAisGkM88tDDkN/9ghKdVvkuvFoArMK7BQAKULYtDxxOuEBUpb93/kTyuS+gDUPzDvfVkL991sCiAawwvCWR6U7er4lyAeG

XNmjDrNVJx/VY9WKjDQFI10N816ZALXfkS1ZobcQMkIDV7IEw6gCAACYReJWuG2XP0cw46SrKqQzsOZD9jCBIC84uHkM1FghAUN9KEBqIalDE1WmIVDw0FUNqAWI46T1DffY0O9DzQ5w6AhAw0X4dDXQw0N39Ro2aQmjKMWaNXYGXkMOWjBo99WC1bNcDVmkgIfaQzDooyOU9hSw5IArDpNJ3jrDieLvRQpQI6oy0MykHsP1w1uIK2FExPiGJGgZ

wy4AXDVwzcO1gGsPcPbVjw88O74bw10gfD6SM0DfDClL8NiA/w6QCAjOw6CNNOEIzHhQjmgDCMOscIz6KIjdIMiNmlcjXzUKJQIJiPNktQ3qOzVVo7vbqABI3C7EjuIOzXssFoJAYg1B3biOsj5bMLV0jZYYyMjDzIxDVlsQtbON4APCFADcjZ1VaQCj62nGMSMoo6AOxNS3ZRTo1ZsXiqwD2KVt0QAEo8CMxiWQzKMPYco8F75DEXsqOWGqo85J

lDGo7C6VDyiNUNDj2I90NNDto/Q6mjs3U04ZeFoyMNjjPQ6QNwTVDghOyjSE86OoTro5DXUjIlJ6OTDPoyBB+jCwwGMqMwY/zQVIYY5sORjOw7GO6MysAmO7IyY6cOAdGYwpTXDtwzmMst+Yy8OoARYx/JD1VsGWNsAPw+GBVjT1bWPvj9Y+/KNjuIM2Otj6sCm0HinY2UgojlHBoTbV/Y5kC6j+o8uPt+E467BEjv5KSPzjm40uO88eI2MPt664

wyOzZlI9uMrje4+3oHjXI2LW8jZ40KPGZhhRwDDjmnTyEchgboW1CapldrYCD7kbKALACsJ2BwAswLGaSD5HqhFZc7HisD5cvJDm6XAcUOtzOIU+Z1UlulAfUHMwq6I7WLW7SRTkaphFdF049pFRYP49CXaT3LtxPbRUtTaXZQ2XWWnuHWHpfOfp4C5JwKHreD6yUqDGYPtA1F+ps5hu5jq62C8DdUf8WX03BzXcAmF1VxF2kiVWuTdGfoE/Vk1T

DSjRwnYMvXRERMAbAxdWb1npHtP2kB04HhHT3yidOkAbA5IbUSKIex0o1WRTWWQD9FOt041kHsTUvu3yldOONkRDYzHTGuKdOadN9Sh531fuXp3mqfTSDneySIqJgYgF4LyD4AZqDHkfdceYBWXw6wC1rvAFxTlw5TjYNHJnEkuqUEJBE1vmD5QjMAzCtgHWMaF7MJU2wFdpq4FhGkUBFVTlEV9U57XxVlgyH2pdYfbYPtT9g+dbR9iwcxXZVfU2

8385/efL0upmtWPnaRPg4qzi5U5mhZTT2Jp/GSVWorail9fBUL3QtilaL2GB4vXklqV7kfgCJAY4DbM8Uvwkr2lAq0++1rgkuqRHkWhaUkPFp9+dd2ltXJtbO2zaeBiBBW9bTZ0qiemCCIEzdUmCLW9UOp6hAsUemCyrAPUowGgQqcr8zBhgXXs0bG1Uy7XY9s7ec36pAs81OE9ws5tKpV1g2T3SRTFVlW0NV8Tl3uDsNPL11aI0xPlBqX+XaDvS

fqVw13tJFCBUazAvYbPl9wvZ55tVVxOe1NUXXfcnY6EEjgOUOMEzaPzzaEx96mThI+nzTjRZO3ojgBgKEX6OExVSPujNI8LU1A3I56Pzzrk26Nsjf1bqjHjSMsaDRAZ1UvMETu42zXt6GIKfMFZk7DzQSuTOGQNtsC8xhNPzxkyNVUOq81OMWT2ejvODFanPvNoT9kykofz+8xfOETh8+yM3zYtXfOJgD84uMlsB81fPC1781zWej141WXGxnHV9

OY1FsQUUbdEgMjOoz6M5jMVFp4Y/Kzz5/bAvPzsE0Au2T8haWxgL5kySOQL+gLvPQ+XC505uTr8wgtELOC1aQstLI5fOrjs4+gvw1mC3urC40izZNiL8i+5O80iC5DN+ut9Rd0MpV3cW1P1fs+5EUAFAHADi8Y4NWBFVoc1IO2dwIg6itBN8HXb0kObscDMB38BcWtSTJBubTAP+dFxhQlwMYhDSdERg3QgkVSYNu1Zgw1P8zTU3ZaJdSnuXMpdl

c+u3QlMfbCXOD2XYn37tEgE6lqQ3zSz0BCQxnKw/U7Wj3O/WiVvNYmYO3E1XLTFfaPNV9VxFcDDGmvckMHYN82i07zHAO/NxONjpRBW6WHV0vbzQi70toAbJbWz7gM9V0Jz1i3WQvZFK3d9MmJv0+63/TEgCMu+JYy30uTLgy3otQBcSV03hTlVpFN8h0Uy/XQgJndWCogJwPQAp9b3YcUOVg6SlA2azWk2CLNSoL55I9XlY6itB8ahuYJy25q1h

MwhwGlCGmezAc0Rdq8dO08zBc4H0ENCS1259RoJSak0VdzR1MOD3UxNG9T8Ja4MNzoojHXJTqfSe3FdAdOqaK6Pcw2Afxj6fPnfAgNjBWDzpJQ0sjzMQ2tOTWJVM1rtLm6pvWKwGILni7Lj2IjgCQWQPoDh8bSDo1+NmSCDG6N2DI4C5ajMqQYlhrQ+djRsG+jni8QbAGmOyLO4/AtKLp1SovYLl/URM7kyqwKtONTrECF+NQ3WquOjZq8QDb2eT

c5KwSvXXytq4wIDjEsJB/RABQSvK/ysRgUy5EUcAwq5kBirRkpavbVueNKs+Nsqx2BK4n4Eqv1jq4aXiarzZNqviLR84ou3zWQFgtqLRq6gsmrOQ3asGEFq8h0OjghBl52rDq841Lgzq98qur0gTYaJ4JC/PVxNd4wk3cdGKck18dm3essVpQY6gB8rmSHatCr5MKKteN4awY1SrEcTKu9Icq3GuKro4cqtC8Co99warWq8gsvzGa+3p6reyAau5

rzZFDWmr/q4MvFrDuKWuITmXpWuOrNayoyek9a2ICNrhRhwNJJoU/SlNmxi/p0IzOHhcuJAXpJ2C+oGIKiCkeKU/kn0kbtMxFnANHj9S9UABUqCTWDaROrfSfwCnWIV1UO8BLEwDeAircnQaqmTtmPVF3RVuDR7ULpCK8H0lzofckv9uKWGLOPN1c5ktSzdc7u25LuXfksnAEFsStFdOkTWYncFwFMAKsVwAlZowPtDKGRDl3I0usrLs2woSppy1

yvhCq4oUTRmY0PbBvDyiDXBljqAGpCqkuOFwBfz/+lbCKb5EDXAqbQQF8MabWmy6A6bHQhTSsddrcjUOtEAxhqJNna7x1ut69b2sQAFvAZtRARm0TZqbDuJpuP4Fm/svadRyzwM9Nvs+cveysoFUAIAuqJgCSYSVBKK/lPKcTbSDTmChWjmBxJLoc9yoS4hu0TmOwqhp45nA3gI/UnGqfwNwIYhnAdEfTC1SrWA+1/dP1C2nGDvxYRsxdcS/O2M5

5G0LOUbMwWkudTG7ZLO1zO7ZHVyzp6SHP09HoLxVbc/FcUuKshM06i2oseoZE6z6omUFIi+YIyvN2w88bOeB7QE5FG9fge5GaA9AHxAugkmFACjAc8o7NgAzs7+mINHxSXqddW07aLa9lVrr2nb525dt09Ss/Gl1pUPcbTOIugz9Q5bbadVARQI8YDaGa0wOYIe29Se1h5ypbn1bAsrSeEu5zvvTEtEbAfXF3FziSx1NlzVG8zmYro7j1PSzuK3d

YDT8s09YcbC3Ke0kU7UrlPJQa7rXZmYEUMYjasS00dErTKveaLOBhAtMDlgU80BkAu/5KvNtsxMcwCogNMjdi76ujV2MCgUuObAsttuP5nIdJbMTEm82DHxBjgQoBgE67LGqQD443uH0jCG16hY6i7jyO2Pq7wsFLtyAMYjXBy7Wk4rtlwyu4XCq7BrVaQa7iI9ru670ZvruNKRuzWFliIxdMtWbKKnMv2tFfIssULowjAOutTud6sxbcWwltJbR

Nf86VAhZPiNqTpbBLu27Muw7s+N8uzXClwQsK7v0ZuWWrue7Y/Frs67eu+gkB7uLY7z0awW502q2xy4DkFpUApFuCYygHBGaAPABBAcAb+fYupTBtX5CqDFpt1QLm5AUqBOozAYzDG0ewGBVW1gCFYj7AvaaYjLEawMSWhdKaujvRL2aljvmD8S2Rt47pc71vOhTecQUZVNc6TuMbo25TunpRdq3M/NsaFMCBQ+fbn2rRZwem4ncewFtuuezK7tu

V9bK7mDsNAm0LtItEgBavl7/4sh3MTwQDdiZtMeBgbv4iI4ijhgokDdiH1AYheyI4ddZbg5idIIge6wO9ZOPRAmcMHxVDLLasowH7uxGsIHu+Ja0oHHY5QcYHwYEwc4HMBDsgEHT2EQccAJB0fVgLFB9gzgTVsDQczL9zkVm2bb0/ZvkLjmx2sO58e2vXHhL43QcV7fjYwdIHFRLiCoH1e70jsHWBybtf4uBzwf71IuHwdxOgh2QeuwIh70hiHE6

w8jBTTKa+v31jKZ+v8DiM4JhNGEULgBqQtBSPugbg6emEBQN8GV2azYO7wD0w6Iv3HGIYNPpZM7EPWwUfM8RytxJAlwMcBS6CBeF2RLRza1snNvMyRtAluO0iv7WxDUT1orq7ZH3izjg1ks4rLgxTu6Bp6fO4v7c2ybRLAzWtStvxXc1Lm9zckHmBMR46qJuJh0Qy12F1fO6cAAssm9I29dFAK/pWw105bgSMnudY0tlvrfMf7TSx8/QrHUTS9MR

7dm1HufTCh1AM8d1sd2t/T6e+N3rHmRgsfAz/kzscndhOpwOVx3A5d28DPIZ4ffr3srMiiYJpCOCIR2MwUVpb+mJ1K1dJpszCceguk1tc6LaaQJOdexgCvZRoUFMZqYLy+tiYVyQF8wg78DUsCQiLW7VNtbhR4CX4g8XWfsUbCgcl0R9qXcTtWpw26xUP7TRzHVCgisypWJmKs6NPAwGbucDwNX1its0r6ojbTfSv8MMefpHgSL37bm+dZ1JuXJh

BAWbuqBMAYg1YNgE3bd21fITHug6RRYelFl7Pt76QWYsXLspxwDynip4TW/bEvV914zbWEvt6mKejm4mI/kDiJTGTYOD2obIEOhvFUMcqBBHAY7Y1HfFUS/kemDR+x1tFziK71FlHVagTt9bV+0oLpdWK2HVk7DR1O7Mbjc06n7Fk2+n3meeYN7RVJzO9V1bcoUCUmElIp+SUgH0QeqdzN0x4Aqetn4HPP/zy81ntrzGsBvOzjZIwuPtsSC9tVyL

hDg2fgLAi62dZIygJnB4Z7Z6It2Txq8fOIL5852c6r455msYL2a6ovi1qx79qGGX3n/Ols3Q8AA9n/CzOOWT5I7Nkjn/8xutbnfC+vMQL/Z3YfDnCWXWfPz8CyfNSLHZz/5dnm62gtZr987mvNr8yxx3R7xx+bE4h2NY2XjdzQL8chk/x87GVFb8qudAG657gv1np502fnnVkwefXnG58efbnZ532fzjA50OfIX7C8Asvnf1fedrVZ80efTn6a6+

fzn750ucshTxzeWt7aHrp0RTne7UY3dgmNGZGA9AKM3DAKafZW4zylk4IC778D6g5uTgnnInmHmTbQdtSR61T6YyFptinApxeVNO1GPTVPczdU3Cs47oZwnRUVF+xXPRnVcxLNnxWXVT1jbMdcBs076JRyc4En1FwWuCvRxBi9Hv1t52gFOopzvK53O7C1VmzgRW6WRlZ4F4bLaABeeDn4YKspdLQV5nCfnkezbnLdMe2t0rLgF2suXH6AGFdYXd

hy3v5tOnbqeP1Xe14eVARIHvnq1uqPoC8XFp/JCaifyIlbqhF7oLpsBEaHgJgiJQQcQ6hymEBVDGyDXjkJBCBZCu5HkXTCvqXQwXO0hnp+6Uc6XFJ+H12D1R7RuGXzzZT10N+KwFanpLcxZcZnl6SZjgsJ3DPn2e8Q8A1VdJJdttAHYp00vjHUDRibxWkB/X0Z7/5LnvS7Nk3nGCjcY9gyu7mew4fId113bu6NxMeeO6M2DNWBjgaVM0COHkgPq0

RrfSg6zhAHAPWIfsk417uUHxpNmsm7ze7psHYme29e6wH1/dffXW49tWFe/5C9d+NqN7defXfkz9d/XAN67vIdoN2wDg3kNz2cw32DHDecHpuzkaRXBx9FdtrSy4+PKHR4XdRpNl1ygQE36N19ekpT17jdajEE69c27N14LfE3vSL9f/XgN8DcGNlN9TdQ3rsHTe9IDN9gdM3pROldcDmV2Ftwzmtp8e627kUKAwAywHxAnAnYEYBCRIG/9tm9ln

nhFJArtLHMgQ5dglxL7wBWjCV2rpx2mdUXzD1TZzcG/idqXhJxpd49w12GejX3puNeizk17Gck72Kwmc5Lpl4w2ygRS41oaYH8HpFdHufYkeOXX8ZcEbgRcsWceXwUWWeLAPWpjB+X705UBoOHBDBhI3fMPXd1sjd2Hssdr08invTjrb+ec3Xa65uqH7my3cnYuty8f63bx+FsmLOV18eCYJwGIO8gDQFTd9mZp+93imOM193pbSIsEoCXbOwx5b

cmUypi1BlpmBsFRrp2FEMR01g1RRoxUY1HrA25vKRIiVpguYJBXM1j0ztA14XNB9XW2Sc9bY1yLPorNGwne0nd+yNv9TjJ4w3L3W6cPkaRjPcrPM9ewYroJQ0XHFYVdPPbaDYRvy+mZ7XgB1zvibhQKbMPLcOVyaSY+qPgDDARgDUCPMelYFHK9nlyRZzNcoWMAyb51zFE+zHsqxeVAJD2Q8UPVD3bcOVYXFvdedc1rvf/M6wDCyQbTiMEt6Y2YC

nPkR+wPUGLGEIGjAhd+IsJ777AZ5jvtbfM51sUVP9/1uRnl+yisxnXU4nfxn9+2A8OpMdYwvpncCnsFfw5tdZ5fW006tvAQj7YZrl52DxGlQth1xJugyDD+uAqpLD9yt13X7LBDWZ7fgiGYTfWSMin890Llk5ibq42sqleBx8ihPisGDe6waMQDen0YvIrD5GY+uoSwqmWKwfhgRLWk8bIZYabioAuqKJjNAEkNreW41ibDVDLXq8Pfe44T7vaRP

LQzE9Z+wpOKtX47q7vimHQcak8N36T1TeZPtT1jG5PzhqgaFPXysU8IjQ56M+t3isPSNjIvSDU91PDTyDNHVJus9Ph76RaQvfnRx0jpOb6AHHv93Ce3PezAC90vc8gvNxIBtPYTwEVAhwIVE/rZLGrE+yI8TwM9JPwzzYXPP4z7vhZP0zxHh5PhRHYbzPWezwglPClEC8VPt9GchbP9T+/pNPkKqPcGLrx0YvvHU9yxf6n3sggBjgatWIMwA7G4Q

8pbQR/I/rYv8HVLL5yoQ702YH8M6jjm+6LI+r762PFD9q64PA1OojxbvtjwbiCpd5z795vGDXX97o8jXSS3/cpLVJ/1s0nmVSA/0nFj+sGDTyA1A9p9MD2bNhW7qfyE/N40z9SHJbJLYFA21VWg+KsBxPMAbbpd3g9KV2r1KdHbFy6QBJUzQLyAQQEEA0BpwKpzzteXALOAgGhzDy9t4Wb2/FEcPPFi69uvHr1Z0uRYc6hFTWNLwlBJWEagy+eLT

L4SZO9bLxAW7AV8BiZedvno1ERLr9wRsFH4d41OR32l9K8x3/91UfUnNR3Gfbtyr7LOP7MddgAZ3EevEEmapr7txvxlS1/FZnKxFg/A2TK7g8srYxxXdLAmUxVRBPcm5BesLX3inH/zaTx08EXwtXIkfK84NZOwXt57OckX7/T6P0qgIWu/WAG72P2oAoUKeMUxsWcTyPIsL12PCARPC0/fzUF0EYLvG50u+vP8C0e/BgcAJu8yLcCzu+4D3ozuT

yA7/V+8nvgIee/8jl7++KmTt76zxu43vCzeyHhxzFe93se1QsAXKTRnvEvRgKS/kvKA61krnc70AavvuC+++0On7yQzfvv7xotjn+aw6S7vp7/u+gfVH+B8oxkHwKNQvBkgUTFPd7wh+h7NFxAF0XGV6FsT3ht6cuP5QoIkBpUlADUDDA5l4Q8Nt0g4Yh5ypVNht6YGIv8zAINmCFD5gHmcbRw75ESCfX3TiCtyo7lU8aZq6hzb1fHGsKx/fwrxR

1pfdu+j7pepL+l+ks379G3ScR1Kr9HWMNrliZ607pK6cQcK4CHp++KG13mc9qNUdCxg0Nr6O+qnvO07d87Nd3aKmwkbBLw/+yvFBDdsIkhOGcgMAF6SkAdEHcLGcRX/gBPsq5FeD5fNY031Uhd1a4UNFnDuz6dmnw7EKZf1TsUg1fhX8V8TFfTuECtfYQKM6bC4w9gNz+JFwo6yL6ZGf0vY03xMUoXn3iaTVf+ODWOiLj59U7Tf9rh1+Cuh4GV+9

feF7zzrfgrpt9aLEi7qgwEd2DIxIgC/NqqRFzk/PPkf5F39WBAV36vwAqAxSDWmQqyu6zbf2X2pRdfK3z18lfu3yDjlflX9ezLfBX3V8hsDX/UUgLEnPgODfu1ZjxPnAPwV9g/p/gN8v4AU5N+38o3+35QOE35w5Tf0LmN+zfj8zAtJxYbJD+rfN5+EZTnT5yd+722326wGkYPwd+s4DPxt+k/p31usQA5390wvfWB0AyIqd3+otAvy7/AtC/4QG

9+kYwpJuNffkhzE1yGzzh9OofZz4odjCXN8+PubP31LAPIf37l9o/NY+V+YU3bGD/LOVXwxCA/0P5uyw/TXjwuouZcCUhI/6wiz/G/QP31+feSP8N94/wNWN9feRP/Q4k/M3yc4U/gHBMVW/3X2t9c/x3zz/M/+vzt9s/+3zH+kXjP/H8rviixd/S/138spi/+849+8/7Izn+y/JyB9/xZmL9DOGL767i8eHpi93uVAnYMoA1AhWqINC5gR3Wnp5

hAscBdSBVh8v/UlnikCqWK6HpFjWmzcpY2aoLKsTAN8BSizqPBJ/ql/AE5qW8n7391K/47rn3K/ufA2xktDbSrz59Nv4D3l3E2vUCSsrRYG8lBr7ud73R2XwQ30eoNxcksCN2njx+klnR1xXcVuIaWyxSNVZxIB44TSAEg98IHtq/PSpfvrAwcvsZw8voD9TfqV9Qfr18RyrV9tvjsgPfuV9ndlR0nDGeoJyA3hdfCD9uoOV9B9PGJPSLeIWUA3g

4EuTFt1tn8P6ML8bvnTg7vojhkIJ+Mphiq0S/tCky/u3pQspyAasomBukKxkGkCf8sOv/856EADqDEpRQAYn9DfpACUAcV8zfnt8KvggDFYEgCmeNb90fsV80AQQDMYlgCp9IgDk/vgB1AX0piAZoDOEuQD+fpQDXvjQDRiq+MOAAwDpRkwCYaq99WAZNh2AYdlOAYIdnYLwDLYEh8u7nIcfzhr8Tjs5szjgPcebi+NBAUaJhAbvpRAXGRxAeAD/

vsoCTftIDYAXgD4AQsNEAYn9kAbECgfmoCOABgC3+HLItAQoCdAXoCPEupJDAWQD9GBQDBflQCZfuYD0wLzFrAQ4x7SMwDKgWXARlE4CEAIOcNcK4CVYO4CsgJX9gIm3sDbkxcPZtPcTbhcsvSLMAGgHxBVtBpUSrjrU3OrVIP4L5A/UI2lYNmWAMIlfBT3OMAOqBZ4NzBcALNP9ZVMJFw8IvD0BqH1Qi3n1cJAkv8SoCv8dHkQ0Izpv8JrrW8pr

rUcGNqA9D/pY9GGpK8HmtA8H4hHpNsKOY09PZdcoGcF8zCsRqrkWZh3u5c8Hol9fXjKxaPN/8dTtI1xbJTZeAKsokQRjYCWLsdv3DZsFulFdUauzdYri60rniocgge5s0QULAMQY8chPlp16LpyExPoMDr8vi8G/hIAJILZB36D6QfgMyc+HrjNWFHbQPOisBwKmyw4IINYPmIWcPehcBfIDqFatl8Ab4Elwl/kHdvesK8MdofstHkUcSTiUco7p

W8jrJScHgfK863qY8G3gf8E+qnc8uv6FWjgg8OPHjk4vqnVb2rtE1sF/khXi/8mulCCfXvQ9xgHTM+rKl9klHr8svtECjfukCYAbgCqQBb8iHIvZ3fv6CkgRuc0JsDVY/qvYM/iz9AwUBsU/nT9uFnf0jvrGCKPrOdygXAwmgSL9bvjR8Jfh+9Mwc3p7AS0D7vteRvvhl8ogeoAIASDgoASoDgfjoDwfjV4wwd18MfsmDNFgP00wUz8UftU4Ewez

9Rzo0MuwRn9dVqYDqAXn98wYX8UFvgtZxiwDSwZ99PAar8e7r4Dllk+N+Orr9KwT6DqwTEDWwfEC+wb19LfrC4WwdACIwVu98LtGC0/tz9aHPGDGwRz88RueDULp2duwSOCKgWYDxwWWC33mM9JfkWDZwe98Ffr0DDlv0C6QSctmLsDkZ7pUBZgPqhdUAOAlgEe0V7o8tAKqqFlTGpZ7aNVtlQmw0vFqmErXshCdgTfBPKlGgLgE1txdJpYTgXht

VLm/cvapcCuLGK9P7qRs1/hqCN/jK9Cdvc0FXrfsk7uY83gaq95ZmpFlrrY8M+kF07MAWBu5sa8XHkugiAtycULI11hGsAd3/n49fKpOYNmtO9pGrTg62Jbw0bJTZVlMpD7YGSDmbDkdKyi2tbxoMJ21n4ClDkSDubpdJHnjqh5ONpDc2sJ89bqJ8cXpPc6/sMCBQhcsYALh8hAF6QPsOKEO/lM18Io+g3QdFZnPJEcrgNlF5gMEpBUuYI/4BNYf

qJUlKtvTAs5l70k7mcDbPv1dqIQ581QU59kVuUcDHnpcjHgZdngd58ZZkaDm3ow0FojY8fgeZ5Wgr1RIvoCCgENf97/g50fUAhUh3vtcR3tJDfHmqc5IbsDEhrSUOlhxRKfGACtwX6CdwQ2Dzfr196VP19mwYn86wXEC5Abs4pvleDpoXuCKvl78ZFsyNXnpXpZvlmDLvmODRfjR8Pwas8vwfR8ZwTmCHAfL9nJhWCBoVWDJADWC0yFIDRobICWc

BNCGHFNDUfuGC5oZN91oYtCnzstD1Fg+DGfrQ5NoSc5toSX9qgfn9hvpODM/nYDhfmdCegBSMFwa2tDIRzd+bKuCe1kld/qldDNwTdDtwceCHoXACKvs9DQfK9DOvu9DVoYDdl3teCxoStDhvl9D7XEDDA/CDCcwWDD9oWR9PwYWDjodDCZfrDDy/v+DrOOPcHIeJ8QIdh4Rgd7I+ILMhbIJ2BZgBBBDeg69QNmhEUuN6gGqIvlXbk5hs3hO8vOl

pg1ops1JgAVB6ti1ox0kvF5/qHcS3vZ9NLuW9nPtv8coW588oR59g6nv82Ia8DioUf9WNnfEeIRVDrID/ACIanovrOhZpgH2lmoeCDWoZCCEvi6DVsGbUU9OlBPQTtMnVsEkX+FyAqxuHwdcIDB1JuSguGPSoFofa54LrvQIFgL9swa+C9oWWCM4e356YeD5GYfnC8wRdCm7gDMb1rsg44ZdpOWlLB1eMa0clIfR9YOnDaYSZNLdr2ddziYCXwbt

CK4SDUi4bvYS4Vn8+4VUC3wZ/N27mkUmOmANEYUoYjISuDtfmuD0YV3VYJNSg64X8NE4U3CU4Q/o24YrcNvrQ4s4c2cy4f3DaAZuMh4U04yDFtDe4XnDT4RYDJ4YJ9r6vosq/ti8a/o5D4ZsbcXId7IwoKJgqgCcACZNxDFPrG8djDCxvaDnlOGvSQwKhbQ5gGFA85BpY1TO0d+0rIJFgMwFwhlMAxgKAhZ/qNIjYeRDUobXl8Go59zYVlC7gYxC

ozjbCd/p597YWY9HYXitkzgStGGqskzQa3Q5dBYJ8uD7CovjgRJzB6cOdkPMDrkmEx3rJCAbBtEEbHX0+oYlFl+ECBFYEzIykDLBmUJkhRYnvgtABR1fWBHgLtFyQzplh1T7LwYEAFIjlEDIj7YHIjXJHwwACJoBlERvCxAE9Mv3AilO7uAN5DsuC+7i5sncm5t0YVojKkLojtkLIi2kPIjljrdhX6GYjVEZLwLEbzDXDrDN6QUVZ6/rlcNlkIAk

qIQB1gMhkZgSb0CAo0kZrHMBeqOe5+/me8H4OnMYKgGg8coZ9AEEcARdGpZXEGy93ZgK8HLtZ9oVilCw7qbCI7nRCK3gxCq3rK8dQdv8WIV599/kVDaEcaD8lhcA23uZ5LiLcVb/ma9uGp/sQhr8hHMDcBnEM/8WoTg9g4e1CBEZ1DOqIQI/KopDf/n2tPSMh0MtLvgO+LvBhAG0gBIDV4yFHAZO6t8pNkRM93uPoxdkSIBUAAciHsKgAjkb3pPA

bYifASoZ7clr9TITr8V4aci/GlsjdYDsi9kTcjYXA8jRIMEiYZoxdgIUMDGQZEj0AO/QeAPQBbIBJAIIL9cATmvcgTo4tZQoa8UoPVskgC50tiFbRDMKUsVTJVEudDy8lUoQJ1YcRDRpEcAh/lMZ8IaZ9iIiHdcETUi0oWbD6kRbDyEVbCt/uQi2kVQiDQZ0jGju8CD2iVQWTubNwrOyc25nJA1uNfcjuO1pa3N29zXmm5NNOjBUrG5dV8ra8CHn

BCiHqbcMQDwAJIBeAjALZB/IoYEaHk7NQ4auAzalKkVkZCjm6D/8BYTr0w3ugAhQDqi9UQaiyoZqilPrZ01NCvIrXtijdroLpb4FlwMIn8hVuK2B8kWGgFdPFA0RIvk74D6cLPg8RGUcW9AziqDiTqSd1/uftSEYY9yjjyijLrNd65nQiFrpxVSoH0iNkkYh1wN9JnHte0goXf8nLjGh+GiEpVUXnUQ4XQ8w4b5VLUSXoEQWsiIAIe94JHJB94cd

91HOhcELgIsC4WaRrzvCE/GmmBxcGAtiYtjYB6p/00cJJMOACPDlqgPC7Cq2IrYKkI5GBfDl0XyAB4fhlx0RGtJ0XnhmniEliYsJlMYrB9QQLbhmAM4AOwPD4UYuuje0R8gO4d2cj4RAsR0YecD0QY0j0bdhp0XrByAHbsgNDHwd0SOi10T2jN0X2jl3iBi90e/1kOj+jW/JbgkFGeiDJJ/1L0Svgb0XeilfjYi54W85DEuc88ihh9UYRIBYUfCj

EUcijwLswt0AN2j0kPEBIMa88Tzl3CdzpvNd0WfDcLrBiJ0YDAp0V3CZ0QBj50cBjDDNfDQMYkUH0eBjYis+jHwYDCBMcDCWMffD90SjE4MZxjj0cgkkMVe9UMTe9QQH0hb0Yx11mM+tqQSJ9AIXaiIUQyDQISLDBMNbdlgF/UhQGlQ2AAkjlPnEA1gHbQKtnaBwEApDgocsih/hrCdzEo9mrsBV+FBCIGYHVJDYQmjzgYv8SoFcDakWW82UcQjb

jBmjcoVmi9QcA8HYY28nYYKieke39yoSLlaYK0FQ0fmBb2mdBRkX0cQoeLkyqPF95kdCDXQZ1QaXj1DREcE8qihGt6xl+plKALBmgT2jEcNgwByp/hf+vgAJKEutO+IIATdq8gCUjTxEcCQwyeJ1iGeHwDdYKkIuZKgANEV6srVohMJ9D7EmsebBH0W1iuKN6VMYgQAesQ1i1GjoR3Gm0heuoQAvEiEAxsZjFw+JNjeABnxdYJYj/GIc8Z4TeMFl

qc9XkXWUfpgldnEagM6sQY1dseCkVsS1j0kOtj1xIJItsd1jDyL1jR+P1jHeINijsSdjOQEXgz1BdjLYFNjrsbNjnDp+sQkeCiO9tajhYV/DBMGpBEgBQB6AOLxsAJ8DDtqBsfgAkBhsH91wRIvFlQmug4gI/AjNN9RFdM1dkgIGgHULyR5gDxsgsYqCD9ptYIsav9PgQ0j00U0imIRisEsYq8ksYaCukSVChUbVgmEbTB/rIREHMV9Ze3vPkYuL

fAIhpJCjZj48FkUl8/YYRERELaja7oJ1iYDUwIAKkJ35Hq1xMQY0MnhDchYEoxH8FbiqnqnBukN8kvsLfoHwojg6QLOi7duLB+mJxp8cInBYIKetWmvv0yVGbiVWpbi8UNbjkOnbiabo7jtJM7izkK7jnYO7iuDKQAHwnE5fcRiMskF3Ag8dXAQ8Zv0w8Rbk7sdYj9jsh82bkjCCQaccGylh8Ljp9iUbJHj29NHirsLHi/GvHiHcTXgk8THiXcRa

A3cVClPcUqsfcbxjKkAHj88ZMggcGCpi8Wjj4ZhjisrnwMIkWBCJAPQAEBAR4JIDwAO4BS9Y8mij+UnlMOjucF8BN1QLaFViDMKsQAoBm4pzHKk3aMcAiAszjMRDLlA7IxgtzPHJ+QSnompJzN/Tgv8k0UScCERlCiEeGcYsaLiyEfFingfW9jLnNd80RsEekYPlORN8Dptmyd4HhHpnpM6g06rVCcShwikrK2BqBL9JeEW1DdcXa8gEdKd3IpCJ

iABBAagEKBQ9N69m0eajxgHkjLgIG9a+h+kQ3nqcmQegBSCeQTKCbZjPUaaZ5psYgj8RJDIjtli9Ql205Bkvl2Xg2gU5OW4ccksA6onxs40acQcEYmjNHr/jxXrRChceyjsofcC47o8CgHpLjqEcliZcc7CPBisAlrhlj6CnjAiAvsCAQXf9tLAlYfUGwEPiqVjdceViW0ZsknELOZjcWl90ANuipMQzCZMTUCywYCFQXpl5MvHs9t7MMNAQiDFi

YmETmnrvZUAIABQclWUvhNYWgmJgxp7xCJRfliJkKgiJ7/WiJSE3CJVpCSJWGIrxXgJQ++ILQ+VWUIxS8MqAq+Ikg6+M3xDzxfGKRIckWjhXRrGJBqwRKmeoRKL84RMiJKMXyJ2RIFU8ROKJV9XLiz8L6BDFwXxHxyXxpmMqADQAvAkmFlApAAgg0Zi+aXIK+6KckW2piC5x64CtRgumDsZvUgQqOWwiVwWkuj9wMwHWHeAKxhmadESs+UKyna1S

IJAPAF5AUgSuA1wKGuUWMAJDllix1sNAJehNYhBhOlxAqM4hjqT+QxaNZ6HRzo8FaLfiMlgSsZwArcz6XrReBLmRLhLNR0RzoJ5tS7eXhOSUFm1lgDEHWQ2QDMAwyGu4GBknGDhyCIBpGgoEpWdYKGV14CAEDacTiHsAqhDxNq1aJYPj54mSByYeyBJ8RAE5Yh0xyA2yE4ABAGzEuYi+wgYykRYcTJQ2fC4yNjDRwTADMA+7CbWVcL/+XFGRA5gF

VKHAGJJnAFJJPZwpJdiW0keAC4otJPhuI4nJkVsDpAzJKeUlsWnxI8LNIXJLPoQ9j5Jq/Vvw8pLKQwpJrgxkgrwEpNYMsEmlJ0eEMk8pNIAipIoAypKnhs9SOe+kKex6vxex+GPrKhRXrxiV0bxEADxJ0oA1JGCW1JHAF1JYC31JmhFMkPYzpJOEnNJTJJJ8LJNtJfhPB89pN1g3JKdJ5gBdJF/CFJKkK9JXOB9JAsSQYMpMDJgpODJ++VDJT61o

uvTXnxAwKMx4SOchweXQAC4CqAcgE7AakGp2RBNSmAln0wI2D7SWZ2Noe9zQ2mxiteycwOISwIBW4wCEsNQXQRwYQqqT+LHgESGCxTxJ4ELxLeJ8uJZRdSI0J0WJ+JwBMzRVamzRM127yJl1lxPSI1qGrzP+qs22MhciymCrEVymBPqk3Un5egcNmRaqKbR5d1Bk2eVWAsBSjhB2F4mzQF1wsoBsB6mwkgWuCdwGsQTogAOH6AkBewJYCgmI40BC

aFMVg1Nm8aSfE4AOFOvUZ2E4ABFIFU+GR/mUriT4lDllcvejP6gfzlcbrg6czrjtcBPw5JfFPwyo/VIp9jCuxlFKyE1FIiK5DmZG9FOaeTFOfepDgpsHP3YpokE4pQBhocXYKEpZPxOcQlPwyw4y4mlwx4mNwwt4QoCURTuE7AASPjhVsEAAPBuAAev3myGRSrsRjwxWn4AbGMDxEUL0BDJkujFKZK5lKaItVKRn8PvGf5lXBf4x9JMU7RskQ6ni

6B0EkPB8RunxmDriAEQiH4Ywba5Q/oH49KXLEBRsh19YCGAnsH41CyLjETGLo0NVgABCCiYSjB4ZojHJQ6HFgC58ULwjgdQBKjKVQzCEJKheLXCheZsSFEKMbZAGMZYU/8REGbGKUdNMZOU+ICwSR0hyUyFS0MTgCgEPSa0aSEa58alCheE8Jsk28CheK5TVsbOIOHCan+yCIppDQymZjbTbkMcFxLMLECCks8DNkK5Erse3F/Kb+iUgK0B6I7za

1UhxIyZKuptIHqmBTXYY1ZV0qLo9Uk5Nf8Qv9Wb4s4NIab9J+xsybymbCKSkh7CAim4BinWk/SnzDQfTVks+iheMlBWgdJCB4PdQS8AoYSMAwgJE5shPDISalIXfqoAeymrKZCmoU9CkO4TCn0gbCmkxPCmAowimcAYinv9UalhrSGm7U6Gl0UoNbyU1amkGFpzKUtpzKOLpwCUrikcUnil7OEIAHOHSkZUqWlqORHAiU8fpiU1IQSU3nhQ0kVQy

Uzs6TUxil805pxz+MhwBUkWm72Qn5yuLSly0/inG0wSnm0kGoGUsTrcTRHDIUwohmU0xEWUqyn1w0mkOUhShOU1IQuUqMS7ldSa5hP8BeUlmk+U4j5BGA2ntgwKndFEKlYAFVx2GCKnwTfmIqwaKmxU9xKBADWCJUzPEJxERYXg477aUgSmzfTKlUZbKl+NXKm4MaqnPU3PglU3xLlUwKaI0wKYCTaqm74Qqn1U4LyNUyQDNU65CtUpBTtU+kCd0

7YbvjRg5tIQan4tNQAjUsSljU3WA7UuGm9gaakCHDsQ/+ZukLU7OJLU4LwnhJpzrUlUq58banq069T7Uu2lGUh2k3DPEmOkE6m0MM6m8wS6m/YHDI03IZR3U93DSIp6kt0hw4yEd6lMTfqk/U0VAggYXDvUrRzA009Zg04coKUW2kc0mik5Gbmkz09MAI0kcZI0rGJdIVGlq4b7iY0+jIIAHGnP0PGkE0gsaOiGUrbZMmklEyMlfnbu4ObexEowm

okN4wj4EgEymU0hxgYU/qkkxEYoM0melEU4BnzDUSnkU9mm38XengM2Gm800Onskr7wsUrIRsUo2kydTdg0OCWlpUmWng+ISkK0x/rK0jhlUUzmka02Rba0+Gm60sgwCM/ymR0kRkm0jilm01RwW01vxpU6BkHU4ynOND+TmUq2CWU8XiBI2yme0xHDe0/uri4a8T+03Vq5kXmDeU5ilaMyMFJ8KOmO/N3xmuJVyx0sKlWwBOlYTJOkqNCSAxUrx

Jp0hKnIHJKnZ0w87/Qjb750y2mF062kTFQEIl0iNZl0/KkRrFunZxaulsAWum20yql5jJunzUpsat09un909ek904LwdU/8bdU9+m00gakjgUelQAcenkU8amqM2emm4WamL0ypnKTRamFEZand0vFCb048RbUsW5WwHalgM0oj7084aH0jgC8TE+ln0gdZB0i6kKUK6k30oWB303/oP0x6n2wZ+kzMt6kD06MZfU4ICf0v6k/08hh/0kGkWrfnB

AMiiagMiIoQM3hmlMrIHI0+BnBeNGlIMucIoMtBmBADBkKUQmm74YmlbZD2mz4kLYGYt+GCw7HFRTaFF0YNSCkACYBkKWYASQYaY+QlCKVBLVhdWRYDGILtom0MEFzmJUCiWfoyWgi1j1UAFakzVaKp6CLiTTE8nggJQkhYn/EfEiV63AoAlag2O4APeO4mPRLFAk/lFJnbpEmE7ipuwzLH6ITqS5ROfZAU4SH8nVx7yhRYF+oiClePF9plY9El6

YTYGGICEB1mDXqrI/y7oAF64+NU0oSud7DpPEgBd8Y8T84NyQGNHxH+ZHnjrYkPhRGC0nn8URkcJUoHdMOwxNPAxkm7JfQ3Y1ZRGs2sQms3ylmslRHOsrenWsiul2s3LLRrFQikMZcLWs2BJWJW/Aesr7BeslNnm031lwGf1n4Mh7HHPIhl2I2Mma/eMk0LJMkUMvDynM3RrBssOn4tZYZhsy1nVsSNmaHbY6wHbson4Q/jxsl1mW4aBLovEvBFx

fAzesnRxZs3vQ5ssYkxJdHFgo6YnsPAl7kKYzqSAOADZaU0HYszKICWVhSpQfKxZgZOr/MLUTrAmYCnuNSxDI6XSyCfeQMCajybs+qJoNAajdXZKHh2C4FhYqiH4ItQmEIr4nR3blnVvYxTMQiXGAkvlHk7YVmfkkwnrE8VkWE6yC5uYejBLHZL1Q36wg0XFjbuZwn8I1wnmoyR7Z9Ho5ME7abAZbJBpiJ0mUHYHhxU3Wke8MVTWAV7AO4AsSa7R

7DOURMZWwd1hGgaBhkMRexgjT8BxkZlB/aB8B88E3h3KSlDv4TZm/9W/AZtHknAYfgHzYjDm/YLDnYMHDmE4PDlcJWZREcoQykcvIgWwGtiRsajm6MEniwuejmkGRjltIZjkQuM0hsc7rycc86ncc3IzdMPlo/oOX5PInDEGJCrLGQ95GOI4kHmQl8ZGko+oicgOlTMcTl8MluCScj5TSckjnQ8OTn9Y6lBUcvRCEMbfiqcy+Eacy+EscnTnKQdj

nC4dxknDQPC8crAD8c0FHV/VILuHD+GzE3HFRgCSAG2E4Dv0GABmE91GxvXFlxQBoK4CJYHUeCA7BQ3KY5vbURMRNcBSHI9mAINGAJAMEQaYNhosRW+5+nPI7f4rBBXkhADvEgXE3AqwaWw7Qm8s3Qn8s/Qk/sxM72pUEmFo2CE/kzjaqzWjzTWJmB5Ysvgwk816W1X1BpuZEkQgqCnqsmgnRHSR6j0UHaocyBJ8wI+k1iT0iLrRTZsgRym1iNMS

hGU+m1+VnCOkPQ5h4ZTJBcshiheY3zCde3Yo4t7C1sPviheR1YBTGalfhMSlvYMlofudgHYMQRLyIh3CMktTnwGavCMTYEYKAR0hH+KABz0tMYWrL/BpiXZmz6BgZXYbyndou5Qyyc5FMtPAZouQJzHeP7knUpnD5AOABmgC7B8AC7CjAL0AmM4BnY8uemNhA2AbPJpzhjJwwvcq7BT2EEaITR0h2raanD0i7DraT5IhOIySpDXnlOM5J69KMvCn

eDngH0w6lnU33CcMEjBNIEOmAhaIzRlSsSG8d+R3kSnyM8+vz+OfAZd+WITegShzK+flxYOHBz+My+EC0zIDkONCaH2bQBwAfnCCuIP5JMl6F3IwJyTDAUY5DCWyKwb0AZITLIvhWCC100pxX9DFxG+U7yM85nms8uADs8uACc8/DJjDGRyjVFGIx8gUZR8gPBvudYZb0/orfYKWAlM+un0ABhIUTbCYPYcHgW8xSjleMXmVeEXxNgu5HOFLAZNf

ROlvPAwj2kcwCY/d3yFOQvlQfT7kHlIBhF7SJnRM2poMJCP5WUGnnO/Vrz08tPmvcjPlnYLPnb83Pmd9Y6EF8yYb5AegCs8+gDs8+gCc8xInT8uVS4gMUzSlT5kXDZZm8TUTBm4GeAWMisIFfZsi72W5F2Sc3k54TxDBJULxT85RAPU1BkRecloO4Qw5WwHMQgacmJY843wjjZlAfUkGnK8aMpqAMvmweCvnrPBMp2ARvQdiQZSneU0pj0qFkqk9

ABXcifq3cj5QN8jgBQSE/BPc6gyi8wQiOOYGkfci3BfcmjlvYX7mEC5lDUGGbFA8gmiA8UHnmM/pmQ8vJ4O4GHnwdDvTw89BKI8vFoSJJBTo4L3jnM3qmY8lXla8xHD48keqyEInl0cppxk8kTEU8ldj9jDsD781fkc+dfkX6Tfks87fnZ8vfl10mBmBTNQXz0z2DtwQXlW4kcIqwRgW3gcXnKrKXnHrR7Ay8/gjy83pCcgHFxhreAUfuPqm6wAF

5Y2TXkw8bXlmM3Xn54K2AG84IBG8lGIm86MRm84ChNOS3lsca3ld8jvx28mbzrCR3llOVfwq+QVxu8/vlUOLxle87oa+8/3mA8cYbzfSP6wuMPlZM5VZR88uix8l7KvhRPkHrYoUp87HlU+CFxb8tnm78rnmmChRaH8wELF8vZCU2U7DFiFwXaSY8RV81Mq18hwX189IWz6Fvl4oPIWX4AoUUuUn4hgunwrrGH4t9d3kMhIfk7kEfmTZOfyzClGI

CjKfnG+XWCz8lOmK7cDpL868iDC2nlr81PmWCjvnT2cYU78jnlTClfkzC8flH8k/lA1c/mX8hInX860jIEYlD38+umP8w6kv8q2Bv85BRCAD/m0/RHDf80CR7C9IwAC3ZBACtgXI8UAUFDCAXuMzA7QCoiTFEOAVqCt+nAjSCSwMNAU3sdbxYCyp7XiGDQjgOuCOcv7lECzpkkC8MmzLAhm4gtX4VEkhlxXIjFlsiC6WA3iYUCoWB3chkZe0x7m/

YZ7mM8lgVwSQwVKc4LmoALgWYAngW76PgXVkAQUd04Lxg8kQV/KMQUqtY3xw83pAI8g0XI8kJKKC+QjKCwKaqChAWm4PHkO4AnnX0zgA03XQXvyfQUlEf8QZPeNor8klDmCgEUlCIEVM86wUTCsEXc85Xk+iiHkrCtwUx4jwXHU2vwS8nCZ+CgZYBC85AT6YIXr8MIU5iCIVqAKIVq8+ZQa8s9TqC9MZP8m4ZJC4UhXhfjk7CzIUkoAXjEiwQgHC

lpBHC8JxPsZPlH2cuhO8ioUu86pzVC+H7EOXynq+b3nPzRoUB8loUpU6WLtC1rzh8roWLCnoVyZKcIKZAYUKUEcXrCEYXp8pMWginPngi/PlQiuYWsOEvmLCjAXIwFYWV8rJQbCiqlak6gW20pvm/8nIWt8+xwJim3lrimry986vTdFa4VTDO4UmuB4XXip4Xhiw7EfuN4VO7D4UL81cVJ8oYWjik8VWCzPm2Cy8WznR4WegGEWiyOEWsOBEWvCp

EV386coP8+2krMm4aYijTaE4Myl4i6coEiwFE9iv/kkiqWCAC4LzAC/JBMyakXQSSAV/gOkVhrWAX6MKsU4885DICtkUN6aMToC5YXci2+i8iljT8i/AXT8/7nECvBljs7jQuHSdlDkrHHGYnHFjkwkKnAQgDv0egB4AFFEAVFdmas72wA2buxEmQd5XFLbjpuFTAg7O2hg0XKbgUprlhoaf5dWFeSGWI7ibTcpE9qUmagsYqKrmG4ASg3nEaPd4

j9cwbm3k6yzdRe0KagpOxtTcbm6gsAn6giAl5okVmw0eICp7OAmavc0iwPPirion5rko8KAlQDx62EsvioPMZHPAYBpECeUhwc0Y4Ic47lTI6iJS6LU4lWDtGGY0N4zsyoD6oCgDxAUTDXEhT6aoyl49GGR5XwUtFzNEzCoQyI7QbZjzZ5azRkBYyKKWZQZMecKCuIH6THAvjTgIN4Br7KTbJccpZRS3rkxS14kDcm8mPsmiEkIOOwjcjlFjcmt7

pSgEntIqXFCs2bl+fIVEFdAqVokBAliopAnLcFiIrGQ9m2BKd4F3WqpWBF5Zdvepb4E+Dkasw4lP/QQn6S7U69Q72YP1B/IOoiAAQQfJD6AZQBpUGAC6VDYnw5SoJ33KVJc412hOYHzpCEoYzSWfCERQIRQ/uFESyCAKCLmFKxlTT3qYVFlkXkvrkXSuKXXShz6umWyxpo8k5PkuLEvkr9mvSwVm/sj6UfNAqrxAH7aLcoL6sNfSzX3dbn9HNXEH

JbuxWIGVHa4nbZoko7m2afuKJQODA4kmeb8MoAws8hcW4jfAyi0wJknAOOlyuCfks80RlPYfGnuc/mlz+LPlWy2yY2yy2lrOfIDxAB2UcUp2WpCBJxuyn+Y5872WBUgP6BMngBBytSlOy0DphyuwqKSqfnLIcWJKAhMVmkHMRBEd76b4MIAxeThit8saq4CuuC8QcukugAG4ATDnyZICSjv9IvbJU6/ybsPCUCjdvSSI2CWnVIsAwAORqZIfopnY

CRiwSV+nli+xjsA0YmjdJ941szdiWyuaq+yy7z5Ae2UhM20aKFamzJy92V60r7xeymeWoGW2UzeAOXxy0n6TDLPkuyxInqMqByRyreVj6HeW5AfIBxyxeWJy4+Vuy9/qpyikXpy6GKZypgXacsNa5yuX6vZAuWo+IuX7C094jIZSWl4CuVVy75SBOWuWHkeuVaTRuWy+GBwT81uX9UTyRXMzuUAjHuW6wPuX+TQeUAo0IUjyjvRjypjrRNbDEGQ+

eHIw2UVkM+UWUYrmJzi6eWfVWeX9OBeWW+YOWHyleXZOcOW0KsSQXyncb9OQOV3yw+Why9hWnyz2WjAKOVHeP2Wxy/eVLyuYpJyoRXCY5jRpym7AZyyPivc7OWn4H+WvhdcSFyjMqAKkuUgK8uVPYSuWFDVrxQKlvDTlQEINyxkLwK6RVQfNuU6IjuXVjbuV2NXuVv4fuXP0HBXXIvBURlAhUpc1+Fpcj9YZc0cmZBYIL6ADEAQQBYC6odV6iouH

Im9SoIncBLhjAb6TpHHO4n4hzxI9aNSaaaDaaDQBATvH7rSVBkh45dHpMsqHTnk29mhY5f5Dcx8yJSzlmPkt9nNInQnPSybnfsrKVMbHKWaAeID3LH6VLcqy4VXIgS86bWbXtVzHVor+KTxCwRGYZqV3BVqWGy/1DOITqU9Sk3EeDGSXMAb+jp4uwzLhfySZKJRngabbFg4hJzbZdQDNhLhK2JMHQFrVrxeK7C7YMObE80RSUdgFZVQpNZVH4WJy

bK+ZmNPUHFmK4+X7K3hBd8WxLHK8gynKjnznKuw6o43NnSHHEGs3PEHV4yomEg2zlmQijHXKpZV3KrnAPK/sSjMLZVaxHZXvKvZXWwQ5U/KrpAnKipCBOQFXBXXpBsDTjRUgqGaTE2kG9StYqZcwyUUAYgAugXeDDATsC6oBbnRKj1HeQdbDiPRUINc1aI3AXFEbc7N6kCKwTphc2rrSsRQsRSwQnEhazFKuwJcyspWLpSiHsshaR2hGpXyBUWV/

E8WUZSgVnTclO7/s3KVeDIDl07MJDRoYMI1Q6qVyQTbl1Sj6hlBC/EBw8oANo7x5wyg2UkRDUIlURCl8wYJqW8SPEOiBxm1idPFu8iAxL4bY6RitQDyyfAwsWEjJ+MmoUx0zAD7yxBWywSWDR8coheK+SgW8JRABEEgCHIM7wgSemoLoueVegAwi6oaMQc4B3B+ydWD7iT0j9OVhymKhWAkZC3iKKldhAMjCUJikEXYS/DJw8GAD1iLpDHiZRX/c

s8W2CzXyZq4gDStafGdq7tVq8N+VHlZlCnlOxrGST0jeIz0izq8pC4MuykApfbo1AH1U68P1Un4ANUU2URkN4cpiZ8c5Fhqy96RqxHDRqkBaxq+NWbipEBJqmxi3IEJxpqwogZqswAjq+2A4OXNVn1fNXVqotUlqtWCoActWhk4xX+ymtUgSMxX1qg8QvyzBVsAZtUM8zCU2CyYUdqyRETqrel9q00oDq3flDqt9WjqsHldqrpDoamdUWlOdVDY3

PB9KZdWUoVdXmc0hW4YqzmLwj5HLw5MleqzdXRlX1U0C/1VQpQNWWGYNVdIUNVAMOwznqn2XBymNWKuC3yXvW9XBlQySPqnFzPq/FDFKHDUfqimxfq1vTaEAtV/qvZkAaoDWVqmMWBMsDV3YCDXplWCW54B1hwajfmtqzDUpi9Mr4aq2C9qqdX9qrCVYa19VZqk7B4a1DWEa2PDEanZDzqkLLkazzWUa0UWPw8YkHLPmH2QuFlhIxIK0qzIIXgBo

DXiXD4AQbgmcq5QZXpLnEvAZxAMkE/E+0IqiWo4XR+oAdrNc6zAdYDTB5mIqBMzPjSFvL/HGwy8m8yq6UAlAhGCynqLC4kWV1KsXGAPJpWSy3VUfk4wm5SrFnmE41X7BTORsBICmQc7eRfwJKwRcCZXfpGClqnB9rxQ+1Wmyg7C0S7EUMSwH6D6eTXOamuDO4sHT5lKhCxwpcBoyURnfeBTr6TJWAH0TTmAKhZRQawwXLIApCjq6fk7ILXnjq5fi

64P+U74RxgDkf0qjhTIDKaswCd4WIR6AO5TY4TvDlILjL75acCTiKCVrOLezribsnRxKXBgSQHiW4bpQ1wGymAAX33AAPB/qykW19EtxFK2qyBa2vfVG2t7xW2s7wCdF21UQAMI1iqO1wSVYy/4gUFkqgQS/4mu1dKGN2faoe1KGqe1DuBe1RmUDYIHwUon2v0A32p2Qf2uxAwQEB1/tJpAU4Qpg4OrH5kOvWEYQBh1Xyko5FosR1IQGR16OoRhN

Gss5GNVIZDGrRhyZKx1ZuGW1n/Lx1jgAU1hOrbxMnW21goDJ1+2sp15HUQOQeFO1bovp1RmqZ1t2tZ18Qse1rcM517Ble1POo+1Smst1v2utIAOvBiwOsl1YOqblh2tiE8up+1iurh1ffBV19sFR1GOpshA5J0lQEL0lI5KhRy+PQAywAaA9AEkwfEAxA0ZkKWWM1RRqWyGAGnxUw4amz6y7nFyA1nTyGIiX29UjBlTMsAQn1DgRjVCduX+V2l3Q

Vzk2onmmrswfgBxgq1TKOeJ1WuVVt0tVV90q0JvxK5R/xLa1vKJaVDJ1SxJhLhMPFWKlM21KlbRzU+FwEClwyLQgB+vlR1qv9SFWwTyE2phaU2vNEINC3AddkYJKpFRlU7NbMmMrYAuAEkwP2F1QCABaOyWx3xles5ViOSVIPVCmA5+JsJjkuqgqWq9QHWFeAJtFdocDUOAV8GL0cQT+Q23EpRQdjWADaUWA8wDRE8aDZIN7M4iE+uvJU+vq1SUs

aRzWpAJWqpely+tzRrSv1V7SrL1bsL+lurzMCmdwDQPtD2iQFNqlfR0VhL6Wymusr4RLUo1Zt+v/2jXK6lqXxYJVlRPyt234A0IGZKKChHyRQGgAA4zcgi4Hbg/QAYAPZN1Qx+w2s4vF0Nuj00MfsSgA/OpFA3MvOlRBs2ABhuRFOQH51WhuDOMdGqVFhvjwVhqMNFNlnw3xL0UlhvIQxhtc+nhrGg3hqel+l18N1hopskwO1VOGkMN/OtEwOaMU

NThq8NrhrY6vQkcNERviNZeOnhQRpcNmQFUgS4PCNzhu8NgDGxc6sCBALeHuk6Rv51Y4HpABRqfoxRtUQpZEARORriNmQEqNzQFhyvUHUNsRr8NrhvugkwO1AjWFVA5OBF1R+WrsfqFU+q5nmAjVFawY2D6NKIEFA2VG8gsMBvxKXBWMk1mYiFhs0qBgAUN8MGORzxC9Qy5h4AcVFKNIRu+gaJC+BHhppAJAE6E4VVEQ5xp6AacHY6VxuIAxm3KN

ULm+09xt8wAxHO+uDDgEygApATOGoEZ2D+NvAA56I1BUwn2QEgSuHW0xCFIA3xtwAvxtSg/xrhNvAARNMLGWAEOn2N7Ru+QaCCiNxuBKN9igEgXZUJoWrzKA2QGeNzxxw0RAFuNemJVAhcB6BtkLwwPECHgpJryKnIHRApAGrAsiEZNK3xZNTxpWY1kH7g+xup4zACFAhcDgAjxtX0OtxZM0IGxwjAAkmj4EJNrJx1AGQDMIpEGDEBgGaNYchtR8

yrOkBgF7IouveQIblCApBClNCABlNmXL6KHYChcF9N6ABm30Ckhrc4vUVQUGkUCipkCAAA==
```
%%