---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
B-Tree Indexes ^KPXuF6dK

- most common type of database index
- efficiently organizes data for fast search and updates.
- by maintaining balanced tree structure that minimizes number of disk reads.
- Self balancing that maintains sorted data
- allows for efficient insertions, deletions and searches ^VbgbOPOk

Types of indexes ^yqVbbelF

Structure of B-Trees ^wAHs2ynW

- Each node can have multiple child nodes unlike binary tree
- Each node contains ordered array of keys and pointers, structured to minimize disk reads. ^lagXccu8

Each node in B-tree follows strict rules.
- All leaf nodes must be at the same depth
- Each node can contain between m/2 and m keys (where m is the order of the tree)
- A node with k keys must have exactly k+1 children
- Keys within a node are kept in sorted order ^dUtTh0WE

Why B-Trees are default Choice in many cases ^NKP46ZyS

- They maintain sorted order, making range queries and ORDER BY operations efficient
- They're self-balancing, ensuring predictable performance even as data grows
- They minimize disk I/O by matching their structure to how databases store data
- They handle both equality searches (email = 'x') and range searches (age > 25) equally well
- They remain balanced even with random inserts and deletes, avoiding the performance cliffs you might see with simpler tree structures ^pxmEiknR

1 ^AlS8MkDM

Example to understand B-Trees ^COPDMrwm

- Lets say we query all column of Users with age = 51
- We will first fetch root page into memory
- Since age = 51 which is between 50 and 90 we fetch 3rd node
- Since age = 51 so Page 3 would be fetched into memory

- In case of age > 51
- we fetch root nodes and then all nodes and pages from 50 to 90, then fetch each page these nodes point in memory ^dybzg8j8

Hash Index ^1aDeEaJn

- Excel at exact query match.
- Simply a persistent hash map implementation ^W2ZGeS7R

How indexes work ^XKWhoCzv

At core hash indexes are just Hash map indexed values to row locations ( pages ) 
- Database maintains array of buckets.
- each bucket stores multiple key-location pairs.
- When indexing a value db hashes it to determine which bucket should store pointer to row data ( page ) ^xKghLEas

buckets[hash("alice@example.com")] -> [ptr to page 1]
buckets[hash("bob@example.com")]   -> [ptr to page 2] ^gtFkLPOX

- Hash collisions are handled by allowing multiple entries per bucket.
- This structure makes hash indexes incredibly fast for exact-mach queries.
- But uselss for range queries and sorting ^nhORTx5H

Chaining with Overflow  ^141y2j4X

Chaining means when multiple keys land in the same hash bucket, the bucket stores one page of entries and links to extra overflow pages to hold the rest, so collisions are kept in a short linked chain.

Concrete example. Suppose we have 4 buckets and bucket 2 already stores alice. We insert alex and the bucket page is full, so PostgreSQL adds an overflow page and links it to bucket 2, placing alex there. Later amy also hashes to bucket 2 and goes onto that overflow page. To read alex we hash to bucket 2, read the bucket page, then follow the link to the overflow page and scan a few entries to find alex. You can imagine a mailbox that gets a clip on box when it fills up. The carrier checks the main box first, then the clip on boxes right next to it. ^uIyRDJhI

Real World usage ^CDEXa1En

Used particularly for in-memory databases like 
- Redis, it uses hash tables as primary data structure for key-value lookups since all data lives in memory   ^7ALAoKu7

- B-Trees perform almost as Hash Indexes in equality comparisions while much better
in range and sorting thus PostgreSQL uses B-Trees by default. ^Niqoebiv

For system design interviews, you might consider hash indexes when:

- You need the absolute fastest possible exact-match lookups
- You'll never need range queries or sorting
- You have plenty of memory (hash indexes tend to be larger than B-trees)
 ^1rbLzfwi

When to Choose Hash Indexes ^brWWUwW8

2 ^x5R608MZ

GeoSpatial Indexes ^MA0ieA10

- Favoruite indexes but only in case of location data
Uber, Yelp, Find my Friends ^a7DMuFcN

Why B-tree is not a good choice for Spatial Data ^l2SvzJ0r

Three main Approaches
- GeoHashes
- Quad Trees
- R Trees ( predecessor of Quad Tree ) ^H1I2mY0w

Each have its own trade-offs but 
- they preserve spatial relationships in our index structure. ^clwpPG0w

