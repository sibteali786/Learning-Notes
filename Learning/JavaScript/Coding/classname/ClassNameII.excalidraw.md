---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
export default function classNames(...args) {
    const arr = args
    const hasSeen = new Set()
    for (const value of arr) {
        if (typeof value === 'string' && value !== ''){
            hasSeen.add(value)
        }else if (value && Array.isArray(value)){
            hasSeen.add(classNames(...value))
        }else if (value typeof === 'object' ){
            for const [key, val] of Object.entries(value)) {
                if ( val ) {
                    hasSeen.add(key)
                }else {
                    if ( hasSeen.has(key) && !val ){
                        hasSeen.remove(key)
                    }  
                }
            }
        }
    }
    let [key, value] = hasSeen.entries()
    return str.join(" ")
} ^eq1YjNsv

Version 2 ^DgHpFQmW

/**
 * @typedef {Record<string, unknown>} ClassDictionary
 * @typedef {Array<ClassValue>} ClassArray
 * @typedef {string | number | null | boolean | undefined | (() => unknown) | ClassDictionary | ClassArray} ClassValue
 */

/**
 * @param {...ClassValue} args
 * @returns {string}
 */
export default function classNames(...args) {
  const arr = args;
  const hasSeen = new Set();
  for (const value of arr) {
    if (typeof value === "string" && value !== "") {
      hasSeen.add(value);
    } else if (typeof value === "number" && value) {
      hasSeen.add(String(value));
    } else if (value && Array.isArray(value)) {
      const newStrArr = classNames(...value);
      if (newStrArr !== "") {
        for (const value of newStrArr.split(" ")) {
          hasSeen.add(value);
        }
      }
    } else if (value && typeof value === "object") {
      for (const [key, val] of Object.entries(value)) {
        if (val) {
          hasSeen.add(key);
        } else {
          if (hasSeen.has(key) && !val) {
            hasSeen.delete(key);
          }
        }
      }
    } else if (value && typeof value === "function") {
      const returnValue = value();
      const newStrArr = classNames(...[returnValue]);
      if (newStrArr !== "") {
        for (const value of newStrArr.split(" ")) {
          hasSeen.add(value);
        }
      }
    }
  }

  return Array.from(hasSeen.values()).join(" ");
}
 ^vBYPqE67

Version 3
Deeply nested array with object can cause issues since each recursion has its own hasSeen set ^ZKjXCl8k

function flatten(arr) {
  const result = [];
  for (const val of arr) {
    if (Array.isArray(val)) {
      result.push(...flatten(val));
    } else {
      result.push(val);
    }
  }
  return result;
} ^ok1u9Jen

add flatten to flat everything at same level ^BfBAbDnz

/**
 * @typedef {Record<string, unknown>} ClassDictionary
 * @typedef {Array<ClassValue>} ClassArray
 * @typedef {string | number | null | boolean | undefined | (() => unknown) | ClassDictionary | ClassArray} ClassValue
 */

/**
 * @param {...ClassValue} args
 * @returns {string}
 */
export default function classNames(...args) {
  const arr = flatten(args);
  const hasSeen = new Set();
  for (const value of arr) {
    if (typeof value === "string" && value !== "") {
      hasSeen.add(value);
    } else if (typeof value === "number" && value) {
      hasSeen.add(String(value));
    } else if (value && typeof value === "object") {
      for (const [key, val] of Object.entries(value)) {
        if (val) {
          hasSeen.add(key);
        } else {
          if (hasSeen.has(key) && !val) {
            hasSeen.delete(key);
          }
        }
      }
    } else if (value && typeof value === "function") {
      const returnValue = value();
      const newStrArr = classNames(returnValue);
      if (newStrArr !== "") {
        for (const value of newStrArr.split(" ")) {
          hasSeen.add(value);
        }
      }
    }
  }

  return Array.from(hasSeen.values()).join(" ");
}

function flatten(arr) {
  const result = [];
  for (const val of arr) {
    if (Array.isArray(val)) {
      result.push(...flatten(val));
    } else {
      result.push(val);
    }
  }
  return result;
}
 ^lejOBZbS

- In this way we flatten items first and then only process them otherwise we fails some tests like

 classNames('foo', [{ foo: false }, 'foo', { foo: false }])

