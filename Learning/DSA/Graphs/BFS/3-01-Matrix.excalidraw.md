---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
mat = [
  [1, 0, 1],
  [0, 1, 0],
  [1, 1, 1],
] ^Szh6674p

[
  [1, 0, 1],
  [0, 1, 0],
  [1, 2, 1],
] ^PoDVSaHk

1. We can collect all zeros in the qeueue and then bfs over them 
2. Could not understand 
3. Not sure but We will have to write value for each particular 
queue value in a given level so we can track it how much distance 
its neighbor cells have.
4. in initial scan where we collect zeros in queue we can check 
queue length if zero means e return -1 but question is how would 
we return -1 for Grid RxC without looping ? ^HjxVGBVM

function updateMatrix(mat):
    directions = [[-1,0], [1,0], [0,1], [0,-1]]
    visited = new Set()
    queue = []
    rows = mat.length 
    cols = mat[0].length 
    result = []
    
    // collect zero
    for row = 0 to rows - 1:
        for col = 0 to cols - 1:
            key = `{row}-{col}`
            if mat[row][col] == 0:
                visited.add(key)
                queue.push([row, col])
                result[row][col] = 0
            else:
                result[row][col] = -1
    if queue.length == 0:
        return result
    distance = 0
    while queue.length != 0:
        levelSize = queue.length
        distance += 1
        for i = 0 to levelSize - 1:
            [row,col] = queue.shift()
            for [dr, dc] of directions:
                nCol = dc+col
                nRow = dr+row
                key = `{nRow}-{nCol}`
                
                if nRow >= 0 and nRow < rows and nCol >= 0 and nCol < cols and mat[nRow][nCol] == 1:
                    if !visited.has(key):
                        queue.push([nRow, nCol])
                        visited.add(key)
                        result[nRow][nCol] = distance
    return result ^mouGtDwe

mat = [
  [1, 0, 1],
  [0, 1, 0],
  [1, 1, 1],
] ^zQL0SWOO

Tim complexity

one loop for RxC cells so O(RXC)
one another while loop with nested loops which goes over all RxC cells once so O(RxC)
total = O(RXC)
space 

extra mat which takes O(RxC) cells best or worst case
queue takes O(RxC) as usual
so still O(RxC) space complexity ^fPuu5iMu