Geohash ^JiezffMu

- Becuase it sees things as 1D like let say we have 5 restaurants plotted on map ^pYMYxPAc

Imagine you have 5 restaurants plotted on a map:
(map view)

    B
  A       C
        D
            E ^4Ml3TFv2

A B-Tree on latitude just "flattens" them onto a single line:
(latitude axis only)
─────────────────────────────────
  A   B   C   D   E ^FXpAGjAe

Now apparently `C` and `D` are close but are they really close ? No 
Restaurant C and D are close on the map. But are they necessarily close on this latitude line?
Think about two restaurants — one in New Jersey and one in New York City. They could have the exact same latitude but be miles apart east-west. And two restaurants could have very different latitudes but still be geographically close (like on a diagonal). ^TYPR8101

We agreed: sorting is 1D, but space is 2D. Geohash's bet is:

> *"What if we could fold 2D space into 1D in a way that nearby points stay nearby?"*

Before I explain how, let me ask you something intuitive.

Look at this map. Imagine dividing the entire world into just **two halves** — left and right (West and East):

```
┌─────────────┬─────────────┐
│             │             │
│      0      │      1      │
│    (West)   │    (East)   │
│             │             │
└─────────────┴─────────────┘
```

Now divide each half again — top and bottom:

```
┌─────────────┬─────────────┐
│  00 (NW)    │  10 (NE)    │
├─────────────┼─────────────┤
│  01 (SW)    │  11 (SE)    │
└─────────────┴─────────────┘
```

Keep dividing, each time appending a bit...

**My question:** If you keep doing this — halving, halving, halving — what does a restaurant's final binary string represent? And what would it mean if two restaurants share a long common *prefix* like `0110101...`?

Geohash uses **Base32** (characters like `0-9, a-z`).

```
Whole world
├── West (e)
│   ├── NW (e0)
│   │   ├── ... (e0f)
│   └── SW (e1)
└── East (s)
    ├── NE (s0)
    │   ├── ... (s0u) ← Restaurant A
    │   ├── ... (s0u) ← Restaurant B
    └── SE (s1)
```

Restaurant A: `s0u3bq`
Restaurant B: `s0u3xt`

They share prefix `s0u3` — meaning they're in the **same small box** on the map.

---

> Two places sharing a long prefix = they're in the same geographic box = they're close to each other.

So instead of storing `(lat, lng)`, Geohash converts it to a **single string**. Now a regular B-Tree can index it! Nearby places sort *near each other* in the index. ^EkQVf1c4

How this helps us  ^A6HgOMhS

- Finding nearby locations in geohashes means they sahre similar prefixes
- Two restaurants on the same block might have geohashes that start with "9q8yyk", while a restaurant in a different neighborhood might start with "9q8yym".

- When we form B-Tree index on these strings and try searching them its only matter of matching prefixes only.
- We can also run range queries ( range scan ) using the prefixes. 
 ^Zk4mVrQo

Problem ^TlqZgh7K

┌──────────┬──────────┐
│          │          │
│  A (e7)  │  B (s0)  │
│          │          │
├──────────┴──────────┤
A and B are literally meters apart but their prefixes share nothing in common.

How do people work around this in practice?
When you search "restaurants near me" with Geohash, you don't just search your own cell — you search your cell + all 8 neighboring cells:
┌─────┬─────┬─────┐
│ NW  │  N  │ NE  │
├─────┼─────┼─────┤
│  W  │ ME  │  E  │  ← search all 9 cells
├─────┼─────┼─────┤
│ SW  │  S  │ SE  │
└─────┴─────┴─────┘
It works, but it's a hack — you're compensating for a structural weakness. ^YnpRuzsV

Quad Trees ^Hyd9okP0

- Unlike geohash which divides coordinates into strings.
- Quadtrees directly divides regions recursively into four quadrants. ^StC3AHbP

How it works ^1bZI2c4p

- Start with one square covering your entire area.
- When a square contains more than some threshold of points (typically 4-8), split it into four equal quadrants. 
- Continue this recursive subdivision until reaching a maximum depth or achieving the desired point density per node.  ^heAXccwd

Advantage ^yvSW4iv0

- dense areas get subdivided more finely while sparse regions maintain larger quadrants. ^vN7yuEJ1

