---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
Deep Clone II ^ijuezHUM

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
} ^nhP5Ww5p

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
 ^MdLCNMGH

- first we have t tackle undefined
we can use both 
value === undefined and typeof value === 'undefined'
simply return same  ^GEWpOA8w

- Date
for catching Date object as per gemini i checked we can use combined approach of instance of Date and isNaN to check if value provided is really a date object ^8c1KyZcr

isRealDate(value):
    return ( value instanceOf Date ) && ( !isNaN(value.getTime()) ) ^JCwOhOGG

- RegExp
since question specifies its being cretaed using Regex constructor then
if isRegExp(value):
    return (value instanceOf RegExp) ^qiIn9xwu

- Symbol ( as value )
typeof value === 'symbol'
as per mdn symbols are used for hidden metadata and are unique so yes we should not clone them  ^mr8l8mAR

- Symbol ( as keys )
Object.getOwnPropertySymbols(obj) would return an array of symbols, we can check its length to be sure ^uqys1Agj

-  Circular Reference
For circular reference i have seen some examples like using a recursion
we can use weakmap in recursion together with Object.hasOwn to check for circular reference and return true or false based on that, not sure about the action i would take since question tells us to keep the reference i don't know how would i do that ^2JLtKt9B

Protoype also needs to be copied ^geQsCey3

Likely Interviewer Follow-ups

"Why WeakMap over Map?" — WeakMap keys are weakly held, so original objects can be garbage collected. Map would prevent that.
"What about functions?" — Can't truly clone them, return as-is or throw
"What about class instances?" — Prototype not preserved with {}; would need Object.create(Object.getPrototypeOf(value)) ^YDhrYPEf

Official Solution  ^ikvFzAq6

function isPrimitiveTypeOrFunction(value) {
  return (
    typeof value !== 'object' || typeof value === 'function' || value === null
  );
}

function getType(value) {
  const type = typeof value;
  if (type !== 'object') {
    return type;
  }

  // `toString` distinguishes built-ins like Array, Map, Set, Date, and RegExp.
  return Object.prototype.toString
    .call(value)
    .replace(/^\[object (\S+)\]$/, '$1')
    .toLowerCase();
}

function deepCloneWithCache(value, cache) {
  if (isPrimitiveTypeOrFunction(value)) {
    return value;
  }

  const type = getType(value);

  if (type === 'set') {
    const cloned = new Set();
    value.forEach((item) => {
      cloned.add(deepCloneWithCache(item, cache));
    });
    return cloned;
  }

  if (type === 'map') {
    const cloned = new Map();
    value.forEach((value_, key) => {
      cloned.set(key, deepCloneWithCache(value_, cache));
    });
    return cloned;
  }

  if (type === 'function') {
    return value;
  }

  if (type === 'array') {
    return value.map((item) => deepCloneWithCache(item));
  }

  if (type === 'date') {
    return new Date(value);
  }

  if (type === 'regexp') {
    return new RegExp(value);
  }

  if (cache.has(value)) {
    // Reuse the clone to break cycles and preserve repeated references.
    return cache.get(value);
  }

  // Preserve the original prototype instead of always falling back to a plain object.
  const cloned = Object.create(Object.getPrototypeOf(value));

  cache.set(value, cloned);
  for (const key of Reflect.ownKeys(value)) {
    // `Reflect.ownKeys()` includes symbol keys too.
    const item = value[key];
    cloned[key] = isPrimitiveTypeOrFunction(item)
      ? item
      : deepCloneWithCache(item, cache);
  }

  return cloned;
}

/**
 * @template T
 * @param {T} value
 * @return {T}
 */
export default function deepClone(value) {
  return deepCloneWithCache(value, new Map());
}
 ^Qkf7RUgA

