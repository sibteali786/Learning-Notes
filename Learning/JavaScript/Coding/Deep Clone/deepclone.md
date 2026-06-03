---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
Deep Clone ^WdX4lYLE

First of all what different types we need to support
1. null -> we should ignore it 
2. primitive -> store as is 
3. Array -> loop over and store each value in new array as part of clone result
4. Plan object -> check if object then loop over Object.keys() and store each in the new object. Maybe its not right approach since oject can be nested similar case for arrays. ^UDytGaUt

- for arrays and object recursion is the answer 
- for null the spec says we do not mutate it and do not create new value for it.  ^1cEec1Pr

lets write pseudocode ^ktF0jOSi

Step 1: Write the base case(s) — when do you return value as-is without recursing?
Step 2: Write the array branch — what do you create, and how do you fill it?
Step 3: Write the object branch — what do you create, and how do you fill it?
Step 4: Assemble all branches into one function. ^lT6j7QPi

export default function deepClone(value){

    if ( typeof value === 'string' || typeof value === 'number' || typeof value === 'boolean' ||  value === null ) {
        return value
    }
    
    // array branch
    if (Array.isArray(value) ) {
        const resultArr = []
        for ( const arrVal of value ) {
            const result = deepClone(arrVal)
            resultArr.push(result)
        }
        return resultArr
    }
    
    // object 
    if ( typeof value === 'object') {
        const obj = {}
        const keys = Object.keys(value)
        for ( const key of keys ) {
            const result = deepClone(value[key])
            obj[key] = result
        }
        return obj
    }
} ^HrY4S2n0

Time Complexity
- we have to run deepClone for each node `n` in the given value so time complexity should be O(n) not always why ? becuase n 
can be an nested object or array of size M so it will then become O(n*M) maybe ? 
Space complexity 
- we return a primitive O(1) or an object or array O(N) where is n is size of array or object. Plus the callstack which grows with 
each recursion call so lets call it depth d so it will be 
primitive O(1*d) 
non-primitives O(N*d) ^TnEVC6gG

🔍 Complexity Corrections
On Time — your instinct is right but simplify it:
There's no separate M. If the total count of every node across all nesting levels is n, you visit each exactly once. So it's just O(n). The nesting doesn't multiply — it's already included in n.

On Space — close but separate these two concerns:
Your call stack depth d is not multiplied by output size. They're independent:
ComplexityWhyOutput (clone)O(n)You create one new node per input nodeCall stackO(d)d = max nesting depth, not total nodes
So total space is O(n + d). In the worst case (one giant flat array), d = 1 and space ≈ O(n). In the worst case (deeply nested chain), d approaches n. ^VKMNRE5C

One pushback question — the problem says return a deep copy. If the original was {} (has prototype), should the clone also have a prototype to faithfully mirror it?
No wrong answer — just justify your choice ? ^TN4JuHDx

Deep Clone II ^SHFrfTho

- first we have t tackle undefined
we can use both 
value === undefined and typeof value === 'undefined'
simply return same  ^AFGu2fTc

- Date
for catching Date object as per gemini i checked we can use combined approach of instance of Date and isNaN to check if value provided is really a date object ^roJikUNt

isRealDate(value):
    return ( value instanceOf Date ) && ( !isNaN(value.getTime()) ) ^PbDz6KGD

- RegExp
since question specifies its being cretaed using Regex constructor then
if isRegExp(value):
    return (value instanceOf RegExp) ^NioDJYgE

- Symbol ( as value )
typeof value === 'symbol'
as per mdn symbols are used for hidden metadata and are unique so yes we should not clone them  ^2FHY1wcG

- Symbol ( as keys )
Object.getOwnPropertySymbols(obj) would return an array of symbols, we can check its length to be sure ^jhAOxbqy

-  Circular Reference
For circular reference i have seen some examples like using a recursion
we can use weakmap in recursion together with Object.hasOwn to check for circular reference and return true or false based on that, not sure about the action i would take since question tells us to keep the reference i don't know how would i do that ^k2JsWBxP

export default function deepClone(value){
    
    const seen = new WeakMap()
    
    function traverse(value) {
        if ( seen.has(value) ) {
            return seen.get(value)
        }
        if ( typeof value === 'string' || typeof value === 'number' || typeof value === 'boolean' ||  value === null || value === undefined || typeof value === 'symbol' ) {
            return value
        }

        if ( value instanceof Date ) {
            return new Date(value)
        }

        if ( value instanceof RegExp) {
            return new RegExp(value.source, value.flags)
        }
        
        // array branch
        if (Array.isArray(value) ) {
            const resultArr = []
            seen.set(value, resultArr)
            for ( const arrVal of value ) {
                const result = traverse(arrVal)
                resultArr.push(result)
            }
            return resultArr
        }
        
        // object 
        if ( typeof value === 'object') {
            const obj = {}
            const keys = Object.keys(value)
            seen.set(value,obj)
            for ( const key of keys ) {
                const result = traverse(value[key])
                obj[key] = result
            }

            for ( const symbol of Object.getOwnPropertySymbols(value) ) {
                obj[symbol] = traverse(value[symbol])
            }
            return obj
        }
    }
    return traverse(value)
} ^LdihdNEJ

Likely Interviewer Follow-ups

"Why WeakMap over Map?" — WeakMap keys are weakly held, so original objects can be garbage collected. Map would prevent that.
"What about functions?" — Can't truly clone them, return as-is or throw
"What about class instances?" — Prototype not preserved with {}; would need Object.create(Object.getPrototypeOf(value)) ^AAbZDnQI

Protoype also needs to be copied ^KfjAGdMK

/**
 * @template T
 * @param {T} value
 * @return {T}
 */
export default function deepClone(value) {
  const seen = new WeakMap();

  function traverse(value) {
    if (seen.has(value)) {
      return seen.get(value);
    }
    if (
      typeof value === "string" ||
      typeof value === "number" ||
      typeof value === "boolean" ||
      value === null ||
      value === undefined ||
      typeof value === "symbol"
    ) {
      return value;
    }

    if (value instanceof Date) {
      return new Date(value);
    }

    if (value instanceof RegExp) {
      return new RegExp(value.source, value.flags);
    }

    // array branch
    if (Array.isArray(value)) {
      const resultArr = [];
      seen.set(value, resultArr);
      for (const arrVal of value) {
        const result = traverse(arrVal);
        resultArr.push(result);
      }
      return resultArr;
    }

    // object
    if (typeof value === "object") {
      const obj = Object.create(Object.getPrototypeOf(value));
      const keys = Object.keys(value);
      seen.set(value, obj);
      for (const key of keys) {
        const result = traverse(value[key]);
        obj[key] = result;
      }

      for (const symbol of Object.getOwnPropertySymbols(value)) {
        obj[symbol] = traverse(value[symbol]);
      }
      return obj;
    }
  }
  return traverse(value);
}
 ^9Eeyshbd

## Embedded Files
2204c1fddce60ac2c3c12c4d369040ab3ab6017e: [[Pasted Image 20260601100830_545.png]]