Disadvantages ^VHZVqg8r

- Not used in modern production systems . Why ? becuase unlike geohashes which uses exisiting B-tree implementations, quad-trees require specialised tree structures. ^DxDfWZn1

Now think about searching. When a user says "find restaurants within 5 miles":

Start at root [World]
Does this node overlap my search circle? No → skip entire branch
Yes → go deeper into its children
Repeat

That "skip entire branch" is called pruning — and it's why Quadtrees are fast. ^rZvwpqDj

Probelm
- Similar one to GeoHash
Geohash boundary problem:
- Two points are close but fall in different cells due to arbitrary grid lines.

Quadtree boundary problem:
- Same thing — grid lines are still fixed, just adaptive in depth not position.
So both suffer from the same root cause:

The grid lines are fixed and don't care where your data actually is. ^ko87fuPz

R-Trees ^XxMrqxr9

- Instead of splitting space into fix quadrants. 
- R-Trees work with flexible, overlapping rectangles.
- Where a quadtree rigidly divides each region into four equal parts regardless of data distribution. 
- R-trees adapt their rectangles to the actual data.
- Think of organizing photos on a table - a quadtree approach would divide the table into equal quarters and keep subdividing, while an R-tree would let you create natural, overlapping groupings of nearby photos. ^ukiDYnyE

"Related groups would always be together"

That's it. The box is defined by the data, not by arbitrary grid lines.

So an R-Tree looks like this:
Root: [big box around everything]
        /              \
[box around           [box around
 dense city]           rural area]
    / | \                  |
[A,B] [C,D] [E,F]        [G]
Each node is a Minimum Bounding Rectangle (MBR) — the tightest possible box around its children. ^Uys3oQJC

"B-Trees sort data on a single axis. Geographic proximity requires two axes simultaneously. Sorting by latitude gives you a horizontal strip — restaurants in that strip could be thousands of miles apart east-west. You can't represent 2D closeness in a 1D ordering." ^Hikv3pCZ

How it works ^obfg1NgY

When searching for nearby restaurants in San Francisco, an R-tree might first identify the large rectangle containing the city, then drill down through progressively smaller, overlapping rectangles until reaching individual restaurant locations. These rectangles aren't constrained to fixed sizes or positions - they adapt to wherever your data actually clusters. ^z5yOwFts

This flexibility offers a crucial advantage: R-trees can efficiently handle both points and larger shapes in the same index structure. A single R-tree can index everything from individual restaurant locations to delivery zone polygons and road networks. The rectangles simply adjust their size to bound whatever shapes they contain. ^1zRGmAtR

If you're asked about geospatial indexing in an interview, focus on explaining the problem clearly and contrasting a tree-based approach with a hash-based approach.
For example, you could say something like:
"Traditional indexes like B-trees don't work well for spatial data because they treat latitude and longitude as independent dimensions. To efficiently search for nearby locations, we need an index that understands spatial relationships. Geohash is a hash-based approach that converts 2D coordinates into a 1D string, preserving proximity. This allows us to use a regular B-tree index on the geohash strings for efficient proximity searches.  However, tree-based approaches like R-trees can offer more flexibility and accuracy by grouping nearby objects into overlapping rectangles, creating a hierarchy of bounding boxes."
By contrasting these two approaches, you demonstrate a deeper understanding of the trade-offs involved in geospatial indexing. ^AXkgQTP7

Inverted Index ^NRX8bmW7

**Remember: B-Tree is a sorted structure.**
Say you have these strings indexed:

```
apple
application
database
datastore
developer
```

A B-Tree stores them in **sorted alphabetical order** — exactly like a dictionary.

---

**Prefix search `data%` works because:**

You know where to *start* in the sorted order:
```
apple
application
database        ← start here
datastore       ← still matches
developer       ← stop, no longer starts with "data"
```

You jump to `data`, scan forward, stop when prefix no longer matches. **One clean range scan.**

---

**Middle search `%ase%` fails because:**

Where do you even *start* looking?

```
apple           ← might contain "ase"? check
application     ← might contain "ase"? check
database        ← contains "ase" ✅
datastore       ← might contain "ase"? check
developer       ← might contain "ase"? check
```

You have no starting point — you must scan **every single row**. The sorted order gives you **zero help**.

---

One line summary:

> B-Tree sorting only preserves what comes **at the beginning** of a string. A middle search has no "beginning" to anchor to. ^qiNaLAmr

Problem ^2EtLmkqH

- B-Tree cannot search through text like  ^nwP2mwg2

SELECT * FROM posts WHERE content LIKE '%database%'; ^Q82GaDzP

- posts that contain word database, even with B-tree we cannot use the index at all ? Why ^lmg2TnFS

How it is solved  ^QwqH9EAF

- Inverted index stores words with their documents instead of documents with words.
- Think of it like the index at the back of a textbook - rather than reading every page to find mentions of "ACID properties", you can look up "ACID" and find every page that discusses it.   ^VQkY4rRC

Overhead ^XVSgYPVc

There are still trade-offs, of course.Inverted indexes require substantial storage overhead and careful updating. When a document changes, you need to update entries for every term it contains. But for making text truly searchable, these are trade-offs we're willing to make. ^kvC2AP23

LSM Trees  ^s25uGtOf

**LSM Trees — Core Idea**

B-Trees update data *in place* — fine for balanced workloads, but random disk seeks become a bottleneck at 100k+ writes/second.

LSM Trees fix this by **never updating in place** — only appending.

---

**Write Path:**

```
Write → Memtable (RAM) → WAL (disk, sequential)
           ↓ (when full)
        SSTable (immutable, sorted, flushed sequentially)
           ↓ (background)
        Compaction (merge SSTables, remove duplicates)
```

Key insight: random disk writes get converted into large sequential writes, which are far more efficient.

---

**The Tradeoff — Reads suffer:**

A single point query must check the memtable, any immutable memtables waiting to flush, and then all SSTables on disk from newest to oldest.

Three mitigations:
- **Bloom Filters** — quickly tells you if a key is *definitely not* in an SSTable
- **Sparse Indexes** — skip SSTables whose key range doesn't match
- **Compaction** — fewer files to check over time

---

**When to use which:**

|                 | B-Tree | LSM Tree |
|-----------------|-----------|------------|
| Read heavy | ✅         | ❌         |
| Write heavy | ❌         | ✅         |
| Use case | User-facing apps | Metrics, logs, IoT |

---

**Real world:** Cassandra uses LSM-based storage to handle Netflix's billions of viewing events without slowing down playback. ^AaqGtBy8

Memtable (Memory Component): New writes go into an in-memory structure called a memtable, typically implemented as a sorted data structure like a red-black tree or skip list. This is extremely fast since it's all in RAM.

Write-Ahead Log (WAL): To ensure durability, every write is also appended to a write-ahead log on disk. This is a sequential append operation, which is much faster than random writes.

Flush to SSTable: Once the memtable reaches a certain size (often a few megabytes), it's frozen and flushed to disk as an immutable Sorted String Table (SSTable). This is a single sequential write operation that can write megabytes of data at once.

Compaction: Over time, you accumulate many SSTables on disk. A background process called compaction periodically merges these files, removing duplicates and deleted entries. This keeps the number of files manageable and maintains read performance. ^uzEGXk7M

LSM trees batch writes in memory and flush them sequentially to disk, making writes very fast. However, reads must check multiple locations (memtable, immutable memtables, and multiple SSTables), making them slower than B-tree reads. ^Pt1mcuxY

## Element Links
l2SvzJ0r: https://www.hellointerview.com/learn/system-design/core-concepts/db-indexing#:~:text=The%20Challenge%20with%20Location%20Data

## Embedded Files
cdff575bbdfea19c8d9062f4f3e3f1168d38507a: [[B-Trees.png]]

50e39d63a4631c09ce65df60501701e4985de40c: [[Screenshot 2026-03-05 at 12.10.39 PM.png]]

2016216c4327bb2c4017b05ff80f7e87c8bdafba: [[Screenshot 2026-03-10 at 11.15.32 AM.png]]

5418791f3656f8b718d067a7411c536c6324cfa2: [[Screenshot 2026-03-12 at 10.50.20 AM.png]]

f1475a1cdbc4b6f41c6c4b6341ae36360f053b32: [[Screenshot 2026-03-17 at 11.52.17 AM.png]]

c27900d43c7ace125fb6c98e9ad7b20b3152d581: [[Screenshot 2026-03-17 at 11.52.36 AM.png]]

%%
## Drawing
```compressed-json
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
```
%%