---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
image = [[1,0,1],[1,0,0],[0,0,1]], sr = 1, sc = 1, color = 2 ^gwzaABXo

function floodFill(image, sr, sc, color):
    if image[sr][sc] == color:
        return image
    original_color = image[sr][sc]
    directions = [[-1,0], [1,0], [0,-1], [0,1]]
    function dfs(row, col):
        if row < 0 or row >= image.length or col < 0 or col >= image[0].length:
            return
        if image[row][col] != original_color:
            return
        image[row][col] = color
        for [dr, dc] of directions:
            dfs(row+dr, col+dc)
    
    dfs(sr, sc)
    return image ^UnHu7fBu

/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} color
 * @return {number[][]}
 */
var floodFill = function(image, sr, sc, color) {
    if (image[sr][sc] === color){
            return image
        }
        const start_color = image[sr][sc]
        const directions = [[-1,0], [1,0], [0,-1], [0,1]]
        function dfs(row, col){
            if (row < 0 || row >= image.length || col < 0 || col >= image[0].length) {
                return
            }

            if (image[row][col] !== start_color) {
                return
            }
            image[row][col] = color
            for (const [dr, dc] of directions){
                dfs(row+dr, col+dc)
            }
        }
        dfs(sr, sc)
        return image
}; ^G6aDnKfC

