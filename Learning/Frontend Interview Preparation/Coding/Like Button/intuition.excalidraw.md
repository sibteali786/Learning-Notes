---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
import { useState } from 'react';
import { HeartIcon, SpinnerIcon } from './icons';

function classNames(...args) {
  return args.filter(Boolean).join(' ');
}

export default function App() {
  // Determines if the button is in the default/liked state.
  const [liked, setLiked] = useState(false);
  // Whether there's a pending background API request.
  const [isPending, setIsPending] = useState(false);
  // Error message to be shown if the API request failed.
  const [errorMessage, setErrorMessage] = useState(null);

  async function likeUnlikeAction() {
    try {
      setIsPending(true);
      setErrorMessage(null);

      const response = await fetch(
        'https://questions.greatfrontend.com/api/questions/like-button',
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            action: liked ? 'unlike' : 'like',
          }),
        },
      );

      if (!response.ok) {
        const res = await response.json();
        setErrorMessage(res.message);
        return;
      }

      setLiked(!liked);
    } finally {
      setIsPending(false);
    }
  }

  return (
    <div className="button-container">
      <button
        aria-pressed={liked}
        className={classNames(
          'like-button',
          liked ? 'like-button--liked' : 'like-button--default',
        )}
        disabled={isPending}
        onClick={() => {
          likeUnlikeAction();
        }}>
        {isPending ? <SpinnerIcon /> : <HeartIcon />}
        Like
      </button>
      {errorMessage && <div className="error-message">{errorMessage}</div>}
    </div>
  );
}
 ^8bwSVNxh