here since array has nested structure the hasSeen would be new for this recursive call which 
if we want to avoid we need to either not use recursion at all or faltten everything first and then 
use our current recursive logic. ^kSDtjuC2

GO Over solution in GreatFrontend for ClassName II
- Its gives perspective about recursive call without flatten array method ^5iYoteA7

%%
## Drawing
```compressed-json
N4KAkARALgngDgUwgLgAQQQDwMYEMA2AlgCYBOuA7hADTgQBuCpAzoQPYB2KqATLZMzYBXUtiRoIACyhQ4zZAHoFAc0JRJQgEYA6bGwC2CgF7N6hbEcK4OCtptbErHALRY8RMpWdx8Q1TdIEfARcZgRmBShcZQUebQBGAE5tHho6IIR9BA4oZm4AbXAwUDBSiBJuDABHeIBNACsAOVM00shYREqoLChWssxuZwBmAHZtRJ4ADhGZkYAGHniAFjnJ

gFZ+MphB5bntdZGlteOeOZGANh4LzcgKEnVuc/O5m6kEQmVpbjWRjaLIazKYLcF7/CDMKCkNgAawQAGE2Pg2KRKgBieIIDEYvqQTS4bDQ5RQoQcYgIpEoiSQ6zMOC4QI5HEQABmhHw+AAyrBgRJBB4mRCobCAOr3STcPhgwUwhBcmA89B8iqvYmfDjhPJoeKvNh07BqbZauagtoQInCOAASWImtQ+QAuq9meQstbuBwhOzXoRSVhKrg5kziaT1cx

bR6vVKEAhiNx4jxLvFJktziNJq9GCx2FwtacRhmmKxOI1OGIJXNzst1kshktvcwACIZbqxtDMghhV6aYSkgCiwSyOVtDteQjgxFwLbjM3Ok1r0zWSyOryRBJj3Hb+E7YO6mF6EiwcGRUFQxAQ7c9J+ZJOwUGzqGw+FCzEauCyzAAFNpv/TlMwAJSoMAAA6HCoOBD6cBCqD0qQqAALwwaQf6gRBkEcNBkihBy0ZgYh6oUKgOFQB+/6oRBzLIqgH56

BhJ70AQQgIKgbDMkhpCASBYFoRBhBsR+HQIKxqAMb4zHwRJqAAOSCj6yhSagABkikiYxzEAISSVJUn/lxPH6agWHMDh2TaLgxDEB+olMWR3H6QAvkEYSoHx1HWcxymoAAgqQ5AwNohDMD5flWWp/66eRBkQUZJkcGZFk0U+Yavu+X7fu54WRTxjlbsxrmhWJqCCcJEmIVJdj1Agt4KRFdlRaglFwbR0H5LCMDUKp+D2ixbEAPKaJVt7aNkkKEOEB

U2ZxWX1bx/GdagU11TN+kxbh8WWW1tnLdlTnMXp20GflhnYWtRkfptSkqepokLftB31atpmBPobCMOdCAwFt93ZeB03LfZf0OYDqAA3VoNocEJ6tR9HXud1iGPXFI2kGNn5feBgRQCIYGCto9RsD6H7ARAqDE7Z9lBpQAAqPSVIex6nueuCXg1N53pwD5JS+b7jd+ZnIQBQFZc1J6wQhSEoXVIvHcZuHiwRREICR6MNVRNFQfRak9exi1RflxVse

5CFabJHDyZdnVMagmllTpd0PSdpnmZZGXAzlzn5UbnnBbg/mBT7MATQg4X21FiPrYlz4pbz6VhSraHu3l/FGwbxtlRVVVQDVocGY16EtW1sMEN1wn9YNUDDTkKPjRluvfUdN11990WO3FzvvZ9wNRYnQtLfXc3h2dF2eddBC3V333h89r0IB38fffZv19zN4P/W7WWr+BkN2oXlsIPDMuxZXo3jSrmPY6guP44TxOkxA5NMpROQcoQRjiLwJplE/

UAAGJvmyhpUDph3D0LyRBlA5nQMEZkvQCykDvO4MBHxIHQF1EyWiUQfRMDdGgCM+AdQo38AQGme46aYCPPAxmF58BXjZveR8Uceafj5r+QW9tpZi0Qqw4WGtD5y3wggQixFSJZTzurOie9tawSbjxfW8AhKGy1qVaSptzaeSNjbaSdsJ7gXDu3V2y8Qa7RcsnLW3tfK+wCkFCxgda45xWq3CODDkpMLStoWubtjGey1qnZR5UBqZ2zjo1WTVeHQ3

ap1EufUAlDWRqjIO4Ve7NwbmPGRzc9EJU2sEhOxj7EHSOoPUIc8Laj3wOPQx6THHTzelkip/0l7N03vVJpCcN5ZW3uEouYkD7hziafLK59SA40hHjAmHAiYkzJqBCmrxmZQDYAAJXCK/d+kImIriwQACXeJ8fcqB4gpD+KaIyJCoAABkfTQg3B2BAGyOBXNwZ6fARR7KbBKGUCoEgGzKE2XAH+ABFfQwomSCS6LTV4Aw0DOCmOMFMSwRiJGeCMHg

QxEhrB4EcrY3xzhLBSEmU4zxaxLAxYkV4dxiAPC1OcIY2gliJGRbOVMqYfjAOOTsr4aAjgJAuAioYzxJjxkrJKU0gIFSfwEJCGU5JkRoixJiJAXZ8SEmDGSREMqqTkAwnSBksCwSsnZHKBU4JETKilJKkUYoJSvGlLCQ179jX8hVMINUGo4w6j1AaOMxpXjmjHNaYcjo9UugQDg1AeDvS+khegXA8Qgw9mIKGcMTzrXRlbKgGYiQKx0vFQwQs2Zv

jCrKJmIsHASwcDLLmAVqw0XxBzYFJskN1xthuV2eN/ZMgjQDaOcck4m37JnHOJYkxFiItJWCVcsI02bm3KaXceyIAADU80c1SCqamtMJBLqzCux+nAoAvzftwPlCQljLHnJMc4axjSTERU6Pdf99AAO+K8OdSCIGVGgbq00mYEEEDfSg+ZcB0F7twFg0gobw1gmRB8H0xCN3oC3SW3gTI5mLOWYetAazbnjq2eyvZByMWvBOT0C59zrm5TuQ8sNT

yXlvLBJ89A9AABCtQAAKVReyphBfIsFpCIWDCeCkKYFZEUjHiLOEYfLXiAJxckJcOKpiJFPVcVFZLLW5kSKysokg8Nxh4IRsEor345ptfCNVlJ0DonldiRVBJfWkmlRZ6AmraT0hGo/NknJuT2qVLGa15qECigpeKNAhaJVCllN5yovm41+EkImt1UGPWwC9Tm31VobQFEDaaZ0PMIPJvo5G/0+hYshldY8yMpowh9trfEeY8Yjh1jBMW/NaBb3N

eXaW0s79a3TESEMZYSn6wNqVn26d2HTTdhJMQdtg5chZe7ROKcWoB1DEXHy1FQwVxsDXFOltIDSESAUAAKmO6hY7qAAACgkzxsWAEsvQpBiAAB5VEdRJNCDgbAKAcAAHyLzhFzBs5h2YcHpDAc7V2bvniAgHZ7gPnwLrUv91ACOwwB0h9d+Rt2gKqNQAAH2o/oTQTACfUfZGT7siIQhgUJ9N88WDiBk4/KRBCv3UAfa+z9wChO0eNhB9mcHZO+cB

wB1zJHYlzsKFAqBE7Z2wIXcu9qt8QE+Z84l0xRe3CFdXcGRhXHo0zbg2O9L9U5CGa3eZjQ1m5bQec0YalFhAs64cN8uLVhABuci0tEby0EYrZWXvuJiOlkbYS0ikmzWoqnI2yjiaqNvuorWmjiZk0j2hDJLswpB4TqgLx/EY9KMksTD0xOmCJ5UhldPLdZZOwSlyFGZsEn/hzxBRe+e3JmJUgHKxAdm/V/AtLAiDfgri2cdzR3scxIt7+vlYfkJR

8p4gGnvJIfeFh7YvP0gwVtC0iICRW+ZM0k8Uzwk1vQM+5NPb7lExnfCqeUL4VOPEAM63hX39NfEjOmRO1mXTOx9q5Pxa4B8o8Cpj8M9HF25Npz8fpckJ58pClPxh4rpRJwCT9HEzxG054YCL9u4/or888b9vF78VJH8rZn9rxbdsx38+5pY9cNdxI95SIcD84Twt9R9EJx9o5mFvx8h6C1J7QZ8+459BER83cl8aCopP9oIN8w1RCF9fJd8fA1AJ

k75Ek8ldFICEoMoWDwIWkQY2luJQZyI9dvIbFtBnQDAPxw53I0Z/xRkb5Jl74g9QZKYKBTlKg5dMdoc7sHtkQXs3sOd7kuc/sxdnxgdbxBdSAIcdcsdEAcdgA4d1dkcwj0cbFvDscYdgA8dCdS8Sc4JcinlKc2BqdrAyd6dWR1QmdCcWdAJ4J2dOdvsOAedUcgcBdOAhdecuZRdWjEc1IpcZcbBTtMdld9BVdvxkixItcBZMc9dmADdG9lBjdTd6

ZKFLcWZKDIiOYuDXEnc/wXdeFOEJZmBW8fdW4/chElZmDyJpDNZCpw9fIZE5FEBhJY9i9wRDdlAK9JEJD74QDT8dCN5CCPYC95FXii9EIS8hAy9SBviq8c5T8G85Jm8YDr8QS78rZzE/Je8bF+8c4h95Dt83dOCuZuC3FAThD+J2DxD3jJDc41ZQ8tZhJqTSAlD99VCj8QCIDa825tDs915L8gSO8g4LYyDxJ3jX8oA6S0Jbid4YYf9S4YkK4+kg

C44uTb8wD1TNCeSI5oC3ZgS9p4D+JEDikR5UCtSa8j5MDRtsCJ59C9D8ChSiDTESCiowTFEn93jNjQdpSII6ClZsYGDxZ3JrjaDeEWSx9STdjeD+DukhD9IRCKAxC4Jfi0DZTZCWS2SVDD9740DtSj59F+TDF9Cr9yJjDuJTCe9LD9BrDHFbDSJ7Dr5xkcyhDXC71n4Vlyx2zf5/58BAEtN2hQFwEUFP0mQf1zA/1hyug0FXgMFQN1RwM01INTRo

MiF8APCjthjYifCgI/CntXtPj3tgimiUc+cIjQdwcMj4isikjxcUjei0i/IryYwsiciid8iyc8FijSjacgjbtGdmdWd6igjPsmiWizz2iwdojhduibFUjmAGCBiOBZctzUBFdRjxjtBJjNdjjZiAyhl5jsjPjljQJViTx1jrdvT6EozJ9+Z9jI9Xc4IuEBZTjeFfcBFLjA8biGT18mS2II97ZniFFJFn8E8SYk9CpUz/itCs9p9USDSNSxS04748

jy9xLK8wppKdT24kSm9a55LhSvZu9zD/ZcTgD8TwzCSOD7cXFaKKSEyqSrKaTITl8/jV8eKJEMynLWS99synD1CJ4ASiy8DBSwYFLiDMTSD3SRKJSlTfTwJZTv9RIolUA/9Ykq54lzLgZiC8y+E68NoPp4yDI0TDS6kEDHEh5CqSlzSNDLS1prTuhbS6l7SDDQrc9DKu83SXiPTyCvS6FOB4rWDUBYzyCmCiq0ICSkyFCmKbKJ8Y5tA+D8KOAGDB

CWDEzkzrZaS3LgZ0y+K5CpqiSfLlCD9/Lcqgq5KBTcC28yzBiMYlqzDsTqzaydT6zwoHDmz/KXDQIUMhB5kllWAMMipSB1kcN1RtkPgOV9lDkiNQhTlSMqNxtKN3QaNShXkih3lIAGMIAAAtAAaXqAAA1AdJgrkX0eMqRwUwQo1nAkgaVzhEglNThJgb0eBEVZxpM4x6UaU1ghgUU0ViV4gfgtswRyVKV9lUxcVeb5xqUph4xMVIAdMIa9lM1Zkz

YxV/MItHNZVrMFUwQ8Q7MVUtaNUaRtV3MnRPM7VosTU/MzUIsgsxawsPiItLbeRrbYsXUwxEsVzktAFa00tiQMsu0g08slyCtTQfQzwo0IBrBSsE1ytyd8Eow+0VhDgJh4haw4ES09N8wOtt0uty135iUL0eaJhzhhtmwxt9tJs20BxO1kbKsygxwlsatVtLhiU1h2tTQJ1K6KMDt51EN7whhQImwEAfAYA5CIQYx2JfZUA7h1AWIlSHwyi8AhAP

YwwmJ5jWAC6898RJBhqqoRAkMjIXJcgWIfs8qcYlY3CNyENOtUAh6OAR6x6J6Wxp7x65697JSl6wIV617mAN7L4fQxAd7sA97AhsBD77xj61B5imiL7L4r7uyD134pM9V71ezAF5boAhzkEP1zwv0i0mBf18B/1pygNZyQMwN8sG7IBVzYN1z4NF076H6n6+yX6p7YIZ6P6F7y5v6l7V68p17whAHt6QhQH96IG86ZYT7YHz7fcwgCGARfq0MAbV

lgaJsygiAwbdMtRoawRiM9x4byMwhaN0b6M00X9oR4ghBEgAApbIbjToCmvjKmnYRIAjU9BYCYM4GYNYdmsEQBRYZMWlRldx2WsTelNTYLI9OYXFCJtMX4elS9S4LBxW3ZCUX4VWoEYzDWqVczbWuVJkfW5VeNI29AakLVNzRkc2g1KLV2x1W2mUe2kLXgXJ21OpxUN2p1OLBLLUd1fET1I0f2i0f1BbYO10UOmh8oIrCQXANgWO3phOlNGrYdCs

WtK4Ac3NPOx4HO79TrMtCtftUYIYYdI4TZ+tCuvbXu6u6bWbOuirRO00Ju3tNNOrC4OcRMdbYWrunbSdYxjRwcw7dAKijmZkJ8GQbID8AS73XhQIf+63RCB0VvXaspB4jiavfKHvUykKVA4/OFy8bQOAVeyQNxMFycbocZXFgym/HOfFmhQl4lsA1Em6is+6ulqAFw6+xhkFsCMliF8ZaF7if0+Fk8RF+0ZFjymQseNFp4/iLF6xHFggAKvudlhl

5gElvmPlilsA8akGBS2l8IAlol9Vplwwh01lrGIZfekVzlpBzs0LHNb+B9J9NALB19KciQUcuBYh0hqkGcsEOcqhyZx5soOhsHBhoFlkfq3l8F7VwVwfWFw1hFu0cV7iuCcRKV1F/ix4jFuVkyhV32HVkA1V41jV78LVyFqlp05yA1kVtVkl1A5lowkwtlpNjl6ZH6v69DNRkGru3DJWuMPR45WGkjS5f50x0oDG8oCxpjZkJjLyTQBsDgIwRx+1

OdJkam8TZIJTSsZMMTIYOYHmpIDm0LEu7QBYSYY0A99O+FKJsWmsPYBFelGsS9FFGsTJ/RnR3gLBozEENpszCkAp+VIppVezVVQD42ypnVDzWp+UHzLpxpi1aJ0Lf9l2zphp00VUeLeO7UJLAZlLIZn1AO0ZtAEccZkNYNiNSO/0chsEFVRZ5csoarV59FGYE5juzZlrTgOMVBvZvOg59+YdNYC9JMcuxtK5mdMoKbPsWuoceukNyAZ55bftd5vl

FFKYS97bXbf5l9Rh52BqWN7IIqNgAzycPPTMGAdQOSGCE8ZgHmVAYIRgfALlyN/TitsCeZUzk8BACzqzs2Gzy+ezxzoIXdDswG04bs51vs59Pu31qBfBscohickhj18p/100QNhc6hhTl/Qhehm+6OiyLzil4zrz8zpgSzyQazszuzrIBznzkL2ZZR/6+1oG3tzR/t9J3RgzYd5gOGsd5tXKCd4ocxyoaEDkBsKAeoIQOEVdHccm8pym00amvMc9

qtem5MLxwWrBwBE59O2ldTucQ4C9HgJrU0UWlp9OwTI4Y4J4FYFJojL907n9tWnJxDgD9VSzHgZkRIBAJcEDg20p/JyD1zaDmprzODq2jDpjgLZpq1d7tDh1U1TD51bDz2vpvD/UAj/Zb1MEdLEjlNp0YNbLqjv0WZlEbpsrdHpZpOtNY4NFFFRlTO1rVAB95n4sbrOMU9dFYTxYM7j5RsS5nTvWmujtOTh5xbF56cVTy4UYZmnNbuiTgF7ByN5w

VAS0Dzqr+YigLh5idzk+zIeY1kFgUWUkIqHTMCTgNhuAKEMQMMc3zIFidQJgO4ZyCgPX0DLcS+AwZiboCEeYogWEW6nY1KKSSiNgKSDqfIYAVWNgQb5yV5aScPyPoCWP+P5ieyQQwYnTQIER4Bzh8e4+0MV+wUIQW8EQX3nTeBigYQfAJnEnfakJc3wKCRyBxgJeinCgKr8R0CVyd32e6wE8Tz3AegAmJnfv9UKezz94Z3uCL7E8AR1vqRszggVF

uCTcfl8r6Ivz5QBqQgE3mCM353sCUCRf4QJqEQHVJf1gdvpEVQbAbQFz+dNXjX5v7X3X4roztQQ3vfg/6wJnY/ixA4DW9beGoB3mMTYCz9XezEfvu2DZCb0feRUcIKfUD4IBg+NFcaGHxKIp9o+afBqDchBgdQsBEfDqDH3D7p8QYWfZChwBz7MQt6+fGxNI2L5T1S+5fXPs72r6196+zEBWHnCs7zFwGbfZiO4DKRd9zAe9XvmxH7468cgpXEfm

P1no8DU0pXGfjnzDSQCOczkQQcv1FgU4qIG/Erg1235Vd/OxvaCP/wd4n8PQzkc/g+Ev4jRr+hAW/mwHv6P87W4XTZk6wwYxdZ0ODd9J6wS7etkucXVBLRwy6UMsulHKDHl3DYFcX+mvFvjr3fp69DOYEb/voCN779zBR/C3kAJAE7YwBzvCAVAMCgwCPe8A73nVz94oDCAQfagbNTJLECcBZAkohQMT5NDSBeA8bJQNsigRaBefZiAXyYHICWBa

yNgZX2Yi+4a+nobgY3z4Fa9HB7fEQbPW74SCOAffGAYPzkGj8SAiguQlPxM6qDSc8/TQcxG0FIYV+eg9fgQE35GDKu1nMwabwAG5DT+NgkQHYN8gODzhTg5iHf3MBuDDMzXbttwCwx3IEA4NLrlDR67aYR2hjAbvgKG6o06M4dCxsEHqC9QmM2NTQByFXa8ZFGEATdpegSDXo1sMwQWgilw6mhAmOKNYPsEXDCc1sCwJ4ENhFrqYceJzbQKinWAd

0fgcwAbNCIVpftesOaX9mgBMwBYymEAKzIU1swlNpskoipqDzNp6oLaHTJHjbSqyw82RjtUzIjxizdMPatoSkaGx9qpYiOIzTLKR3+CQAEAawdULUDOSNAGwbAXqAumZBiYAAso6J4BsBzg9QCAP8GyxfxieUQ8OjM2jR5BKecdanoxwECpo4wzKRFKsHmDs9IE8QdOqmIE5xgkwftJ9vz0xqC9xOwvG5jJzF7zYJeYIJTi3Rl4ooO6ndTRr8x7q

SdAW86LwtuUyK+Eqo/hA8osSPKgUfsp5NolsSgoxE0KUODsbDhsTw47yYkQcc+Axztjryd2N8qpQKIJ1vywQMonTl9CVEp6NRICg0WPLc4YK4RSCp0QfIFsYA8FRCgrlNwoV5cY4pXPSBVzAA1cM4nCtrkfFzEFickEimbgoTkUmYGxaNg0OjJ0U2EMLCREcXc5QtncrFCROxUb7CIiqKLK2DK1zbR5oqbxFymJQtgaItqx+c6jZGpbokBIWEiEi

pWhL5E4SmlBEjJQ/C6VlAKJatknAxIeQoq3VGKi5UlKDVEqu8ZKr/iVIAFMqapPJDlQtKn49SxZfVkaWogmlkC1sGqsEnDgNVZ4UkleJdWygsSNSRlLqsJWwl3weWg1f0pa2WpKIxqLBSahtRJIO5xoI1YOGtUcoHVF8BE9UqhOYjMlvKWZE6moTOr0T7KxVR0mDBZYttTJD1SxE9RsJqQ7C71Dks4WmSDEeWn/AVjm32jCsWYYrCVum0ZJZsdYG

Ej8PKz7y4ti2bbetqS1SE6sSJpVfSCW0ZaNszWrVO6mFPZZfUuAa6dwowzbGPidy92LsfuUCKNEBx8Fc8lEVHGK4ept5PorOPgoLjupE4oiosU/JUTSchRCnITipybjfyFRACvuLqKHj+xzRE8WGBGkdFoKXRecXBQvE3i0Kd4oYg+PQrPixir4iYu+IQDTFJYX4paoRVUR/iyKVCK3LQioLbEMBPBcCQcSgnElkpsE/YvBMwjnEOKAeUMglUlZ3

E0J2bdFoJVBKcSDJ8eT4jRMkquS6J2lPkhdTCrCklKz+VcfjJshaUCy9eT4sxLJnOk2JopciZ6W4lxVtqfcPifKQEmKly4wkmuKJOyouk/JxMgqp9F0J6s4CZVY0hVSKQKTSkuVfMvVQrpNUNJxZIKe1WZkikH8bM3qi5SMlcz9IJkwMuZJDK6sE2EiCMjZNsp2SlqDBS2RqQjJSV3K2U3ivcU3xeTfKPkzkrVSIkOTNJrSYKc23qH70wpVZKEDW

SiliQYpTZOKa2USkgSYJ8bIauy3FhIs021EHKVIlSlZRMW+bIqUqzxalTS25U8lpW2LlVSSpdbMufVJDnmsmpF8FqQlLaloMwuPWMuu3J7KPpouaATZu61wYBCYEiXeBMENS6hDgMOQectglDGhsYhcGSNl1PGnzS9yARQ8iBRCJzjjpZ46Is+QSKTSwwDBbeZeP3mvlPiS0mEktLWmoANpNOcojuJ2nUQDxm8sCkdP5zDjzxIuS6dhTQG3jBiy8

q7BhWelYVXp705gHhVMnfTiKSFP6RRUBnDjQJtFVhODPMGQyU5cEyCXDJ5IXFEZKElGZInQmYzMJ2MiibjMWLUyNIhMv6AHN1YlVFK+s8Ui5SpnqU94hE+iYxMZnazSJukimbFXLi8SCFSVYuIJIFkqk8SIsu/GLLpkSynZehGSbLLknyykCVVM0kqwtIqzTIqk9Wc0iDnXUmZPCzqnwsNnRtjJibUyUGUQgWzLJllZyZDJD72yLFwVWRE5I2quy

dqBCrynYqOrskWy0itaIWVJkhUrqjc1qqFIviRyrCMcjeg2ViktlWpoEJKRgoxlYKTw6czKVnIzZ3Fc5KSuqAXOxLYtC2xU2tka0ZaasKpVbAxdVJ4i1STW9c4OaEtMItyOAbZQEV21UYgj1GYIiEZDQIypNYR5yeEeNmG5TssaiQegFAAACqcIYUFABGC4iJA4DKIK9w3aDAgm2gSTGig44VgGRNYE9rwErAHJR0CKPxvTQmDfMygF3bMWtnPY3

tkU4mS9PSkdppNelN7DZfpmmCHszgPwK4Fk3VrvdJRqIb7r93+6yiwOColzKbWqYqjYORqfUe9zh4ocEeao+FSjx6Y4d+mWPX2rj1ND49LRdoa0RgDtEIAHRTol0W6M9HejfR/owMUTxDrydSeUdScAs3joY12gC3IYP8DRpVZ4xaAXmnSkZ76ZUxR6SsJmM565h6a8KNbCyPDqFjRsSvVtLc1k7liaeTzHtMpzeazg1O0q+sZAC0ZUZYxEARXuO

yRFmMURlQNYIQFqCQCEAXkeZWTScaLcXGy3NZXShSBzB0xJKIYHykuCbNAEAtXFIuGpR0p4UtNY0bcDZFiZcUc4JTL41RQVgBRbwAdq6xFErKxR/7QFQgD5Hp1Y0YKw2sD3KaQqqm+I/VBDzhUIdNRdtbUahxRUVqygWHRZuGpfymjCOePYjvirI45YQxDKwrNR1mb0AWVMYsOkx15Xi1vGcKE5sKq1DHAxVBdbMWin6wVhLgYneVcWKk6i85sSa

KZlWNeat0UwNIrBsavT66dI2AAcV6ipVMw3vXwHbh9CoBT1gQScD/ChA5BsgTOPOHzmjjq9LQoEF/qfVUCMB5iiAFgIgEiLt9cAU2NJQfSzBLDV+s9NQJIGEBXhUhb9VAFkHUBsANR9a9dGeovW9Qr1fIX6veDvUPqQgv8F9RS3fVURP19nS0D+pcDq9/1PwoDYWFA13hwNkGxYcILg0f0kNyU1DehsQ1YbIA38ZBl2W7lRdMGJ6qACEK9a50fWE

8wDFPMwSRCe1K5BeRG3nTnrL1pOQjberAikan1FGt9U3xo11c6Nv6xjfMQA3CNgNtITOD8JgicbvhsGzvghr4368hhgmzDZ2xUatdQRoNcEUKKHYwi+uo7MjOnxGWjcJAawJdlAFsY6ZeoCy9AEst/b8YoUVwOIJpnpS/A1sSQJJjt24CnocUtKK9DzSJSIoh0d7FprlpSBDpUwB7dummE2YvL8MGKA7smHu59YEwHqv5W90rV5MIOlmLNQNgGwA

85RDmAtc5hNrFqYOZa+DtD3CxNNq1yKyHvU2R71rUejazFYMxx7DM/UHaoMSJu7UViwxfa6NFQCjGLM2V0ADlVyuWavMPVPwBFIOinX7J0xs6w5kkEWBTArgKYFdcp0Roi8lVZYrdTlx3XS8tVOKZFPpguV6r4Rhqo9QiJMamrJ20W8plTBGAUBNkMAH+AumS0q98RK3FFCkGZFLrKwKYOrPsqLpjA6sVaNbM9wRTVbuALWp7i92yZ/sAVU21ECN

pzXjbwVU2xUVCpLWqi1t6HDbUtqQ4O0a1Yu9Ue7TR5Gidt2PP2uaIO1B0u19K07R8nDHR0hAg6sHQ9u4CSZDgJulWrnSzqcpPtPWVFM8A27Lr6Mcq5TgFpLEzZlVBuysequrFQ6aw8YNFFpz+bHq+6lQJ/sHvcHvwIuEm7wa62k2ybAh8m8eUPLS5hCygmXWeWpvnkwZYhjDXzS10BrO6Ou2jZNVCP6Vha4REW5HQgBeTgBss0dOAHAC5C9puA7y

aADpiyCVAJwpAUmkUAYBjQKATGUDvmqG1SjmQI+0fX0AgCSMdUloboPoAbyDbPuUo3nWNs2AT77BOQafZkH72A95RguotWD272T6RoG+/QD/FF3lroeq+z4evpn1z6pdLTQtJfqn036AseoutY/qP0z6FkW2jFQfrX1QBj9vUFtXtpX2H7r9mQH+Og17lSbf9V+//TPogMdzxNKev/cftOSx6R5IBlA8/vpAybfI32HTOZHT3v6wD+gXsKSGCj4G

QgFjWCN9nH2gG4DmQCg+4QW4QAVUdBrA+AeDRf6FQjHcENgChDsgCaBaMYLbr9o7KzgN6FfcwH4OIh8AtQQYGtiHTaB0UHy5lKd1vbd6jAJRErGgCnbuQQQGyyTHyKWDDdiDDB/QF/umyLNWD8acfUSBIBiaHWK++w8QC5Cj0fBkAFwx6Mw0IAyDEG4IAqu70uGymU7JjIiAsbIQ8QH4RYPmF4BU64jsRvYGsH/BMglkygT0PSEqCRHcA0Rg9h1B

RQvBeAeR1AEkZSOmH6Dt+hAIAdBzu7gxPMJZL6EWJN6wQ2Qfw32nz2QBHwhAIDJhi6Vggwcbe3o+11oa/UtGPbZXvoHpCwhSA0cTpcMYgCTHO9TAPw5oACNzHK9qO2hkqWMhg44A3hs8CsbWOB6yg+IdjQgCpglFnOuh+bo6vBAZBhx6CVevMn0BUwFuiOxsYEa7UGAcIwQB48cc0ahAZNYG845cfk6mHHAdnVY2ZlfV7gPR2QPXZFrADcqWQbIc

IE3vsggB7IQAA===
```
%%