%%
## Drawing
```compressed-json
N4KAkARALgngDgUwgLgAQQQDwMYEMA2AlgCYBOuA7hADTgQBuCpAzoQPYB2KqATLZMzYBXUtiRoIACyhQ4zZAHoFAc0JRJQgEYA6bGwC2CgF7N6hbEcK4OCtptbErHALRY8RMpWdx8Q1TdIEfARcZgRmBShcZQUebQBGAE5tHho6IIR9BA4oZm4AbXAwUDBSiBJucoArIQQjAAkAVQBZNNLIWERKqCwoNrLMbmcAVgAWeO0ABlGADnGeYYB2RfiZ

xJn+Mpgh8ZnhqeGANnjFw9GeRMOVzcgKEnVuHlHR7UWeRcSAZiXE+Mn4o58IqQSQIQjKaTcUbDG4QazKYLcSaw5hQUhsADWCAAwmx8GxSJUAMTxBCk0n9SCaXDYDHKdFCDjEXH4wkSNHWZhwXCBHKUiAAM0I+HwAGVYIiJIIPPzUeisQB1e6SR4otGYhDimCS9DSiqwhkQjjhPJoeKwtjc7BqbZmybI4EQenCOAASWIptQ+QAurCBeQsu7uBwhCL

YYQmVhKrhJvyGUzjcxPSGw46wghiNwrvbLolFhtHYwWOwuGgxrCi6xOAA5ThibirH6JHiTGZA9rlZgAEQyPUzaAFBDCsM0wiZAFFglkcp6fbChHBiLg+w3863EuMrjwrrD8bSM9xB/hh46epg+hIewg4KhsfjjahXa645QACq9SpXm93zgIR/Pv1OCgUVCCMcRUE+Q5AJyAAxXB9GFW1UBhU9egAQSIZRS3QYIBT6CsmCgcwCAw8FsOgS1+T0HJc

AjJggzQFN8AtUhwQjAh33PT8EGvW97z/J9+VwIQoDYAAlcJQPAtFal3Oj6jBCEL1QCYFlhSRQk4qAABkIwxQ8hwQOSOH0xjQ3wIoAF9NhKMoKgkDhJAABWGBUKGGOB+U6cDoA/WFBjQZwZk+GYEl+OZhjbf4Zhmc1HSQ5weHiUZJm0T5JhCvZRlOdZPlGWE7mIB4zSWVLTntRZhk+RZJkWUZEhQjtQXBSE0B4C5GrKeEdQdDs5Q1FkCWJckySQEc

aTpeNmTxIb2XIDguR5bJ8MdIURS1HUID1TM1XlBAlSKlU2t2jUNp87a42EI0TQbC0rRtBt7VhZ0F3dWdfVWgMEAY1AmPDSMAvQXB4kuxliETZNzJRHj+xUvZDk+J5Dm3Aji04BtPniOKO0rEtaw4eszVmZYzh4ELw27XsDwHQyRzHYhJ0yZb3vnRdl2plS1zWcZ81+KDHT3LFYaPE8OzPZSMEwOACSgVBiAQQdQ1lgVGWwIjODlni4B/Y0AAp6AI

WoAEpgAAHQ4VBLdQc2rdQajUVQdMLYAXl+hAKFQBUQgxZpcDgXWjZtq2g8tlWCfVi2OUrBB9cNhAjdQM2Ldtq3CAFVBdcdniOG0DTmFj3x49QBOk5TsvUECKARAtp3tGUBAoAL42Q5TyyW9ttOM9Qby2HTg3C9QZ2h9QAByOUI2UEfUAAH2n7v4AQXvUH72pB+HkeQ30TQmCn2f58QXvzZXv8h9dkfRzxEIOF3ufl7jtfXaYme5+Ph/UDBhW6OIZ

/98Xvu4/NqfUezAYBbzxFPEu7dy6V2rnfQuUDLZtw4Ag1AndM6vwjKiawYgl5dnZsXROKDbYwNIBbY0Hs8E9CbvHFBSCUFoLgavTBUQCZ/1QBJZQ44paQOTuXK2JCyHu3YQgThUtqHaEECIMQ1BGEIG0AKfA0RmCB14a3FBKClCoB5OQGAqBNDzWwJIeh6ddZoVIDo7QhBmBmJ0dQhOPC+G23trLQIzAlY2MHl6b0RCra1zCI3Y+MjXHuPMSoxxV

sBQEi7s4rR5iABqBBUBL1fg48JKcYnBPwLLV2UcmBhF1tohJ+AwlpOIeEEJpBtBwCEMwSQutMlQBKeEpBpSBEV3KVkmxtD1GqNtpouwVQEBq2tr01OJjf7JPvkAkeAyhlQBHqk8JMSBmeOAC0tJMSsQwGYJ4gA8poQZattBbPzsfJpji/EN2odQAZ5y+GRNINEzgDstlJPTicghpdSlWwyR07J3dyDR2ofkLZ3o7lpIGSChAMBvSeIaT4xB5sEWo

AeU8hassQFgPwG81A+zDlQDrg3XZFAOBOXRIgUgsBRSgNHMeOxnzkW20hZi2lsKcmAryTHY++QWV4jBci9Z4S2kDO6aowV7Sq6kIBbgIFZzzaWRfBQLSlQsDS0pZrRWWSUWqwjpra8OsuVxxNi3FuMSnaePIZ7b2vt/bnJbmHNWJZpWyqNYQ0ZlsGG1zzvSxZji2m13rgEo1oq+EMJ7v/Ae0zx4cEnj/cNsi34byEFvHecaF6TMjevC+wRrA30tq

/IBT894FuHh/IUxpv573jSWs+vL8AQLda0husDj6iuMV3DB6LsFsMoX+X1fC2mWt7XYtt7rUHjM7Vg1hS8OFcLgP26BzapWWtnWI4+EjhCiCMrI+RijlDKJDeXDRChYk6L0QYoxY60E2NwDASx1jzG3p9Y2jZzyXF/I8a7H0yLLlBsLkEj9oTkWoszjEwpiSM2rwXUst97S3FavZTKzlBT4kEHBUKwDlTqm1PqX89Daix1lMlRbBpXSx3ittsepJ

By5kjNDeM6tUz16zLVgsl9MH0XUaqKsij5dNnQp2a7PFczjkCZHYR3x2cJFXMCbc4DUTQOwdeUvD50HHG/Pg/83JLBDWFyhTC/DfDIWgrhX8gVSKJOhwU3bWDdacXCaOYG4lpLyWERgNSrFpzXVqaMwcnlNK+WeO0/k7ldb+WWdQLxsuwqDmHsRaotpwXdPNw4Aq6CwEpLcEguluCCF8BIQLGLdCmFyK4RWjjQixF8CkSwt0SisJqJRDoqQH6f1H

QEjYhwDiH4JCqplhq4SWqHW6vlvq/idivmW1NbZ7OFqhFe1wD7P2AcTWqOG06pL9LJsp09VJ71ZyGURf9VJwN4m+FRfHV3Rjmba1ognnm67q9pmb23qQB76aI1PazWwS+uaf4JsLeZH+Nb36RnLRmNNB9Psn3XnWht22B1Lotq28jFn6Mdvvsw7tuD8E+f4Ujt2FD2ZnfLnQq9E7MddunenVd872N+oJyukRc7xGSK3TI9dCilH4Yu1R7Rt7z3YM

vej0xj671WJvTAZ9CO+OwdI+Yzx36Iu/uuXBiphmInWbA6h7FkG+309KRppWQWOU6ZQ6QIpGvouYaqTUupDSreReRW0+XpA4spyoyx2W7bM6PZh2fL3bGZdl2WQcnjyL+PbL2TRo5JySfhJV7Jg5juQM2c48p95AnDvfJ+XLv5JukNm+5aCx3TK/MmddvCiLZPSmp7NQF3X6cHMEqcySsllo3MedpV5wu9iDcQr82FgvLq9NhcdxdojsCRWo7FS3

RLpuQvBtS0JES4lJJgQMseIyAt5KKVaipFInUQSaV6LpEym/RZlCIOfsyIorI2UdPZdAzRiDaWxNWZoABxeoXkF7dD8o6IDM4MsKlAsHsBuL8NlNCPzB2EhH8EsCkB1JMICO1O1PlI6IVMVCpKVK8IcBVFVDVHVA1OpHvspO8NCLCN1OBL1GUP1FiINGyOgESDwAKIkAgM8PyNSLSC9EyAwd0PNItLyOVmUGtGKBKOdHiPqGmOqIqMqKqNIXtGdJ

UBdAaFdJIBDLdO1vdLAI9DQZAC9G6B6AUB9B2P6PBN9LDG1h2BGPLIDHCKkKoWDBobfsxGmDDNwGsCFLsHVKjFWNhPEJ8M2L4XjHWOBHgZVJjHsIVnZJTMECuDTFvnTGDIzNOLkMYazEuPEZzDMOuJuG8DuALGwPuMLLTKhFxBIAoAAFSVE2yVGoAAACPQ+gPg+Cr4tRDR3IAYicr4lksi7R9RbSwAPRtRCg5sfW6q8smqysOqTqo22s42B2XyZq

s2j8821qy2RsAA3GjtquHBtgvslkXNtmgl6qEHYgusdtkISn+sbNsbPqomglAn7m/KbFtHdjGq8c/E8R9gDsPK8S9kwJ8bPN8VDr8a7K8dmlfECdPFAiDkWjCaMiDmWl/F8aMs8UAq8XWq8S3BcQTsfHcbbDXmMhnJOiwjgunL2ricRoTqgMOmcgSVbESR6iYqSdjjTsztwv3oOkIrTqzputIjulzvulsS3EyagJovzrovokLi3NemLvepLucf3k

bp0grl+t6AybbInnHABppjYiKaMiBtrhbhBtDmpiqVpgcebpbpqSnK7rbjhg7rafFtbtSa7raWKf0jHlALKSYuiX8RAF7q8QuqHtxkJt6boIEMTs3tce3qJN5LsgKOcc6Wni8lnuGfiqJtsnYimdqf+lxgaWXEaUptCjiicuaXnppsPshsXtCmCimZbMZnWaZppimWKVZo8rrPXlivZhGa3i5h3pSu5g3j3sbGpsyg3mys6jWXHP5livWVArxjFl

UB6UHOsvPoXovr3ncUgoqsqhUdUf0U0S0T0KgG0RbHUfUZ0fBN0b0SjqgJeYMcMReaMcaFLP1pMYNtMXsRrHMQaltkHMsdkHNh7AtktrancUHOthrJtosb6RnKcaOfHFSbAgGjJkaquQ8SYiCWwiDpie8coNCThXri8RAACW7hAKiWXP6eCRAJCdYERYiUxo/EDsCUxTdqDpMSiWxdRT8XhVtA3tiaoihVKviaKTscySSZTlOuSbSezCJYIkTlQv

SeJcglhVJQPFjtTsIqInTjLtyR7LyeumzgKZznusophS3BKWLoLgTMLsSaLhYhLmLkqTLhaZ+l4rmVJv4qrq7oWSnMWZxuBo3rIhWZxg0tWWbsFf5dbnqeYg6fbnhm2VAi7phpZaol6fivBbrDRdbIGd6cGcqbBishmSJtgFGVQjGYGnGWwAmUmWcjFbnunumbihGXHipaMnmbJAWSmYFWmboipgJmFQ7BFYhiPrUPpguWOk2TCi2UrMlWpUWQpt

2bSr2Zmf2e3hSlSiOa5SghOfOZFVuRNWPgta6VPgcphS6RKrArBRhfKubPyJEjkCBBvmgNlqtEBLlohB4bCOLDVqVgrMIZAEWERO4P9XVp5A1kBLRMaC1pYVDO1qxP4N1uUegFUTUReQ0ceYoqeeeQ+R0TyDeUMXeQApjQMQTsTSMWMe+RMQrF+bsY6r+VrP+XBcnEBS7DSWBTagHJBcnNBZHFaazR3CYohbtaMpcTnKdh1YSdlcRdDqRdGoRZRT

xSnLlf8cmq9oxbxaCfxfRcgsrQiWXHCaxYbSnEiWDtxabbbGrQJVikJbbApbIulcLRpUwlTrJZSVyYzkInSXdfcdlaydpbTo7UzrpXyVItumZdzs7VbNZWetKXZdlZLgqS5Q1UVeFZhorhqVAl1dun5b1ctbBsFTikLbLhnVWWNchtFQ2WrqqVhnbrhppo1VdZPlKu6apVZSekGepTlXxcxXlUGRACGcVWHqVUcuVSEJVX2Q3DVXVcmVApHoJq1Z

me1X7WXLnTIrcgXZ2ZHmWUNf3pbBaYdYcZNc3VbDNVOQ0gtVAn1Rig3mtSJhta5kOV3niEhUbOOYPpOcfcCidYuSlQTgMpdU7snBueNfHDuQ9ZQavhJKwK9SiqUR2NfggApC1MpKpEflICfueGfqZAg4kTvjfr9OZPfkULZJAE/hAJ/uOAqHALsmhDMFQL9X/uyAAR2EAYkP8IgTMMcB8PVAEVjLCAlClCsGlDwzFPEC2JBFcDAWUJgUdKgOFGlG

THgcFOsKMNVJg81EpA2DkZQTGj1CdPQTNIwRACSKNBSONNwVNHwXNJyJ0ctI9cKGIdqBITKEY/tHIcdAoadOIcoZITtI6IaOoTdGaHdDSA9HaHoU6AyIYSzJ9OYa1gjdYQDNGJ8KDAmKE8Q6mH1O4WWKsHMO1JFMEejG1MlCUxwPjITCpJ8JBC2Bo9E1Yj2HERzCLNvh2KOMkVOMzOkY6AuJkRzCcDkdzPEFuAUUg0UULBfu02UOLJUM4CioQCwL

LBQH+BpIwN3N3BNMEJxZ/BWubKs3bNYO/GEHorVZICMubVxRWlokyBMvLdMsiRWiPObKwM0fltdVKswOYegAaG+D1ugAs0KMs6gIc+s3+LLFELSDs08xmAc3+HgBbDUn+KOOoJc/3bC9/NYN/LlSPJiy8wtIQO87ov6j849UBC9eBO9aYZ9fBN9WWL9cVmRJUGVvyCDVVuDeyPVo6I1jDfRPDTk2UB1sjfgPuYC4syC2C0hps1CxiDCxbfsxwIc4

iycyi+c+ixxZi7czi33RxXiwqxmAS28z4CSwTt81kL846MJKJLA5lmgDJDM5AMg6gzo2aIfupNgzpHpNM8ZHg0xKQ6UOQ+ULDBADMNgPEAANIwAABa5Vv+XQrDXE/kQwMUoUowyMeYhwwwLYAR3wQjQwXhiwCQORywqwozkjG4BUXjnM3w2gwwJw/wAIxweBTwJBaDGMmDVBSIHjtjTBI0ljjoXBk09Mvb0AAhDjfIfozjShUoATsoMhnjh08hfU

C7M7uoc7jh10SYmhHYloETOhUTz0sTb0vTphX0STgrFDqTEguAowGT4MWTVhtBeTKkKUeBBT6wFT3AvwFTVT4EfwuUsUkUsjFDsRDcrTiDZQnTE43TM4p7ZQ/T7MsMQzuRoz+Riwu4kzEHBDRWqNEACzva5sqKeAUAhiE8clp5XuWiOyFKqA9cCEHAhAqCdsoIxRoLCLxzyLNmW8KJfscA6INIFzS8WlYgby5sva2rqCzA1YuA1Y3cbALHQyGIl2

r8/HbAZg8s38Vi7SBAHzuAcs+CXue5AL+HFHCARHUSJHZHMaZnXGtGoQqAtH9HEYTHTHhiSnEOyrnHpzegPHNzfHAnhiOKInf4OOp52LUnMncnokintIKn98anGnEO2nUZIoui+nAzdnas5Lz1drEEIHgotLeWSEmDf1JWLLgNbLlWYN5XXLkNPL0NzWF7rhu7SN7EorJnBH7MFnjyVnkg5HEnVHDnTnmQLnzH7nbHXnSLPnBgmgvHcAangnwX7t

oXFJ+CEXViUX8nsXynncqn6ISXWnOyqXenBnlH3pK+Nr6+4EbTxkKDpBDY7rjoecWkuDPrhDfrJDpQ1kZDj+IbAAUtiBQLspILsp/p/vGz5HM8m4FBI68PU9mycEkJMGpPFAW1m6FLVClNVA1EcMlAV/Iw2CcC8OEWMIEdCJjKj01A92gJw/owiNQT2yY8NBY2NIOxNDwdNKyPwfY0tJO6tNO347O+4z47IUu94yu4oUL+uyLx2ME84SpOE9aAey

pE9I6AYSe2gHOAk4GAKy13ZNe0DMMPewr0+wIC+029CHMG8O2GULjKUzU7b8DXkiEawtwBEZVGTHlBTM0+ByUTh1B/TCkT01ryYQh2zFkShyM2Mxh4UcUe97hxLFYhJAQL7b3sgHPgTugtJWSQgImbZwnAAGSF9dwACEm3sn4igar4RLMcH9xcxneHyfIQ+AafxsGfCWWfCaIX+fEnRfJfmc5f0nlf661ftfAc9iOXGW8D1LIhRX9LyEjL54nLOE

lXqMoNJEtX6Aok9XHYvLTXevLEnWKNSfzAKfrfxOZyHfrdFs2fmlK3vfuOqAxfZfFf1YVfDcNfWQE/Df0DV3cD0kUgLJEIb3d22brKnmUBe6n5vWCRS/E6xgHZMLI33B/NYRDYABHQgK6A4CJBMAFAIQJD3/xJtACKbZGIfnagY9s22bPMPm0CjfAuGTwFKA1EOBZt62BPatpIzwJTBvgZwCnpIy0Y084Y0TLtmgGiZ0EcQzPCQOYxGicEOeNjCQ

dv3HZ88gagoQXq438ay9aCC7A6FgSd5vEpeag4XlITl5qEFe2MIVtoTgJq8OwGvIwqHz9DntD+j+Q3nCEOAm9H2yTZ9hzAuALBEg6wArvb2whJRPgv7UIquAA7DAcw0RUDr7yyK3dB2QfWDmkTsF9MI+gzLmBuDQ7bhY+EzePrAMda+Q8OCzWnK8wjCic0BtQVEE6i5BDI04hAcIKglyB6IwQNnCelEAhw1JyOHCLAKmRkhqwok6gbIObE7jN8w6

V/TPtSWoSoIH+7JXSkbEb4SwihHJOACUNYSoByh4QXVNUOtBCh6hagHZNvHI6tDcA7Q1gDZy6GYAehQAvoY8gGFqVhhZ/JYXYmv744JhgdMQPn2DpT9KWWWArk9SgBfV8s3AUrky1qwSBWW6/Dllvwoi78yg+/WGs1yP4isxWpnYoYS1WHrDKhGsLYbUN2GNCDhLQyuMcO/gdCzhIiboc4iuGiQbhoIO4enBGEs4xhnfV4Tn27QfClhcwv/mvgAH

cAHWd3F1vvgwYetmAr3BAXEKQYID/WyA37qgMqD6BSAMwfADMH0BoQxIBAxNsoKAI8NDg2gWYDFGGBLBZgPAWKGYMgAJREY7UNKPqLOARDJgeYZsGwPF41ttR+YPKNlG3CAh+BYAmpp2wMaM9Re4g7npIP7Zs8OmsgkdvILHa88hCTjdaNLy2gbt/R2ghRroLEFrt4xGgyAPLyyYmjAyFg3QkexdCa8vE9gxJo4JSa2FowiwNwduxcLQwOY+ovgX

aPQIVY0Y2ERYMEMLAu8awoQs0HlDwLQhlgzYmIjEOw5wC6KCQpmHB2SEdhEOkfdIXkSyGYdch+DMcXMwkALNX62KTOA5xSTmxcWcOc2MNyYCoB9A4MR2COViR/hkW38VFP12IDywLYWQKIJkX04RclooOQgOsMdgKcYA9Qw5rUmED4Bv4HAWqnbH4jdxQQ+gAAAXzD5mqATcV3B3H3wVE+4hvASyPGPJTxNcC8e+OvEoookd4h8SeIbi4AXxknXC

Yxy/GCBUAv4nZP+MkCATgJoE7AOBIGHQSvheXWfpAD+EAiSuS/KACvwgDgjOxlKSEcyzq5URGu8IssUKza5dYOuhQ+CffW3E7JdxOQXVl9lrRoTDxNHY8VhPPGeZLxqrG8QRJIBESnxpE5cK+LuYUTPxq8aibRPY6OwGJoYJibLBYm/gIJmQGCZyNtbwNeRIA/kegye5NRPWb3PIb62DBfcwAP3QNn90qBCA0B2yeIGhGUBVA1R2/NhgMBIEvBYo

MwFYGcEmBZsNGugs0faG1EbgoCKPRGBoyiEQBCeZoa3mFCOD5gVgtozRm21daKMhBvo7tv6NHZSDRoMg6xuGMDEKCoxjjKdrGIMEy8jBmgvaEmOXbzTfGM09MXNMzEmDsxSvSJqr2iY2D4mZ7UsVFMvblBnBuAGYNWMhgnT0wsMBYIcDWCqNdBAQx4O8BCFu80AbU9KEaOYE+8qY/vMcdBwZiJCDp4fAZsh3nGZDxmV+LDv9PyFrjxWCElSagFUz

mwqqRKNvM/W2qeZdYtyUFoxM+YWxjmkpHFHWmYAyIpuO3BoTsmCAxo0WMXbeI7BEAhiyg5AJVJ1yUk9kkZKMjgGjKgDOZNqneHarjIoD4y2kRMmykvFJnkyOOFsCbrt0aE0zlAdMhTgzLcSBAOJM/X4fP0BEMsyiAkqEcJJbEb9qsUInfpJJogH9jp+vSAMK3a7IiNxyk6jsjKzwqJeZ/MzGcOWxnCzRZBOcWWeklkjlpZRzWWax3lnUzsgSsi5v

TL/BqzmZkAa1lyLy4BTxRxoIKY9wgHH5hR0AohmKKvwSjopsU4oPFIkA8B/u2kKABGygCJAAAQhlIKEaiU29bHUfjxii1RbRXwGgagESguipg5U7NpBCKkkwq2johtkW11FbgNGGbV6c9wEFFN6ehjfqRGMGkDtQxI0sGKOw5ALQJ2yg0QmmJUKJjq2KY1dnGP3nGC/AITGsYry0L7tLBe049rYOLE68LCVs/6BWJvaJBLpL8twoM2bBzBfB7Y6J

s9Laitg3p1TdKEsBbArA6pTTP6Qn0D5dNJxSQx+TONSHgzhmGQmPkuKmYRS9ZcE28Es2wChgeQwiAUEwGyBiBzYMESzgQqIWPJAgpC3kKJyY7gss4wFQQBaywDwQfA9QogFiBObkd9OgQQha2PhbBzVW7HRbPoD9hTD2kwivwvJ0DSghHkdwNFjGTzjOZtucs/Cb1xoWKI6FCsMhawkPF3N58q8KJG0z0ShAIcMFDSFABkQgSMUTMrRJ00haggtE

jNC2ExxFmuStmfC04WUIqERw9xQQY8Cc225YheIAw9pAwvIV/gmOxATgCPFlgYgQJHsBiR7G8VATmOCSiCcuFgnrjLY2IXRcQokgxKjFHAKhTotEC0LolhiphagBYXmp2Ff4The8x4WEA+FJI5QFolkUiA/CoilVlx1WaSLpFEYXpa2IUUNwlFoLNQBczUWhANFMXLRcR2KX6KylonCLqYtC6PILF1IMIN/BsXLh7FoE2Oc4uECuK/wNIXVF4vxl

RA/FpQv8BiN1Q9ARQOyGpOEq1heTaljCuJXLESXJLUlDStgBkvxnxKFO6gPJelm+FvUtZsEOljrMX56zBJhsu3tV037iTt+3LPflJP5ZfzWux/BSQsMKWrKSFdS8zhUuoXVK9F3y2Jcx0aWzZmlqAVpdwupkdKrxpw7pYIqGR9KSwAy7zn+GGUYgpFN4MZUIp5UwU2Aii48SormURl1FJKTRaHO0V2wSV9CslZJy2VJIdlhkSxfsqSSRxbFxyxxY

EDOUiQvlVyp1Dcp8V3KY5DytYYEo2whK3lOyGLhEpvBRK1VPy7Jf8uRmAr0leMnxWCtyXKCE5fkm7pB3gGpyBBgo57mFNFERqhJ+cu/FKLikyiJA9cAAIrMBsQ0KdJswwTaZSiB7DFNqsEQJkwIh3wAEN8CHGmiPC2UOtsaKuDjBmwyUHMQ1OQi/A62AIOqIQQyh8DOp++Cgla16kiCmeY0sxsGOGnDt15EYzeYIUmkC9ppm0U+ctLF46CPGe8hM

WfK3aegcxe7ZXrfILGvQH52vQ6brzxUG835QMNCJ/NrHfzYY9bfUZlE/YiS/CUIQBV2MqY9jeArYdNrUwba/SWmsMpIjB0QUgzIAs4tIegoXFQynWMMuBR0BM41UF4WiY8Ap2NAZgXVKshFpaDqGBM5e/zPDshsQCobqJGGj0NtwZl6A4AeGjWVS1hX/D4VfEpFQbLX4iTjZgks2VDQtnSSL1NsuSSf0qDEbLlaGt2Jhso04aaNB4Xyddx5FAD8h

zraNSFMgFxqc5Ca6/J92TUxSUBdkENgAE0uwkgUgHpqcjjgBQdc6HsQMCj5htRhwL4HlDWA5F02BXJCJBBeCBETgRouqNVAyg1r6ph894MkGQIAgAiVwVYJVAHVkEM5cIEdagFEELsBpk6qxtOt4KzrFB0YqaS42XVbrV1i7ddf6M3UZiIAWYy+XurzGHt1e988DYKAcF8bTpV6uELXMcKZNL5ZvLaBb3rZ5gxgIBL9m9TqkBC/2DYJ4HVHgL5hA

NfvBDeOIQWpFqtkGtBahzmDTBMGgsUcXDJM66QsQHzLAT0FIBmB3Yx4qhSKGBXOAFwzACzK8QVCSBdEXNaRep2PE2oAA/J8UAAoBFakWw2pnZUed8YKo+agggJMiaibbPklZdGhKrBmcoB5DUh64NmEUHMgzDaBUAH2zJd/H44IBGAOQYNdoCRQQBLty4U1d+Q8XMAntlFV7diFzSQsgBHzDyQ+DYkAZqSoQZwNp36FGbgV2O3HbLFwAuKwJoQHZ

CFyJ0vbUAs9FDQ4sc6uImAjAb+DKsTiWRNiAarJeRuXplUKqMcXmULsQCJlzi+S9ABtqCC6Jtt4uuoas0eSHb8QFAE7XIHO046rtb28CkkiLCI6/YxO1AK9pu03gPk3272L9qCDEAAdCnIHRBm9I7Iwdf4CHaQCh04bYdaseHQ7pvDI7RdaO5aJjrZ22L8dDNCOPzpJ23hydAKUMLomp0QtIJdO2BAzqZ3Uj0QFAZPXjs53nLudSYKYTJXCBO7Xt

auv8CLtR1hBdtnnWZdLtl1x6FdMZCetGWnpQAW9GuhqnRp+E5YmNQI/icirY1GyxJoIzFTCMgBwjcVd6/FUiPW1sqttOQA3ftuN14hTd5us7WpQu3W7Xddu+7Y7oF2X73dJqn7boj+0+7vxWqglSDqD3HNwdkO6IBHuCBR7iACOpHfjNR3o7XFy4LHfrXZ2p7+aGe53VnuvgU7c9YEzybToJnUdGdOyZneXsr0c6udLEnnfXtz5wHm96IeMsLtAn

t7xdXetFmsl734z+9EZQfVPXWoz0yDtVBeGPqNQcirWMDWTfa3k18ilN0WqATg3jUB9I1mmpAdpulG6bKgHS+gDBCMBoQ0Brg/NVDyymQBAYAjbUY+u+BVRXRCMbIVsCGAnBO1KPcqNCEuDbhaow8nQRuC7WRRfBGPKRjmO0aDqfRDPPqZLwGhLykt7PNealvHVzrt5MYrLW43Wl6CNQi0iXrlsK2RGStu67aSrz+B3zCxJ6sPtxNq0b7L1UYG9t

iFvWIC6xsMN4M2Gzb3T/Bn6rLB+tbGDaiYxwPHhlGgVgdYhCawGcHynFFGUhYM1cNBpbBGi9GcfbBSuLW14dEyQoa0IklFB4gRITqLXRAHGPmArA2KaY74F1QT6YVU+4rjPpY0YqhJ8+1FaJJq57GuNDXHjevq6Ob67ZJnRY5MZWMzH1jMm7kQIeAEpzQBXUmNaFKzliG1NW+ANkXLTXoAM1GIAUIsDEiNBlAN69Q4QIbm9jMY2gThn8DyluaNwH

Y2AqYYRi2aNwpUBzdjz83trKozo9YA1H+ANRKenoj43VB6leHR1i88dcvLjl0UwxM64I+loXWmFVB2WorWIJiO8AN1J8nLRtPPmmDkjh6yrekeq1mFz1ORq9g1twDjhCjbWm6UNuODcx2xfmoBSpDzA1G/CdR1AGsBt5vBymj+Fo6tpA1AywNdWubb0fXCnB3gfwArituA24KJA/NKTmSiJZqBCAjAV8JwdIAwQZinAACqAyz4txnipfZjN6Xew6

1+6I8fmnmmNoigg4BpMnG6er4Lxgzh9WDN5CCwaSEADJNBDmYjMB4ozvqRLAvAZJElNEAAA1EjihWIMaas3LCsREQY0QgKxKCH2HtmskjOhaKgF4V/hJcMiG1DIlFANwZEvaGRBF1pyQHLYbSGMmp3IOIBtAdZgii3F0C6d48qAbQIEBaJiBdYCgAAHr5AqOusU2KbFFAABqQOKbG9AAASBQDIhHh3n4gCydc6JG0jAqmAZO/JCmYsxum/y/EJUO

oDJ3udVceAdzqkjQRWIPTCEIiD6b9MBmfyHAMWjfydprkdiMSHM67HTOIAcyOxQsyhqjQNwg802TjPnu/irEPYY5xuI1U5wEhxwgnXWLrDUCZAE4zsAAHzKl+IgB0icQF1iAXfwwFyQKBdBAsWmiMiCC6CA/oelGqbSCi5WYIt+kiL68YVaRdUQxIKLIFGPTzRbj0XSAjFwxMxePgAB9GRFsnYtcW3KPF6TI3C2QyJBLxoYS6JcOJmWjmkFxqpZD

ksE4FLGFxapdl7okbpk8Zss3iTjiKX/LhFoK+vElLqW0L66YVcxdYv6BLLeqeYkJdmUuXxLbF/ykSSiv+5R4AzOKy8NgRDpL+a9EBkHHyuJpAg9cKWMVbnPe1DKjw6WpVeThoIpLcifbNwfpyaIJIXHKJfnso1RllO2AGACxPqERcqDne9pIgCQ40rWEzAWcyValSdXri+F5OFWZPRkpwg1Br5f7uxSLmODJG5hCEAOXpwCAFAW9DsiPDX5ulQ7b

bvpxaJjKvcy1zSzxejyZlmDKu4faPvqrcHeah9QTnIh8qBIUDFafyrfU+04pSl/+glMCo4ARsxMadbbDWdhsiYEbSN7MkbCbOlDfA8sHZHZg+SiQ2Ay1rM5xmSueJayMKW0hRcmqeIYLrEOC96YQC+n1d/pwMyheSvgoHtDQzIFAjQCOXPGIF4G9lf0CSXgbuVnYvJZ4uQM1K6NI8pkBPJ/g8al5a8voFvJ9EyaT5FpJUVfLjFZYn5Y3ABeZoLFX

UXyNpELecui2wblqbmjJfupcA/mbMvDm6cZuen4LrNxC5zczPoGzzqicM5GfxTRncKsZ+M8Dn7pMRkzctojpzbo6f8MzpdLC0RfuboX2rylkjcWdHiB5Qr1JbyBFaDg1nVzDZ5QE2ccCVC2zHZ+oZoG7NQBezrKvhUOZj2jnxzZnKc3cxnNBx5zEZI695BXNsB6zE8dc+4HwBbmdz14RRPuaPPnmTz3pDOOeavM3n7zj50eC+bfOqJ+7n5o3T+br

4x2OAJtsbBlZFtgWwbnVqCyYndvM2EL7NpCx4tQsrXkc4Vvy4BWzMp3cLhxA0lVYzsFWx4JF31O9d/CUWaSNF3S6on0uGW6kYt1K9ZcAfaA+LAl020fZEui3krEtjy7JdtIy3AHBd9OxnGwuqW/YDVnoeDYhxUWdLdFuOPIgYtMXqEbliy4PCssL0bLPley2lYNTW2T7ccNy2fc8veXqSvlza0pbwcqWz4IV+nG0jEqCPIr39xNLFdzstpKHiVqB

ww7YdAXMrKDpog7akdf3hH0Vs+EVfkfLofa5V7cs/dweBWf7tV1VEQ4Mo6UGRFVvKyYjWvdXe8vqPqwgAGtuKhr9Mka3bHGvBAdkU1sXTNd3OT0Icnq2JUtfGGwI1rUtBxzsU0Q7WO9GzKJQddF21VjrcS9FGdZxSXXrr+DO65Yri4xcnriiF6xGRfvkWPrY9AlN9d1iq72Dc9BqoDfcughbL4Fni5DcLrNUBq7JBRBjZJRY336bjk9NWfRtHJMb

YmHG1MJYlCACbBk1asTZ+xk3iHlN12NTezoaWeL9N12Jfa9PX28+HN5C1A6gS83krAt1R0g6yuoPWnEDMx41f4ey3Hb5sBW2TWxqtF+i6tzW/eUfIU1nyD5fWzTUNt01jbcdoW77ctuIOnL6jzh/mTtsbE/zTtj6rl3gajMtjC/OqWVz2MorneRx9FUvuhHmymsvGmU4GQE2ErKgbt5gLBf2de2b7Pt0um0n9vW08zqALOzMijOQ5Q7ercO8Wkjv

mRo7zz/e3Hffu+3k7QV1O5I8koWO2XQduZDY4Jz537n4pUZ8XYnhl2WzE8ds7Umru1367/ZtlagCbsjn4Jrdyc5J07shnqSC5xpwvH7uD2PiG9ke2Pd3OT2Y4R52e/innsXnrz555e0+bXvnJN7X50gDvdAepmwXUL4W8g9hfdUz7L6aC9S6Zu0u2bhz2+xHHvsPOFHhcHB+TYdjYX47UAVNxtZ0cyviL8yf+7Bi0tkOQHFDwuFQ4Ms0PubKjmBx

Wjgf3iEHh96F8fbEs3OeHGD6J6taefaPzH+Ds+GpcrdVPAH2l+27aXAc0PTL5l6FNA6YewOWH0KBy1G44diXF3tzrR4ST4cxPh38WUt2O9HhiPtsEjp+yO+ldnuR4cj8R2FfrdKPm3nFy5925je9vNHUt6R7o5/sGPH31JMq8pXie/uy368Kx/VcMeKU7Ha6UD6W+cdnEUbndYRJ44RasSVZvjsaxNcCd3NprGzUJ/NYieLWVn8l4G+tdatbXBdw

TlJ24rSe92UNp10ibk/wBXWo8t18jg9ZKeOcynFsV65U4djVvFd49ZXfU9+u2v1d/11xy07Wug2dSJD4gF053ollenJCuG9oEmfZlkPGVUZ+M/huDOpnuNgmPjfqFE2s8JNlZzEjWeyJJqtN7ZxXndPJvPbqb3ZEc7vvc3TnfN/QBc6tswuv3mQNB9JdzfoGBHZOV5/jUaJK2caKtz54TQ1vE0tbEXnW1TTfJqpgXUxNPbMSjcQuCcvnnt4cXsVC

J7biLy7onP8mCHApwhrRqprwZtMrI4AEwnCAW7ih2Y3AWyNAEgk+QlwpAfSJsAYCG7q5zJoI7NCYICgxv43/oBAGEVCFXQTRes74fpP+HYRIgGb00UG+BGueI3yMVvKUGTfpvy0Wb5kBgicmIj+G1fSt4O9zetBh8vr/t5yCHf9A83rEPEbO9TeLv93pomJE2mlbbv73qAA992Tlbdpv38xJd6O/ayCsIP1b+D5Rf/tZGb30Hx98yBaQ59eEPb39

4e8tfKUNiYFaCFIkXqEf0P/QOOCZA4+KAePkNtomBXo/Ef/3pomT9TeVApoNPonzBC+hfedQT7LaOVSP0AANIYMwNChvAqBPMf4LVESB9fmAPPkUHpseAZRPg2gZgf8FUZnBEYqwPr0YB+z6A2vhYOOEiEV/rgng/xwn2D/0BfenCWTYrfTEm/0gSA0Kn9X19t/EBxQ14HY2UCd/NA2A8sEn5zuCDOn3frETb4wSDbVy8QIbUgMoGpC6wkoGHXgC

cBkQx+ZEqUYYDwY7AcJaFTPyP7gGj/pQE/uf3gPn+T9zDjfd34CAu0B/p6CfUphABJEjAl2dfHYbIL745jJzYRRATyC8fyFdYsgcm140KxEjINe/+QqRT16YAyce/nf2ECP6xAGWusmgP30P+N9e5mAooLrHAE9/e+5/C/nBV1EdQ+mfs+ABv7MxYa6gMgHiqiDUlEj6BGfpLp05Nv9AGAxzcNksJNsUSog0Ie/1mwf6tnG/y7zf3EHvrngzQNkD

4CeQuACxSKggE5telkCACWQQAA==
```
%%