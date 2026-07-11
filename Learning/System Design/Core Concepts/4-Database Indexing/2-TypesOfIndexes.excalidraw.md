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