%%
## Drawing
```compressed-json
N4KAkARALgngDgUwgLgAQQQDwMYEMA2AlgCYBOuA7hADTgQBuCpAzoQPYB2KqATLZMzYBXUtiRoIACyhQ4zZAHoFAc0JRJQgEYA6bGwC2CgF7N6hbEcK4OCtptbErHALRY8RMpWdx8Q1TdIEfARcZgRmBShcZQUebQBGAE5tHho6IIR9BA4oZm4AbXAwUDBSiBJuCGUKI1wAQQAhAA02NNLIWERKqCwoNrLMbkSABm0ADgBWHjGAZgA2OeGx5bmA

dj4iyBhuZx4AFlGZibn4g/j51fix1Yn+MooSdW5V4ZmEnlvNqQRCZWlufZ3SDWZTBbjDIEQZhQUhsADWCAAwmx8GxSJUAMTxBDY7H9SCaXDYOHKWFCDjEZGo9ESGHWZhwXCBHL4iAAM0I+HwAGVYGCJIIPKzobCEQB1R6SAGQkXwhC8mD89CCiqQsl/DjhPJoeKQtiM7BqbY64YQr6k4RwACSxG1qHyAF1IWzyFkbdwOEIuZDCBSsJVcMNWWSKZr

mHbPd6vmEEMRuGMeCMZtceGb2gwmKxOACxpDGCx2BwAHKcMTcGZ7NY3OZjNNlQjMAAiGR6cbQbIIYUhmmEFIAosEsjkI178JChHBiLhW9x4qtJvEJnseAs5svIajibHuB38F2vj1MH0JIR9NEEKgALz2/K6iHxJ236gQ4aPl/UB9O1DMUhX1C679sD/AC9GpP9UjVSgABVekqU9zz/fIn3vR872fN9nw/B0vx/YDqEAvDUFAtFwNZNlOCgblCCMc

ReDrSByJyAAxXB9E5Y1UBmSFDygOoiGULgJGCNk+jzJgoHMAg+N+QT0CgfVWT0HJcF9Jh3TQSMxy+NFfl9AgYKPOCz2UC9ryQtCH2oZD0Ks99P3w3DrwA5ggKc/DiN/a8IK+XAhHkgAlcJqNomEhAQDdVIACR+P5j3/FJIUkUIDKgAAZX04R3TsECKABfO4SnrNt0AAVQ4SKhFWNkGiEVlOlo6BYMhQY0ESCZtGGc4Zh4RdElrJcrkhDjnHiGttD

2CZLkSeJF3mGZ5shB5iCeVqPm0ed4g+RKYv+NBkz2SEQSVeioRhOUqTRTFcRxJBuyJEkQ0pFFLtpcgOAZJlslEr4OS5BUlShFFVWjM7xUlaUQdFeU+QalU4zVYQNS1Wc9QNI1Z1NSELQnG07UdZ1XQQdTUE0n0/Ra9BcHiYNe2IMMRyjdMY2Ky4JmGRJk2WMSC2zNAbl1L58yzYtS1og4Xh4GZVj2A6vgbZtghndtsu7WmB0yL6Ga09MJynJX/3n

CZFwmKZkxmE7NwRYrd33dMeMqNlyWwCTOFQNlUTYYgmM5fAAAp4JMhzSAc7B3Oe0gAEpkAAHQ4VB49QQg2UT4yEHyH8HXT7AHSva8PJjuOE6LwIoBEOOA4QWOi50/wCAAfQ8v8K/T0hM5ch0q4TxxAmdwtmEQ/IRps+07y/fIIRGseUI7wv48djhe9d4g2WYX3YQoMP8Cjzui/jpPUHX1AAB5UGGVASMPgA+a8K+0YIOGUdRz9/UDj9P5+iJRVBr

5T89x4dO+2RH6SALrvMBB8ECl1IBwHeu997N3XpnUCOcACE14a56XwA3cOoDwHF0gWXWBRcEFsAoEglEOc87hyIQnciv58hkHwsQbO59k7dwQIvd6uC8Hx2XqvdeABqRhn98BCOwBHWBsC+G+x/CHCRs8IFQPLqnYM0FYISHnpwt2HsvY+39qnIOIdN5om3go+BqcW5txYZeKh1JuG7xLmXX+JlYEYI4PXRuN8LEZyzjPIu7DOH9zMoPUe+FkJT2

oJPMJ09YGaJdnHaR69N6mLwfvQ+J8z4X1Id/Lx55AEPyfiRV+GSP6vx/s3V8+TgH2LwY46BNC97JxIWQ/IyDUBoOfrpdxWD84NIcQQ+pCjiEWMQa0ihf4PJ9LofaYRzCc5sDYYQHu8T5B9P8SvNepChHBxEWI+RRcpEbNkYBfZCc6nKPPGRCiVEaIAhOoxKALE2L4A4lxA8vRpICUqMJb66Z8wSXcJ82S0AFKQiUlEVSpBiak20qQLp+l1HoDiYW

bRbBPbey5Po88hjALGMjvY8xf8fHt1ziItENSzkDIuS4hRbiPHhybt41uvipFLI4SsgeQ9XxhNCfaCelk+VYT8bQp28TUCJNIckiljSD7ZJKVkigOTnEICqYUl+X95XqvwEqipAD77VLWZSpRfTCUmXyKMtpHS6U9JwYa+O5yTUjNIeQ/AlCyWkCmSRBhOy5msPFWywJ0rd4SooNszeezJEKOkcclypz7VUuVayXyAUgq3LQKFcKXwiCamir8Xa8

UNjpiSswFK6UOCZWVnuHKpR8pFEKpACoEgADicxcCNg4AAaTZIiOq8AGr22ahjOIew+o9WGFMdY6whrliuOMPYkwPijQTD1Uai1wYmmGKscYm1PhFp2nFOYiQ5iHQfsdGUoMkTh0xDwNkiQEAy1ZISYk2MKQXRpHJN6H1mS/LKL9HkMNKhw2FBeiUy0pRoELWUWUCJ/qwyBvDL46pJD0xRtpNGsAMYnWxtaW0BQnQ/UJtC0cZNiD+gkLgGYNNyR0

2RhpYj0YEDbjQPOuYMwZq1lzILTMhZnjc2FiWBetERgfDY2MWW6Z5YtiY27FWXwezUfVkOXIHp6M60nNOaTc4FyTUTImE4G42BbmtrJu2iKIAKAAFQWarhZ1AAABRkrpUDAE9PoTQTBHSOlysqmz9nHOsWc659zpBvM/l8w5pkAWXNCDc0wUL2Bwv+f0IFmLwXvOTLjrZuz5yUuxdIJ5h0uUbMKFjvQJkqL0U+z/MizgWLA7fh2S5PFEdnOwP3nV

tOxLrE2PdRHYAdrFFOIrn0orQyE5KWhN+KIpAoDYLArks1XXhVgIm1Af1yy+6ct5eE6JkSBXjyFVM0VKKQ3JP62NsB7X0nvwAD43dlYq8pqdVWSFQHdkRb8z7vbKQttOlT9XqBa+dnh4CHUXd3qNgb7XmkutQT16ETJZseSBwN/BxrwdF1GyDveTqWltNsWiAb0zfarZmT6lhCz1vsr7n11HXcNmCOEaBCNGOE5Y/AezsB0bGviL6Tl4bHBcoAG5

VEUBSpUSz1nMt+ci8l6LeWCveYF6gLLSXctpYa4l2X6u4uAS105+XGuMsq/szlw3HnM6FeK6V8r7s0W6K5NV47tWK44qa711rZjk4dcsb43OBPI7A+x/z1OI2+mk4RzNubJFfu+/buHzgk2AkcuCVyse23+URM/EdheYrTsiNp6zmVmzFUlPe1fX7L23v3eKbdmvX8nt/3+0AwHnvsf9PR+3yHRfE7e5h2M117T4fTaR+HFHPe0eEJ75znh/f8fu

qJyREnie1veqYRTxZG3E+F/b+s/hWymcohZ13sP4PudyL5wmgXwurk5BubRVMzoKJPPYuWbiHz+LAp+ayf5kl8BAu6FBS+HBRUk1ChWKhhXTGtXFwkEl31yiyCwty8x82lwiwN0QJC011QLV3N0wJcngLlwwPS2oVQLNwwMV2tw4DK1/Dt0q0d2vBqw4A6zd1Dg9yD2L2biW39163YJ4RD3PFPzwQjxH2j08mVTj2zgT3ejW2T021T22wzz2yz2w

hzy0Xz1Ah32xyuzlTrwex1WewB1e2+w1V0J+3EObwKUkHH13yNSnxPxgR72h1x1hyH2vEj1H2pGsJsMG0GXsPbzn3GQD0X1/GX2kLJ3X3mU32p2314PbxDTDV2WYTjR4Rn0xz6XPxOUvyURQJv0Oj8jYEClYDTVQAzQihzX3VnASi+GLVLQyiyirTygKjlmKggFWCgmIAaFSiLAACsO1e0uhaQmovgKYZo4hJoj11hEgeBVgj0JgOZp0IMlwEgxh

EgRhN1pgZiaw3l0wloVp/x4h1orgbhto804pAQfJT1aITpoNL1qQrobo8Q7pn1Ho31uhP1HMvoyIfZYNAN4NgMoZQM9jIMBAL0fiBQ/iEY/BkNaN/xUYiR0YN0sYyQcM8Z8N0wXRWIiYIDVN6xyYAxvJ0xHoUM6NGYoNGNipThFwXhlhMYuMeZZJtiyghZCwBMywdQJhzY5g2YbhgTygmwpNipSi5M1ZBxNYVNSTIBdYNMKTDYqTpgphJgDMjN6j

bYyh7YJBRcYD0Bb9KJgo7kn9mJWJX89p38jwAChIEARIf9xI/9zS5IgD0wQDIUiMJSIBoCzMk18jCi9T01SAwoyiEBc1YpKjeSajegy0K0ZMGia1wA0SIBcA4A4BeQNNuBCpoBJANZKgpxSBMo7gGBCAEAKAGh7oX0no7iJAMQ2Qqzqz+gIBsARBv0rQeh9BeQoZXiKyb070H08z6zSBGzmziznjaZ2yP16QPiWQeyGyvomzMgMV/1FQ4MhRJy+z

pzmzWy5RATwNeBlz+zMh1yYMANwSlyig6ypycgZz9B/JEZoTwxUMyhezdz9AAB5dDDieIWk+8s8qAC8piZ/I0l5N/E8h81c2c65H0uiHckC/QFKO0iAb/SC88tckfOoPs0hDM3AbE0k08lcxCzIPsCkFC9edClopkdeWs4C3C/QQi0hKCPtSoR6cir8n8wmK8pUSAgQbAWELkJobgCaUYfYGsSsU0NjDaPMlyLi/AAATXLCWMSFWFY3nA5hmleEV

JPKMDRX0FTMFgIDCnBG0DmNWLakaKAqYubKvOo2JPQAYrzNJBIHv31JPNsuIF5AQDgG4F3UgCcoAFlPYEB8LcBNBghjMq0bK4UyyXpnMvgGgUQWjSBlBCRfYepVh8IkqUq5x8JRgJgI5WRAplAvQmR6L4rcBErzYUrSreByrMrsrjLPycLKIL0XyVlxTtYGIWLshSM4UH4tL0xsgAqgruAhTHSiA3LfT/Svh3EsgBq/TM0oC/Js0QpprIQzwcymA

ixMSpqxr0xlqERSB/LArpMM0arIA7Buj2VmBuR3E4AfLSM9r+rK1VT4ze5GAoI0V8Buq1S6KBQMhOFFIhBoQDBaKBiSYcTIBLZpMbYZrf1YQWzvr4kVTIbQbQheInqEAXqURmqjqIBHBmA+rL0chegvLshap7rq1a0GJORwhUzcoQBcogA==
```
%%