%%
## Drawing
```compressed-json
N4KAkARALgngDgUwgLgAQQQDwMYEMA2AlgCYBOuA7hADTgQBuCpAzoQPYB2KqATLZMzYBXUtiRoIACyhQ4zZAHoFAc0JRJQgEYA6bGwC2CgF7N6hbEcK4OCtptbErHALRY8RMpWdx8Q1TdIEfARcZgRmBShcZQUebQBGAE5tHho6IIR9BA4oZm4AbXAwUDBSiBJuCAB1YgANABZ8AE0AGQBRNNLIWERKqCwoTrLMbgBmbXr6gAYANlH4gA4ZmfqA

VlWpgHYF/jKYbmceJe0F9ZnEqcueSfj63cgKEnVuJPjtKYXNxNX45an41YzHire5SBCEZTSbhrUHWZTBbhTUHMKCkNgAawQAGE2Pg2KRKgBieIIEkkoaQTS4bDo5RooQcYg4vEEiSo6zMOC4QI5CkQABmhHw+AAyrAERJBB4+Si0Ziqk9JNw+EUBKiMQgxTAJegpRVQfTIRxwnk0PFQWwudg1PszZdQXThHAAJLEU2ofIAXVB/PIWVd3A4QmFoMI

jKwlVwUz59MZxuY7qDIdVEDCCGILxmH1GiUS802oMYLHYXDNBZTRdYnAAcpwxJmFvUeDx/h9Q8wACIZfoZtD8ghhUGaYSMtrBLI5d1e0FCODEXA9l7bKb1GanUajBaJc0pvE09Pcfv4Qcp/qYQYSLsIOCoLF440xygAFQGlSvN7vnCQPs4UBFhCMcRUFGGYfxyAAxXB9CFW1UBBU8BgAQSIZRS3QYJ+UGQsmCgcwCGQiE0OgS0+T0HJcDDJgAzQJ

N8AtUgITDAgX3PN8EGvW972/FNcCEKA2AAJXCACgNRIQEFBIhjQACXBSEL1QN5gVBSRQhYqAWjDdFDwHCTdy0wNg3wIoAF9dhKMoKgkABVDsYCgABxXBrKw094CA6BX1BEY0GcLNtCzH5NlWRImwWUZNn+UFYMOFcAqSPMN1WSLfkSUFHmIZ4zQit5gouDcW3mZSU0kOSoTtJEeI4eEgMqrpU3VTFmXxIkyVJbj6qpGlHQZJlcRatlyA4TluWyVz

6sFYUtR1VNcX1FNZQ1BVMqVNAVXqxbMWmjy9QzA1hCNE0XgtK0bRee0Ux6l03QKb0U19KCEGo1BaNDcMfPQXB4hjEdiHjRMjORdje1QTZRimPMLh4NKKyYKs0LWUDYeLGs6yA+Jlx4UYW3idbLM7bsDz7XSh1+sdMjGqc7vq2d50XMsFhXNdVg3Lcd3qvdMRBo8T3qs8FIgcDCBYKBUDYflUAIfBUAoVTRccfl+SYMbUB6cIZYQF7gdVthUGYWc4

HxKAAB0ODeF6jNQZwAD4Nb1yRhHwYhUEI/FNbUVBTbiVA4AY6DcMYK3bZRN3JeYF3w9N8ZUEQ0hyBgIPUDxS0xaLSXGT1/jAlQEJsEkVB6AIcSXY4LWKEluPcAT0Ife5UXxdQbAuNQQJ9fwE2OHqbRUAABXwawxc0AArBBsFFm3G9KmkXYluwR7H1XStL5ObzYNOAHlh9HqBtExGBmAACgASnT52Q+z3P87DRfNeNcu5+37uAFkq80d3chethRYY

+TJbgX22DUnzqwDgYgxbz1FngUub8tYonTHrQg0F+6kEbqETW/J8QV3jswbQj4KDqUqELEWYsJZSxlnLVACslY8lFmrcOFBb7a34nrA2RtTbm1oonBh9tHbO1dtnD2Xtu6+0QWoQggcJ7n01jXQgkcODR1jvHROK9U5MFPpnUOl8C5F3dqXO+WCq5h1rqQeuEsm5fhbuEYMHcu6937qXB+C8J551HuiGeg8IE32XmwFOa81GbwgbvBA+9j7qKkTn

IBJcb5lw8Y/VAL8YAwLUOHDgX8W4QmkH/ABkSQFgLYJ4qBqAYHxh7AgpB3JUFhFQBglB3JsG4LAn+ESmZGmQSQbBeCfMkIoSIhhcaZQiy4XcARVCfQSKgjIlESipBnqvRTPiRiHBmKvgkEQlEJDJbCnIQuShhBFbKxyKrdy9DGHwOYfrf+bCzbd04RPbhzAHbBj4ahUOgiODexEf7cRmtJFZ2keHWRnt5Hd0UYYieKi/G1IzuErRhdfC6JiXUwxN

cuQmI2eY40li242O7n3Aejjx62xcdPPZsSF7qGyEnHxq8N5bzHkEkJJ9rBnz+REvOUSKUxIJc/V+78UlpJ/pk3A/80Q5LDHkgpA9inhFKawcpKC8BVJqQY/eDSeJ8UEsJQC3AxJ6Q5pRWSGSFJKU6WUVSzB1KaQ4NpYmx49VlCkjai2wpTLmRTFZdA8RsBtFHvEHuBJQRqz6F5FMH1nCAhSEcL49QcyfFWPUeIK5ooHEitobYqxgQLB4OcKY+Zyz

1QyllVAcwZgJG3NMIEprIClSNdCOqZQ4Q6nrWqOU2J+qsnQMSdq5IhzUlpLGPqLI+hDRGjQvkk1RTih2nNPaC1GoIGWkWvGLaNTbUqLtH6fhJD/WOvM06sBzrNogFdV0VMfR+ieiDOZ9UwzEAjBIXAqR9q9R3TRQGC1gbKlXLcH4ENsIozQljHYyN4a1lAUBbNmwE3Q2mO2LswR6bVJJimYcvVyYTlyLdGcc4FxE0UsuVc65Nzbkkmwfc3NkNdNY

hIZw1TMFIv3uoglljsAiHhhHaJHIGEoNNrR5VnDOWclHnrKuJzKG61SaLfQfFcMu1Fsy8Tn9IGBFk/ouFxdlVqG7ngghNG6O1MroxhTzHAisYAxxzlXG1G8f0866WgnEDYBE4x7hxAJNpOk1Efocn1FuaU43FT3m1M6Ns1p9AjT/zarNEjCav42kwW4FWzy54Rm9IQJhPkgy8L4FS2MuApFfwUWNDMq9776oLP8Ms6j6A+P0cM+HYzdLv6jzYyWC

zpV07MG40C2rKCBMdaE055gom7Z+ck6gTzsmPYKbG2k7AgXGHl3U+gzBYW+S8X4kJVgUXVakHEpJA1ZVjUpCS+ay1BlbW8wdRduzrqigWUgB6iAUwACOPB0QADUeBKz5EGiQiDogdWGAcOYZbcyJB4JsYKiNTjJt8vEcYq5RirC3MsbNEUVhJcLatYCCbtChWBDMDNIF6hfFuCpI751S3Y0bODDG3xoOjFhNVJtyJ53NQ7dAEdqKxp8i6v236HPh

0ch57yH0QpJ3amndKNnrbF04+XQ1Vta7JQzs3YdBMu7yv7tgomo9J6bpoGnPdC9syyuWXepGUYm64xHTfcmDan7srzFGGsECSXKwlheAj/9oG0YvEbLcaG1w4OEwo3a0maHxyUywymWmuGQYY0ZoRlmxH2bXetYZB3DqyNcx0hHudC4hDuggIgRkYZlDjqFJeyozYVzYHiPyYgxAxBZmpDwbAowG8d/qMQECFxpi4E0KMIfWYMZA4EO4IChQuhgH

T6UeIqpqZlHmyRe3dESpqQGFap1PMEB3dKA98oIMIDoigOBKYQ917/l++5YNrFvIg/GB8KHNx5jxEWFmpLuvJjaA2DMSKQEbNGYX4V3dKRUZUW4AKEKcKFHAEJsRIfNM1SnNaJLRtWqWXDUIXCQLtNqPnPtHqRkbA9AdkYaUXfpSACdFXXUNXTA+UCAtaOgzUKdddWglMQ0bdO3RSE6akM6CqB0eka6M9E3R6M3bPR7S3B9eoG3P6Lg69MoNMRPA

EL4LGFKX3L3NAcGdQ1GcDF4QEW4JYKYI4UPBDPDPfSPUcaPScWPGmHDRDJPJmIjNmUjcjfPK7boFZdCBAD+CgBibzOQBAIQNzPQO9HTTwiABDehPwzWAIoIsjNgUIiLZpNaI9DBCCKCBLNAJLfmXLCQPpTLHCbLXIkg8ZFMSZIrKiUrcQiACrJifAXTLwnw6In2MIOIkIifCADbTVbbUSPbe1SAKSBAQ1eSF4E7FSLfc8HfNw/oiIm7WiA/Yod1E

/eomYIeTYAARR7kIFv16DZBDXqjDVBxfygwTXf0/2Knql11Cnxx4FuAxhZhZhWCihTGx24CJziEmGCghk2CJ0rQp1rTQEZmZxqkRCYOIIgFwPanwO6gHXBNINHV53FymhYNVxlznTlwYN4CYOoNmjRPqg4NfW4L3V4IPX4MukENPRsLKAen9CqI3xvUkM+lWBkMJPkIECd0UkZkBBCjBhhnqk904G4GA35LhhLDA3rDtBbBZk2F+DuHdQJlMPD3c

IgFQ0sIpmsKN2X0gHj3sII2ZlZhI13FzzMMozKH5kqDFA4niDQCqGaM5SpCqUVQQAPmYBPkABQCchSlPzGAYQSxKAEQUuZbMOZwQFR4dQYQZrMzEBZQAAflNktJvB4BtLtI6wYyKSGnZQ9Nlh2W9N9PmxCH6GoHUQdnLlzKEGqQlzkzjI4ATOAmTLUE1k5WY00AzPzizIoTLICwLIkmLLYFLN1h9PLInSrPjP6BvHqDQEQgTEyE0GCE2WlhbOsBc

QBRyF1gsX5AZDHhLDVXxOfHCNrOtNQFtIbOiQdM1idJdPdM9NLk7MCH9NIEDJC1CBDPoTUEeUjNa2qmrNrKTKPJTOkUM3TKXLbO2XlgHLzIWyLIUxLMU0HIrK2TUG/LHLrL/JPKbKayAtARAuzLAtQDgvzNwygozhgs7OHMQtHI4gnJjmnP0FnOkS2UXKwvVjDGYXXM3Nwk4B3OpN/Ei3Rhi24vSPaUS0DW6UIkqHyP/SGXwh6TywK3ImmTEPpLK

FqKWXqP3OQsPOPO83tLQUqWdNdNQHbK9PAvLLvIDO0XhWDNDLfIjJY0/NjIosTPrO0tTMAsYszNAtgogu7KIudhIpMvgulnIprOQtGGcsbI62bNbMMs8s7IIsLN7P7Lwt9LIqgCQsosnJorovnMwuXJLlYsxQ3NAQ4o4C4sgC6K22SN23230hkhQMUjGM3wtW3xu3MNqqdXmNKDMnuyWMqGklICaHqBFB4A4GjEDTvz2If1DQOHBjTRZlzXTUZmh

k2GMJTFgg3DeEQOBBWtCkTVzGFLKFeMBKbBuJWtXAhgilO3qvjSPXQNBPRKwPbSJG+0SAQEmGhIF16jhO51GjF3uglxxI3SYPl2VGxJRJoLxLKAJK4PnxqJ10PQEKdEpM1PPVELpLejvQ+k6JmBZLkPN3ZLwzWBjTmGhlhoFLQi3CZxAzFP9zWkTRlM+AMJMO8JNIL06jJisMwxRrjzsLwwcJTwNNhs5lZuVPNIkCwENjRTvX7GsWqXYrazvWvE/

GNAPmWyPmAFNlNlQG1vcQPiOUQAbiDIAF4TbUAAByWUCvM21AAAHxtv1oQENpCxNqNvNqDFoqYGtrtodqdsspdvNuHFxBCA4C9vtosuLn9s4RPg1tLh1rjrMofPDoQC1p1pMhTu1vTtQCUBVVyskEztJQPlBRgG0FkSLtVp0RPmjszrjrInWVbmsUUVQFdq9Grp1uVT1trvkzjg+wIA2SDKrtjrjqHsbk4DrqsXbibsoXYjgGVudLqR7vwCPlbuH

vrvbkUW0DgGL0kAPlXqgCXsHqHrToPvju8PMt3sUUzqPrjszuzuY3zolj1rVl9ojtNrNoJTNoHuHu1s7o8UnuACvq/p/r3nDldoCUfmAfLvhX3q/tsw7tHtFj3g2WAdQE/pgZ1p/t3snsVpnq4kgfEnyD3k9GgbQe1rngIeCU9Ent3uXtQAAZXtPsTrnkvtNhMjCOqwwEwElvlnS14gnqKq3M4CnqVtwbVpjvvtQEfvcmfs1n9ottRCtttvtqfol

mNtfvdrflIFDp9pUedtfsDuCGsC0aTqbtNqjtQBjpgYTsfPhWYYPpvoUBzvcrzoPoLqLpLuYDLrVpQfMZoYwfHqgEbubs9BofbpHuGi7tIAXr7pC1QZIb8exSwentnoPnnoIGIZIfPrjg3q3p3v8fScPpoasaxQbrjlsevoPtvowvEckYNp0b9tfvftiaHp/rnj/roeafgdQGQdAaawZUPjVpCcwTgfCa6eCSQeCXDiaZgfidltduweSeW3IZgCI

ZobjrIcIaof8ZofaZPvvIcWHlsdYaSJ21+FaQyPwA6REpSxkryPSwoIYEKOGRuZKPywmUKwUvRvmR/jqIaI4a4anplr4flsEfmZEYrrEZcYfu0eMdkctuqi0eUZhbUaEA9s0cUehdUddrNv0eDqMcxbs28Ysa/qKeWzKZ1vsccdbOqbcdLsMzwYQErp8ePvQc6cyZQSCcGZQWGfWVSelmkcJdWZZZGcwbmaSdwd5fycsf8fXs3oeVyexUldTsKYY

dLjZbJYzoqYcbvshYkYxd0axcaaZemc6daddv/t8c6e6dQDAfpQgYGeZe1tCaAbGYbmQamcAdZf8cSeEa/HpaWZWYdaHvWYoc2exW2eVb2Y8UOfWw1Uqp211QOzqoBIaouLNQmI0latNIGLmKMgWKPyeyfA4DaA+yxBmGUAch2I8nNMf18jBnx1bE+IWAR2xlTcgFgm+AWAmAh2zUuHqAJzlILUxI/3jRSBzA2CSBZlxiuuTd+CmBSAANOA2HWFz

WRwOvKpZwwIeqaiepwIQFzQR2+l7RhMFx3ZIJ+rHSRMlxmiBq3YXUxMV02mYKl1YMhsgGhs1zNB4OtFJMUgunqgN2EImlN0+YZMxsjE2Fxo/bsyBjw3OBAMMPOG0LQhlKQMgHJvFIg17cBB+NWpvQVJZqVJmNVOIHQxj25tsLpj5r1KcMNI5mNMI6uYFifEQU1hxH0B8CwBtBs24VUkDmYT2xvLFfXMwS0VSTvVQAAAMOAJOOUOtVBGBrHi5BBVY

WOR72PghMAbQeEnkilNZ14D4OAT5xsCAKARtZYE4YzdPWNdLS5TZCkYEB4Sl4FmM6slEG4ej4k9ZdYPZHgtkKVoFR4DA9ODOAAqJ+E+fQXlVASz+Mq0c8gwDjzT2AHrO2Ip3AH2P2MRQOfT+IE+ejfZzxVzwxfT6sE+WWZWDjUuQFDzhuNMzBblOxYvaJdwY8KIaeWWcwfOR0CgV89QIFLRUzVrQRlrrzpObw8OEbj2O9OAPrs+bz0WXzhczWU2T

5LL4L+IEL4gE+U2VJFwVbgOdWErzbo+Nhpj1TtjxLrjlwO2Xjxs3WAToRnB4TlBUThIzWKTmT6+TleTylIM5T3CLINTy75Lh5XhXT61gzoztJEzszyQCzqzoQGzoFez6RPRGVZzjCorhOdzkSTz5Tnzys/zqzoLiHjgMLiLqLmLmsuLoHjTrT7jzWNLjL0RA7iH3LsWKFMleuAzJRErsr0qARFJDjGr0hQC+r3pxr8OTlFrlEPtchTr1Abr3r/OU

2AblrczEb5TyI1BBC7hmb/OObnzRb8HlbzL1nnL47oFXb7wM375cOI7rb8dHiqq34d4SDRdqYZdjcfiyguLc52CNd5LAJ55iIu5gokxIokP/iV5so954rRS+iRZKrM7wHi7un2ABn1AW7nWFuBkR72e2zV78Tj72TzWH7xTzWf71TvQdTzjkHx5J2cH/Twz/zGHlzOH6LhHpHuzqVVH2BUpFznnwxHHwCPH+bmWQnpeYnwH5v8nibSnoFEUGnmv4

HhOTPpn/b75NnvLznwfnOvnz0wXl6YX3H2rsXlBBrvuJr6XqWWX9ryQBXpXifvr1XyJQbjXshLX8bnXoKvX2b0bgngxWW4cBN+2XA+Bty25W9OANvFnnbwh7VhjuMbTbFql6I1V9USbEYmaEar1QzsLVTPJdhmKOos8xkLqm6hvQn4PsAAaSfjVgBIbQVYFiErb357mhxTtgYS3A/BfinAuHIpABDJBEoHAqDBDESBbhwCK0c6LjG0A5hCMQINcF

mFuL/FMBvAFsMCVZy3twShIF6m9WkJHtPqRBU9lzhFy/V7mVBcGriXmgbR50INRgre0BpsF8SB0TglB1hqWgSSuuP9mUAA5UlKCwHYgRjXvSfQFgkHAGNUUUIvBbiCORsCINQ4PMAMyoGIeh1pqckF2vwW4EelkTwYCO0xCwiR05qAcygOpKjsnn1Jp4XCeeAgYx0qCABeDcACwu7eAS7p8E4OIOONvBLDMBTY68UuMx0B4elByKCMMCiHFSixAU

gqUWJoD4hlIfAeyBOGoGQCmwnwAvBABbU/h6xrw3IWTE/G7jOgJYnKfiFEGlh6AGQpiHOEWAThidpEq+BMDlRKQV4xujAY8JVyLJwUzArAUWFoiwDUgoAFzU2GjG7gih5uywoeMXlFjN8j43cBYYwkGHVRxM4QEOlJmsSEAfACcD0moGWEEAVMxAGYaAl8B3o+EeibQJrQ4CdDUAS/akJrA9LmIqk4w0WGEFRSyYKUVSKABQF1hkQxAD5eQKbCaD

CAFUn/Nrm4mm7/9AU42aTO3ERFEB4EmgbHnxE3o0iRI4I0qDADNoCJwwZeO9DkDmEcA0+dfGAFUDh7rxpREwg+BigZagiuR5ZeKprAsT6JzhPsNRGGBlGfw70WIXkX2n05bdnYrtSLpgH763CBRkgIsuNj2EEAdub3doTWV1hBjpYI0MBICmb6oAAA1JQjBGoBnQpcTlMyOIROkJGFiVQNYFFj8h+4ETKuEfCLIejFIYSGnoAAkiUnsmNTHRIMx6

yJ0qbAPjYMLm/feBHnCKwljKEWSUVHlVKqndqhdQrUUlyaH4hTMJVMMcSO6HkjkqIgEuFCIXgjCjURSCYXKimH8gZhUADURCMCDLDUkqwukd5k2EpidhHWSMSPSOEbIEApwx0RcLRBXCyENw6EcEHuEAoUkTw30i8I9jvDMAnwtsb8JJEAjw4QI9ZKCPlGQjcI0ItzLCLNrwjRRSImKqiIaz4AMRWIpuEEXgTXxSqhI4kaSLAQUi8QVItcWsPIAu

VwgjZZkWEzZHDQNRZonkVsjv78jrwgo/lPBNwhTCJRUo2QGuLlGoAIRio5UdN2yBqjtxpsEcTaF1EwB9RPE0WEaK4hHxTR3lWTFaIQDlwbRiAfoSAImHnDnRjEvkW6KPhlivRPo6CSxP9H+YLx5wsMf8J1j7C9YNPWMQZwTFJithaYjrA2MgS6UD4OYpwPmMLEqpuxZY+IBWLJGoBqx4ElMe5M1ieS9KEjVsWcPR7OxOxYYIKb2MAT9iyqAoZ3ic

x97ZTBKmRVAIHxyIh8JKyMKSjlij6lF6o5RD5n4K+ZJ81K7DWofUNr6jj6hLQgRsNA6FdDVOvQ7kQuKglLjw4ow1cbKPU7TC5MO4xYfuN1i0j1hx4rYWeLu72TDhhyBuDeKYBnC3uksS4ShOljPjlAdwoIO+Jeifjyy34t4ZEg+FjwAJ4GP4cBNQCgSQRkPCCaZKOkwTmAcIibAiMQkoioAaI1CSEExElwMJuIqJDhI4A9SSRNPQiWwGIk0jSJ9I

0qIyKomsimAtEzkQNM158ip6+vHsUKI8y/TxRzsSUWLANGyjAIEEwSbomEnhh1R4khodqKkkySHR8kr8IpMh5miuyKkzFNaJ2maSS4Do3SS6JpCGTjJuAb0YdLxnqAAxaSKyaGPjIRiv4vdaMe7Ht7OTExW3NyfWPxCNjvJvkvMdUgCkMY0prtEKQpjVnhSaxOs9MXrK8lVIWx09NsU52SmqRUppY9KUAnVgDjYQsbFAdkNqpDF6qJqcYs1UmKZs

2aGeDqrm1IE9VyBlQJ8NWHqAAApIQNJA7AjBxquxEgvsWBy1tNgEwXGECCxhwE5BgfXXBsDiDAgIo4UMGP8EupiCi04UOdh8FChBRLqIUPKTWiUFZhVBm7Swa2g0F7sXch7FDAQVhIGD4S5BKvMiWfaokLBChKwfezBrzyIai8t9o4MJIuD4aZJf9hSUNwegtSAoXwevn8FY1cAiQYIfVMdx4ZpSRODYHmCQ6JYPcopHQhKV4DFy1gQBQPhkLDyB

z2aUedUlzSPnYZKOieajqnmcJGlXCFQhCOw06ExEt6/OVAC9nEiDDBGHpTlAAjor6BnMI0lVpLEe4j04AxdU8dEhUq91TO4cf+hI3NSm8v4X8dyN2NB46dpezcAcLrGz7pcAEew9yDn37BvkNywoBONBDjirY0qpsWsDLDRDQirMKCD0s9KenAjJpfQyeGwHMCawYyg4iQIgp9jIK5eaCmVG1iwUdYcF44fBX6XMrpdsGJCshdsIoXfNVKMsGuLQ

oPjmoMujCtWCwob7Ox2FFiThVn1wCBweFaIPhYgAEUUR1AwitsWIrRD9DJFHAaRb4U4BHT5FMVJRc9NUXYyHYmi6Lk7xyC8UWk90P3kJUBKMdiiofDLJJUj5iU2Q1UlfHH0qI3zlKTi5PpUD0WytJAKCoxRgtLimKYiaIXBZYqZ62K9ApCpaY4sakuKaFJkOhSijCVMLEAPisHv4sxSBLuFni8JXdyQxCKjIoi4WPEpHJJLdYKSuRcNG6yKLgRyi

wYZuLnEKpclYCbRX7OQE9EAFGeYOTO2wFptw5GbfAUhijnZt/lnVMAN1UPy9UJAIoaSOBFID8gFhbAJgZNRYHKgtgyQJtiuEbDNhFgSOHgYcG3ApAE0n+DcNuFdzJQm5CuX/CtS+DI4yc/wIAooPKioAYQVUEEmgCPSPsNBbUHtOPOPZfUp557REv9TnnXt7BS8jEuIJsGDzV0Zgm9g4K3Tbyv2fBX9vrgPn5CfBaNFpRITA4PpEI18s+R+j5q5o

PgABRIHlPJqJYyab8k5boRSJNsoMxc9Ifh0QxtVAFapDDCEKUraleaEC4oTRyFr0d3lHhdhu+E4gWJnQzoHRegBDUF9w1BSppDthAhnMylcECpaVLD41KnmdSl5nJSmTx8QOrSxqb82jXNxY1Ly7olVQTZBzhijK0OU1XOz/K98ebCFegBaCOBJAxAasG0BTmIrc5U1A4kuCzQBQACnvb4gsEbAVylwLMP/B/kTTZoEc6wXDodSHbJQ52PxS4MFA

ihbA+207JQc2G+D9z7qUq7dkOhwJcqOi/OQgoOgGhnsjBF7IVVe2lwbylcS0FebYJlWirN58qmGoqp/Z65Eas4ZGqApEK0lNV5QRkp0QABaeq6DgaqUIgFtwWYAdgMitXhCicSHDDgHluLNh40Kg+UpkOdVZsVSHNYBR6rAUJ4B1K4FKCtVOCK5haDHeBQLAlpGwAWvDfMcC0E4+sVaojTOpnR/pphS4rtfRFUBCDogX4cAY+DxoPr8MSqu2YJXD

GdJeMiWw9AuqsOyDaBzU9LRlkprQZFN+N2gZQN4U03htA2KmxFvizkYMR4W6LMzfqzdoosNGCLKRvyFNjmacWhjdFki0E2Wxva+LXqOlkojOxvaNmmxhwFhYwBaKuIa2u63oaRtSWgbI+jQxU1BkBhUQcDA3A7CyZotQ9Ipvogy39AjN8WwkTAyS0hYUtS5R2hLCEjKA2gnDLLbs3Mr6IqtNW8Tctm0CCARAYgIsq1oLHRBXSxmmBjQ2zppknGiW

h+jSw8Z0svGdWoVmPWxSBMj5grbWnprCBQB6WRZNloq2HpOtOmvLaJpZWm3D0ZmE9V2uyErBz1u6aTRbdlulZZMul8raxJtoKaBt6tidNVoVsDaDatWVTEzVC2C0v0DWTWD+kaxIZhN1kprcxjsw9YjMrWNrHeHawrpXblthm5bNQDniPa46226HS6wlhutgdIOmbc1gSYnbyAZ2v1oQ3R1f1g2yzUNtYiu0JbntbdIZqDppHhbhwfLCWLDv03eF

14FADgP6ktA4QYAIoVnbiH6YV0BWDO4emQ2YAi78AlDYnXJpYAKadE+QGXRFrl0U7takOmLeZSYbva467TIpqdvk0Fajm7BPcuwyY1S0eGstaTQrSE5cbwWkmmup0342T0hNImsTRJrsZSb2Nsm0nYptG26s9NGmqbXjp02EK9NBm1bfaxgba7daereplizhbKBHNtTTzXZtRZp6KtGe7Fj4gMYh0PN+LThD5ts1+bBQxoQLUoyc2561dbOqLeHq

laxadExmoPXrWS3hNyt6WzLY3uJaELctuGArXHqK1f0StllMrWlsq0IBqttW3vTrsTqNbp9zW+lm1u5Gdak62gHrcoD6366v6n2ylsBTb3jbPG4ug7czuKZr044k9FupLtU2lUVta2i/QEzjia7YG5+3bfyzP0u7hWXrBXaTolZXaT6c227Tk13qv749L21VjdtID9a99gbSpp4jb2J7/t5tQ1tpuNYjNwd5rW/c60Yw9NAk8OqBojvYj37kdOiV

HcPFf2Y71kiDV1hMwl347v9s22Zv7pN2LNydgBnWlTvl1P66dI+khtQZZ3q6NknO6PTzr51ohNJsAYXerrF1QMGDjB0hsPFV2y6eDxupXX6zr24gA2+OiAzrSKZ67h9B9Q3YQvUNhBTdcaopZoTylpFz8/vIUqmqzVVL7mWWTNaMnqUx8apTSkrKBsoVNTGNnDZjdLVY1y1iq9uzjcrqgbabeNrukg+7rUlHlPdwqb3eUwx1+6zDkR8SFlpU0h7Q

gmmhQxk0j0kGudMehHbvuU2/aa95mlPdnv5ayN1GntazVUds156g67m72hnpL321fN4YCvfAiC3NGk95tLQ/gAb3oG+9zekLUYaQMd7Zek+1AHls1hn6ctCRxY0Pq/r07itULWY6lrEANwmts+8Y/PrR7lwDjLWnRKvo609lut/cbfY9vj377htVLH7RI2P2TbT9c+jpj/uAPssFtt+pHaUfhTrboDVBpnT/Q/11Ni4X+gnU/snoZGUmF2xepwe1

pstsmcrMA3wdv1FM3tRhgbfAa+2IGXjNTHPeZrQNXaWmw8NpuSctb0H8D4DCZusZIYAm1taOq7YIdGbY8cd9B6E9/U9ZE7WDGh9gxQ1f1rNlDGzV2tQ1v2bGQd7JkYyId6ZiHed/OqQ0Ltl1yGsjBRxg9LtUNwmSdbBlXSMZ0Mg69DKJwhYYY2PqsrFideE/azN31QKqAcuBegM+VKDa1OA9NlMQIFNqE5EgRID6n3jdLZ0fMCar2uRVmhTgc7LM

Eas/wIFPePA7dW8BXCTA8wMpSHCFHJV6FU0a6rYNKS3X7qSo9VSHMyvtMbtD1Yqx6ies7RaD3qugy9d9VvWCqJoANd9a+2fX0EJVWJN9WvPMFBmoaW879cSW/buCVVSNQ+cbiA4ar9VoHAIZBo+zQa2SqYDksoWxjnAScz87KKIOprvz0YWGl/EcCQ2PYnVItIjsRvdWgbChPqyjUYQTSXBA+dGwNUH0qAKAQuIXLWiF1QAAABfoOp1kxPg3zn5u

kXguABPg5lcW1AO+Y/NFNgLV9ELgoFV6BHrdgLNjWEZBYO7MjDLYHXxriOCaEjwm3AKJuSNHwAA3CPrt2CMbT4u7TQXVyPqmGW7rXTcUej2aaSLxh6pq3T+0yNTaxsJXBXm4uKN2LgxlA9xYaMwGIA/F5lhxZMau1uLbmqGWJbtqt1i93mm2opbL29GAt4l4epJf9rcWRj3FzOvRcIXLYWLBu/g7rR2Nd6JYixwy5GwH35a1aJlpVlDJ1b0tBpll

1AGcZssNaEjZxlfe1tEDXGLjW+10o5a11mWhtblZ43HVcaGZ3GJ+qBu6yO3P7fjXoUKzrWZMo6n9iiYi63XbrgnETe2jU0cfP0isBT5hiVmlaAMlNSAaJ7emAcqu0NW62J6A2lelPa0ED28aptpa4s1Ems3FxKya0pN0n6UFog+KIe8L87tl68fkJppyvMtcDIDa1r00INZGGrGV8gx4jmtbahmuB8ZvvCy1JXdTiu8w0KeWZbXKdYpkNhKf8YNW

2rjOrlnxtl3ynAkipiQwLpMSqnZDs1z49qfV1qG9Tgpg06ofOumXmWBh4eK1ZToAMjdANk6xXRYtH1I1EAZ86+dLgQXvzPgX8/+Y/OAXzGIFpOtjagsgW3zcF40Ahe4ZIXQjXU/PmC3kNEssLlKHC+XDwsEXxNc1lOmRbTGw30LTTai8UdD0V0vLidKPWQagaQ2XLAl9Pfi10vyNqofFhSxJcEucXpLEAES/LZUuK2pbtmmS/nuDrq3VLQxrowbZ

QPl6NLCtrS0rakuexUwsu/SwfSFsV9xb1TCy/Mesu96Vj5cNYw5dsbO3Stne+Y55fdv96fLS+zhn5bX2BX4Um+24yFZ9uasD9WFalrFdpbxxvr4xpK/NtSut11rQJrKy/oat5WdtBV6Rgdb5MsH4TFV5Vj8dqv3b24INpy8cbzukAnb8dglF1cts6XerECfq73opNDxJ6nO0a+NagCTWllCAaa7NYasLWB7y1hk97eZY539sm1guztZpOcmOTBlY

q4db/36n4U/reu6KaHj+sad7cW62Zcdar2RmcphuMPfEPKnBdMhtnbRaPhZbfrbO/68dfQsqG/rB9xq2DbNMQ2yW0N0w9zeYssNTYlhqqompKUFSLmDhhjZUrKkikI+bhoiNHxzUVEfDU5gtZVn8NPmXz2NjG4WM1h/m0bAF9YUBfxtgWILRNmC6Tat0U2QjnNmm760D2x0GbAmmJCza93s3Y6zDii3TeqY0W07TVoo2pqYvz3Qb0Vh+pLZJPa2e

Lct+SxrYtta2hjwl+zUwH1ua25HajojW0bkuaWh6SlrZObaMdqXpaZt5R0PW6sq29LEAAy0HcmPiQW70jiRi7b2NWXcMDtmJF7fhtx3XHrlifR448uh24A3jxfTPvONR3/L6+m471vrt3WIrSiEbS5beOp21aA1749Vev2eg1rxRh/ZlY20r2HrRdyJr3RLufHt7ZV87WU8XoNXTT1du7fVdbqQ7mrPxlxzrQ6tjx27qjoS13c6sQBMnYOoa0tcC

RD2FTE1xZWrAnsZOp7a9xa5zpWsMs8namgpxtbR3FOJGu1ug/tcqdl3jt1TsncKfqceJj7117FGfecvbWSnV9p6zfYmdQA77khh+2qZEeBs372ho6wHqBs/3LnjdueOLbCux0Ybn9sBxwERtlq42QEF1R8urXHZW2UgD05HLCDenLIJ+RCOBAchCBvsT4bAD2sfM1t8MSQAKODEhxjq+2Fwb/AcAxiFzkoiwPMB/lHmLAMzaAbcJ22xggRswIgmN

MFAZXGogSLKtQUerbSVmISZ6j6nWf5UNm/qTZ4VY+t7Mrp2zS6VeSKtbPvt3QO8twQjXJKjm1VJ8yczBunMXzcA85/Goub5okqM0WaI9OarpqWqAMGG1lwARjQxnmaBGwFURqAVnnsHXq8BRRoFqlCYF5QgFaLXCJ8ZhY6yHjnJtViqw+0c5U25XtNjcJCkxeTWMOBf4cAejFjyveohsfm0E36YM2qbHXFtjdNj0cLObvwRhuKyxCKN3x1jc0h43

6lxNxwGTcDxU3RSL+Cr0zfmP/NObhTHm7NoFviARb4aIgkQllvAekDhNTYdKWFTsioldw14WqXlTalS74iJ4caXyU81vhtpXg70yCha3msbPrQjjeaxh3Sb88u26pFdugUWbvt/AgHcd3X6w70dyW4TiTvNYSA8tfGz6KJsXTNa75dWiRcNrdIqLx7CfjRApzCA6IayNWHuZ/ZQzfID6BjGxhSDvgEOIwtsChh5TYIq4El02F+BFmK0nwFl/hmRz

TqUoAIEAvIIPNggZ2yOA9WyrBIGDIS3KzqBPJPaivp5xg2eQ+pfZPrH21gzs8K7sFqv+zzgn9cOf/VCFvB+rkDT67A3arPomgU16EI5IrmtgiwG1yhsBKB9EhNqz+S2H3aAg6Pf8xUg+eI6kcNShrgod6v9clDoFdHWBSG5mJi0asCx3DKbGVR4AoAecW4Ysa55GJBZBm6CBwEIAuxJ4rieBG29Lgdua+mgDS8KmyTsoG4QTy0c5o4CBeFMsiasL

gGrA59iUbiUlEGQARmBwZIwkICIqIWUcueSN2jIse8+YJfP/n6EYF+Ywoo1EoXsMBF4i9FeYvV7uL46QMCJf+3IqDKfnDS/+28knj7zDl+YB5eCvzCIr+4lK9ohyvWEghVLGriUIVJTWad0BGgexZYHlzBB2mpXfIOKplS9B2823fNLFPfh35g1688cAfPC4Vr0dPa8YVOvKCbr+F8i/9fnYsX1APF5G9JfxvkSKb3MZm+ee5vGcXL/l8K9Txivk

JwZWvBICbfLE23mr3t4gTfuoXD5wYnC9GIIvcBEc0D3anA/H5KgPcTQB2CMAzBKBDkDsPi+rbTUywOYBIJuEmCrhIczbXD8qAo9CDvgDcvtrcRjRkeP8UGAKDmZjTtyioO6xlRcCY+oB2V7OVj+K9rOTzuPAqmV9SWbPdnZV5ZpVwrhVfyv1cTgjV1J+1f7zdXcnmkjXkU+3oZz1INT56vNcgxxfcHBnPp90+KRoY6GpIb8BCgQw1giucz1kKdNl

ArPeQ88/Z4ZiOEoFtHHPC55hdBqBYsiISAQF8dQMNRkB3Vu4/HuzeljqAAAGSl/dWAAQgR/VgV90emccfErpI3M/VXnP1kbz/6HCF7ev29D6L+w+S/5fqvzX7r/eEG/L9lBgd7GCzuTvwlM704aQfIaUH0lJwzd9j53esHtnyAI9/CIt/s/g+tWh39NORtu/4+6b338C8nxB/etavwt/y8j+oAY/pv5C8dPVVCBh2L5aT5A+74wPcc8FT6fQDVg7

AB2ApyTQNVqs+ecpAAoewUJ2xZgywODChQROLMB0e61BDh/4kUFuDXAwIEYRJoLxEOw9s7wMjgrAbuFOx8uAeLdSlmzHuoIa+3aOeqcefKjr7SuJggb6qugnsvIdmD7POhieT6uq5a4ylLvLKqMnoBrjm1JKfKb+Sni74KuEAAOiskZrmEJoAIBEkAtyGaOuafyOng65JCUpDXI5ov8keb0arqrkIkacfn64J+Abk54p+wbmn6PmemGcbFu4qJrC

9KMmoNh7IhAMxQfwb8LcL5kUQPAjF4twlVpYAzOnthjwmCP5ymwpKC36ROmmof5WmpcIE5n+01iE6ROJ3AaAW6AsLRg2BY7uBioK6Co4GOYzga4Hhw7gdCKeBuAN4HRkCQf4Gd0gQVnBeIoQRLDhBy+gf6Z0RTLEG9+8QZ5aT+1hkmrzujhuu4L+aHI8zL+67qv5eG6/gnwNSuDk94JBzWrYGZBDgW1hOBgoPkG6cHgXeQlBzsD4HQifgd6KVBQg

EEEoIIQeF51BzAL5aNBB9M0GF+bQaE5JB6qK8oVqf7lWohyQHoi6/Knpq55U+T2DwDgQ0kE0DxAFANgAVs2clWwQBEAFAEjsm6iuCJoGwMFBUu8gTKQTAIUK7jgwjMFBibgkvmDClo2wK7ik42aEASK+xqIx6CuA8sb4iu16mK40BErtr6khPHneqyu/HgvKSBQnq+qieLZtwESeVvoOZKqf6jq4AaY5sfIO+YwUa6RgHRNIF406nnhio4pnmFAq

BkUIH6GekwMlCMwGMOH66BlnqeZkcYgReYOefqmULHmlQnpiP2uILqw1w/dKbCDuIxqO4/eE2H9B6waphXDnuYQM7DKoD/M3iUoWQFEB0w6XApijQIPuF5GKo3DADqw9yL4r+YxojfD6AAAAX1eJIk9Z60xoTEymhz7snqy6FoeHCCy+gNaEjGDWNnCpujoZgjOhaohNjeEuAB6HqI3oQyCEAfocpwBhYmKwqN842KGEUoEYR0HAQ0/nYbJqC7tc

zz+6aqu6oOslLd65q93mIHb+7DLRgGh0sLGHhwJoTkCJhwxsmGmwloemGlwmYXaEg+DobZj5hroUWElhXodmG+hSnAOSBhlfMGH1hzcI2GRhz/m8poAlas6bE+WAp/4vByLvvi/+ixP/4QAQ8JICIQ68JgCaAL2PsCAhzAsh6TqpaCuD/AjMDmDXAEOHyR7AQpMcCfA15otQQw4UJL6NghchOwLsMpBdS8uBZsmzK+hIWWaKuJIZzhsetAbyr6CD

AWQS8el7FwEMhbAcq5dmLAZIE8Bn7ByG/qHgpABeC5HCIEGuC5s74Xy/IG74wcIMGDAAg4UMTQqBzYHR4GeH8rjDyhruIhpuuuoShhqhNnguaahJgY57J+AxAGpR+6fpUCjhMYUYhusHQg85PO71tIavOaOjLBg8aXKXB1cEsJmFFkwPit7JIY3NVB9czCDAj6wgQFGFjhRoeHBGRRIiZFKmzzh9Zjhh8JZHMiOnDZE507nGqaORg3lF4koH8MEB

uR+cB5GV8IgB0S2GVhi2FdBcDlkQ9BaWBd6L+V3lVKbukALVI7uD3nu6TBvkROEb2KDMZEvW3OsFFmRn1k/Y+SlBlZFRRhCgPB2RNobIbxRqCKXDORyUdkDKA7kbrCeRmUfj4v+14bC6PB94fWrf+lPs+H5sJ+OiA8AKcswBVAAAEKYAPcOAF9q+cvhjnAEwJMAtgnwEcArg8wDwIzqc7E2wxoNKtDCnASwGiFbAEwGOoAE1wCBDB4MQj3KMq2Gi

r5q+Q8tQF4EWvlx5UhuvkwFyuAnjRHiqdEcyGG+H6lIFshvAVv78BXIbb48hervyH5qWqi76V4z6LbhQcC5nIFMq+1KASmq4kXGZbm1qtJGRQHLlXKOq+GopH6B1niAqqR8fvhi+qSfv6qp+hGu54QAtGLeDCwrGMgghO1CNkBiApsOBDNeYscGAVIgQFLGZBEXtnxu6ggIDwfCtfOHBEAmIKuG3C6XO/zwwl7sNGrhMUiJqRcN4NfDGxbWPxDR6

AvM/z5wnOuajiGSPq4i2Y1oKICKxKCMrEHIMsUsgZwMNsXCYIe+EUhoIzsORZywcsjSKZRksKhi0IqZNTYRekUY3xRA+sbkj2B2QSWCmhQQA8LX8usJiAcQnKH7E8gMYuJjfS6IKkjlwMFKnF8IimOoALgUYaLHexEsUJAqxAcXLEKoCsRLGlx0se7BBKgcBrEk82sRxy6xMHvaGGxdlABimxKblUgMI+FlbFRItseRZsADsWohhkzsb0yuxvOu7

HTwPnj3FKx6WP7Go8zsMHGWiKCGHFnkkce5ILgMcSwjZwQ+LZSWYycd1Fpx+FpXx2BWQcYrkWeceHAFxozMXEdYfcarEVxcEl0zVxWfH2Rvx9cX5iNxJgjlKHerYfFj5RKanP69B3YZd5ruaDg0oVR3hgKE4OPzNW4tx4sRUjtxJ8bLHyxrcUfEdxA8erFxGmsZrCjxwQOPH6xGwWkrTxJsa24JRHbgvHogS8TbHq87GPbHeEjsZvGjOj8DvFpiL

Isj6exh8b7HHxZcafHRBr/hzyue4cWuFRxd8f5heR0iAnGcYr8XXGxuGcV/FzBv8cKD/xUvIXHT00SCAnlxbmJXGQJtcWDwRecCXLCzRl4a57/ut4SmynYX/tMTvB6LohCaAEGh2AcA6xBGr/hSKoBHhmlwNAQ8kyIWuCIh8ZtMCI4eYJjgYwywMWZLq7AZDjJAnvACAI4ABIsBYROAoWYIud1JQHCunKuSEQx9AVDGMBfHtREygtEab70R5vs+g

a47Idrhaue8p4Kqq9vqIE8R4GrgBKgxMbISkxsgRyQgEHLrtSK4trkyqyhH8iFAxoHwDRoKRegdH7KRnMWa5qRPMUzC5gIBNDBHo95jpFWBLahPFtiqYv0CkAZgGpJqIcscKB9kzgLOBhimtNUAd83DsKiqIKCGJpxkYlh6RfJN4MgzehfCW2KlQTsEWTKcfhlzwTcvfIrzcgVIAZoj0woNvDpgPKDeBGJvsJtKHI8CQSJyWuojshPxEwpzbMA/y

TFTOi30mJBtiDYaVD6AwJpGzPkgKMEGSAaIBQDvJhKfJj6JTcKEArkvfmSl8WHpKPZqw/mNilhAtyTF5vkEOkRYwJWsPAiD2C2GNYPOwqe5AzOgtkjaaQmIFck5ATAHcndYjyXiAUALyXICEi3FlJKJG+FmJo/J8SMKjkpgKUkbAp9BqCkia4KUEDEAUKWuR7usKWbEwIygIimA4KKcEBjw6KTamYpYPNikKcicQuD4pZqRQjEpyFl1ICpAKbeCG

MtCHtg0pp4XSkMp1iswAvkaieoBspHKXGncp/cFcLpeSaTFQqpESuNhipuqZKl9c/9DKlGJxoPKm9M4zs1Ej2UzqqkzWGTs2FHeAlG2HdB6CUVEuGAwZVIr+uCRACVRg4QubDhAsJqlBACcNcm6pLgfqm4ghqcalvJBKZ8kOp1qX8mCpFqazYNRzqfhaupkKaNwwpBKHCkBcCKaQBIp8XKinBpxABimypEaSrB4pRaUSn6JpKXakppVKemkJwtKZ

kDZpidEynhwLKYWnbpX6bZQ8pZaWf4VpQqV2nVpaSLWkSpQPlKmNpsqS2nOwCqd2RKpHaVWlF+s1h4l3BaAgtEf+fiQ+EU+KLmtHNqEAJQL8gQ8IhAOQxAE/CUCR0WGackRhCS5E4q4J8QbAWwPGb2q6HiATrAj8qUk5JRaCFBvAPwMlCk4WwPuyk+9VNknrsrKqr4seorsREUhkMZzjUhjZvr6wx9IS0kIxbSUjEMRFvgqosR0ntyGyenEeqoKe

YgbxGRg2xOMkyBYoYnihQpqjOoh4dMWMAJCVqo66oA24FjChQSwDoGsxmyZSDbJpGjzTGB+yfJnYqhhDqGRZ5yRACj2/CoErYZVieDzjKLgYxEpBNPosoZZx4BJjAw2WTAi5ZB4McxIJeUad5UYwfF2HFR/QUv7jpQwZOnTpG/rOk1R4ROlkRKmWWVk58FWZaB5ZJGb+5kZQKgB7wulGctEBJXVOADUwnRP/BiguGNwAWQ0AHSkeQ84KQDaQuwAw

Crpu0XQFkRpIYSCKwp2fxG7ZZmDQjOg35mKCgxmmdWY6CRQFOkiAV2d+YHZpEVeq6Z0MUMDPZLQjkDXZmQELCGZ68r2a/Zr2ZkC3ZL6uwEXZL2WNAA5+gJDlbQLIaDmXZcOd+YCQaMcxEr4sOf9nfm68JjEeCYOWjmA5c7qgmmoRObjkk5hSlA78UFOVADw56kIg6YJFUTjn05N2VEAmIiiH2SlQxYS0p058OW0CMgXOeVy85D6OIpUAMOX9ls5m

QMLlPgIZqjG9QP2ajmU5+gDCqPQGOTqDyEqYKvjCgtQEKRxQe6nATI4IENsBIE2uWiDCgTQDNSQ44wLcQKZuYFsAcueMBABGAPiPoCrZFYDoiIgKQAsT856Ob9CEkCuYyA/ZdICQA5RuGv0lh5Y5LP6R5rGW9yC5Q+MECbJx6AxCfZHufVC7RuIJB7KAVIAfC3EBYJ/IF5+eUWRzsqwNcH1QVWj7GVApADnm4AeeVoS8ADeVjBIgqvn/gncvucrl

/g86PjmTifOQ75CQ4YJZqV4aAEfjZAieXhjzRFUUQD5YV4fcH1QSyFkA6oc+cpR8QgxEvnjZEAJFzbZTAHl6L5s+Rvlb5mIKQAJ5dFCDC6ovuVekigSyHABPw8eUsin57yp0RbkjAE+D566eWaTy5YQEGklUpEMCIGAcuTnILmpyV4km4BgCKAZAXUoT6hAATM/kIAr+biDECvuY4DDYdFDiA6p54E/DZAQgLNlgqAoNXjug/9CAAmQQAA==
```
%%