%%
## Drawing
```compressed-json
N4KAkARALgngDgUwgLgAQQQDwMYEMA2AlgCYBOuA7hADTgQBuCpAzoQPYB2KqATLZMzYBXUtiRoIACyhQ4zZAHoFAc0JRJQgEYA6bGwC2CgF7N6hbEcK4OCtptbErHALRY8RMpWdx8Q1TdIEfARcZgRmBShcZQUebQBGAE5tHho6IIR9BA4oZm4AbXAwUDBSiBJuCABlI0kANjqAdgAWODTSyFhESqgsKHayzG5nePiAVm0ADmbJnjGx8ZbGgAZG

/jKYYZ5Jiebl0ebEnkT55qb1yAoSdW54ve06uYupBEJlaVueZefrZWDub5FARQUhsADWCAAwmx8GxSJUAMTxBDI5EDSCaXDYMHKUFCDjEaGw+ESEHWZhwXCBHLoiAAM0I+HwVVg/wkgg8tOYIPBCAA6tdJNw+ECINzQRCWTA2egORVnnj3hxwnk0PFnmxKdg1Js1ctAR0ILjhHAAJLEVWofIAXWedPIWXN3A4QiZz0IBKwlVwy1peIJyuYlpdbtF

YQQxFu8Umk0aAGZmiLDYwWOwuGgxs1ninWJwAHKcMTcRqxk6TeJxg1lQjMAAiGV6kbQdIIYWemmEBIAosEsjlg678M8hHBiLhG7cS4l4nNmnG49s6s9YdiI9wW/g26Leph+hJ9OPUABeK0AHQ4qCt6tQ31Q8Vt58v+Vv1+WD4vV+od6/9+o5+tfqUAAKn0lQHlAx5nh++Svj+75Pi+X5vn+0HXmh74AXanBQFUhBGOIvBVpAdLYQAYrg+iMrqqBx

s8O5QAAgkQyjpugwR0v02ZMFA5gEExbysdAmq0noOS4B6TBOmgIZDqKcJvB6BAgbuYGHie+SPp+N5wShCE/kh8FaehKGYaKuBCFAbAAErhHhBEgkICDLhJAASrzvHud4pM8kihMpUAADIemC66tggRQAL7rCU1ZNugRgAIoBcsVR8gA8mltJdAR0Cgc8QxoI8jRTGcOyjHGMY8I0iTPNRPBxsk9U8M0mbTMsMaZs8VzEDcar3I8Yw+e5Hxql8Pwc

H8BFEWKPIQkScKIqiKJIO2WI4v6hIwgtpLkBwFJUtknGigyTJSjKYowvKYazfygrCs84q8mdOVypGCrCEqKq3BqWo6rc+rPMaI7mpaNp2g6CBSagMnup6BXoD6ABqfqdsQgYDqGhrhnFYyNM1Mbllmoo5mmtydcTTC5hwBYcEWaCJMsZzLFVROGjW9bBBOzZhe2qM9pkh0Y7JhojmOXN3lOM7zHcexJmUK4QnFG5boa9GqRB6maTBSE6VriE3oZ2

vfneGGARQ/nq5BGmoTrJu6Va+vIVraG6xwpmGiROS4fhwrTZ7UDkZR+DUbR259PxLGVOxR3JtxvH4BHgmWW0zyiVEEmkFDMNyaQCkcEpoH7mpUFPrBdt6/pBv20bxn/rS5mWTZrA+2gDlOaKRDKm5bwjV5cuQL5zD+UFHAhdzm7haUUVFDFkAVBIACycCI80ACOpAAOKJMo0RWQxPB0qaC9jAH2BZfAOX2ggEbkFQ+XcHU8TaDMc7zEcdQLHG5yi

tRzg8PVDweCPEmIkL+jQmi40mF1O6aAdjaDGPOWMLVRiNGjI0QaopJDDU8hWbQoDTh1FjBgw0vwZTTUenNLaJJ0BImWmiVa2IgYEnmtQ6Au19rUhjmUE6zJWQvUum9a6Epbo9SFGgZY8CHo3WepUV6KM/CSHRt9OSv1YD/WmkDM0FoCi2mOhDLOg5YbEC9BIXA8R5EBi+tJQxYZr5xR4KMMY+xJjLErFxVMnAH5Lgph46mhYCLxGqomRYDN3R1gb

GuceKsygdnxMQfmfZcjOhsSLUc45IkSxATOOMJY6jLDqKHQ0ncx7QxSfLNgq4lY81FHANgHokloEKB0MATTmlEVKMsIEYBdHNNaR0CRTiSxSwuB0rpPSOh9NKE/MY05qqEPQSMsAnTmnjNKJMsAcY8HxDyeMAaizlkdFWS0rpYBiqrEIXOIBgS0HEOac4CRMwnFxlGFVI4iR5ljDGSM9Z4w8GTAKdsYZJz7nPx2K4l51VjgfK+V09ZzU/l1ESEih

Y1yiGLJBY88FM5IXvKITC3pJyFzaGeeA0slVyxPGBQ8sFzzsVvOhSs75JzmhP2eZMOMMycm3I6BimlEL6V4sZbCk5CwpiJEaOAx+FZAWUuaWAXlTz+VQsFYcplcrcbwMfrMf50qKXctKAqrFrzlXoPxRMk5jxiUgITAuR+qC0VUtBYqulJrPlCoJXKwhUx/n2oWY6zFtLjW4tNe681cq8bevapyv1crDWBpxQy1Vwrw3FUeIzf+X8Fx6vRRI+q4C

9gVSjaAkNSaPXNJcSkZYgzs2OrzXUAtLidjFrdaWsN5an6IpmeymMTQbk5pSDk+trjG3RpbaUI56zZjaAlUiwhVzfX6vlbmwdDai1crNWsk57KUixhLOc1FMa7nLvzcOtdJbx1qvLZs6qb9bUHsXSCutq6m3rtDZuuV27HiVlKoenlx6h2Fpfee7pl6OjbplQ+gZsx5k5ITSqi9yb23Tu7S0FFC70XTJ2FCgpZ6x0gcQ2BiR6Dpjdp9X24FcRH75

NjHMMYQG8MTq3bm5oLK9h7OBZsqWG7jnhuSHjcV4rM0QfRZs5oKx8n/3mPR7j6zqopHGAsT+vaHWxs2YkaYr7W3vuaSWKYKxEz1QBTW2NzRiXHDnHjKTo6ZMnN02MOYDUJMPtM04pICCuNvp4zpyYCQXEcoJsp39BrTNNBY9MOYxxXU2ZTQ8Bo+wxjsdjRMfYJxnlzGizp4q4xtl4yE8Zu5Ewv4tXwVW6TnnZN1CmPkodiWCvTuWO8vYTjIvBoY6

B0o4Dn6PzyQF9DwKJiVWuThsrWmvMdE62cbZ7Ue19djZVqtP62sEY65V7YDNas8vm5mRNCGy3jcqy1dlM51PaqBXN7QC2dv4b2ytwB4DmpofI0l71mYHHoJa1dxjMXXvHHjEZs7dWCl+fiPqOj1nyu2eKjGXD6Ldiffa6cnzeNcsVTIypurFZmbRicWD5tGXxvJHLDOaM86nt3NM6gjlZx3sCuA19pDlYviPBO8JjjeDCEg+nJWEbu221gafgJtB

+x70icAScL9M6osQ4/XEEl8yWf5Z5aJvJ2Hufg9G5OuIsx5j6hmKd2VdzNnHBB7s9L0ur3wOZo8ZBIuKN4Psy/THPPrt89KNMC7IOLPC9m3cuIJYFzgrNxrrdpmEzWuquSgHPLKMVmLbB2nS2btgHdwsWYhxHvo+j8/Fjvbhvq959psDIXM8GriCx6n2y1d4/N2B5LQCJPe7J1nqqCD1tB4L2Nt3Ew3NpYfXEEHj98aS9a/jrvxL60JeOJHg3PKB

dfybU7/PLvC9j4QRVVDKCm8Grn4QmZi/q/B4/YVx+Wao/b7wfPvfVfNMd8nUb6WZL9eQeJUkeLzWE+j+T6y6MHLm2LNZQUkcA4kkHcE5p/rpkkB/IkImBVKznKmpoJugnrhBuAbsCWIphtqUJVggvWjkgrh5ofjpqHtDrrtPousVF8IOnRoiqAQNOAdeozGxvGE/ossVD9oJv9u3svp3qcpsr/lyqwdOo4v7jQWxlwfTuNnwaOoIdDs7hIR1lIX/

rZpGnIUCKshAHAIEEGCIOEDog9IQPoK6OkgAApaHMA6HcBtyRTRSijzzoDGFsC1iIxVC4AuQhR0QXw9B5Sijwxubj4fx0arDp4oK1RbDTgXb/K4yrANQtCPzQKiK3D9Qz4vA9w4JjRmQTRkJSLCIsKLR0IrSiiYiMIbS5E7TkiUicK0g8IyLsgCJcg3QCgJHiKSJCJPR8KyJ1HvQKJKJqg/RYh/R6gaJ4haKgzqH2gUSQxxTZxsxwzeipBdGWJBj

JKYxlDYzcALgNSIrirTQkyeJoDzjuJUw0x0x3hgIsboIVRhIcwIDizKztyGixLdi9iCzLHCxlCizpJxSBJZJ5qCZJDLgVKKyhQTx0SFzoDWyly2y/gVzGxOw2y8CuzuxlC3wWwSAQlaQviGyOyGzXh8DlxuxVHYTewETpEexkQURUTrGgm7iJxRwIAcS0gpg8TuC0mkjCSpzYTiTKiZxTFlKQDyT+AFwqRonOxQlYmVxwmQkIn4lImQANzWS2Qty

oBtzORdzYK3DeSYJ+R9AjwlJ3HWEzy2FxQQAuQABWmAiMG8AAQojAvOfN0KSN4YaPDCMA4ngixkigJk0FWggqEWgM4O8gkCsIQvWgzCxtsvEb1KgBKqJgIZguqWqEcONJNACNkbyKUTQktPQoUWtEwptMSD0OwhUYdFUYyLwtKPwpyGmRCI0VGQMtWQgDUbKJ0aKIqIolYt+Cov0WooMYDMMSDHoXohMQYisXPLMaYnGBYmjB2dMasXYpOI1vqIi

jsZTKTIVNAYcWmMcQRKghHpmHRlcRElUiCYUXzM8f2K8cOGkuLN8dOM1JWA1hWACZUsCdEp0GCRAE/KgHyAgKgHgBeHoEyAgNgBBAQPgKgPhKCMwKgB6MqVgqgKvAgI5I5KgNYMQHBdkKgJoHSNBWwCmBhfoKgOeHEKgNCK6OhRwGwBBHEpTFEASERRwJsqgAWBBOYYEFhRZN+b+VcEyKgL5IwMqWwKgBQLnL0KgPQAQChSRKQKgCENgJIKgBUcy

UYTJeeKvMhb+RJb4L+bBbgKgKoIwBeMEIwOBYIMJb+f+cqeQNiDBRBJIGwBQKgIYfJagI4NyNYGIAxWoNBcqD3B2DJWIEyNBfxQgNoOeKZjBReB6GoFYKZZZRQFguxRQBZTCMECBRBUwGwNBbBepUhdxRZdYH+VgjZWpRpagMEBNOoDBXSBlaCE5SEHtLJagIEFACIBeCMBxRBLldyGmDBcFQ5cJcIPgOheeMlc1TcW1agB1dJagBvLnOhVZJgJC

MJWoPZZxbCJqB6MoKgAAPxmyonoBfk/l/mFWAVpWgW8WQVZWRUYUIV5UoVoUYUXjYW4X4XqCZAMUkVkXDXQxUWoA0UsB0UjWMXaDMV/VsW/maCcXHU8XgUhWCXCWiWaWSW/kzVyUKVKXmAqUMW5UoVaUoW6X6WECGXlUIAmWoBmVjWWVkg2VqB8UDXOUKVuV0WeXnjeXQzDT+V/lBCbh8W4CMBhUcARWwXRU8QEAU3xWJX5V/mpXAUQRXXZUXi43

S2WXyXAVgg41lUVXKBVWEA1VXX1XkhNUtWTUdVQ1dWOQ9WcB9X02OUUBDXA1jUm2kDtXxCoAzVzUkCoCLXLVXDqDCAQQbVwBbW7WElex2S+xYQ5CByUn7HUmMTMSCTRyMlxwsmJ09DsmihpxcmSS8mjkQACmKT4AHWfmg3HWq2y3pVgW1XXWwXvV3VlWPXvXPU4WoB4VMAEWfWg3fUUV/UA3uX0XnhMUsUU06GdVcUrW8Xw2WSI1qDI3aXu1wiyV

YgY1UjKX4BUia15XiUo03V6UGWYXGVBAU1CVU2FU00a1032WOWM2uU1gs2/ls25Ac1+VL2BW80hWC3C1RUcAxXi3MCS1MAq2V3y2ZWK0IVlVn0AXFUa2lXb3a26362ZWG2NW/nO2u3j3dU8TW01i22DXkUMVO0TUu1TVu0e3zXe1LUrX+3rVsCbUTSh0/AWQKnNz2SkCOSqkIDdweQan9xSDam7i6mvmTxgDTylCzzlDGn6DCAbxQC1jJX2k5Rqz

3z+l5LJAWYViQKxgn5+m8BVQJD6hAI3rnHeKGjdRRmb56bcopE8OwIxjJlZGtGUIFkSC0JLS0hFHrSowZlsLlEHQ0h2hllNkXRVlOMiJ1ktFYzSLtG1GhOGhtk9GdmGiajdnUQg5DEmgDmNJjH6J51vFjnGLwwQC4DNBTmJOzkCDzloBfDVTMzGObl7F3iHBQI+JHH+K3DsqZhTZOKHmcwZJ3G8xxIJIvHWL50fE3mSxAL/IOKuLPlAlRL3FlBqw

SB0j4ggW9XjMIALzji5yYAAAU4EAAlMgJpJeI4IEOs5wNBepPkCMNQMhJ+A88+NQL+A7NQCMNaNaKc+JTWHPehSeMqI5VUDcXs4c988rVbF8x+JeKCBQNc05eONoAgwpd84BfC+BM+NaEi9kDrSi9C+NeYfgBrFaFC5eJeN80oDLUBelVdd8zNbC5BMsAjbC9Bc4HeCc/i2S4vQFTCIywjWi1Ney981y1yxCDAJBAAAbACwsRTODACAURQSvCsiu

Xh60ItQD5CwvWj5CAXWjHgnjLAcsqvGtktmCsCNjaC4DEDEB7NitgucsmtkvK3aBwBCDMCSB7OasOVfi6v2uOvGtaGugatas6swh6sGvKsqtBBhBGv+siuBtEtesUDau6uQQjDfNqvOvIv6s3ixsqvoMEtBvfPM0eW/kRv4sJWMi/lZs4tVUACEBrebIrR9zIdkkENblVkgkbd9A9nlAA1CePEN2zNYQHyzPS28SYK/EE2ya0m9QKmyeM6+63rVA

KC921yzNfkGQF+MQNgHq2wDVec3LWmPIOu8axwESJBLu324BWeyqxwFZANSeGQH27C3eyK2K5K8AA+w5bK9+0SIq++1y0B2S2qz+45QAHwGuoX0XgeoAAA8zVDl0Fj1F7vLUHN4MHFFl7iHArj1GL4H2raH+A4bg7M7cbXLardbZrfz2gg8trCAMAxzIH/rzrrr7rnr4HX4xH1ofrFHcbNHFrVrNrdrLHjrCbGrhH+QPHV799pb3zBbEn+1H5qzt

M2DF4mz2zIIhA+zRzTbR7lzjVNzdzTz6oTz3wrzzzHzpLprvzjYkEgLqAwLq7fHl4EL6kNnMLyHkE4E2LnbDFXLArJ4GLb4fnuLAXZLEnkL3zFLCgVL51NddLS9DL0HM9LLU75Hl4M1gFY7QlArbL0777n7J4UrMrcrCrSrDrKrarGLIbC7jbYngnEYlr1rDHTHYnbHbrHrc7VLvHYnEnSbKbYbjL770bCAmX4n4QQbg3obJHabQ7+LmbGlYXVVR

4DXVX41rVJDEnxbcntMZbN43zlbwQEDeVK3ClDbub3bE7bbi7y3yL3bJb+3qAA7d4w7S9o7qXQlN3+EGX77c7C7p3jk2gy7HEa7G3G7S9W7pAO7e7bdh7hAFz6np7EP57l7z72AN7MIYncHz7pAr7DlYnxXqAUr4Hf7xHgHqPKrYnYHj7kH0HqHdPCHSHcLWH0Ml7GHTLqHOHVLKH9FBHdPRHRIpHQrVPjrVHTXxAdHoQbXzHYvFHnXHH0ndP3Hw

vrn/HJrkvLXInjH6vGv+bU3ibUnMnz7e3YgCnxDF4SnUdOEEd1Tfs5JQcIc8drJbE9JXCkATJ8crvQkKcWdnJGcI5+TBducgpxdKnaz6n/115WzOzOnBz44cvXLBnyPVstzZntojzmfzzln3w1n3zkvDnCAQLIL6v7nJLCn3nwXiL2bqLMI6L44mL53EXMLhvxLNoMX+LlLZ1ctiX+L9LT7mHaX3nBXE32XvLX3vPf3YvxPpXv75XMIlPFHNXjfd

Xw3a3V38vtn5rzXwnsvHXy37H3XsLPrYbevcbA3a/c35bFHY3E3Jrl/DlQ31/pDGbNVHb4XG/hr3binbfu3vbB3ZYEd0kBVsgeoVbNpd2/4bcfuB3D/uoEe5m9fyr3BbiaxHa5dSaJlSdqP3+4n9AeS7EAWD3P4qtN227VynDwPZ30keJ7e/mjwn5kCse+AHHkzzx4E8KARPRjl+zJ5ysKelXfXi334608BqnPNnnB0Q7pdue6HBnrBx554d+ejf

Y3sLxzaFct+1XGqtRzs7Nd6OdrGgRr0V7dcuO7PM/mJ014aCpee/UTioMm6EtJOgvaTooNN4ACLeW3K3m33rjMMm4dvKyhww7iuQEyfcHyAI0CjBRhGBpcRkaUqB0hjCQgIQGMEIALwhAijLwipBUZTVcYT8bYDsEfjvI50ICXRhWBySAJnk6mZqEAjiKihzGYiVALOguxKFDQWCVIsKD2AOMpoDZHxm42WgeNcyJRKhIWT8aVFAmp0GJs2TiarE

GiMCG8JE1GHCJgmciLop9CWK9Euy2oHsneABiihNEWTEluDGHJ5MjEJiBGGMDKYzk+SYoKpqgHZQbFQEZwBpqxFZhlBdififbtwHszc4lgdwueOEj6bHk3yEAR4vEnPINJSkYzGPl8UmYhlPcLTIpICX6bVJVYH5ICAYRlr6AfAWAHUOeHPCcBfyQdblpQ2Wrv1oKZlNKHsysgAANSEPa0xEwcqKiVYSiAJO7Yi/aClQMPZyDrQVK2LlZQGwHCBt

18K1dH2tzSCpt1nuhI4kUtXtaWQog4FE8ESNJHkjzw+0VmhwHPB9ByA6rWkeYAUpRAIQ0FGUWKIFG81NA4QCCEvXtqA0TqYQOBihS1HcjdR5I1CtBTdZCACA8ooSj1V4q2jDmFNLUClWRHBBMAf0BUMBHhGIi9Avo1EbAHRGUVlQ5VOhnABxH8j8RJ9VADKLJEUjox1gakR3WO5YjYx1DJkUaIjAxjNQbIkARyK5GvUO6fIqhomP8RJiPR54CUeL

WlHEjUx8o70QxWVG7hVR4EdUS5WtE6jRRdoxMYaO5Bt0ZKpo0cXgAtEcAIW/Y5MYOM9GhB/q5hZ0XtFdE8R3RC4r0ViB9Eoj/RaiG3sSUjrHRHesdGiC73ToSBk67iZknxEvHoBk4IkAPtySD4ahQ+RdEugiMIqhi9xaIpUVGJzGah4x1YnmgSKEopi5RAEqke9XHF0jAJcYxkRzW5CFjWRvYhSpyO5Ht0ZKVYvEaBKFGeURRPtcUVRSbHzjZR9r

BUY/X/Eqi9KPY9kZqNwDaiyJeo4cUaLHGDUzRU4hAJaN/JziPR9o5cU6MYFriKaG48CvxMolIjfxB4syO4MVJsNvBRSXwQ0LVCak6hgQoRgs0ijgAekxTOAHABZDpJuAMUaAFgiyCVAxwpAdwkUAYCEBi+VpLod4x6GuM6QrktyQMAgDYARAnCU0L0H0AsgcizkzMvkQ8leTSAPkvyQ5OKJOSXGD4osv4y4SeTvJh0XyZkFIhBMhhITK6GUDCkRT

MgAU3kLWUqH1kbJuUlKX5IKmShMpsw0qclJyCpT9Aj7boh2XVC1Twp5UzIGlFURpM1hOUuqVAAamkRTxwcKkm1Lyn6Ahp4dJUqSUgBlT6pfk/yD72vFjSOp/kqIKQEYjhSHKWCK1peRWnzTMgXYAkAxC2kJUQgxpKkLC1Cn9SGpJ02FkBE8ISANo109qQdImkQxH2MoWcmKGwCggmQJI24AzGSCVgGoSKA4IigajrAfpf0/AAAE1hggZcBFWhWBN

QgEmaKGUYDob6BjJxMFGgCHHz4weAoQ2aTdL8lNTFiloCAM9Khm4gSAR4+3jTPmosgEAbQDMIzJIALw2AxiI6bgE0DBBvhizI0PNQzISMrSMIY0qQGUCYg9mb2L8LLN4CBIkI8CQ5rSBsjKAVKlQSWdLPqi3gdZcstxBMLGAqziZSU16ThBuhdTkee07hB9OyDGJc4E0HGYaGyC8z+Zlhdhos1mlEBWZXgz2RAHzjmTW4HsjUBZE7gKS/ZB4KyUw

DzATF3ZiksoJHIhCkAeZfMjJFYSnhQy7AppOWswCqD5w4AnM7mfnFTkCyoZWIHiIwCAh0N8ATspZo9NlAZBDOIkN1pZH0APSHSQI4PgrBhEnkPYoIfyY3PU7CNlwoQRiOs0rnVzXiJstyq7KhDYQ+gC8bIAkK0miN+A9IKtpaGAARQQAEUIAA===
```
%%