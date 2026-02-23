```table-of-contents
```
# Intro To Service Workers

### Resources

[GitHub - FrontendMasters/service-workers-offline: Code for the Service Workers / PWA section of the Service Workers & Offline course by Kyle Simpson](https://github.com/FrontendMasters/service-workers-offline?tab=readme-ov-file)

Download Zip and it has First Web Workers Exercise folder ( Folder Structure below )

```bash
.
├── README.md
├── service-worker-exercise
│   ├── package.json
│   ├── server.js
│   └── web
│       ├── 404.html
│       ├── about.html
│       ├── add-post.html
│       ├── contact.html
│       ├── css
│       │   └── style.css
│       ├── images
│       │   ├── logo.gif
│       │   └── offline.png
│       ├── index.html
│       ├── js
│       │   ├── add-post.js
│       │   ├── blog.js
│       │   ├── external
│       │   │   └── idb-keyval-iife.min.js
│       │   ├── home.js
│       │   ├── login.js
│       │   └── sw.js
│       ├── login.html
│       ├── offline.html
│       └── posts
│           └── post.html
└── web-worker-exercise
    ├── package.json
    ├── server.js
    └── web
        ├── css
        │   └── style.css
        ├── index.html
        └── js
            ├── home.js
            └── worker.js
```

## What is a Web Worker

> Its a javascript file that runs on a different thread from the web page thread.
> 
- IT does not affect the web page javascript thread
- Generally multiple web workers work on different threads ( But not guaranteed )
- If we want to keep our frontend usable when there is some kind of heavy lifting going on and blocking main thread, we should move it to a web worker.
- There are different kind of Web Workers
    - **Child Web-workers** ( a worker  can spin another worker )
    - A page can spin up  multiple web workers
        - A web worker for a given page is **Dedicated Web Worker**  and is terminated when that tab / page is closed.
        
    - **Shared Web Worker** if we had multiple tabs, this worker can communicate each instance of all.
    
    [Worker: postMessage() method - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Worker/postMessage)
    

### Web Workers Vs Service Workers

| Web  | Service  |
| --- | --- |
| Cannot run in background when tab is closed  | Can run in background even when page is closed or terminated. |

### Creating a worker

`web.js` → worker related code 

`home.js` → web page content related javascript

home.js

```jsx
(function Home(){
	"use strict";

	var startStopBtn;
	var fibsList;
	var worker;
	document.addEventListener("DOMContentLoaded",ready,false);

	// **********************************

	function ready() {
		startStopBtn = document.getElementById("start-stop-btn");
		fibsList = document.getElementById("fibs");

		startStopBtn.addEventListener("click",startFibs,false);
	}

	function renderFib(num,fib) {
		var p = document.createElement("div");
		p.innerText = `Fib(${num}): ${fib}`;
		if (fibsList.childNodes.length > 0) {
			fibsList.insertBefore(p,fibsList.childNodes[0]);
		}
		else {
			fibsList.appendChild(p);
		}
	}

	function startFibs() {
		startStopBtn.removeEventListener("click",startFibs,false);
		startStopBtn.addEventListener("click",stopFibs,false);

		startStopBtn.innerText = "Stop";
		fibsList.innerHTML = "";

		// TODO ( Here is where we are going to write code 
		worker = new Worker("/js/worker.js");

	}

	function stopFibs() {
		startStopBtn.removeEventListener("click",stopFibs,false);
		startStopBtn.addEventListener("click",startFibs,false);

		startStopBtn.innerText = "Start";

		// TODO
	}

})();

```

Then in `startFibs` we have to make a `listener` and `message sender` 

```jsx
	function startFibs() {
		startStopBtn.removeEventListener("click",startFibs,false);
		startStopBtn.addEventListener("click",stopFibs,false);

		startStopBtn.innerText = "Stop";
		fibsList.innerHTML = "";

		// TODO ( Here is where we are going to write code 
		worker = new Worker("/js/worker.js");
		worker.addEventListener("message", onMessage)
	}
	
	function onMessage(event){
		console.log(event.data);
	}

```

then in `worker.js` 

```jsx
"use strict";

var curFib = 0;

// TODO
self.postMessage("Hello from the web worker");// send message to home.js
// **********************************

function fib(n) {
	if (n < 2) {
		return n;
	}
	return fib(n-1) + fib(n-2);
}
```

![Screenshot 2025-02-11 at 2.28.37 PM.png](Screenshot_2025-02-11_at_2.28.37_PM.png)

Its a message from worker to web page 

let send a message from web page to worker

### Sending Message from Web Page to Worker

`worker.js`

```jsx
"use strict";

var curFib = 0;

// TODO
self.postMessage("Hello from the web worker");
self.onmessage = onMessage;

function onMessage(event){
	console.log(`Received in web worker: ${event.data}`)
}
// **********************************

function fib(n) {
	if (n < 2) {
		return n;
	}
	return fib(n-1) + fib(n-2);
}
```

`home.js`

```jsx
	function onMessage(event){
		console.log(event.data);
		worker.postMessage("Hello from the client")
	}

```

![Screenshot 2025-02-11 at 2.42.16 PM.png](Screenshot_2025-02-11_at_2.42.16_PM.png)

The data we send is copied ( not reference ) using an approach called `Structured Clone Algorithm` 

[The structured clone algorithm - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm)

### Data Transfer Solutions

> Shared Memory Buffers are v2 of Transferables, its a shared memory segment which can be accessed ( by web and worker ) by multiple javascript threads at same time.
> 
- Since its disastrous for data consistency, an api named `atomics` which makes sure only one thread is accessing data to a moment
- But it was again deprecated because of some security risks

[SharedArrayBuffer - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SharedArrayBuffer)

[Atomics - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics)

### Receiving data from Web Workers

`worker.js`

```jsx
"use strict";

var curFib = 0;

// TODO
self.postMessage("Hello from the web worker");
self.onmessage = onMessage;

function onMessage(event){
	// start generating fibonacci once we receive a message ( whatever it is )
	getNextFib();	
}

function getNextFib(){
	var fibNum = fib(curFib);
	self.postMessage({fib: fibNum, idx: curFib})
	curFib++;
	setTimeout(getNextFib,0)
}

// **********************************

function fib(n) {
	if (n < 2) {
		return n;
	}
	return fib(n-1) + fib(n-2);
}
```

`home.js`

```jsx
(function Home(){
	"use strict";

	var startStopBtn;
	var fibsList;
	var worker;
	document.addEventListener("DOMContentLoaded",ready,false);

	// **********************************

	function ready() {
		startStopBtn = document.getElementById("start-stop-btn");
		fibsList = document.getElementById("fibs");

		startStopBtn.addEventListener("click",startFibs,false);
	}

	function renderFib(num,fib) {
		var p = document.createElement("div");
		p.innerText = `Fib(${num}): ${fib}`;
		if (fibsList.childNodes.length > 0) {
			fibsList.insertBefore(p,fibsList.childNodes[0]);
		}
		else {
			fibsList.appendChild(p);
		}
	}

	function startFibs() {
		startStopBtn.removeEventListener("click",startFibs,false);
		startStopBtn.addEventListener("click",stopFibs,false);

		startStopBtn.innerText = "Stop";
		fibsList.innerHTML = "";

		// TODO
		worker = new Worker("/js/worker.js");
		worker.addEventListener("message", onMessage)
		worker.postMessage({start: true});
	}

	function stopFibs() {
		startStopBtn.removeEventListener("click",stopFibs,false);
		startStopBtn.addEventListener("click",startFibs,false);

		startStopBtn.innerText = "Start";

		// TODO
		worker.terminate();
	}
	function onMessage(event){
		renderFib(event.data.idx, event.data.fib)
	}

})();
```

[Atomics - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Atomics)

## Service Workers

> Every outbound request go through the service workers, although its on us if we touch those request or let them pass through un-touched.
> 
- When we listen for outbound requests , its now entirely on us to make sure they are routed correctly.
- We essentially have to act as a proxy once we start listening to outbound requests. Its like acting on behalf of page, when receives a response sends that back to web page.
- Service workers can help use to modify behaviour of network requests, because being able to access network requests opens many possibilities for us.

### Use Case for Brainstorming

 This mdn article explains all possible things which can be done with help of service workers 

[Offline and background operation - Progressive web apps | MDN](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Offline_and_background_operation)

### Push Notifications

- It comprises of two thing PUSH an NOTIFICATIONS

### PUSH

> Push is how your service worker can be worker can be notified of something from server. This is how server notifies the service worker that something has happened.
> 

### Resource For Checking Service Worker different implementations

[IGRICE Za Decu Od 3 Do 103 godine - ServiceWorker Cookbook](https://serviceworke.rs/)

## Working with Service Workers

setup this repo 

[https://github.com/FrontendMasters/service-workers-offline/](https://github.com/FrontendMasters/service-workers-offline/)

we can start from git logs to move back in time if we want to follow along.

- In my case i am starting from `initial commit` or very first commit.

### Detecting Offline Status

blog.js

 

```jsx
(function Blog(){
	"use strict";

	var offlineIcon;
	var isLoggedIn = /isLoggedIn=1/.test(document.cookie.toString() || "");

	document.addEventListener("DOMContentLoaded",ready,false);

	// **********************************

	function ready() {
		offlineIcon = document.getElementById("connectivity-status");
	}

})();

```

```jsx
(function Blog() {
  "use strict";

  var offlineIcon;
  var isOnline = "onLine" in navigator ? navigator.onLine : true;
  var isLoggedIn = /isLoggedIn=1/.test(document.cookie.toString() || "");

  document.addEventListener("DOMContentLoaded", ready, false);

  // **********************************

  function ready() {
    offlineIcon = document.getElementById("connectivity-status");
    if (!isOnline) {
      offlineIcon.classList.remove("hidden");
    }
    window.addEventListener("online", function online() {
      offlineIcon.classList.add("hidden");
      isOnline = true;
    });

    window.addEventListener("offline", function offline() {
      offlineIcon.classList.remove("hidden");
      isOnline = false;
    });
  }
})();

```

Now when we turn off our wifi we see an icon on top as 

![Screenshot 2025-02-12 at 10.18.55 AM.png](Screenshot_2025-02-12_at_10.18.55_AM.png)

### Registering and installing a service worker

- There are some intricacies to using Service workers
    - Making sure its supported by current browser
    
    ```jsx
    var usingSW = ("serviceWorker" in navigator)
    ```
    
    - we get a registration when we create a **service worker** unlike web worker.
    

```jsx
var usingSW = ("serviceWorker" in navigator);
	var swRegistration;
	var svcworker;
initServiceWorker().catch(console.error)
async function initServiceWorker(){
		swRegistration = await navigator.serviceWorker.register("/js/sw.js",{
			updateViaCache: "none"
		})
	} 
```

- the path we provided here has an issuw that it allows service worker to access files only in this path and none other while we want it to handle all ur files.
- so we use `/sw.js` , still the real path is `/js/sw.js` but on server side we have handled it ( url redirect on server so that **/sw.js** points to **/js/sw.js** bts.

### Service Worker Access

- Our `service worker` can have three states
    - **Installing** : SW made for first time, or changes made in already installed / active SW.
    - **Waiting :** When a new SW is installed it goes to waiting state as previous SW is still active ( remains active until we move to whole new page so that previous SW is killed )   ****
    - **Active** : The current running SW instance.
- The browser always checks for new service worker when a page loads.

```jsx
	async function initServiceWorker(){
		swRegistration = await navigator.serviceWorker.register("/sw.js",{
			updateViaCache: "none"
		})
		swcworker = swRegistreation.installing || swRegistration.waiting || swRegistration.active;
		navigator.serviceWorker.addEvenListener("controllerchange", function onControllerChange(){
	svcworker = navigator.serviceWorker.controller
		})
	}
```

- `controllerchange` events triggers when the new service worker is either **installed** / gone into **active** state from **waiting** etc.
- Thus we should assign this new **service worker**.

### Creating Service Worker

- We should be mindful of what we keep in our global scope for service worker.
- Why ? because whenever for any reason its restarted after termination, in-activity etc it re-runs everything in global scope.

```jsx
"use strict";

const version = 1;

self.addEventListener("install", onInstall);

self.addEventListener("activate", onActivate);

main().catch(console.error)

async function main(){
	console.log(`Service Worker (${version}) is starting...`)

}

async function onInstall(event){
	console.log(`Service Worker (${version}) installed.`)
	self.skipWaiting();
}
async function onActivate(event){
	console.log(`Service Worker (${version}) activate.`)
}
```

- `self.skipWaiting()` as its name suggests → skip the **wait** state.

### Keep the service worker alive

- Sometimes while we are still in different phases( wait, install , activate etc ), the browser decides to shut down the service worker.
- Thus we need to make sure that does not happen
- we use `event.waitUntil` function for this.
- the use case for this might be
    - caching items when user shows up on web page and readily leaves the page, ideally we cannot keep the cache partially filled so that is where argument to `waitUntil` method ( another function ) comes into picture.
- Then comes **Claiming the client ?**
    - Suppose we have 3 tabs and we open new tab which invokes skipWaiting() and now we know new service worker is handling this tab, but what about those other tabs, which are still controlled by old service worker.
    - This is where we use `Clients.claim()` api. As stated in specs this triggers `controllerchange` event on `navigator.serviceWorker`
    
    [Clients: claim() method - Web APIs | MDN](https://developer.mozilla.org/en-US/docs/Web/API/Clients/claim)
    
- 

```jsx
function onActivate(event) {
  console.log(`Service Worker (${version}) activate.`);
  event.waitUntil(handleActivation());
}

async function handleActivation() {
  await clients.claim();
  console.log(`Service Worker (${version}) activated.`);
}
```

complete code till now for `sw.js`

```jsx
"use strict";

// TODO
const version = 1;

self.addEventListener("install", onInstall);

self.addEventListener("activate", onActivate);

main().catch(console.error);

async function main() {
  console.log(`Service Worker (${version}) is starting...`);
}

async function onInstall() {
  console.log(`Service Worker (${version}) installed.`);
}
function onActivate(event) {
  console.log(`Service Worker (${version}) activate.`);
  event.waitUntil(handleActivation());
}

async function handleActivation() {
  await clients.claim();
  console.log(`Service Worker (${version}) activated.`);
}

```

now check in `Application tab chrome` ( better refresh before checking )

![Screenshot 2025-02-12 at 1.33.12 PM.png](Screenshot_2025-02-12_at_1.33.12_PM.png)

### Message Handling in Client

- service worker might be not dedicated to specific page in this case thus may need extra work than web worker ( `postMessage` )

`blog.js`

```jsx

async function sendSWMessage(msg,target){
	if (target){
		target.postMessage(msg)
	}elseif(svcworker){
		svcworker.postMessage(msg)
	}else{
		navigator.serviceWorker.controller.postMessage(msg)
	}
}
```

this is to send a message, but how to receive it ?

```jsx
async function initServiceWorker() {
//    ...rest of the code
    navigator.serviceWorker.addEventListener("message", onSWMessage);
  }

function onSWMessage(event) {
    var { data } = event;
    if (data.requestStatusUpdate) {
      console.log(
        "Received status update request from service worker, responding...",
      );
      sendStatusUpdate(event.ports && event.ports[0]);
    }
  }
  function sendStatusUpdate(target) {
    sendSWMessage({statusUpdate: { isOnline, isLoggedIn }}, target);
  }
  async function sendSWMessage(msg, target) {
    if (target) {
      target.postMessage(msg);
    } else if (svcworker) {
      svcworker.postMessage(msg);
    } else {
      navigator.serviceWorker.controller.postMessage(msg);
    }
  }
```

- We would also like `sendStausUpdate` when there is a `controllerchange` , after assinging `svcworker` phases and in `online` and `offline` events
- 

```jsx
window.addEventListener("online", function online() {
      offlineIcon.classList.add("hidden");
      isOnline = true;
      sendStatusUpdate();
    });

    window.addEventListener("offline", function offline() {
      offlineIcon.classList.remove("hidden");
      isOnline = false;
      sendStatusUpdate();
    });
async function initServiceWorker() {
    swRegistration = await navigator.serviceWorker.register("/sw.js", {
      updateViaCache: "none",
    });
    swcworker =
      swRegistreation.installing ||
      swRegistration.waiting ||
      swRegistration.active;
    sendStatusUpdate(svcworker);
    navigator.serviceWorker.addEvenListener(
      "controllerchange",
      function onControllerChange() {
        svcworker = navigator.serviceWorker.controller;
        sendStatusUpdate(svcworker);
      },
    );
    navigator.serviceWorker.addEventListener("message", onSWMessage);
  }

```

### Message Handling in Service Worker

- send on port2 and listen on port1
- `sw.js`

```jsx
"use strict";

// TODO
const version = 2;
var isOnline = true;
var isLoggedIn = false;

self.addEventListener("install", onInstall);

self.addEventListener("activate", onActivate);

self.addEventListener("message", onMessage);

main().catch(console.error);

async function main() {
  await sendMessage({ requestStatusUpdate: true });
}

async function sendMessage(msg) {
  var allClients = await clients.matchAll({ includeUncontrolled: true });
  return Promise.all(
    allClients.map(function clientMsg(client) {
      var msgChannel = new MessageChannel();
      msgChannel.port1.onmessage = onMessage;
      return eclient.postMessage(msg, [msgChannel.port2]);
    }),
  );
}

function onMessage({ data }) {
  if (data.stausUpdate) {
    ({ isOnline, isLoggedIn } = data.statusUpdate);
    console.log(
      `Service Worker (v${version}) status update, isOnline:${isOnline}, isLoggedIn: ${isLoggedIn} `,
    );
  }
}

async function onInstall() {
  console.log(`Service Worker (${version}) installed.`);
}
function onActivate(event) {
  console.log(`Service Worker (${version}) activate.`);
  event.waitUntil(handleActivation());
}

async function handleActivation() {
  await clients.claim();
  console.log(`Service Worker (${version}) activated.`);
}

```

## Caching with Service Worker

- We are using versioned cache → since the version changes each time we update the service worker thus each cached item using this name would also change and discard old cached item.
- There are different things we can cache, for now we are gonna hard code  logged out items ( stuff not sensitive to sessions ) by listing them in an array.
    - it inlcudes stuff like css files, js files some assets etc.
- There are different ways to specify items to be cached
    - **Hard Coding** : the one we are doing
    - **Dynamic** : Generating urls we need dynamically
    - **From Server** : Ask server to give us thing we need to cache
    
    `sw.js`
    
    ```jsx
    var cacheName = `ramblings-${version}`
    
    var urlsToCache = {
    	loggedOut: [
    		"/",
    		"/about",
    		"/contact",
    		"/login",
    		"/404",
    		"/offline",
    		"/css/styles.css",
    		"/js/blog.js",
    		"/js/home.js",
    		"/js/login.js",
    		"/js/add-post.js",
    		"/images/logo.gif",
    		"/images/offline.png",
    	]
    }
    ```
    
- The urls here are / will be loaded exactly like this on client side from server

### Adding to Service Worker Cache

- If we do not have asked to do a force reload, then we should not cache out these files again ( unnecessarily )
- Now our purpose is to simply write an  asynchronous function to cache using the URLs specified in the list, mapping over the array of files and either getting a result from the cache or making a fetch request to add to the cache.
    - While making request, make sure to omit `credentials` since this request is for logged out resources.
    - `cache` is set to `no-cache` as we want to tell browser layer not to cache this request itself or return result from intermediary browser cache rather than getting fresh results from the server.
    - When we get response successfully back we usually save the `cloned` response to `cache`.
        - Why cloned ? because if we are returning response and saving oiginal response to cache it causes errors like headers already closed once, thus its better to `save clone` and send back original `response`
    - Here we do not clone as we are not returning the response and have to save it anyway.

```jsx
async function cachedLoggedOutFiles(forceReload = false){
	var cache = await caches.match(cacheName);

	return Promise.all(
		urlsToCache.loggedOut.map(async function requestFile(url){
			try{
				let res;
				if(!forceReload){
					res = await cache.match(url);
					if(res){
						return res; 
					}
				}
				let fetchOptions = {
					method: "GET",
					cache: "no-cache",
					credentials: "omit"
				}
				res = fetch(url, fetchOptions);
				if(res.ok){
					await cache.put( url, res)
				}
			}catch(error){
				
			}
		})
	)
} 

```

so complete `sw.js` now is 

```jsx
"use strict";

// TODO
const version = 3;
var isOnline = true;
var isLoggedIn = false;
var cacheName = `ramblings-${version}`

var urlsToCache = {
	loggedOut: [
		"/",
		"/about",
		"/contact",
		"/login",
		"/404",
		"/offline",
		"/css/styles.css",
		"/js/blog.js",
		"/js/home.js",
		"/js/login.js",
		"/js/add-post.js",
		"/images/logo.gif",
		"/images/offline.png",
	]
}

async function cachedLoggedOutFiles(forceReload = false){
	var cache = await caches.match(cacheName);

	return Promise.all(
		urlsToCache.loggedOut.map(async function requestFile(url){
			try{
				let res;
				if(!forceReload){
					res = await cache.match(url);
					if(res){
						return res; 
					}
				}
				let fetchOptions = {
					method: "GET",
					cache: "no-cache",
					credentials: "omit"
				}
				res = fetch(url, fetchOptions);
				if(res.ok){
					await cache.put( url, res)
				}
			}catch(error){
				
			}
		})
	)
} 

self.addEventListener("install", onInstall);

self.addEventListener("activate", onActivate);

self.addEventListener("message", onMessage);

main().catch(console.error);

async function main() {
  await sendMessage({ requestStatusUpdate: true });
}

async function sendMessage(msg) {
  var allClients = await clients.matchAll({ includeUncontrolled: true });
  return Promise.all(
    allClients.map(function clientMsg(client) {
      var msgChannel = new MessageChannel();
      msgChannel.port1.onmessage = onMessage;
      return client.postMessage(msg, [msgChannel.port2]);
    }),
  );
}

function onMessage({ data }) {
  if (data.statusUpdate) {
    ({ isOnline, isLoggedIn } = data.statusUpdate);
    console.log(
      `Service Worker (v${version}) status update, isOnline:${isOnline}, isLoggedIn: ${isLoggedIn} `,
    );
  }
}

async function onInstall() {
  console.log(`Service Worker (${version}) installed.`);
}
function onActivate(event) {
  console.log(`Service Worker (${version}) activate.`);
  event.waitUntil(handleActivation());
}

async function handleActivation() {
  await clients.claim();
  console.log(`Service Worker (${version}) activated.`);
}

```

### Service Worker Cache Demo

- Now its time to call this
    - first in `main` ( without forceReload )
    - `handleActivattion`, here we want forceReload since service worker was changed.
    
    ![Screenshot 2025-02-13 at 10.54.29 AM.png](Screenshot_2025-02-13_at_10.54.29_AM.png)
    
- Then go to browser,
    1. Stop
    2. unregister 
    3. change page or refresh 
- some misspellings we had so change those and try again in Application / cache Storage

```jsx
"use strict";

// TODO
const version = 3;
var isOnline = true;
var isLoggedIn = false;
var cacheName = `ramblings-${version}`;

var urlsToCache = {
  loggedOut: [
    "/",
    "/about",
    "/contact",
    "/login",
    "/404",
    "/offline",
    "/css/style.css",
    "/js/blog.js",
    "/js/home.js",
    "/js/login.js",
    "/js/add-post.js",
    "/images/logo.gif",
    "/images/offline.png",
  ],
};

async function cacheLoggedOutFiles(forceReload = false) {
  var cache = await caches.open(cacheName);

  return Promise.all(
    urlsToCache.loggedOut.map(async function requestFile(url) {
      try {
        let res;
        if (!forceReload) {
          res = await cache.match(url);
          if (res) {
            return res;
          }
        }
        let fetchOptions = {
          method: "GET",
          cache: "no-cache",
          credentials: "omit",
        };
        res = fetch(url, fetchOptions);
        if (res.ok) {
          await cache.put(url, res);
        }
      } catch (error) {}
    }),
  );
}

self.addEventListener("install", onInstall);

self.addEventListener("activate", onActivate);

self.addEventListener("message", onMessage);

main().catch(console.error);

async function main() {
  await sendMessage({ requestStatusUpdate: true });
  await cacheLoggedOutFiles();
}

async function sendMessage(msg) {
  var allClients = await clients.matchAll({ includeUncontrolled: true });
  return Promise.all(
    allClients.map(function clientMsg(client) {
      var msgChannel = new MessageChannel();
      msgChannel.port1.onmessage = onMessage;
      return client.postMessage(msg, [msgChannel.port2]);
    }),
  );
}

function onMessage({ data }) {
  if (data.statusUpdate) {
    ({ isOnline, isLoggedIn } = data.statusUpdate);
    console.log(
      `Service Worker (v${version}) status update, isOnline:${isOnline}, isLoggedIn: ${isLoggedIn} `,
    );
  }
}

async function onInstall() {
  console.log(`Service Worker (${version}) installed.`);
}
function onActivate(event) {
  console.log(`Service Worker (${version}) activate.`);
  event.waitUntil(handleActivation());
}

async function handleActivation() {
  await clients.claim();
  await cacheLoggedOutFiles(/*forceReload=*/ true);
  console.log(`Service Worker (${version}) activated.`);
}

```

- `style.css` instead of `styles.css` and `open` instead of `match` at start of `cacheLoggedOutFiles`

### Delete old caches

- Make sure to delete old caches which matches our urls but has different version number than current version we have.
- We do this `clearCache` in activation method so we are sure that previous service worker is terminated and the old cache is no longer being used thus will not halt any on-going
- Had a missed `await` for fetch in `cacheLoggedOutFiles` method and return nothing in case of res there for `!forceReload`

```jsx
"use strict";

// TODO
const version = 4;
var isOnline = true;
var isLoggedIn = false;
var cacheName = `ramblings-${version}`;

var urlsToCache = {
  loggedOut: [
    "/",
    "/about",
    "/contact",
    "/login",
    "/404",
    "/offline",
    "/css/style.css",
    "/js/blog.js",
    "/js/home.js",
    "/js/login.js",
    "/js/add-post.js",
    "/images/logo.gif",
    "/images/offline.png",
  ],
};

async function cacheLoggedOutFiles(forceReload = false) {
  var cache = await caches.open(cacheName);

  return Promise.all(
    urlsToCache.loggedOut.map(async function requestFile(url) {
      try {
        let res;
        if (!forceReload) {
          res = await cache.match(url);
          if (res) {
            return;
          }
        }
        let fetchOptions = {
          method: "GET",
          cache: "no-cache",
          credentials: "omit",
        };
        res = await fetch(url, fetchOptions);
        if (res.ok) {
          await cache.put(url, res);
        }
      } catch (error) {}
    }),
  );
}

self.addEventListener("install", onInstall);

self.addEventListener("activate", onActivate);

self.addEventListener("message", onMessage);

main().catch(console.error);

async function main() {
  await sendMessage({ requestStatusUpdate: true });
  await cacheLoggedOutFiles();
}

async function sendMessage(msg) {
  var allClients = await clients.matchAll({ includeUncontrolled: true });
  return Promise.all(
    allClients.map(function clientMsg(client) {
      var msgChannel = new MessageChannel();
      msgChannel.port1.onmessage = onMessage;
      return client.postMessage(msg, [msgChannel.port2]);
    }),
  );
}

function onMessage({ data }) {
  if (data.statusUpdate) {
    ({ isOnline, isLoggedIn } = data.statusUpdate);
    console.log(
      `Service Worker (v${version}) status update, isOnline:${isOnline}, isLoggedIn: ${isLoggedIn} `,
    );
  }
}

async function onInstall() {
  console.log(`Service Worker (${version}) installed.`);
}
function onActivate(event) {
  console.log(`Service Worker (${version}) activate.`);
  event.waitUntil(handleActivation());
}

async function handleActivation() {
  await clearCaches();
  await clients.claim();
  await cacheLoggedOutFiles(/*forceReload=*/ true);
  console.log(`Service Worker (${version}) activated.`);
}
async function clearCaches() {
  var cacheNames = await caches.keys();
  var oldCacheNames = cacheNames.filter(function matchOldCache(cacheName) {
    if (/^ramblings-\d+$/.test(cacheName)) {
      let [, cacheVersion] = cacheName.match(/^ramblings-(\d+)$/);
      cacheVersion = cacheVersion != null ? Number(cacheVersion) : cacheVersion;
      return cacheVersion > 0 && cacheVersion != version;
    }
  });

  return Promise.all(
    oldCacheNames.map(function deleteCache(cacheName) {
      return caches.delete(cacheName);
    }),
  );
}

```

![Screenshot 2025-02-13 at 11.35.35 AM.png](Screenshot_2025-02-13_at_11.35.35_AM.png)

## Service Worker Routing

- Its Crucial to understand that before we go on path for caching with service worker, we must understand that it will no longer be working unless we have a complete the whole implementation.
- Plus its also better to do this at a later point in a SDLC rather than at start of a project since its time consuming and will introduce many errors and problems along the way.

### Routing Cache Fallback offline

- `fetch` event listens to `inbound reques` coming from web page to our `onFetch` callback through `service worker`
- for now we will wait until we have finished all of our work.
- In this tutorial **we are strictly ignoring to cache things which we get from external resources** ( in my case it might be items stored in S3 buckets maybe )

```jsx
//sw.js
self.addEventListener('fetch', onFetch);
function onFetch(event){
	event.waitUntil(router(event.request));	
}

async function router(request){
	var url = URL(request.url);
	var requestUrl = url.pathname;
	var cacheNameObject = await caches.open(cacheName);

}
```

### Caching Strategies

- To make sure we are only caching stuff request from our own server ( backend ), we will look at origin of these urls
- Now lets see different strategies for caching ( outbound requests )
1. First get resource from server and if it comes back us that response.
2. Request it from server, if it succeeds, then cache it proactively cache it.
3. Check cache before making a request, if its not there only then get it from server.
    1. In case if we are `online` we will check for `server` when cache has no `resource` 
    2. Otherwise if we are `offline` and `cache` has nothing stored then we show an offline page.

### implementing a Caching Strategy

- Make request to server and store in cache if not already, ( single strategy for both inbound and outbound requests )

 

```jsx
function onFetch(event) {
  event.respondWith(router(event.request));
}

async function router(request) {
  var webPageUrl = new URL(request.url);
  var requestUrl = webPageUrl.pathname;
  var cacheNameObject = await caches.open(cacheName);
  if (webPageUrl.origin == ourWebOrigin) {
    try {
      let fetchOptions = {
        method: request.method,
        headers: request.headers,
        credentials: "omit",
        cache: "no-store",
      };
      let responseFromServer = await fetch(request.url, fetchOptions);
      if (responseFromServer && responseFromServer.ok) {
        await cacheNameObject.put(requestUrl, responseFromServer.clone());
        return responseFromServer;
      }
    } catch (error) {
      let responseFromServerCached = await cacheNameObject.match(requestUrl);
      if (responseFromServerCached) {
        return responseFromServerCached.clone();
      }
    }
  }
  // TODO: figure out cors request
}
```

- Repeat changes for sw.js

Stop → unregister → clear logs → refresh

- Now we see it works offline as well.
- Some errors in network tab as we are still tring to make fetch request even when we are offline. which causes errors.

### Logged Out walkthrough

```jsx
//sw.js
async function router(request) {
  var webPageUrl = new URL(request.url);
  var requestUrl = webPageUrl.pathname;
  var cacheNameObject = await caches.open(cacheName);
  if (webPageUrl.origin == ourWebOrigin) {
    if (/^\/api\/.+$/.test(requestUrl)) {
      if (isOnline) {
        try {
          let fetchOptions = {
            method: request.method,
            headers: request.headers,
            credentials: "same-origin",
            cache: "no-store",
          };
          let responseFromServer = await fetch(request.url, fetchOptions);
          if (responseFromServer && responseFromServer.ok) {
            if (request.method === "GET") {
              await cacheNameObject.put(requestUrl, responseFromServer.clone());
            }
            return responseFromServer;
          }
        } catch (error) {}
      }
      let cachedResponseFromServer = await cacheNameObject.match(requestUrl);
      if (cachedResponseFromServer) {
        return cachedResponseFromServer.clone();
      }
      return notFoundResponse();
    }
    // are we requesting the page ( routing to an html page )
    else if (request.headers.get("Accept").includes("text/html")) {
      if (/^\/(?:login|logout|add-post)$/.test(requestUrl)) {
        // TODO:
      } else {
        if (isOnline) {
          try {
            let fetchOptions = {
              method: request.method,
              headers: request.headers,
              cache: "no-store",
            };
            let responseFromServer = await fetch(request.url, fetchOptions);
            if (responseFromServer && responseFromServer.ok) {
              // since we return 200 network response with a 404 status we do not want our sw to think we did find a legit page while its actually a 404 so that is why we need to make this check here and make sure we do not cache another copy of 404 page for same url
              if (!responseFromServer.headers.get("X-Not-Found")) {
                await cacheNameObject.put(
                  requestUrl,
                  responseFromServer.clone(),
                );
              }
              return responseFromServer;
            }
          } catch (error) {}
        }
        let cachedResponseFromServer = await cacheNameObject.match(requestUrl);
        if (cachedResponseFromServer) {
          return cachedResponseFromServer;
        }
        let offlinePageFromCache = cacheNameObject.match("/offline");
        return offlinePageFromCache;
      }
    } else {
      let cachedResponseFromServer = await cacheNameObject.match(requestUrl);
      if (cachedResponseFromServer) {
        return cachedResponseFromServer;
      } else {
        if (isOnline) {
          try {
            let fetchOptions = {
              method: request.method,
              headers: request.headers,
              cache: "no-store",
            };
            let responseFromServer = await fetch(request.url, fetchOptions);
            if (responseFromServer && responseFromServer.ok) {
              await cacheNameObject.put(requestUrl, responseFromServer.clone());
              return responseFromServer;
            }
          } catch (error) {}
        }
      }
    }
  }
  // TODO: figure out cors request
}

function notFoundResponse() {
  return new Response("", {
    status: 404,
    statusName: "Not Found",
  });
}

```

These things are usually ignored in cases of frameworks like workbox etc.

## Background Sync

```jsx
"use strict";

importScripts("/js/external/idb-keyval-iife.min.js");

var version = 8;
var isOnline = true;
var isLoggedIn = false;
var cacheName = `ramblings-${version}`;
var allPostsCaching = false;

var urlsToCache = {
  loggedOut: [
    "/",
    "/about",
    "/contact",
    "/404",
    "/login",
    "/offline",
    "/css/style.css",
    "/js/blog.js",
    "/js/home.js",
    "/js/login.js",
    "/js/add-post.js",
    "/js/external/idb-keyval-iife.min.js",
    "/images/logo.gif",
    "/images/offline.png",
  ],
};

self.addEventListener("install", onInstall);
self.addEventListener("activate", onActivate);
self.addEventListener("message", onMessage);
self.addEventListener("fetch", onFetch);

main().catch(console.error);

// ****************************

async function main() {
  await sendMessage({ statusUpdateRequest: true });
  await cacheLoggedOutFiles();
  return cacheAllPosts();
}

function onInstall(evt) {
  console.log(`Service Worker (v${version}) installed`);
  self.skipWaiting();
}

function onActivate(evt) {
  evt.waitUntil(handleActivation());
}

async function handleActivation() {
  await clearCaches();
  await cacheLoggedOutFiles(/*forceReload=*/ true);
  await clients.claim();
  console.log(`Service Worker (v${version}) activated`);

  // spin off background caching of all past posts (over time)
  cacheAllPosts(/*forceReload=*/ true).catch(console.error);
}

async function clearCaches() {
  var cacheNames = await caches.keys();
  var oldCacheNames = cacheNames.filter(function matchOldCache(cacheName) {
    var [, cacheNameVersion] = cacheName.match(/^ramblings-(\d+)$/) || [];
    cacheNameVersion =
      cacheNameVersion != null ? Number(cacheNameVersion) : cacheNameVersion;
    return cacheNameVersion > 0 && version !== cacheNameVersion;
  });
  await Promise.all(
    oldCacheNames.map(function deleteCache(cacheName) {
      return caches.delete(cacheName);
    }),
  );
}

async function cacheLoggedOutFiles(forceReload = false) {
  var cache = await caches.open(cacheName);

  return Promise.all(
    urlsToCache.loggedOut.map(async function requestFile(url) {
      try {
        let res;

        if (!forceReload) {
          res = await cache.match(url);
          if (res) {
            return;
          }
        }

        let fetchOptions = {
          method: "GET",
          cache: "no-store",
          credentials: "omit",
        };
        res = await fetch(url, fetchOptions);
        if (res.ok) {
          return cache.put(url, res);
        }
      } catch (err) {}
    }),
  );
}

async function cacheAllPosts(forceReload = false) {
  // already caching the posts?
  if (allPostsCaching) {
    return;
  }
  allPostsCaching = true;
  await delay(5000);

  var cache = await caches.open(cacheName);
  var postIDs;

  try {
    if (isOnline) {
      let fetchOptions = {
        method: "GET",
        cache: "no-store",
        credentials: "omit",
      };
      let res = await fetch("/api/get-posts", fetchOptions);
      if (res && res.ok) {
        await cache.put("/api/get-posts", res.clone());
        postIDs = await res.json();
      }
    } else {
      let res = await cache.match("/api/get-posts");
      if (res) {
        let resCopy = res.clone();
        postIDs = await res.json();
      }
      // caching not started, try to start again (later)
      else {
        allPostsCaching = false;
        return cacheAllPosts(forceReload);
      }
    }
  } catch (err) {
    console.error(err);
  }

  if (postIDs && postIDs.length > 0) {
    return cachePost(postIDs.shift());
  } else {
    allPostsCaching = false;
  }

  // *************************

  async function cachePost(postID) {
    var postURL = `/post/${postID}`;
    var needCaching = true;

    if (!forceReload) {
      let res = await cache.match(postURL);
      if (res) {
        needCaching = false;
      }
    }

    if (needCaching) {
      await delay(10000);
      if (isOnline) {
        try {
          let fetchOptions = {
            method: "GET",
            cache: "no-store",
            credentials: "omit",
          };
          let res = await fetch(postURL, fetchOptions);
          if (res && res.ok) {
            await cache.put(postURL, res.clone());
            needCaching = false;
          }
        } catch (err) {}
      }

      // failed, try caching this post again?
      if (needCaching) {
        return cachePost(postID);
      }
    }

    // any more posts to cache?
    if (postIDs.length > 0) {
      return cachePost(postIDs.shift());
    } else {
      allPostsCaching = false;
    }
  }
}

async function sendMessage(msg) {
  var allClients = await clients.matchAll({ includeUncontrolled: true });
  return Promise.all(
    allClients.map(function sendTo(client) {
      var chan = new MessageChannel();
      chan.port1.onmessage = onMessage;
      return client.postMessage(msg, [chan.port2]);
    }),
  );
}

function onMessage({ data }) {
  if ("statusUpdate" in data) {
    ({ isOnline, isLoggedIn } = data.statusUpdate);
    console.log(
      `Service Worker (v${version}) status update... isOnline:${isOnline}, isLoggedIn:${isLoggedIn}`,
    );
  }
}

function onFetch(evt) {
  evt.respondWith(router(evt.request));
}

async function router(req) {
  var url = new URL(req.url);
  var reqURL = url.pathname;
  var cache = await caches.open(cacheName);

  // request for site's own URL?
  if (url.origin == location.origin) {
    // are we making an API request?
    if (/^\/api\/.+$/.test(reqURL)) {
      let fetchOptions = {
        credentials: "same-origin",
        cache: "no-store",
      };
      let res = await safeRequest(
        reqURL,
        req,
        fetchOptions,
        /*cacheResponse=*/ false,
        /*checkCacheFirst=*/ false,
        /*checkCacheLast=*/ true,
        /*useRequestDirectly=*/ true,
      );
      if (res) {
        if (req.method == "GET") {
          await cache.put(reqURL, res.clone());
        }
        // clear offline-backup of successful post?
        else if (reqURL == "/api/add-post") {
          await idbKeyval.del("add-post-backup");
        }
        return res;
      }

      return notFoundResponse();
    }
    // are we requesting a page?
    else if (req.headers.get("Accept").includes("text/html")) {
      // login-aware requests?
      if (/^\/(?:login|logout|add-post)$/.test(reqURL)) {
        let res;

        if (reqURL == "/login") {
          if (isOnline) {
            let fetchOptions = {
              method: req.method,
              headers: req.headers,
              credentials: "same-origin",
              cache: "no-store",
              redirect: "manual",
            };
            res = await safeRequest(reqURL, req, fetchOptions);
            if (res) {
              if (res.type == "opaqueredirect") {
                return Response.redirect("/add-post", 307);
              }
              return res;
            }
            if (isLoggedIn) {
              return Response.redirect("/add-post", 307);
            }
            res = await cache.match("/login");
            if (res) {
              return res;
            }
            return Response.redirect("/", 307);
          } else if (isLoggedIn) {
            return Response.redirect("/add-post", 307);
          } else {
            res = await cache.match("/login");
            if (res) {
              return res;
            }
            return cache.match("/offline");
          }
        } else if (reqURL == "/logout") {
          if (isOnline) {
            let fetchOptions = {
              method: req.method,
              headers: req.headers,
              credentials: "same-origin",
              cache: "no-store",
              redirect: "manual",
            };
            res = await safeRequest(reqURL, req, fetchOptions);
            if (res) {
              if (res.type == "opaqueredirect") {
                return Response.redirect("/", 307);
              }
              return res;
            }
            if (isLoggedIn) {
              isLoggedIn = false;
              await sendMessage("force-logout");
              await delay(100);
            }
            return Response.redirect("/", 307);
          } else if (isLoggedIn) {
            isLoggedIn = false;
            await sendMessage("force-logout");
            await delay(100);
            return Response.redirect("/", 307);
          } else {
            return Response.redirect("/", 307);
          }
        } else if (reqURL == "/add-post") {
          if (isOnline) {
            let fetchOptions = {
              method: req.method,
              headers: req.headers,
              credentials: "same-origin",
              cache: "no-store",
            };
            res = await safeRequest(
              reqURL,
              req,
              fetchOptions,
              /*cacheResponse=*/ true,
            );
            if (res) {
              return res;
            }
            res = await cache.match(isLoggedIn ? "/add-post" : "/login");
            if (res) {
              return res;
            }
            return Response.redirect("/", 307);
          } else if (isLoggedIn) {
            res = await cache.match("/add-post");
            if (res) {
              return res;
            }
            return cache.match("/offline");
          } else {
            res = await cache.match("/login");
            if (res) {
              return res;
            }
            return cache.match("/offline");
          }
        }
      }
      // otherwise, just use "network-and-cache"
      else {
        let fetchOptions = {
          method: req.method,
          headers: req.headers,
          cache: "no-store",
        };
        let res = await safeRequest(
          reqURL,
          req,
          fetchOptions,
          /*cacheResponse=*/ false,
          /*checkCacheFirst=*/ false,
          /*checkCacheLast=*/ true,
        );
        if (res) {
          if (!res.headers.get("X-Not-Found")) {
            await cache.put(reqURL, res.clone());
          } else {
            await cache.delete(reqURL);
          }
          return res;
        }

        // otherwise, return an offline-friendly page
        return cache.match("/offline");
      }
    }
    // all other files use "cache-first"
    else {
      let fetchOptions = {
        method: req.method,
        headers: req.headers,
        cache: "no-store",
      };
      let res = await safeRequest(
        reqURL,
        req,
        fetchOptions,
        /*cacheResponse=*/ true,
        /*checkCacheFirst=*/ true,
      );
      if (res) {
        return res;
      }

      // otherwise, force a network-level 404 response
      return notFoundResponse();
    }
  }
}

async function safeRequest(
  reqURL,
  req,
  options,
  cacheResponse = false,
  checkCacheFirst = false,
  checkCacheLast = false,
  useRequestDirectly = false,
) {
  var cache = await caches.open(cacheName);
  var res;

  if (checkCacheFirst) {
    res = await cache.match(reqURL);
    if (res) {
      return res;
    }
  }

  if (isOnline) {
    try {
      if (useRequestDirectly) {
        res = await fetch(req, options);
      } else {
        res = await fetch(req.url, options);
      }

      if (res && (res.ok || res.type == "opaqueredirect")) {
        if (cacheResponse) {
          await cache.put(reqURL, res.clone());
        }
        return res;
      }
    } catch (err) {}
  }

  if (checkCacheLast) {
    res = await cache.match(reqURL);
    if (res) {
      return res;
    }
  }
}

function notFoundResponse() {
  return new Response("", {
    status: 404,
    statusText: "Not Found",
  });
}

function delay(ms) {
  return new Promise(function c(res) {
    setTimeout(res, ms);
  });
}

```

here `cacheAllPosts` is called on `main`.

- We effectively get all `postIds` and then get each post `one by one` in background with delay of 10s to make sure network is not burdened.
- This is a simpl background sync
- if it fails we retry using `needCahing`

### Add Form values to IndexDB

- We can save our form values entered by our user to the `indexDB` if we are offline and when we come online we can send this to server and delete entries from `indexdDB`.
-