%%
## Drawing
```compressed-json
N4KAkARALgngDgUwgLgAQQQDwMYEMA2AlgCYBOuA7hADTgQBuCpAzoQPYB2KqATLZMzYBXUtiRoIACyhQ4zZAHoFAc0JRJQgEYA6bGwC2CgF7N6hbEcK4OCtptbErHALRY8RMpWdx8Q1TdIEfARcZgRmBShcZQUebQBGAE5tHho6IIR9BA4oZm4AbXAwUDBSiBJuCAAOTQoAZQA1ADlMSTTSyFhESqgsKHayzG5nHlHtAGYAFniAdkSANiqZgFZ+

Mphh0bj4nhWZpfHlw/jl+bXIChJ1biWq7USABnmeVaLISQRCZWluE/mH84QazKYLcAFvCDMKCkNgAawQAGE2Pg2KRKgBieIILFYgaQTS4bCw5QwoQcYhIlFoiTQ6zMOC4QI5PEQABmhHw+DqsFBEkEHhZUJh8IA6lc2mg+BChXCENyYLz0PyKoDSd8OOE8mh4oC2AzsGoNtqHuCOhAScI4ABJYha1D5AC6gNZ5CyNu4HCEnMBhHJWEquAeLNJ5I1

zDtnu90oQCGIv2Wkwek0mM0myxmgMYLHYXDQZwhWdYnCanDEvyqKYeR0Shx9zAAIhlenG0KyCGFAZphOSAKLBLI5CNe/CAoRwYi4Zu/fYrZZz8bjeKJwEoomx7ht/AdiG9TD9CSEfRwVFQVDAVBCMLcycIVAAX1QLoMqAA5IFCVAXwBuAA6HEPx6kKe54ABIhEBVp6Bw1CoHUcC+hqpCQZw96PjC+ivtoCjmJwzDfn+f6smS2BQDmqDYPgoTME0u

BZMwAAU2hMYyyjMAAlGef6oKggRQCIHCoCxzDaOy+C9KQ9EAEJsMiIQcGx2gAFZsL69Evq+bG/hwd4ERqmCAaexAIG2XqnkRHAkWRACCcBwPRHHAFxqBKKgjbifovrhKghCsqg6i3poQgyChhDMN5An+agRkmWJChEPCxCoFCN7aE5UFQva8WxjBYRQAAMoQCUOqgAC8F5XlEvT0ZuYSaU5Lkih8/mkH5HyBC+YW4KgiDkr6yioASRIWmSiVWQAC

laPEIAAjkI4RQKlAnkbhp75KFY3ZI4HDKDlCBQFazAbb123FWVl5ypVCDVe2CB1UtLk9qQMItXRzDRLeUBsANt7MJIbAUAJPmtbe42TYEs3zY+uAcrGi3celq1MM9ACymrvbtUCPSjaPKAgp3lRdN70ZG+B3U5oQwBZj7EaRKFZQAqhwWVWZZnD2ZxS3cdCMAc9xfNJXtB1HVtyj0dCc13fz3G5VjqKo+G73E8OZOc3zCNTfSuG3mVlDQ2Ze3YJI

9FOVLr7SLI8hKBDUI5sJJIhFAT45JtugGAouDwQo1u0xwERZc4gXBRwL7UCbUuOarptZOobDEGgL5jQA8nUAAqIdh6bHy4EZLBoBHpumy+SLOzkzgp/ACAvvHHs+OYk45goimCMHoeR1Ld6twXfNdsQMBoAAUnUidNNoQp9T5MD0fnXd8x+OZoFliUAPyvmSWXqfH6+dzPd5sdvpsdxnqAq6bQP0QAhIEmu+wg2hwg5R/wytGulYJFB6xrx430pz

f2VpXcyyenLHGV0r7aFeu9SWBdeL8X/u3XSptcoFQShfReUDuIPnZBwAg+AebT35rlIWm0+rXS3LdOBGCnI6Q4E5GBpABLG1VgAHkcPQcilFww0SyCVH8EBA6fRcFBKInlSC8IAHxHyYfwzgj9BKkCsN4K+YRiAlWAIvahXcKJUS4QgVRWjOG0XCIwmer5/bSJbrI7ii9UArxfGYoKAjnDOEXhvUxhUEABwcZwJx0VcCmXTm3bibENEF0cG9TQwQ

VHAHWsQ7aITTacAREQIkqj2YlTEbzGeDMmbuJZj7P+si7x3gkYEs8MTjr9RXkwuCCEmDIQEgoDJaAmFgUZPtKCzkxHxKlsghAkiFDmJKabYASNgEK1xqgAAZJM1ALDCBsP0dRQxPCMBANIM4CBuNxEjLWfLN6uM7xMIUKwrpYcjknKcndahwZKApz6JUACJ4zwE2vL0VCT4MJvhCCRfC/4jxPNAuBdpnAYI1I4Ihep7z0KYWwulX5hEaZkUWTohi

TFtBCQfktOhAkhIiQ5OJKSMlgjWAUspVS6kXxXN0lgAyUVjJ+LEtTCyPtUA2Tspi7iLk3JMA8mGbyvlIrmO8mFX0wM6UxSgHFdxiVkq9DhstX2q1F4Y16cQfG51XlXRquQ+qChUCNT2m1YG7VOrdVif1QaxIQyjQmlNb28r1ZrUOuajGRCKnqoqkTbVUCHprNQJsj6X1NA/T+gDflYrQZ2rmhlNsMNiAOufvkUZpA9nowFpjXZICPWEyqiTE+glm

CU2wEy1mAlsnM1LezfBflSB4KPoQ51FSxakAlhQvmgDsbjKunmrSR91ZXy/mEV+us1CPgNkbWRL5zZyEUF7aNPs7bvkdjCEu8a9CGA9oQOd81bZSvhJ4oOASu7Vqjoa2O8ck6pyPTPLOOd5CZJMUXTgvRS7l0QFXV8Ndkn104I3Zu16u6H1KdxHufdUCD2HqPaE49WSTxPQXOenAF7SpsavHJ8JXF2PcQBguu997t3w0E3tbcz6X3CIO2+98H1S3

7V5HW79R0Dq1j/Nm6CpYdrGfs0B4RwEgLY/zbFbbKE0Lbkg6VqDpVscwb6HBdbROC0bSLUhtU20hOobQva/FUDGL5nMhZHClncN4eY5wQjoaIXEZI8xsjGQKLgEo2Mqj1GyORcs4Arm6I6a7lh/d5icOm2sbY+xQcnEuNQJvdxB7HHOF8f4wjfNgmyLCbgCJjnomKb6t0/miTkmwlSRxdJ1GAvuMZhW/J/G+ZFKGQXdLws+qoeqfBcFdSOmNPC7M

1pEFWunNKb0/pgyj47M7VxqZMy9PsO0cs3hyaNkgO2cm1NBzznzJ6/zZb9BqtUq4M6Z9dRCBGHELwU0ZRWTPoAGK0Q5EaVA4xAS7igFZIgyhczoGCKyfomYmCkXcI9r4L3oB6hZGZkR7o0Ak11PI/wBA7l7gef8oCzyNWXShc+L5H5fmPIR4Ctp9TQVNYhR0zB0KXxYRwr7eFHBzKlomwYzzaKMWZOxXI1ieKxJMEJbJElSkVIcDUhpLS6m9K0ti

4yqnLK2VVt1a5PaPLPIioFR8AaXjAYioiorkXkrrGytvmlRNyr02quzZq5TOr7p6oNc1Y1ldTU9RFgNQkVruw2rBjNedCbFX2nKSLV1GWTqvyR16m6Pq9WyxeiAvyQaQ3/UBgrkGtrwbzqhnG93GUk2Zq7RjUPi28b+89bm5WxHuIUypmLsi5bcmVo5XzbmRX01uqU+LU3iC9pZ5AUrTk+b+a0evkO+jH9WTjq81LKdMgZ1W3nbbbQ9tJxOxfWut

2m7t021wnujxfn4vcXg/zaOf046vkvWnDffNb1MHvVv4fxcX1QDLhXD9L4v11x9n+zg/mCOWIGrHMDEGR5j22hPKe7+RepayGCUqGL4a82G7WPmlcR+GCe8hS8WnefMpGTG38VG5+3ew6DGp4qBYQLGvOFW0sLe6eXG9EYCAahBU0fE9CQm94CC7Ge0qqEmCUUmj4MmnIcmze+0vuos3qqmVC9BTOQ+42Hmuixmyupmz65mTAlmbcUiyuNm8iuAi

imoaWzmpSoheiBmKKQ+hcwWAir+/MgWbivmEhzi0qmG+h3iMW9KcWsiiWpSyWqWUSXumWsiOW5geWwAaSGS5+ViJW6GCAeSOYBSpSVWsitW5qDWYKBOKEbWzSnWwKDSq2BcfWchAyyu1W/MQ2nG70o2syrCNOhmYhqyz0s2Xa82JB70hyxyK23S62m2Auf4LIfin0AASuEPtodo3iuJ5GBF8D8NqCkICJIKEDDvlL6LCBuDdEUHeOAE6HQDXJqtw

CUJ0B8FkJUBOKQFMWsAwIQAgBQJJA7sNOSJSKiBiKyJcVcQMBANgCIEyPtL0PoNyMKIiMiOcRIJiNiN8TcXcU9NkI8ZkEcUNNamcdSOgLSL7AyA8b8fcQCVaE8WdhyFyDyIdpCMiCqEULcXCTkAiZkC8bKGKMQNcJKLsX8Q8Xic8dCLKPKIqOiQKGSTiYCfoG0cIOqJqL8Iyf8biU8YnPqIaL8CaFyRSYiedpdrgtwLdlieSfCaKTkHtgdtwDwMd

tidycyeMb9s9pUG9h9tKUyZSdeEBFZEAhQLeh6MOMKbKZkD2OSMaTCKaSEC2OgIyPabCWqZSXaf9G+midam6SKZkGdq6AgKyYqODlicwNgDCJyAABrcCJCTDjDaAJgPA8DzCJAzBpkmjjBVC7ERlRn4AACaNwSY2gcwVY+wlYMw8Q8QOZWJRgMk+gKxBYBAc0YIKQiQHZiQywsxlpPJmQrJI0YYdoEAvpuxJIJACph2ypY58ixA3ICAcA3ArwZQ4

5xAyMscCANpKWkS0xZCM5JAYJTZZo0k+ATpI5ygBI9EPAswME15GYvAN5qADwSZbELIHRygXojIlQpAF5uAV54wAIvAAFt5wFT5L5EAPZepapBJ8IfJC65pUYJ2QZHRfo8i20R5ZQ2Q2564aAPREIFEhAi5uFLaCAgI2CGxxFc0uoQURAGo3AeFZo+gjI8IpAOi9FJFgITF2xTAW5zh7Fc0kFZQdgikCAJEzAdQ2CcA65RkvFO5rYN0uxc8jAKcR

KGFnQFclQYQwQpaQOl4n0+g3pCFI4EIq4CUu524ZoHydQGQOl8le5JloQD2lkylqlYOw4glkAThwQl+fQqMno5lCA4AHcdAok4QKxcxd4QAA
```
%%