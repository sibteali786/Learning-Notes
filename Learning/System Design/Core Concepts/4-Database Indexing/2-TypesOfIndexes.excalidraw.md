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
- each bucket sores multiple key-location pairs.
- Wehn indexing a value db hases it to determine which bucket should store pointer to row data ( page ) ^xKghLEas

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

Geohash uses **Base32** (characters like `0-9, a-z`) not arbitrary numbers, but the *idea* you described is exactly right.

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

**Your intuition nailed the key property:**

> Two places sharing a long prefix = they're in the same geographic box = they're close to each other.

So instead of storing `(lat, lng)`, Geohash converts it to a **single string**. Now a regular B-Tree can index it! Nearby places sort *near each other* in the index. ^EkQVf1c4

How this helps us  ^A6HgOMhS

- Finding nearby locations in geohashes means they sahre similar prefixes
- Two restaurants on the same block might have geohashes that start with "9q8yyk", while a restaurant in a different neighborhood might start with "9q8yym".

- When we form B-Tree index on these strings and try searching them its only matter of matching prefixes only.
- We can aso run range queries ( range scan ) using the prefixes. 
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

## Element Links
l2SvzJ0r: https://www.hellointerview.com/learn/system-design/core-concepts/db-indexing#:~:text=The%20Challenge%20with%20Location%20Data

## Embedded Files
cdff575bbdfea19c8d9062f4f3e3f1168d38507a: [[B-Trees.png]]

50e39d63a4631c09ce65df60501701e4985de40c: [[Screenshot 2026-03-05 at 12.10.39 PM.png]]

2016216c4327bb2c4017b05ff80f7e87c8bdafba: [[Screenshot 2026-03-10 at 11.15.32 AM.png]]

5418791f3656f8b718d067a7411c536c6324cfa2: [[Screenshot 2026-03-12 at 10.50.20 AM.png]]

%%
## Drawing
```compressed-json
N4KAkARALgngDgUwgLgAQQQDwMYEMA2AlgCYBOuA7hADTgQBuCpAzoQPYB2KqATLZMzYBXUtiRoIACyhQ4zZAHoFAc0JRJQgEYA6bGwC2CgF7N6hbEcK4OCtptbErHALRY8RMpWdx8Q1TdIEfARcZgRmBShcZQUebQBGAE5tHho6IIR9BA4oZm4AbXAwUDBSiBJuCBgARwA1TU0ggDE00shYREqoLChWssxuRIA2bQAWAA4hgGYABhnRqamAViXR

0aX+MphuZx5xme0hgHYjnmWj4aWeeY2iyAoSdW5ZuMSZqbeZ+NGhibXNyCSBCEZTSbjrAEQazKYLcGaQ5hQUhsADWCAAwmx8GxSJUAMTxBCEwl9SCaXDYFHKZFCDjETHY3ESJHWZhwXCBHKkiAAM0I+HwAGVYLCJIIPNzEci0QB1R6Sbh8O4QKWohDCmCi9DiiqQmmgjjhPJoeKQtjs7BqbYmuaQ6nCOAASWIxtQ+QAupCeeQss7uBwhALIYQ6Vh

KrgZtyaXTDcxXQGg8qwghiOD5utxkcZrc2gwmKxONwholIYwWOwOAA5ThibhJY6rIbxZvB5gAEQy3VTaB5BDCkM0wjpAFFglkcq6PZChHBiLgu3WTjxi6N4ksjqNbcqiBwUf7A/hIdjKSnuL38P3ld1ML0JAAVeDhVBsHmoEPELDhKOUO89SoPxBmGfV930/PIvU4KBBUIIxxFQKYhggnImlwfR+WtVAczKa8oAAQSIZQuAkYIeV6UsmCgcwCHwk

EiPQKBzW5PQclwEMmD9NAE0PZUcRBEMCF/G9/0fICXzfUNMC/SFcCEBiACVwhguCkSEBAjzYgAJYFQVvVB4hSLDAVCQSoAAGRDPcez7BAigAX02EoygqCQAGkAAUAA0hCaIZiBc7kOjg6A/0hAY0GcYsDmWJJsyWGZlyWcYlVzDDnBObQlimHhEjWeJl1mOKjkhB5iCeNAeDXDKjiSb5jj2JY10Q5UgRBME0GWaSOBhOD4STJE1QZHF8WJIkkAHC

kqWjeksSG5lyA4NkOWyMjlT5AUNS1FUsV1PrpQQOVSoVcqEX6tENqCnVUz1YQDSNOszQtK06y3XN7RnZ1JzuSA5OqSs20wegACkAHEhgQKAAH0XDvABVOTmBc/AeQgO5PVWn0EA41AuODCTw3iKMh2IWN4wPBEEFPNBRmq8ZEiWIYhkMvNy0LE1GfIlmqxrODrnGeIhh4I4sqK5VCHbTtKdQc9L1zQdaWIUdMmWyc0dzGc5wXE0l2Lenl0io82BP

bspesyEcMqAAhZw70CBBUEdCSpOVcgKBMy3rdt+3HfA1bIOg2DFXGJCoBQtD8AwpmcJowjKhIlbczLSj3GjujoEYyFmKiNjSCxnGeNIPiOAEv8JCtm2Ka9j9JJ93MZPkxSA7QFS1O3TTtLavSDMhSRjJ6czdzPU3W4HziDzshzReNiB6mUTQAHk3LnvczcfLoQuVMLUAiyZDnGTLxkWGYjnp4/IVSirDlGPY1kSJK4p4BrivlIs5hSaqELOeYhkz

JmWp057eq1y6lqQBZRVRokGkydABJRoknGpSN6dJIFdHmotTk8cyhrSFCKC620rq7TVAdMqvATp7XOpUS6hM/CSBJvdHij1YAALtDSJ0LoChfQgD9P6AMQZg0htDOGCMkYozaKrTBGNc5k1FnjCQuBUjXXlrQ0eiZczJmNlMeIx9MwMyZmWAsdEpijBLMqPRFZqwcFrGzamD9xjjGpq2DswRNYmwvC3WWRNFbjlyAUMRkB1bzklpo04OsBYMzeAb

I2g9XFmxLugZwqB9BsERKgPQ+hEkcFQIFYCqANa4HJGEcSVcAA6LhUAIB5HyS0y1w7PlIMoawSkgK5KljiE2ySwgcmwJIVA1hiCoH8d0Zg2gSnxM0DABJrEWIhhDMoVA5J8DWDEH0pEFcpRCGwFAEQdt1DzgSdMtCsEgIBn0I0Ug2THDMBRKgQIuAXTDNKYKIIr55mLJmZknuUAJkhizgtVAghSBdhyfOXAIyekCjYBQICPJWnlMqYQZa4kwgAor

MwagOTOwop6XSP5IRRBAhrmUF2bsJDxMSck1J6TMmPnOcC/JdtQKYFBbC8w8Kcg1JxPUjgjSgVRBaWc3s7TcVdKxX0gZ4R7mjPGfoSZPy3kvIsSmTJns1kbK2e83ZaEuUHKfMc055yxZXJuXc0FjykZzIIK8rq6rPnSu+ZMoC/zAW5NBQQbEkK+VlIqSyhFIYkWUU4Ki9FTjMW9JxZ0/F3JoU5H9nBfmwdQ7oW4JHHoKdY7lIwZAROVF8CpuZOnZ

UmdJnsWNnnXMvF/DFyEiShJSTPkUs4FSxANKoh0sKVgJlXqqlsvGRyhphyeW4A9QKz5HS8Uiv6bOAJQzQVjK+VMrlVr5VLKVaslSqrAjWr2Vq7luqmD6sudckIxqHlPPNQsixbydk2plfav5OInXApdeC910KznMq7Z831FEUVoo/MGgN47R1dKdrXWSbAFKsEbkq1S6lDRaVarpfSD9u69xvP3SyLiZZlB3Bhri48iiOUgM5dAFBcIaWYDwGAHA

ZQBVXsydeuZN7b30kMeY8RbG/H5klYxKU6waO0F8bMiRb6JGynlSYT9DqKniAcamt8FjxA+L8Oxoxu7t10sh5U0IQGkIGjNKBEACSJGqtgeRypyQIKmsguarJ2ToMjfybBmpcESl07KZ+x0CFnRwRQvBVDbpxjoWWhhGEZOgMgG9Vhn02jfV+v9IGoNwZQ2toIxGyNUZegkSWqRuYGXhimFQmMd1lHcVURTY2/M1zCfyjxsopjWa8HihzfR5jLGo

F+KcCYeURa5fFk4yW0s3FlDliOMcysfHTknc4oJy46ahP1tuQ2aJjaDZiVW9AwpSDrM2RusSZdbYEsgES2JEBNvbbVXtj2FNDu8j9kpRU4XbvIVQomtAyaby5vQHHbkWbk4EVTgxOATFIJFpztllRZRy38XwMSjba6dt20u+XEDZQ67gYbspLbQ3IA7gQPB/+Jou7NVQ2ZCyUSsM47JyV/DpRCPlCngs5QHlsDYCEOMWjnR6NCVCjsb+4xL5GL5v

FHKMxaZnzrPsMY6x1x2OPmcUTqnlQlWITTDKgtDFTFPs1dTaZOrdThG5jE+nhqwLGuZiaiDpqMhQbZpaXIvSOfIWKPzhuiFHRIV59UPnneuedjdGhxW9IPQpE9G0j3IsfXYTFzhcWeGJf4Sl+GaWRGlF8byLL+4IdEZkegXAoxCvE0D6WsB5XFRXwuAfDqJj8wVnBEcIO1fOatZ5tTX4ax7Giz6+DAbQ93Hy08eNtAU5lRioq9rObetwmLciVZaJ

V4TvxOHBSbpHA2AfhSdYVAPdGAJMDJRHwdsun8j6avj8QFaREDRHM/ipBxkrIQKCpfwrT+H5B762pH5Ah9I5OQHtr40QwBAShpwBsDfL5hooqoI7LJsBbqEDao5IGqHq3JDLfiuwL6oBP4r5r6H6b7b52z6B76EAH4pKSDH7YzYHn4cCX52yaA35362yP7L7kHr6Frv44if6Ko/64B/6oAAFAHYogFgEsAQHw5bLQGwHwEXKGpHooHBwxp1hNS5h

RohwvbhxJprZ4T/ZpqkQ/bfp/a0RdD5q5isGGhg6Z6laQ4FwVow7oGYHME4EZJ4G774D77BAkFkEv6UHUHX5Fy34roP6lJ2Ev4pJv6/LsFMCcGkC/7ZJ8HjqCE5DgF/KiFf6ZIwGapwFKQIEHpGqyFaZgYQb3ZNxY6wZ4466E6aa5g9zMAmTobk7Y4QA4bmE07FCTyVDEAwxQB3iSAzAyjDgc5BTmw87hTfxTCHBXDLDDBrjNg5Ti7lRrBVS0xXw

MwvB0wN65jK7u4MyvDfzLiaLsZa6VFlF6Svw8B7DFhzZxQ5RJB646ae7WbQIjRwLm6WZEz3HQCoJ2bLQObrTe7agu6e5u6KiG5O5/G+65j6gB6BYmjB6WiMJh7MIOiR5D4cJcLxa8JJYCJJ7CIZboyoSYzg4WHZ5VzhhLAF5KLYw5Yl6Sw8ATCnGNQ9Z1Y14NYVSmiN4tbcx1iNiLDDAd69aOLd4ra97DYeJjYTgTYj5TaBLj66xhKPbHjLZ1EaG

VBBHYHiSoBWz34tLPoOpIjmCfJbbBDTqlL4T4CoDBC4CvieG77JKNA9KfLqB2zMB4nopwDqCMHP6ql4AZImFzLgwUAUwZKGA8Djr6C8EICAGoAAAUFAQIG6oZYs7yiOpAn+2SDp/hAAlKCrhPYagA8OoLwWGRGQQckk4VgBSFADUiiAANTxDuH4BkDZCgouThlAR5mkEZKDrBFLRhmulqmOqKrhG4h6g/gnYqnr4hjqnOCanQralJEFwbLXKBjip

ZkChmkhCWkUHWmfK2m7JplOlZAulumBFMHBFekhHzq+lQD+nZAJKxAhmFlATRmxn4FvhARpmDmplAgZlZk5ltkFmxHFmfKlmYDlmVk1l1kNkcBNktm5lqDtk9I5ndloi9kTn9l9KDmRp3ZQb8wCYIRLCJBJCzCriFTxqqERwaGfYNHpq6HIr6Exx5pA4ZyhHFrmFmhWHQ6w4QBjn0oZIamewzluo6nzn6lLlGnxImlrkWn2FASAW+l2mJl/LOkfi

umSDulYEsGb4+mNBXkBm3nBmhqhmxFPkREJKvkKUfliRpn36ZnGm/lwX/kwWyXAWgXjLVm1lH71mcjQURltkTmdmqlIUIAoUZJoUf5MDcho4FFQbNwlH44dxIa/wk61Gz4U4NFU4UkCjNF07EYQCVjuQ/AABaMAgo/Ra83OG8vOfM2gH8eUxYHwHw7Gsx8EpwKQ0wV8Zwe8Qu7wkmxC6wBw1UwwjMVwQsCwBxZQf8HcFRqOwCPUhubxMCI03IFmk

0rxxuNmC0nx9uq0juvxW0YJYCp0+0HmHuqih1IJe1O04J/u5JrJwWIecJxx4eLCSJboKJseCWfCyWsMWJ6WoimWeJkiWe5QOeUIQwZJRelJAgpeJo7GxFDUVeCcTJdE/MyUjJTeHJJoGi/MKw+UDiEsgpc+feo2SsYpQ+aeo+i4wSE+spESCpKV9R5sEgMokg4y+212PSG6H4vYe+qA6IkgoBYgap0qHA4yeAYQN2x262EAzNrNV2T43ZXNMkLhv

N/N5gPFEyItG+4tmF0ahRjWpFYc5F8+H2WhxE1FHMSc1Ept9ERhZQJhLFJWbFhclauk0tLNk5yOQBnN5SStnyfNAt6twtotoQKOkAkVGO3AMVw8pRCGdYROlRSV6Vq2w8uGY8pQ9kBGrREgcAmA+gw4hAKIHAckpVXOGaEATGxwRwYwiwewpx2Yy4tiTV5e2gQs+xfM+wbwfMPV7uQsIw3whiJwfM7GSUih41RxeUj22ms1dxa1DxpuS1FuVms97

xtu9mDuPxzmvm+1Agh1gJnmp1ZCu1lCCiAWrot1kOIWTCyoEebCyJ0eqJcen1mJQiv1qe/1voBJuMxJsiRw4NUJGVhJKo0N8ExYKmxFzWteWsDJmaSNzeChFw64iwY1RGXeziydRNCsop3iZNk2GsUpVNMpC2uY8pPehN2E6BXR4Zc6Pyd6AKA5yZTAaK0qKIby80ygds1QqkBc8t2Kc8ckbYw4ck6pAAms+IgOQP6r8u+qylAKCpQzAAAOQbphB

IzOBLozJorZDMAiBvJwBf56l5JuHiOvrC2C0ICMAdlNLAqoD2iQpyNAhSr7KZFSH2wKBzxzJSrzhH5WoOmEBnKQFqoMRb4QoDp0o6k4h2zOqlLyNb69JuGDj5kICcMEBWhhp4pPiRmZCsSmkAC8qACjmACj6Z46bDjpQq+KUZ0QdsAAfLwEsMU0k0IK6uMv6QKPY1Q4ELahkkuoquYzeX+fNMQAYIihRPwX0n+t3oGrgPQKAY4D41+cYziKY4fkQ

BUswCUjAMIHsjpDinbH+awPoAfmcpqQE4EBLSOVLfEjE10zQ6FYOUw7gCw1aqU6gJw0wPCmM6gHwwI0IxbKI+aEwPOJitI8tO04o8o08moxahel1JowtDo1anoymAY5oEY0wCY4snbH05YwOjY8iHY9Ew4xIc44gY6G4x4xMlAN47Mr4/48kdsjAfzRQKEyHeE5zY+oS1Qz3HSPE2wIk8k0QLAGk8Bo+Vk/yKgHkwU0UyU9CGU+Ghk1U6gLUw/A0

wKzUq0/gGC4el02epi30ti7BfmYM8M1+gCp8xM4MmitM7M5egs+i0s5iykqszyEBJs0INs9ILs4a90gc0c/4XOedmczrVBHrXGr7M9obeocbZoQYWbToRbdmpRYDsDvOg7QA07dYZxVc0Szc5MrQ4CvcxMk87Mi8289w58984IyI2I4C5I0BCCzkGC0o2U6o+o7C2UvCwXIi/oxsoY3bIs6QMs2UhYz0lY7yrY+s5y449urBFkVcmS+47OtKlS+2

TSy1HS1tuugy8E8y7kmE0kREwOlq9y8QLy/y004K+MkBhU5k7ark/k4U8U6Gi89ewq+w0q3U6qxe+q0EJq1O9q3mz0/qyOwM70iawtKM+Oha+EFazMyQLa/2/a4O469gM6661s2hDs8mN638nAX6yc/SzduHZBnBOg9hm3LHeUYldUX3EnUKZTiPAA1lVnegAAFYUA8BsBuRyS1DAwl3oCBC9szXchMbVRV0rC0yZQbhrD17n2QCpTNj6R7xXAVQ

fAK7HxycQAbHcD7CjHZRHxqdJRGL4VqaUd6QPxLACagPCbsai5Lg3HT0H16bW4SALWjQL0vHyxvEsgbV25l1YLnXH0AnHWo072H2b0+6XWErXWB6afmj3WhYvRlA33Ra5gP0fUYmJ4v0p5gBp7egA2f3SLf257s4KJFb/2EbtB0bwR3AZ1laBJGLfArCGK6JI11jCYQOcBwMmj4VCz0wyd439YE2pUjaYMk3YNujk2Slj4EPzZT7EPpXF445LakO

pVVE1F0euLMe5ZTwACyMMKI+gXRHAHk/HGAAoRBYQInOweF2gfMg1dJhi2UTM58r87G+Fm4+wNJ2s3dSayQiQhi1MUwdixYRwxwiuhxZnvwDnBuM9Ln0CPAPIiQCAawHnK1Xny9eImgiPPADQ3xTmm02AyIcYzgHyXSkou9IXwJR9/xV11CN1MJoej1CJ70t9r199716JCe312XOJShGejtRXYYsiiQf9rolX0A1XPAtX5MksjMrGt8KwnXdELJy

v3XqA9ewsZwmnYs/JaD9HEAo3A+pN7PbQlXVXnO9EDG0eOV+Ego4wu3KIbYu3OXYAtkfPZQFNUDs2hD835HjHS3DRK3w39R63tHjHg223TkU8dvDvTvLvK8lvwU5VjGN3V8Am1wGYEnimKwEPWwOw73d3im5w+w6Y38v3MN2gdM+FAPjMZwo1v8RxCN01+uaAj24CRu8PhmiPyPqP8C6PSCy9PnaCXx69BPLmUXYXhCVPnugXtP0X9PsXjPD1YWL

PUWUeaXnP8eX1qW2Jf1uJH9rFQvm8UIuEYvR/9XFWSQjXpwa4yv3AFwavGNmEswHw8wdMg3Apip5mIp43KsuDASGbj7zm5ylg+3/XMIzXQAExhyaBKWtAPDYhsoMewA2q9kwgUVraEAMQAkSHKN5LaOaDAWhGICnszcxhZimYQkD7dDux3U7hmw4onZ4BoGeuCR0jrFFo6cVRDPHXGqJ0I+BvRotTnToTwdulQdEAvGd6kAKA+gM7oMQqrDEWqV8

VcGuE3CrB4oUwJqk2AOB8wzi9eb+IlGqgV94IzYBIL10+Bv8BYjfMzlNTDrCc2+c1THo8RIHDZF6q1Lvljxx548x+51InkkmYCk8vGCoV3DPyc7eYIuoJSfhAAhIM96ECXK+q9Geps9CgHPbhBl25679X6uXd+viQv5OQQauAC2Of0F6X8k0MwAHj8Erz392oaxNGuyQVR1g8o+FZsO8FqwoM9eq3eokbywb/8JSeDIASEknygCZ8mGBmqORAqHM

3CQTeWPmCiDYo2aodcIRc1drDgRhxBcYaGBYBTC+kMwm7MoXkLlRHsyhBNGoTezoDY2X2c2rgMTYYDk2TFVNuQPTb5xnaNhKWosNQjLCYCEwtYaGk2ERV8iEdIojBjYHj1OBRkGjmhk26pU+BTHAQZnSEESBqgs8AqtIG8hnc4CVTa7sMWOAJAKotMIWJMBpKPxlQGEeXgkA3DCYG+qwE4PoLiiPYJqGmTcC3SFhnEfgG4SYAfBh42C4es0eiB8T

85o9Lc3nbkWvW2ob1NoPcLpFsgp57Q96QeWfjT23rhCYu/9OLpfXhJ+5FEENIGmoh050xVw5QjXo9nqxcwahJoQWCcBih6CuhgAymsAL6Gf99eZDCLHENS5lB0uXPHfj9Ry5p52hf/cUgtwD6Q0g+AwsjpAHy6H8ChXAkEaTh4H2jeQ/ITIRIGwDEAKk64JYA0ETEhAkg2AcYMQDeACweQowHkFMAQBTAeQzYb+MQGB6FRcAkodwHBASFtA5OYAe

IB70gBeCgcYYoksL1zzogKe84IQK6AgCIA6QMyFPHVxaIwj0AxAGAJoCMDKBxgrHUrleGq7J8y6FdJsHd2U4yZQk6wPKE1VEzJBNEq4RmJ1mOA7ilcx1ckXdxzHrAVwXwUeoCHHqsY2RqAdvodXmr2DeRS9Fwdjx5C49NA+PTwcTx8Fk9/BwXKTPvQOrhdNoQXOnqfSCwX1ohKo2IYiXiFvUkhro5+snmbHp4CuWQjsSf1wBth8hdwwoSaEzBnB1

wgsJoczH0RJoGYT/I0ZhBEynE+YTMXXvjXAHCl+8HQn0Z72m5WjehNNafHTUGFKlq0pkcGA6m4K5kOGXDcZK6hCK+B9AGSMSDDCRStl7KirPJg1FBQyg9mjmKWH42SQ8hwYwqZEHy1QDsh323yNIpkBxAwATUIYQWppMwi1kYy5gbpAmW0rXkMkcUcdG8GklSwTJ3SKYMmXsIOSFUPSd9lpNrKCBUAbkRVlMFzLCB6yclYySu0VTWSEktk2/CUlB

QOwtaiOV8Iq1qbaTSk/pQKSu2uRsBzJVpUNA6Q7KrlapAhKplCmRChlfJQTcJCUnqkVThUIQYVJZO2T4o7YVpeIp+kDLZTtgMArNqgHEm5BFKLTGSUwDkmrk9Aik5Sa+FUn5gcOzk0qfEl0mwVVyfINYb1O6RmTPkg08SEEyyCJIcpDyRyXbF2muTSCwqTyX6V0q+TQ0/k8qWlOFQhST82BcKU5KikuS70cUhKUlMDB9JbSv0oEH0kyk3S7JuU0p

PlLFqFTIpNTFyaCh+lBSqpNUzcnVKBANTTSTUvpINNanDMOpMBcJImQySwyykTBS6Q6QKSjTQCOQIWpNODY7C9Id4p7CoUjZHDo2lFb7AmzooA5baLYsgYDUAZQ4i4jw12vEjmmSTFprzWSWClNJrShASk7JFtJYA7SQZe01AAdIeBHTDJnyemedIsmKsEZk0oGY9INnPT3JZlLyR9JmB+S3ZOMyqf9LCn3SIpT0sGfFPfaJSKAyU6GXbFhkZScg

Nk26fZKgoozvSIdbJMVKxllTw5uMy2aTNpnqzpKcRFqVLDamYQ3ZnU+EFnPpn9TukTM4aTnLGkcyY53wpgXrSDFpU4MgIywVIG4EYYm5EIvDFCNpwscIA8QAiQgCXyAwuAifAYtb0gCbxNwowQ4MDw3CrANEYPLKC9x2DpR68241YD8AQgaJQuWnY6muG2IfBa6pxeXm3JpHPAmYU9WHkEM76cjDM74/vnyMx7fjfx/43al4JJ7ASJR0/MCSdQgl

qg5+coiIUvyiGwlEuT1ZCU6MgCmREghdUyDOGBhTAPIbYGAMOGBiYBhGbkHkJoFICscPRGQ6WV/U7FQg+iZXQvP/UD6aiTQomTMFjQ65slIGxxaBtRLMTP9+YTYRmBrltGtCBwv/LxJ0LVh8TveISUoZuFpq8Lo2lQDSKEG6QOxiS00k7DIuYByK8YchPWsgIQEHCjaEAlNBgJFnnCxZhhRigWilmFcy07FOWZxWUWqKFFeRBudFVYG+iY6BOTuO

fI7kcSGOqdTKr3LHHR8ugLkGUB5DkhGB0QygZEdKnYZojeANJDKB3VboPxNEi8pqrsH0jkjNc38L4FlDxEsLtOb2JLveLM5LyBMDUS4mDzeBXE8+Vg1vs+NsFd9h+m1MustWfn1KBRo/IUeP0qCiiNAgQH+e5j/macO+QCsISAsVHL8IF5C8klQuAbKCweuoxTJpwNHq9VOXWZYlRK956RpSvwb+OIs7wtCQ+a/F6nWLKCwL4FiC5BagvQWYLsFu

C/BVhK9ECKeJXi3CQGOElNyQxcY4ieGI25RjUqa0T5RADihFjEgxAaYHnmmDxBsAxQsQIzETGsY4omiL4Cj0V4fhNw2AasQQFrFfQGxTY/fsYWRBtivleE8MC0BOi9j+xg4uZuEqj5EYp4MoHgAVWBjqgjgxdceWVRXGKhTiYxP4J8BB4MLeM7UZYMSIB5rhbEV8O/meL/nLBLOz3RmFfGGA/xTOri3ZUAhqUvi9ob4+ek/M/H3zXBP49wR0oAne

DfBK7PpUdT/l7yhlsokZQqLPrjKYhyXR0RvxOVwKOACCuAEgpQVoKMFWCnBXgoIUH9PlgfPLLIj46TL1RgDahTzOMyrBjMgseZeuHoltY1goSDRPyqcioNJFGDY3hN2HxCLuh/EubGIv6FvKDekAiAIvhwBBB5KZZBcmW08YrsJUqAaCKMLkkWSa8iIBFFUW6TSo4Ab4UYeNyBaFhFFlzDAlWtNK7Ja1nyetZSy6RNqW1PgNteI1YCdr2Z3aiZH2

rw5YMh1Y8hAdzLDZKFII2iqNropNonCqK8bQxVbXPVXDTFNwohfcMza2Fx1NakCnWrVnLs51Dk1tQhWXVixuga62RRuv7UH4vEO6+uejmYF/D6iuOdgXHXcURjkqIklOk0V8XZUp4HkQJfzXRBGB6AUgyeeXWkxV1d5swW8VmA/i8yMIq4WeTnzmDvAFgiUbKKoMlXEJ+YyQIWLfG/j8xNwZgpVZNSvnWDalHIgzG5yeKywnBGPL8W4L/EeCP5gE

k1eTwCEWrqeIQi6vghgmQk7VYCpnqv2vpOq76uYU5W6vOVeqrlvq25QGv544T2xwNYrlCA0hETplgSI+OsC6wmdGFDWGTIstgbsKgk7wdcC2D2XsT6afCrid6JwYWjpsWy4tRIoOVSKJAGkEJgyifAhzSAy8Z2PMOkVJbvYSUtLVzI0V7Cj1ZFE9eQzPX0VThl6xGrRWvXla04Ji0gfevMWWEHh1i7LVXBS04h0tjAyDXrSjrOK4NVHFDIhrBEwb

FuadN3oIP8USBMALkUEKZCXw3ZAo7K6JRVFeD1CCKkwI+GuEShN01xwsUXB9yMTZhclx1X4KMR2LHwGYtibGuYNcW6bVVtxW+ZqsWrarnBuq1+QaqUI7VVNn8oCX4LNVSjLVZ1a1epoX6wToS2mlfgUogApdnVMC11e6s9WXKfVNy/1VhI+UPrcsOQx0I5v9FRqkgwmL4KJmmC6jEorXdGgxMUxg9qYm4R/kFqG6eLDe/CwfJNwAFRbZuMWoSVmt

K2u1cIdaQ9uuuS1e07YrHPsZ8hsXAbktfSegAQFUhvkYC+LM0obB3WPkrZ7DICDZXiRthaUic3Nu/i4I8FNA6yNELkCbXly5kxu8GLQyfAEEXCRBNwgAWcDHgd1VswyU2t0k0I20mAN5IOhl2+BImmgWJuLTfD2kYCH4boIOzYi5kXp3SI3SeBHT80oZB7QICUjGl7ogmiu5pJGTV12x0yqBTinzpCIbpBdOW7sqLuSQS7e1XuxVH7rl2pEqpzLZ

3XWyjI56NdqAUFNrpbS66b0+uqIlJLEhx6TdYlBmcKkH1W7/kNuwgsQUd1N6KwrulgO7oQCe6GUPu1ALXoD1B6nwageveHqYCao9mMei3fHr+SJ6UpiIQ9mnuOYK6QmWenPagDz3qLsKvM/YcVsFmnqY2tWgxVVrwFJsJZmAsxS8tlku1KghevQMXqA1C6OaIusXagEr24BN1jsaXbLqfAZ6Qms+gDNnvJn3729pSTvXkm712pe90RAfZbtN1Mom

CY+kdBExkpT6Hd4ZJ3crskbz7h9HujJCvqtS+7kDOSQPVUS32h70UEe/fdHqdmUGT9oc5Pf2zZkR769me6xpgcVYP77FPWqDF3Io53agR7c4bb8tG1+ifFE26EVNvQDKAQ4KIUyIvBoGLik+0g1PuVCSDVVNwG2k4MdtZEEi/ulnRBlmGPit5FgvMvJagB+AjA1OywF4CNU1y3aO4Kqlvo9oAUQI7BWq54gPytzvbpN78n7fJu/lKbiEQOyCRP1B

1HZbVcEyAPF3AUOqHRUCuHRACM2I6Ll3q65X6ruV4rxE1molbZpIW4BAYuOjUcAySDKdS+XdDzcjVFxJq4IBFb4KuAIpUS2JDOkLT/zC2PKIt+ay0SIqLU7KS13O9oCdkoPMB8g3ayMkUihBEAxAAAATLIDrdABgfY+mXdBbxam+QV0lfrv3xB3QJSLYzsdkV7GmdmgE40sOCDnH9Alx646gBuNuh7j9ey6TwHdD57NjpB7Y7sf2MpNjjpxg/H8Y

BPAm7jSIME4qyeMvGYTbxlRR8cHBfGkTvx1JKiaBPOBbjoJoJuCchOP7Y0z+orQLNQCVCNjZW1OF/rRo/7Lhf++2rcMD5AH5ZlQV43CYONq1vjLwkkxcYgBXG0TVJmApdOxMcBhT7x/Y4SfFNnHST0pwE7KYxPUnFWEJiDVFUxz/D+trc6jj8s7m8Cxteh0cehsqAcBJAfDO8JgCWAOa2VpdFbVyuKG6DOF+UK4GoOqhjBJi+8TQUfD3l+H8KcQS

TimpOChGWTUgI4o+K0yCb1VznXVY/ISMtLkj+qmTYark3GqMjoErIypqgnz98ji/MZZDomV6byjBml1Wco9U1GzNqOho2/UDWY7shdm3AP5HDWUK8dwDc4FcGLCBaqtNE9qNDqWXP9lg8uUIzwri3ZruJCx3iQWuWP9dVjsWxneWviQS61pRAfRMLtiY8tFUs6V1BCjeS27XCWLHIOW3bVnJKDTarogmVOb4FHmT4Eve1qAiOT9GqLcZMOg9RTrn

A0qYVGWw+ZNqLYskfpCozjAepS2XDD5oBnvTDiR1Cs2A0Bt3NiwQ04Bo89DJWlupzztBq87qSfDiMj9Juh86QSEqBsXzaIICO+bAjiQieyLH820nNkwo31UAQC0wRAvLlSk4Fz5H2KCDQXX01yWVqrPeY8M+kjqJC3utDYMmI2qA97B/vZNnDv9Fwm9TyYAM2aBTM0nc1iD3OYW7YJ7YIDhfVlnmrUF5+3YRZvMkX7z9jJ8/SyLZvmIDOWr80xZq

R/nhLAFoC90m4vD6+LkFwS1ClaSwXxLnzKS11ENO/DoMOhlxfFQ0Nh9QR2h2DN4vwA0r6clQb4PEBgA8BWOowCwxAKXHWH+gnK/nDMAZg0wsoAsIilUqqAP8LgYwSTnvCEzHAxcLG93KcSrrCZb4WUNcDXW6ra4LBAmtVXUvTPGZIVZmcTZ50H5SaczqRwnukf+2ZH2rJZ3I/5k02FGIAxRnTdDth11n4dDZpHbUfM1o7GjwYgXi0ZDW55TInRyN

cAyuJZQFBzG0c0wtEzDGHs+wb+KJglV8lgtyGhc+FtZ2Rb8GwAzncQzAEzH39wgnuNMitR/k54ZYHkG6nQDIWobkyN5HDYRtI38tSAwrfJcOFoChZ+ilS5ybUu1bb1DWn5Gm35OWLgDEgPmmjdhv2V4b6LLG9JB+FQborsVM00NotOM7u54220/3KECOgYA/DQGJIBx3umreKfYq+VGyhGDih9eZedmGzBNUR6VfBqDJk1xnF2MmnPwwLH5yZRv4

jMYoQsHeDxmL5cxSeimZGsiaMzk1xI/NQ+25mvtwooKL9oU0gTb5gOla1vRtUVmtNd1Eo4hMdW1nTe9Z4zY2dM0o76jlmpo6GIus5CE+qo8rqTC6OBJeupGxYLqNOLk7qhbWTRD1fKUEU5zjOh5SzrzXLmljmyjneua53zmedqNmG7MiyCsho9N5Cy9Ppgrnp4ZGSPcs6XXWUG0UaZSgyUnP1nNnwhoO/WJGWg3nQ0OGeXWUhvDkBnwmNkJlgaCb

80UpaZM5lAGoBj2YC6F/c1AZ7LjSEKKi+9GaQsiKoukkye5CUkxAWJAg3QJexKYQDaBm1M4EAgUnKlOFRgpFiSeOlEP6V8ARqK9gxDOYlIET79o2TxT9RgosA46Ee6Qbv0JkeQZMAObWmpDqgAAiqZB6RED+CJSNgGveZaXT57FkT8/weAdoofAIeDg8EEwCJlAgH90yAEjOSoQVpggEpN2pQMwFgH46ZQGwCfCQQYCV6VeyzfXtVMP7d4BXUegQ

dMPf7si7qfw5Qd8AkCyyL8qIcGnD2iZWpJG2mRwz173ypDnPVA+xTMAzyg6Yycy1nvwWgmfIbFJiswAf3hGWzM8iiP8CPSvk+AQcEw/EfsN5pg6VDkQWIfdM2AijvR9vqwTn44AMjr8ngCiLwozkwGSkG+S/I6s/HBktYbo5vJpkQnfazgC8YidPgrCnrQ0DeHr1qBtAUJqWvTebtZS27MZDuwRYfJmlQ0E5fuweUHukHcnADkdBA5EdT3LpM968

/BYoe7hF7PQFeyQ8kdkO85m9rEJo7ti72ICh9vSxhYAyBVgq59/mgCivu7gb70NjgPfY4CP3GLL94kzA8FBf2kkezQy9Mztj/2tjQDtR2CjAcSGgChxmBwdNNafJnHSDrRyg8uloOMHsUtyFg8CCCg8HBDl0FigkekBEbUj99hM5RBUP69NDiyQsktAMPEHDpFh7NPYc9J9AXDxlrIr4f9PeAgj4R6JCjmbpZniLpG4NJkdyPbkCjgKeuqCaYujU

ClbR1U1yd0y9LITQxxZGMdfkGXSL+Zyi4sdWPAptjsZxS8cff5GHrj9x5vk8dR7B0d7LJwE8AfBOiAhT8J5E5vLRPHMsT+JzgSSd7pUnaLhSpk4ifZPEQArhSgU8ntzISnQEMp58gqf8Hqn2N+kygPxuKXhZxNmBtVvwHqX6tdtTSy0e0snZ6nC6FuyEF+TNPAyrT2Ij3bVJdOHnKi/p309EPj2hn/bRVqM6IufMF79e6Z4OgldMuFnjLJZwpVWd

gyj7Bl0+2qUHQX39nOGI53feRnnPn7WLH49c9uc/2HnO+Z5zCdefH6QHHzwt187Vof3fnEHfZwC8Jk0FgX1sqFGC5gIQvEQ2D6F/g9uRwvN8Nb5F49OxQVvt9XLtR7Q+xc+7GHzDmB2w+kOcOwUsU3h4vYEehohHQzoJuI9PdSuYHsjjR+y6Ue5vr307tFDy+QfH6dHpcoV8yxFe7gxXiOUx+Q5leb5rHCAeV2W/r1KuFHqr91h48iWaufHOrj5D

Yz1dOsiCbrrJ6m5D0GSBQ5r1AJQw3xWuUnQINJ3a8A4OvjpTrrOfk4Ne0ePX1yBDNjB6BVOoANTtmw4tI5WmW5ZnBKjzfD6Wnox/Nm05NtpWVB9AwwJoDyBwAwwzugnKYfriGK8A8o6494E2G+A5RhgmuJqmD3cO2d6o5wGkr4dO2JQW6dMLbcZmMwca+NukDRLPNYw0kKo0wRKCvJYXXz2RT2uwWNdMwfi3tBmBpTyNk1pGCzi1os8tZlGqboJY

O9axDqDvbXIFrPaBZUYR0mbkddRizejvOvBqchlYIiRLyW3tQZeSYGZVcGGBiZvNnMWoVRMnMMTxj6wCqKxMzUN2yQzOk3pXb8TCKa7INuu76JSsbmIb3ylT3UTSs5V0QAjDyLgHiDDhd1BVqwwRs3h10W60wQxDlE+v0xVbrhmGpVEuANQOMWUOhfoO42HAejQsL+IqoGuuK250XoTbF5cH23HBU1pI8l7aVbVXbnS+MQtdNVLWgSOX0s8AoKOF

f4Jwd5njWdK8VGqjlXo6y2bjtnXmj9Xrs3PBuuy8KscwdYFlH69tc0Ae8N62gE++a4zbT1jNfsrLuTfc1U3Fc3N9EULfsM4Nv643YkAKQCARsnEClL7GoiUbIvkIKaRlAS/RUTpKJXSYeyBudFPOkN5VpJtGKGKKbSm3yf9Fxupaov+X4r8gvS+lDRplgSaf96xWOBCG3myt+eX8D9Dfc8cRACOC4RTIuENgC5CEC/0pby4z07PIs6XatbB8L4Kv

JhrFg7ukZ5sBpyuD+m2rRYFquxjC+PeAediPeZbfazW3hrwmk3C9szM6rwfq9dpVD6NVfzMv3twITEa9y5eyz8ogOxta2tQ6Sv6/Pa+V4OtNmY7NX069hITvE+2jbkMn+18CSaJb4fXY4LqJa4M/mTn397u5p+vTGhfE3uYxXe5/V2ZsfPuxGsfG/B+JAW0smRyCTiBgOQ7l1pCGEAuTSWWwe7wqCgUgXI0U2+gS7RaA0tpDSo7CyQXGlR+Fmkz5

h6iO66+krqogM4A6gPS6siUjNIRAIwCfmE0jHJAmtTq7TH+VsrRTn+pAJf5nI1/ojL/+Ouvf4F0dsI/7IsgaK/7B6nLn2xAEQEHowoieAbyiABwlsAFcG2IGAFyAuHH7KrkMAYQBwBtcnZJIBqvmzDq+JWqyZKW2hGXS/YNWuLJRukso1qAGNNoKZH+YQCf7oBCyJgG/mV/i4C4B4yHuyssV9lfjEBz/gx5v+Qet0if+8tNQG/+HINoHWMDAa0hM

B/uqAEog4AewFOSnAdYywBW+ggF8ByNlb5RWqhgp7qGjvmt7O+zcilYbeU8JWCEA1QMI60EeGkH5FWU8pyr6QoxsPTCYtiLsRNUtVPzinED8HsCiYI3jMQp+aAMsRV84PGGYJQvGj94RG+ftEZT8sRi4IIA7wAsqJekmvfIpegopX75m1fnD5ZeCPrfLDKeRs37g60okV7t+hyihLR4OPlHZVex1q2bpC7Zk1rEqsiDg5j+JEjzICwm4KRosKBoo

qB06z1l1zsKJ4jLiy4pdiEHl2U3lv7s683nv7Lea/of5xIHtAdi3mJjGChko/zkBAS68ivRYTkjTCkxCsqSHZibOKbqQRuEBBKPrgwEeiUgTkLzKGjhWa7H2JxSkLrg74OxgZsIUsitHvjSeGWrAIoWaIQOyhkBAG8Hf+nwS5YZIvwZewhEhzByBAhrZCCH4E6yLHoQhTAFCEZIMIRY6IW8zAiG7uUAPu4wuqIXLRAQs6BiEuEWIYeq60T+kIFv6

mvkTba+YblyaRu+vqDgdmRRvIEzSeIUhwEh+AESGhAqFrm5fB1cGqTkhqTACHUhx9m5KghDIZeSQhC6CJZdQ57pJYch8IUBDchvISiHB6aIUKE+0mIZFYc2fWnb4DabiuabBBdwep6pWaGv3LxApAJoCmQRgDyAPA+GjLaJBctiMCm2omGVasYGnOzC3eekGEZV8kxNMCi4pQq9ZFBmEDvDGcEwNyR2IYRgF51g1wE+Kpm9QembxGDtlmZl+vnB0

GYI32vNYZePQbX7KaiPqtYn0BXiMFo+xXuMFleUwYdbNmsdrV5E+/opdZQgrKinYUKadrdbUkdQosBEUPXmOaoAJdgMbq8Y1suBXwSvPTpf8ZwZz6CKVdlcG7+kRstyBiZaidhNArSMwCAE3QKGRn4tEFdJMAZgNh6BobrB6z86C0CQB7odFgaGpuyAMjLxIbju6yGgiqGmR5I4oLJDhyoQIMgXS3goQCosg7uWScWlUiwFOBcgKCjQRCjI1J9MZ

yLBF9IIVjebPhjoYRFbMThAfg5APBFoFRkoESgbZA4hLaSqB7DMczcsk5PfjMANlMgGVAT4f4yvhmQOiisAhEF+GkAP4ZChoo/4ZhyeszEA4AgRzlh+bt2HABBFxyUEVszkRClAhFYgSESxbhAaEXGAYRbhF5Z+CjgeAG0RQgMREkypEeJ6KolEfBbURyKF1C2RsTDvgMRQrGJDMRkZKxFvk7ERi52wXEenq8RfFNdiCRAgTzKShBNu/pa+4gXoS

SBxioqHZwyoZtaqhj4c+FiR74YpBSRQhLJF/hGHGJ7KRwEWciBRGkVpGeRekfBH2AhkS/bDoJkRZLoRmEa/YbIOEcKh4RNkaUhERJEWWBORFEaJa+WtSPmwzInkfRHBAjEdkj+RlUQBocRoURyDcR6qLxRTkB2NFG+BvoU4r+h3NsThaGqnuCLWmYYW75+KWnhIC4KMoDKAwwFADKALih3hPKJhhGnLb84FwHsCGIHCsJg6wmQYsBIYm2g1TpgHw

DVZ+Gz3C3T4UI9AzBR+lQZDy/eQ1rUEqgr4nEbF+LYaX4247YRX6dhbtpUAe2hZn2HFmA4X7aDBoyoHajhYwZj6d+4dvtaR2U4X34nWbZlZpD+84TkIlUvZquHk+tQioJjG24UwoyY2wT5qU6YqnsCKckxmN4c+G/hcFs6wNjeFykR0bcFNy5aszR5OMBP7R3OuobYpgQQkUzR6OQTMrEFIJIR+b+uavloqv68UdKHnqHJnKGk2UgWlGmEGUcb6u

0CsX3ZKx/NCrF6x6sTJ7KGxpjFYBhSnntFO+gwuEGVAfgKZDKAckBpC++RnggBCcpnjIJ6QtMHdyMwBFLMCki9ePGYKcimNVRWeS4BohDUZVvoInAlnJrgjUcwHLjA8vMrn78wmuC3Si4cwDJhgxvXPWG22Rfu5yvarQW2Ej8kPhjHQ+6ANjE1+9fj7b4xkXITEo+I4UUbKiGPkhJY+XfpOG9+1XrTHzB9MUGqMxXZneBNeHCC141cbQKOJQ0DXA

bYNCbcjsGY0rPmG752saF8A5BHGjrwix54WLFc+EsT0IrGNwSho2aJDAf4JWkYgdE2Q4YR75GAQgDwDVARgGwC7cMwN4DCMc8IkDDgPALhDOASwB5CaAgfpYZBQv7JdwOCSYYXJxA28qsA9Gm4B1QpKvMGMQHwDGvUJ2I8ZhGb/cgPDiI/AxmODw1hxQTVb/eDYXfIiaPfCjz54LcdNbZmb8ml7dh3QYpq9B4EnUEN+SPv7bDBSoghLjxodpPEUx

vIHPD7EmAEYCYKRwPoAQwmADAAQwc8G2AzAygG5BTSHCNPHR2s8XMF5cdXkvFtGhnizHcAzXlLxteawbVDwq0wC4b7BKvLfDz+imL8CrAknMLHs+18cTTzGFMebyS8R3omGGG5dEsByQrGA7wFUrvO7wD+Gyjv4Pxt4aEEvKL8YzpvxSGpHxfxwSS6ZhJouLtyRJ8Qcd5JoXKmsAuaWYApi402Yc4DX8KQHvBg8sUNVCLyR8fvIDKyQDXyE6KmME

i6wNCfBCwxjnPX7zUzCX3wl+SXqjHtx/nF2GDhfCf/ICJAwWtaRCowdWYTx5MccrBiMiZmByJCiUokqJaiRolaJOiZMEVe0wXj4zhA/hjqLBrRvhK1AqwVSQVYixPFAnBAxgoTxmA3m1iJQxQoYhR+pwXcHnBt8UDb3xa5o/Fg294dGLlqE1oSiZaEgKCnBiWFDzDxmL+kybBuGAlgIR6NFPKG1ahAsQLWxabBAA/xf8QAlAJICWAkQJUCTAlwJ3

IHbGVAkKVCDs2vWttEMc9vvBpBhiVh/HJWqGidF2mFArhAzA8KLhAyYCYRyomgfwAkA+GNOsMCDUKSt/CHAn0W8DUwcUCpgkJIXAzAa2+xIXF7ixYF0nN81SnDEd8z2s3FDJrcSMmNKc1u7aw+vCbjHZe/QSDqzJoCvMmlGMOvpqA2C8RlELhuAPlYL8qdi8r46NJHzAMweUDT69e7ULzLPJsaDGq2cmUJ4m/WTct8mXhM3jz5BI1PgsCZgRiI0n

JJIQeWpMqbAIKDsglEGL76hswpLSu06aZmlAsOad7AGx5ULCmMmClscKf6obszCopVsdcIG+tsVlFS0haVmlWAppLmlEc1KY4q2+dKd7HxWHiiEGhhAcT/TO83kNgCNe+SY9GbwdQv9xU6kXrXQSYFSenFbEI9LTAIQB8JlD6CldNXQrA6fksQDcVQbpAJJ9CY3GucwPmSASa7CW3GGpXCcak9hpqX3F1+0yZalDhcySTELJEiUslGJc4UDTOpwj

FcnbxxsKcSVKeQfMr2e+4b5r14cwDsosKUxmeFfJF4U8oQAsSePj14I3viKAppasCnoEKEDMxbYagDxTqRRup8icANSBORoy2SOgYZIUTDDCnIaKMIxBAcAGihNA74AkjjITQNwx0g5zDiGVA8SPhk4gQgERnV6goRBbkZ4yJRmJyYkDRlHsHAPRmMMqAExn4ALGagBsZ2KCS5qZ3GWwgxRB6pgiVpQbtWnKWsoXWmWxqUY2lKhZyeSnVogmYRkv

2kBqRmT2FGQnIFIMmYwZz6dGQxlKZzGaxnsZmmVxmsoOmZtGNy8nvSmDavscGH+BYQRklnRX2DwCCg9AEYCAwMwDgL3Ry2mZ51Chtk2CTA7VEvJNgTVCsDri1wCsC58w1BZz6CRiHEDZgTXPlAni33tDH8aBkFtrNg+wGsDki8ZmemF+rnI0EaIGiC0E3pBqal55m6Xjwle2z6f2EWpjfsj4t+qPqPFiJ92t+lHKv6QzH/pOQnknLhUyv2YT+inL

FB+pO4UlDz+xwKxhHw9dJ8mRpyGUuYxp2/icC7y2UMpw7aT8egDSAsgPIBKAFAO9naAQIOCiFR8KBQB/GCgOaSkANgC+Gdq+gM4AfhhEAoBgGCAM4DMQYgK6QRAxAJoDOA7BsoB4gyAAAB+yADhA5MlDAACk1wPTYCg2QOwwE5MwG2Rk5pkO5mcAZOXgbcgKaXcHyx7tJFH0oRyOZKDoQjmvgkEAdB6hFp2aaaR05MvugAy0fEZ7AJkq+P842M1U

n0hdIPOcJZ85HaagCC5MljjYpAcwPTCLEDGvYk1WcKVWmE2ZsbWkSBEbmTYaWsgVpYtp9sczlrRFcOLns5UuVzmy5atLzntpYvsrnda1vtBpc2inoOn7R63jFnpWCWvECOgPAPoDCM5OXynRKeUOnybh2SuuBzAb0WoLfACQLpwXe9eM1zhmx1A1QJAwmJ4ZNB58uPTQ6nWYD5NhSMSD6O2Q/BD5jJmMTD6PpY2QIn9xk2UIlDxM2SPGbWY8Qtll

GkidN6D+i8atldmVYuYk2aUatVDXACEEemOJioKsAuJFwJrgVK0Oghl2iI3BdkOpV4fgy3ZaQb8B7yDOXLEnYXRJ7A6suEHAB6MbAMvjhAoKOmk2KZ+aUg4OTTH0ie0j/ix5PBmBl/iRxRoK0hiQN+Wy7I49+hrHoAe+RXAH5R+ciCn5k7PEgX55LqAWoAn+XfkHYD+Z7Qt6SLB+BiAcYO/mvg0BY/kVwihmKGICPMLjb8yeuQlEyhSUeG6/60gf

/pm5sbhbn/gkgPvl5sh+cfkgF5+QgBsAl+ZAXoF9+aUhCM8Bc/kpgr+SgVnIH+bfkYFuej6E0pfac3JhZgYcp5MpfNkdGjp3cfgAUAcAG5DAw4edOn8p5nB8BV8fMK5p10YRpRoP8RiCkBTEAPMfKrg5ousTHUPwCxjV89ML8BlW+eWZynpNtl1kI8SPCwn9ZYPoNkdhwYuMlYxJqXXnwxkoi+lBFgCm+mqiIifaoh2neT+mEKZyc6ku2bqSuEep

d1lVbFCcwHtncxziVBmU6zErMAnA0PKeGL5bQsvnd5aGQkrZQnGlfCyxD4U8JMEThGoCiQFAH3bkAH4M4AvgLrBbqfIoKA6TjISLEig74i0PzmHoCyHWykEbAROTCA2ARJABsW7KKFgpfGRIB2EDRfNIQoLRbcgw5HRWJndFpSL0U/+4QN+GOkLuaaSBAoxSijjF8Ac+AiAXurMUI48xVCnihAbkbHwpRmWIEopZmXr4WZ6UVZlUFSxfUWPOIek0

XrFbRVsVdFOBvEh7F/RYcV/IxxSMUq6FxWqRTFNxc+b3FVKbJ42+XsbtEJ0vucOlyF/uTlSAw8KLGE8gu3EIAR5GWVVYCYpYgdoyY93GrZaFNJMUIA8+FKUp62B8jhTHwpInQpfeyDAmZFKPSTfJ9JiMbqnIxwyetSjJRqf4W15AOiEVWqU2cInDhoiej4d5dqWHbd5pyS8rOp6KoPktGUaoLB103WDnZ1hORQXYbgA1E2CnAZ2QbxRpKGeUW7y2

CW4n7+m5idjpp3ar/kQArpbIplpvABWl42GviIGJR7xbr420ZBbybNpLWi6XMFbpe7Ee5nNgCLe5QQTIW4luhsdGC2HvnADCMu3MIyYAbkLhDalCCelkxxc6aUEEUeIkYgKYBhWgDDAZ3qLiKY8qnhRUS+tpXFdWfVCMT4UwPF0nGlD2r0kCJOqWJpl5rYd4XoxvhdXndxARTKUTZ9fjMnvp1qZ+m2pu1ivmE+K2YAzOpzee6lD5wDN6n8wWYMWE

T5MNJkUHBlOgPQqYgsLzIL56xkzo3x0aahmzecaXlB7AJIhog1FuGaOoWwkcU0wFI2+smDpOMyFQF6QbYHoGhR4+lJJKOO+EsCHoiIDJDzQ80j4B8sBbIGTwG7pfEhvlrOInJfl7NOoC/l3/vEAAV3hE4gLSHLgCXgVu9lBXWAMFdiAyAA5AhVkF2wrJZxRCKQbkmZRuaQWYphvkDTWZDwShUfl9KCOgYVq7H+U4VgFWuQjoIFWO52wxFSZGkVE4

Fi5wVVFRuqiFvaZiUJljKe/GyFKZfIUQAowLtz4AUwHeBNA9AJSnrxwfhlmCw/VHvBLy93McAaptVpjT6QtJZlBLESDPGolhb/LvBg8ddORp1CXSd8A1BPZaEWNhdts2EDlKMeKV3pw2dwl/avYeNl4xjeRMkaaH6XNnKlO1vanqlxiX3ltGKCc37rlupcAzy8KwAyI1WB8TmHz+bnrXGfRVpdGI2ll2TeWxpN2feWLE88s+WpU5ao6AkeU9v+FO

EElZBUiAZFdQEUV8FQhS9qWkZGRV6skTZQlIQJkCYWwE1agDZkk1ZNXogM1fNVAmbYEtXLV81WQrYhnFK1XRAUeh1VEVEFVEA9V0lbBWUV6FB2Qbqw1aNW/Z41RkiTV01XdVzVy1YtV3V61atWvV61ZNWbV2BfupyW+BYZn65NaUxXJRxuQ2l3qTaT8URlUtDtVeOqAPtVgVh1VJXkVsledWDV8BldXwGa+jdXIy81Q9VAmT1fNUvVn1UrlrVxNd

9Wo4PaZ7Fe5gQSpVpJ8ntFlsp/ck0AeQcALhDAwrHLhCZVRlQkFPR5nJ54rAROtTBCwmvNH4+lKYVT6DUtiLMACwlIpooNZukPsANxrhQ/JBVV6aD78i5fh3EjlXcZgLjl8Pvwn+VgiXFX5eCVW3nzZyVWqXLZveSuU5CyMDqVOaxsJlBa2XXk8m0+scfP75x88inEVVS+VeW2lt5XVXMSIuBYUC+QKc1UnY2ZDMJuuZxZsjr45et0W8goxQBrrM

EAImShkojufYzIbhLjjDVMdUIDr4uAN7q0u4cDZSAAAKTl1FdZXVV11dTXVV1M1U9UWwC1ZNUAVQJuTVHY4KegCR1ctNHVAssddAbJI+xojbzgydfsZp1k9kEwduWdaFFsQudb3X51j0kXVOZMAGXW11q9WvV11j1fdVN1K1V9XelemQ8X/V/pcuKBlosilGfF4NZZlyBUNbzqPBFcA2h51cdTAaD1SdVoyj1DpOnV0uk9TNQHOCALPWUQfdT0iL

1EmSvXr1oDbXX11W9UCbogzdbvUxlUVn6H9pWJat5JlIYXiWM1HvneBYKckELgMC2EIVYFJxovhRq5HVoyX3WmnBhC5hG4A4UyYdMIsCtWlhX/LZZ1VPCrzALItxhUS5cc4UF+xeYFWl5ateXmtKmtVXk61PcVFX15spcDrylzeZEVVm85SlVW1TqTkLhK9tVtlX8ARg1Cnls/qeKOJ6vMyIu1ctWz4Rp1paUWXBa+feXGYLmkzDb5tRa7TVgzLP

AaNKNSAAAG6IE43joTjW2BuN3ZKhwqxjmd2R7FNyAKCi02IAUgAA/KgDVgOBhBhHV0FbzTjoAFd40hNiOH3YZO8Bh/b+W/jUSyGgyBU6QFwNSD42uZccphVAQD9dPWGgoTSUiPmyHnkjCA9pCHKI1x1fNKAAKAST26tJWDYeqAIDD5gVDKGicAbTR01uOaWrzRWg9yDEx6ASek4RpkU6opQHkpTWCW2kYcPLR2YnyCECIgzgP6SIgH9rhB0g3UvU

0kVjTUBDjNKUk4Rlg2gYQAVIEROzKlN2xUkT6StpOwxsA1IPAYvSzTCUgFNdsJGTeEDaIOiOA0QJwAEA6ZKiX5plQHY09IR+X5zONrje42eNJ9u81glmTR0xy++TUk2oA4TZE0lI0TUjVxNoaAk0bocLQ2hpkvauk0QWCLeMjZNRoNSHItKsQS0UW7Tv/Xz1P9RU0cAVTVcg1NEFleRyO3VdBVAQLTX01qk7TcyxdNLAD03YofLROQCtSmZ1rDNs

ABa6i04hpM1fk0zfuSLR9LeviOZCzbGJAEyzQzJrNGzVJ6zV2KBy0NN3LSEQTNAJac0IEFzegh0tagPPU3NiIHc12wDzU81wALzUE1OsKsZ82EBbrj81WAQjnLKAte9X9XHqUoQGVEFQZWfUhlrFeGVPqUtKC0ONELeMguNXjdigeNXjXi0otfjRugBNSLcE0qxaLTAQYtklY03Yt2KLi0rM1LSk0vmcTuqQkt2bVk18FuTehAethTe8gJkczbjh

MtLLT0hywdTZy0xNvVagC8tU9uK0dNQrWEBySorSO0ZIErYM1XI6ICM0seRLEc19ICrVhELkyrTa0AN6rfgSatYLaf46tHFnq1bNhrXs3FtJrSu1eRdsBa2OAVrQijXNYJQ62rk9zcwUutbrVS0FIXrVfjfNCBH80BtqJcRwhZanmoZxWiZapXJlDNWmXBJu3IIxCAH2DRhB+xntfImVewHdwPwouDGplW98E1SGI1ScUJBIMmPKof8JYeRpV8HV

pViHi9iV0mZQoxMLCJQEwCxL+aStTw1Nx/Zfw2DloVUNmdBI2ZFVPp4jZOWvpUjVamVmNqdEWqlXeQo3xFOQoEVTQ5JJYmW8UwNYnXJD/C1YV4+om7VxQLiTmLM+u5YY2r+52X7XVVdpeY1GcbcqGFNVofEOn+x+JVPBtggoIkCSA8QFAA4OHRkH6eOmVbOmfwVcYlACwX1tKmNJGEJ8BVQJ2c2AIQ9Gidp/yVIp2VCwGUBWGZgxQpXTVFyZtw1C

lgjWjFa1hvNeleFnHT4Uxio5e3JiivSvrWt5cpU3nCdxMYlVjhG2RGpsxjPicDEde5f4aFVfMaaXll78JaW/JlNCRo+GB8JfFeJdwQuXd5VVYuWJJz8YL7vKaVYAypJI2uvQAq1wCjT8w2AAsCCwDQDwBLdXwEcCaA2YBUj7APIEcAIAmYJmKaAc4DgoD5SYDWJw6OKlhKtimpTkKEAPYpsgUq7EcOIaVw4CiA4OtQCWJLd5JUWXa8VfBwp6FnJf

1YCq5nA/DVUa4KLjXA9GhMB5xiwIcDXApwMfCmCBjYUp3aewL5WClvZcKVsdmXerUV5QjZKU15o2ROUxVU5eEXxVs5ZV2kxiyUtlxFt3V2ZdaSRZtnp2NyXFACwlPs13+pu4XvJBp7XJoLZQzIj7UlFhnSN3Gd5EmYIjmodThnh1UtAdLRAtsMQBoAcIWZQ4VaKI5mLQgtAmQ8AbYB/aelKigoyChVumLDVRHALUwAAVPsbM0uyOc0BSl7TOR9I2

vTCUUgPFEEyCVflLmRSS4joaAcgs6GNI6kUkt71RhMABU0QAFvXHJvlr6HbCOgS9nQ4TkTLGij4VB5KEBXI/4YIBZAmFVajfIwmZRCMApzlTmog8lMU0bqH9jDVR6jgGYBUqClMtB+MezOb6ZS8dagBm9ZvUa09w+AHAFN9Q7WuSkQJTAhglIkZLpLJIoaAtpQA6ZCb1ON4/SUiAAMKRgNgADSkYDYAAIpCUiAAQKTE1y1Sv2r9k1Uv3L961W7Jr

961bWRr92/ZNX99JkcUxAm6/UCaRkw/Wf2oAW/RwAX9G/Q/2r9d/YAAopGA2AALKRgNgABikJSOP1ONyMqC3l9wESPrdIrfUVL1IE5C02A4QDnBUGAY/RP0cA0/aA1z9oDYv339QJnMBRklYDKA39t/UCYyYWA8OC4Dd/YAA4pGA2AAPKRgNgACSkR/V8BRkgoDgPzV6/c2D0DRA0wMlIb/aA2f9oDT/0cAf/cjLNkQVAgQV9GjCAOZIcBI9JH5z

3RwbX4UntoCnOTfbtzjIbzA62cAyAB32Ogr4P+FogQg0My2sCZC02t9ZgO2xGDog6YNWoLTTGS7IQzPLQlI+zdBUG9BknLI+EVgXOSsMQVGczLQ4Tds19IVg58ghySetvqt2bBq+BGt9g4O0qK3ZCChUEnALMj1oGSGb1IsfIJgBm9QlU41fAXml8DyD2gE41MtJSHr3dIxgU30WwIdFlAd9kZLfbkAGyNtLeE6Q84AlgPSM4BGATjcUwS5HNLQQ

sgfhLujCEYJWmRm9wEbgBh9/4WfhE8GERlL1s7FjUheupzvwPUYW9rX2YBxACUhkDpdbA7JImTDZQX9KwxE0ygUZI0GbDm/ZNXbD2Q3sMzAPIAcNAmnA82q7DmTPEA2UVw8P1RkAkWtXbDlYMOBPDMwDZRMDRw+XWoAJw5GTMAMwEIDFMgAAmEqAJi0ltuEGtVbDvw/8OAjwI6gBgjEI7E141k1VcOCg7wwCN3Dv/QgNFtXLWRWzVaAE43wjUwJo

DVA//UXTntBIxbBEjJIzeAUjlTUSyRDG6EkOEATDsSNAjUwG40tNwQwhzgs6tH0Nm9m7cwDSoz7RE4d9NLdW2nOzgDKPIyTfdBHTFmyGoBz6RcLGLLOhZD/4AsAKDADqDYfSUi1Md4PU10OyBSfrUhMg9iDds5SGyMSsiZPyNZuX5Ju3Ot5AK63mA7rkw55MvRc2wttDLCUjm6fLLGSnOgoDAS+o3QGy5iQ49m8hONnzfOAJ9XUOmRONaKAUPnki

cOi4T1jfUKNT1bg11BN9H9vG2HoygBgElIUdR44zFagAACEETbii+92Lk+COojfYH1iD/o0wCpDnTl+QMoQLR3XS09sgr1K9joSr1tgavRBYa9rObwA69qAAUOOD2lK+Qm95vZb0UeNveVJ29Dbo73DjV0jARu9F1RQCe9FHoH2+9Uhv71ktVY8H37GeoxwAR9h7NH1YAsfY4QQoCfVbpJ9B6Kn0GA4MKuxXS2fdwHv2yMvn2st9pLS1Et9sG1WR

M3AfBzzMhFjX25aKUvX0wGTfS30EA7fakMtNccD307MJ/YP3Yo1/fAMUjSA+vUoD69WgNP9xNQROfVd/QRO793w8tUH97A+gPH9A/SP2HDx/df2b9R/Rv14DLE7f0cDH/d/04jDI1zC7swE+vjm6YA5FJ5sUA+aAwDMgHAPIysw9hNr1uE2vX4TGA27KRk2A8QP4DSk28PEDywxQPUDtA7WSRkDA6pN6QekxiOaTHAJwPr13A+vW8DswyUiCDfak

ANUqmjEwSUQSfVINDiMgx0PZDco2b1KDYlqoOaRGg1oNbMOg/ZNsya7AYOxMbfWYNwT0U1FMWD0etYM0uCFOEM5Ajg445i+tBL4TgOXbCWweDBxTkDeD2KH4OQykEzajJub4KENnt+I9JXMj3jhaNxDBgJSiJDgQMkOpDtQxkOCY+kPIO5DyMkmNFDZvSUNhAZQ6kMVDPcFUMR6JTd611DDQ7gBNDLQ+QT/OUYWoDkAXQ1rKnIgaI5l9DAw6kPDD

4QKMONA8MhMMuUonjpAzDCA8zRYgCw/WRaTqw7RN7DFw6gCvDNw/sPMTMI6sP/DjQecPMT6I89PYjZk78OPDAI18M/Dqw28MfDwM+f0gzfw/IMfDCI0iNUj7MlCMfVb09DMf2AI0COgj4IwjOfIqI5cO/DGI08N/TNk5SPVTnyLhC0jnI2SMUjyI9SMUzQgFMD0jyMjEy1T+xckOoAHI/TPcjjTom62jXo62N2wTfcKOijppH44SjVbcX2QRso3H

LyjSJVn3KjDaKqPGWClAASaj4jLAC6jyMgaNGjNYw6hjTq+vVOsz1ox6MOMfM+LOOjr7c6MvSbozaOejGbSrFBMfo/i6BjwYwtChj6FK+ARjVqFGOjFsY8oDxjiY1GVoWnACmMMeaY4LOZjUoDMg5jETSEyDogQAWOqBt9Q4Q3F5Y5WM+9fRTrP5s9Y7iiNj+Li2Piz7Y0G30VrxXGzEF9aeZkX13xVfWxt9sd2PlYvY+5GzICZKr2PtFoCOPa9u

vYHP69hvZ+jyAms431zj1va+CLj4hvb2jjTvZr10uG4whRbjd+DuNHjLUd8gHj4nunMh9p4+eMbol45gDXjO7HeNlTo7Cn1bMafS+NvIcszn2fjcct+OF9f42k0ATu1VPYOTCHB2yUQG6KlqQTdLg30wT9TUYPhAHfYhPpoyE56yoT/zuhMoRo/VJMIDMk6vVyTq9QpNsTRE+tUkTO/Ygv79iC8xNRktEzf0P9V/WAtMT1EyxMILh/f9NcDXE3wO

4jvE8IPADgkwQDgDIk6kR9qoaAkwMQ+gJhNT9s/Qv20D6k4wP0TBA8pNsDeCysPr1lA6A00D1E3QP6T3C5DNGTrA6ZPmTa9ZZNr11k+Qt2TlC45NiDLk5IOUqq+p5PyD3k75MqDkjLqP2wQU+6whTOSGFNttPLZFPGDygGijmDti9YtvIlgxR42DQBMa1kVaU9DguDfhJHPPMeU2EAFTBrb4MUeAQ6VPczFU5khVTA7TVNjTdU7EOUhTU6yMpDaQ

x1Nea2Qz1NxyfU8HrFDpQzwDlDlQ+WQ1DU08AkzTc060Ps5S050Nkta04kSbTX5P0Mfggw3DVbMIwwXAHTZlFOpTDCGGdMUjF024RvzSwxwDbDd0xsPMTT06cMPTKMx9NnDD0z9N7Df0w8MoRTwxDOPTvw2DPozKy1Mswz6M3DNYzpM7NXQjUM3CMYziI3svRLOM2tXojmI8wBEz5CzTOIzdM6SPkjeI+cvqkjy4zNxyzM7EuGz7IySNczvI6BN2

j/M+mNCz8kqLOpDkoxLPaRUsyUgyz1xWfMqj2THBFfkKs8flqzOo0339zho/KaZzzI/rPxLSSzbMmzG6MCvmzjzZbOujWTsbPhkXo3C0OzTBE2OkAzs4ihuz2SJ7OzI3szGNmkcYwmPjjXc90jMQIc1e4wEg6OHPf1vi8oDRzeY/HMYBScxvhsGpY1AAVj7TenNYuzvQ6iX2ZvQ2OOzsZPnMKUhc3A0c2/gZIU+x2JX7FRZrKVB2xZEALhBDAGkM

oBzwu3JIDMxBZR6YmVuHZogPwawB3R5QimE1QWcs8hd6bB8UNMAddDDaxrpQ6wLfAg8hCbyRj0g1sx2pduqgMmsJeqQNk5dw5Xl0iNetZMnZGYRUJ0zlInXOVidg3ZJ309bRgd5M9NXeP4VYvnnzgqYOdnnZsKDEssA1JOiHvLnlB/sN1lFAdQko7ymuH6v12zpVLSJaiHrS1fZbAQiHulo65Ytb4zGefhAQ3pV2X6ZfpcIHH14bafWg1FcxTaX1

5udfVZaY6wmQTrC6z4Hu58DbSkSFA6WB101wHepU2dlQAVQogowPoC1ApADg5sAP3TYaaFlnOz2ZgThrnxDG2YQ/C3wcfrXFZgudoDF5xSeYLhlWODf+udlf3i4UsdrnCmueFGtel3CNVfrx2BFHfA3lk9BaxEWKlUReIkxFtPQsHlr+Eh+sqNLPUmiaIdVPWCz+HZSaX0mZwBcBvAyfiv6IZBnT4mb+d8V115QYRk9xWN43TY38Zame+BvIu4+M

g0ZlxQ80fu3M+k5UMTpDQWOkGRInNJLV+VcxRLSNbS4KUm7aixLYAEVe2UebAPJviOkFQCglIf5PsaJA1QOMAwAMACiD7GaKOaHeOKU2fa+td7ezKGgrUIOCkAzsX0iKRAzqf5Wb9lDZt2bDm/8YQA0o0bJ6OP0ksxyrDKG67MyjpLqRdQnzEiBXs5TAhz/GXKKsVUEDatIZ+RfgrowtTbI0M7hwi+vKujsCurSC2h77CNHZ6L7GeTFMfYk/MabQ

yDgZIV4m+5OzIUm0rp4AzehORybEBQpu2jilCpu4cYcByA/Lmmyx7abBzclsOjzpAZuUgRm04QjbKiigYUeFm/4NhbEALZv2bjm85vCGbhHHPYz7bpa3GS1rT5uggfmwFtGbu2zhzhbR21FsxbDsQFIvBUdUluSjBSBKsZbPi9lugT8ZPls1Iy7EVuvgn6q+MdbS9VVtWOsUltishw0XBYZM9W46QtbkFu1tlb1cB/YlIS63gUhtJsWG2MVZcx8V

RtXxTbGQ1Nc2JvqZlff1sybapJtsVMwQ4ptXsuAJNsHM/IDNsdbcjAtsmtkK/pvyk62wCVM7227shPb1mwdsRbx2zQCnbbmxdvu9t7ddsIot25ID3b0uY9tRA+zpLuHbkW/sbvbcW+HIJb32zMW/bqWzlMA7WW+Gg5bgJUvWUsEO7OrQ72OxVswAcO5h4I7dWy5Go7zW5vitbrAKBOzbnW3juGrQHYdEBBoHbTUzdj2T3LoNwSXeD4A1QAVSggRw

D2aur0thoUCb/ODPJvRDhQFoBdgcEQ0m2g1L3TUw8qX/IxdbG3TCI9YaQ4WdlApTF5JrImj1nNBbCdl1ciBPfelSlxPcV15rwQmV2FrFXWbVJVHfmRuOpUnV2ZkFsndWs2J7ifVDaI8ylzGHlbWNcDCYExBcBnlV8Uhki9Pa7VV9rSUBuBMb2GReXlqbkMiCYRkgkLkQAp+3YBjg+O8XOA1xmaTvBldWtG1U7dAlLTX75+wpVU18ZTTXSF4Hag13

rse9avCMHAHAByQQgCYCXJ6hZHlnAcQA9bXwxmMEaH7+fOWnVl1npLXckG4HnHy2XmisAdYOUBrnqpSZt2WY9htfNTN7fWa3vobEpZ3tE92GyT3mp+G/3uEbptW35fppG/EJlrNms6nVAQGUAyBIQXghDuVrtVz21xHtTnnfw1UBvv9d3G2Ny+JO+9dl9raQYLgWdokugBQLVdTAtV1cC4ROP9R/dmSZMRwGf3r9jdRsvn96CygvP9N07XUKL1da

IvZknwifaCsgLO63p920vAYHtdS8CBnIMOyzMS5r45RmNTnAKc4zrQzO2rmg/S1K0cgRMLOsTkejOWRq0TLR9up95TO3rhC2M0cg5zWQKPV/kBQ/JEtLnAAoyfIDfdezNL1xWsUpIv7EO0bMR82kdusKTtUdVk2cuMDievm7xBWoYgEx5aRUCzAswLCk9gNSLlYJDNgz7E0MtV1wixXWTH5daIvr9uw3gMwdUi+8OsTYI2UfySiQFUdMeNh+XXTH

pdbsezH1w1IuCgkMwTNjHci6XV2Hdh7wOOg/g51obTEFmoCODg6KKJXILTW6y0rBgIOJOklEFajCWHbskRi+/pI8wkwHY4sUaHsk/JOWHe/dYfUThhwgDGHUi2YeAjJh1CfkThE9sfV1dh1XUOH46I3XdkLh+QBuH3eHrKeH+zt4d+Mge6aMboAR6fPekwRyc7IyYR/KbMFxBKlqstU0HEcZICRxshJHJSCkd1H4aOkfubWRzNs5HqdXkf8rBR+6

xDMHAMUeoApR/UdIllR10emkbxwKdjoDR5semkzR/JKtHqu35tvIKp33OIDWh6aeV1Ax/Mfr9wx3gOjHpAxMf2nldQcdGykM4sesTyx+v2rHaR+sdank7IIs7HDpxXUHHDA0ccnH7pxxOV1lx1XXXHtx2lr3Hn6FABPHsTGttqndkXi2fHWjECy/HrSP8ebsO2ICchAhdEaColtFRKHPFBBabFA1T+5G0v7FO1TZG+vxeCfQLkJ/gvET+h7Cd7DC

J6xNInnwxYctnVh+ifjHq9VieOnJSI4fTCzh0RmEnYO8SdatXh+y3rslJ/4f+jtJwkshHjJzfrMnkRwsPsnsR0X3xH407ydzDN5KkeCn+xsKcrzZyGKc4c+R+UfmLspyUcwGZR5qfKn1RymfCs3SJqcqnqADqerkep+3AGnnR7+zGnvR2acV1Fp0McjHYZ4OdTHAZzMdH9lp6gCun6/e6dAmnp4KfenRpxie7H+x9v3BnrE8cd4Dpx6/1V1kZ5XX

RnuWmi6Dj8Z4mcvHnfe8dpnhzBmc/HsyH8e3FPVaaRAnhZ3GAAdlNWpUmrPueav01lq5p4B5RhtUDCMjoJgD8wbpmnsZHUcbCAZZ/MFFAnwo+dTA1xatkfDVJt8LBmuainPoLCYlnEkD1JpwFcCxQmnLn5ers8uxvLAM8ltrLgia1j1A+qtbj0CNbQZXmE9Y5dKXFdNVqV3G15ZjI2idJG+J2xF5Gzwc5CqWVWsVca8dVyKdm8bV2xxtiJgkPWuo

nRLMbD/PFBJAtdI9idrosTxvixnXVAz2lHMYUWLeSSSJvRi03doYaVGkDADZiqIG5CRgMB4peBm1PgsrfAtMJog4dbWWMDFg1npyV8wkGeGvu4VWJiL1Uw9K3idJx6ZfIOX5B9j2ZVzSiFXt7GGx5e61Xl5Mk+XkjSwcU9Ra1T0cHwV6Pvx21tcQr4SEtETDM9a4SBk+VwPJMAkHVQtzGBpLXbGia43JA5XZXm+3Ic5q15WL3rADIoBtH7B/uWrs

FB2O6VA312Euu+lh9WutRwG61epbr59TutVze69TsSAoN7MKAdildTUR7/+zeth7kHSJc5UwoOiBTAZGJoCj+TV0WUcKBkFTpOGvnYmrZhQa5fCaI++/MCaNJYVcAvRBCdYhny4RiekY9De45cl5IpcFVilS17QfhVD6d3vrXvtoPHldrfu3kW1EnXT1hXXZmXRT7fZjRukSSaS1yK1DyXLac9J8YMDp+OeY3RFFF5d2umNM3PaWD0UXUOupp6BD

DBUE3rUzvCGwqA5NPgegOwT8QgyGuNZjygMPrQF/EQgTGeNSG7eeuCAKoAAYgnCICsAjAM5kOOSJckyeAE4KCczSDt94TO3bkq7f8T7t9VLJkXt54FBM/202oB3TwY4DB3ZzRX2lO4d5ihR35YLHeSZdLtCjXFid9y3Fn0KQoT37hBSTsRtcN+TuVzlO9XPv7KFmndO3/Ky7fdIodyESe3RcN7eZSRd6Cgl37NGXeRxFZBXfARYdxHe/ItdzHdBA

Dd/HfN3t+a3ff7GJZjcO+ke0lbR7AtvjdTw8QJoAFUweUt1kF3NQQ1GTGIuKrkaRnMTosKFDRJxUlr0ezc7EbJQMqxKmYDZybhxcZoJ17M19qlzXaG/j3LXdB55eS3ZqeCDS3oQtI1EbsjSWvyNSt4nZdmZJdRsXXEuNcBnE0a7qILALiRo2DUDG6bddrJjXxuFXUebiKU+ah/FroAM69vpsnvGa1rMsnD3cd37ZZwDVd3lZz3csVtZ2xUyyDZxA

AcPMZ2i7H3nub/tY3EWSg0WrrvlauiXCZrhDM42ABQCDBz9zOm1CG4PYbGcbZcVn577UGDHVUywO/zheIa40l+GhB1XEfAYnDraGIXSbdeapflTA9OXfDS5ccdot2FXcdEVZ7aMHqDwPHoPst7NlD7VXTT1cHuD8P74ScQdV3q3RD2zAOVmtjD2638EAhAuJD8OEmVFMh0Y2VV9DwVc129pZMBqcNVtY0vlKFsKAHtf5Hy3MAyTGmdlgbyJqfV9G

6EtC4A7uno4duzT6/jzoMlIew7IIVM+PvIZzFvbuzi89JWRkHQNmg1IowM4DjA6ZBAQ+A2+us+N3SJeSGqytyK3fglvNJBAhgqkLOvb3H438haAQA/oj9IOQOKw3I1LGjXe6BBHlEqUo0cvjwoNiwpQfhKRDXIfgQEUKwkWL+B/bdbdT9rv2UjT/08hErT1ajtPNz5083IPTzeR9PTTGmeDPNaPW2b4x8+M/hAkz9kh+9UZHM/uACz0s8rPMJYKw

MemUk3dvoArDs9J3puvs+P2Px8c9F9pz4MUXPwE1c+0glECcXlyq+tKiPPWsoeTdI2Z0fjmMT818+KoPz1oypMAL9gRAvumcG3GxDFSI+brYj/3d1n7FVI/xIIL3tv5k4L8i+v4UL7MgwvL849LwvOkr09/IELyYRDP6L6M8Hk6gBM8NuYkHi+zP8APM/jIiz8s+rPZLxs/73VLxew0vez6CgMvRz0NIJkLL46RsvZgBy83P3L288yDfL3AQCvyl

Lq8cOIrx89pk4r2TJSG6KH899Fe6IC+nrFNeiXJl/F9etR7pV2o/X3lQDAD0ADA6MDcBjV7Jc81s6VxiHAH96F3D0R8Dh3xd2hWRKCwN16WKveWQ754TGCwBMTVhU1+VD17APo3v4gqG9QfwPYt0E8S3DB95doPampE+t57B3I2W18TyYn4SAwIQ/xX3WLnYcYohzuEk6aVz1xg8hFA2u0PuV/Ie8bpT3eXodlWPvWvKx+xHXEAMuixAq+W1d++/

vUQP+8/VBWp3cVnj+6I/cmoZTG7U2+6xIC4QP72RWW+Z61tHiFsGkg3Aigl7et43Bhtav0AlYEcAwAQgMOCAwuDRbwPRGe5TckPX3JnGerOHZ3RWcJlzJisbOTyWHHA/3FZXWFBFDxo5+RxMuuePZB94/Jr7hYMmil+qRmsZdAXF0FrvUt+E+bvA+3Lfm1I+3E+hXeD20Z7JkV6zE1rtYV8Cba8UOp1c9mTzo3sKpfIphnAhT/p3GN2+xbf8bb79

Z68y1TzL0oWvzwUhdPQEIE7nPx3dneBbh7I4673cu073Ct+Y5ih66GSGFFnILd71Up36BK5+mvqzZR4joUb8BG+fG6P5/qsdIUF8FI8c6F8964X0tF7oUX8ndFzgj0fXQ33dyq/Qfr+4PdWKsX1ozxfOoZ5/aM3n5Xepf4cmxAZfsYll8rO1dwBhhf7TnUiFfh99F/yPcZaabKV2NxW/+8uH+77BJtQBpAFUtQHCLjAEVxR+FlX66WIyqLIr1mCw

tJeY/wQl3m/BHww5uzfZQr3unyT+8XfCqlCvJRZczvDCRQdNBVB2mtt7K9Ag/i3Xe7J8oPVMBu95e/l5g+BXKpaWv7v6VfhJGA/B3qWl8OsB+9FVWYSZ8MSVwKXurgOt5xvFFoWnlc/Jixuzq7yCKg5+sPkNhIBtgYsLchAfLUu6VE/TpEh9/vswiWe4F4H8TvKvsN6q8I3A90jdD3lQBT8k/yH+rqjfCDZeuYfmhth+43wl3h8aP/0G2A8gMoAV

QcA5HwEmUfkeW2+kalxDZyJQAPAx9vAGUPsQ3ZLwFZX6XVwEYKZWiPbTBvJXSVw1apCMQ0FPfsvwtci3b38u+dxWGyE/rv8n399DBAP8WtBXwP2p8JPQpnMAQ/3RnfDvJpGrP43e8P6aWTAA1I1BC96P0+/5XWP2Y32fQ77beM56BNWD8WSgULTYEQOZqPEA22HPog5b4UBCLu7tOE2NAqFQUgX4o96Zujbmd4UPB6WABhbMXouTbkDqYGnWz72H

AInfW5Vd5wzgTbIJHEdpYsHBHKohHDF+jqafwFa92NaJ/hcnyILn88nDaAX+ZARf7FvjIpf++WJylf1fii7tIU7LGBDf6wBN/LOSBrbq7fzS/d/Yd73/KMiAJaApMGfwRy5nWyLkSgfpZ9gWE7Sr5B+VfCoeI8xt7P9WgT/Alin+iSBn+Ofzz+i/1yiK/xFy6/3L+dsC3+TrX5WKWkP0+/yLqyoytQx/y3Ug6jP+Xf0DugQCv+RxQH+d/2H+q6Ef

+ZzB4uJb0AOZb3PuzKUvuGnlF+OVFIABVHoAShWqAbYHwU5Nw2+bb23kOWSCQmYAcSqBxAYAPDO8DdAzAy4DO+7H0MEOfFGoGQxpgFtgfEfN1neAtzts8XkpSNvwk+ATy46Dvxk+Tvzk+sVQJiW7yVKMT0WyqnzH2FG19+svzVu2nzWCY1m3K6+1J0+t2bWBdhygt/ESgdiGj+sxgx+X117WOP3mA6YXjMTnyGEcbWFc7ZFZavbXfOMyGL+iLwCs

/jG4IQEEHq7GXPOvlB8keyENI+xhN62r3kolsnyACvkWGzxg4AbYCSmRfWCIDLgWQfak0yZR0tAogGCABbVQAgACTCP5AsMPtQdPGgjzQLpAlIJjJAQOoFCOdFBBUPdCZSRooQULyiUjRADzgJmYUefYyXIGjxNAuZAtA1Sip1BMiEvCV6I7JxbjoR460hcZCL3eWhpfFCJj/WxpBA0VxstXirW7LqARAi6oCWaIERkOIHYoBIFwUCcjgVRZop1N

IFa7f5z6kaqSfILIGK+XIH5A7ba25dfDFAzGplAtI4VA1DgIAaoF1AiYGNA2F7NAxZCqUDgDtA2oFS5boEkWPoHzSDyiQUItrDA2RifLMYEqgBoHPzcCa4KaEGj1eYGuoRYG0gZYEdOBM5rAqAq35QO7dkYdBt3R4od3Ur5Q3PRQVfJn5VfH/5v7Wr6BAw9bVNUIHXscIGxbSIFnAhaSxAmMRXAzI7esW4HJAs/IoAZGTpA3ZCZA7IH1kT4EFA2l

pFAssAlAjjLvnFJB+MYEGgg+oGTAyEHTAwkGwgp8CdAsPQUwJEF0ufoGogwYEKQDEGjA3ZDjA3EFTAgkEWIWYFmUBYFkyJYHxTCkGODGMjrAmkFPBOkHbA3n4XrDD4TfZR4AHVR6QiYA4aPFEBsATMDoONyDg/dgGy2V+5RmHj7LgMqwz5bdLZhJQTsaQsLKpE7LDASkR0wTX4i4Aijr7erLxrX7yF5JDZzvC9LKAuB5pde37a1R344xaKru4Da4

5GPQGKfKJ47vbB57vb34HvX36UpCwEpFSWCZQb0xcaHnpu1FUq89QhpGXNrIdrd67WfDwH+1XfY4/ULxZgYTZh1AIGu0T/ZBAXLZavNTYzbPlpBMcAoqKfIZj3UbiuDY/Ln7LSJabeUz7jWFqZtCCzngU0gTkJXaXNOtBAXHJBMvEVaVLFabjIakAkAH+pGkEpAbA91zywB8Fn7McDPg5tTOkDPqzIFprgQvpC44A8xPtU0jJDFMBooBvq3IeAzn

zNUgpvLAimReWYMnDgBBjd1z5kbRhWtfOTDMbNx4yOtAyQMIAm9VjwYQyCEn2PCHf4bFAynOU6JOA/QmUTU7NIcsjfsSTLP/BYqcUY8Fahb9Rc7AQpT2K8HMFGxS3g6v65ue8F+ER8GIQ3navgpebvg3xqfg+SQ/g85rK7dmRGnQCHbsH3rLTVwZcQrCGnOGCGaQvooIQzIBIQwUAoQ18boQguCYQtiDYQrl64Q8rbEAAiEwGIiGukM54/goKj5k

Nobf2SiH3IGiEJMH1hCABiHegJiHLbA8iWyPAACWDiFfkOyG+QniGBQqDhFHViGvzZ8jlHM5BiQ1VDNMV8gMgnApMgt/6KvEuYVaKs693Gs5qvCR60CbkFHgs/Yng+SGJzS8EwEa8EwgpMZOQzUZPg3SHTPIJx2zApCOZL8GkQ0yF/gn06WQ+vTWQqpZ4sCCH2Q5GSOQomDwQm/auQk1AeQ5YG5Q2MAn2HCEGSSSBBQ+U4hQucBhQnfARQl57RQp

JCxQkpDxQ/0bnPZKEFyZiEZQtiG/1UYFOtbyHcQukEFQ0NACQ4qHCQjdCiQ6xjiQqqFiwMgEexE+6KPM+6TfC+6VvOMHqPHKj7QfQDYAFyAUAcYBhqWS5IdYTiKXZcC7wePI+pe8ofALq6VQNYAfwI+AA8bqxAxA+TZgEYD5VLPzZKZ7wsKXPzG/f7oLyBmCsYFqxUSIvJNgh4gtgxd5tgwJ6aAnjraA777+GX75N+ImJKfYfbjhFDIalZW4kKLb

oFYHUrydOCCxXXxTAZTlRUJD4Ao/O64NYMNbGww0RtYPmDVQR6xrg2Q4bg2P6Y/VfKW3DcLHhbIoowwPj+ApGEfxDSoeQTAC7cUgDVATACkAUXjpg1BLNgeYjbiciRMlJripxcEAIQEYD7AALQbgE2woHe4DslA4ACbJwH90XPhqpKd7dJaB4W/QW449VQHprdQG5daT6SwrsH8dXqiyw6bIBXD35A/HB6jg0H6+/VNZ08bKoO1PjCZXd4CFheZS

8xCnQF2UXDXadtZuA/6wKHWz6MPB+DSqVjDJpcq7OfSoByQAULulBeGe0cG70/ddZsg1SzP7cmzRuCgpwfZG7oAZeHA3EPYY3BGEMpT2FqVGb6nRDR5CAFhhtgUA5oKT9YZg0Lr7iePJfAcd4XAevBN0cd4GQAsJHwNjYRdVjRsYd7zEURmCEdPmHeVAT5QgRsGKA1jrzXLLo0HcWEdgrQGVww2pSiXsH5rLa4m1SnrRPanpGA68oqw9T4n8Lbqk

kY946fAVJh+PnD2A5kgo9VhRL7U+JeGWhRzKB97eJe2GeA7cG1UFfYIQTTgewth4VqL2CdqMMYezNZ4yAN5CrjCl7WjIr50vR/wChCi44cRGwN/TCJooP4FH5dwbyXHiz7SUqGDoRO6akdiinsNe5n4MQY5fBtAUvLZ7UvZZob3DkDECaCxiQZpAXIXUikZCsC47TgoX/AhzEQxMgUnAmHdQRezwRSqGmkXJDkWUVxiQXtBcoSwCIsfmgMQXTaDo

MwJbwBCjaIz2AONYArCoUJbjMbO4KUaJGZSbZ7NPCabjoMxbNfR+btsVzbmOcEbd/EqaYQq3T/hRiwBIbGC9iQk5KIzUEONN5CRYLCpiQfrautPlhJIHYFibB2ACIqZ5sgQVhN/MRGN3CRHDfZO77PQ+Hs0Nk5yIxhzmRNSAIuEoFwAVREmeQ0gIvTp40vHRF8QPRGqLJ8Dm6IxEKrP15lIMxGn+CxHJkQ0iiQV8C2I/9RtLWSCOIsZEuI0KG/jH

w6HoNRHeIr8hQwvxHAoAJHIeIJF1IPtC6McJFJIH1qZIPtgxIrRHBgiuAJIk/JJI8Qxu3NJHAojJHUvLJEeHbFC5I5L5qLVzbwuBeGakZJHCVW86VIl+wz3di51IpgDzIxpEsIZpGWkBeZtIiJE1Q36prw8r6M/TeHVnbeEyBCGo1fWmwPBbpGsrcMbCIgZFtzH25szSRFB7ZxHwFSZF/keRHe6RRFzIhpF+LZ5ErI7xxxIiuC6IkO7Z3ethMEXZ

H8o0xEBvcxH5jSxGnI5tC+tSOYOIkI63I2kHXQh5EeIle5T0F5GPSXxEDoT5FXIb5GcoGCB/I9pGRIoFFtReJCgo25CakCFFMEbFEwoqyhwoulyZI5F7ZI0NAoolr4gTBxboozfCYoz2DYo/CoVIm5D4ompEEAIlGYBaVGzIJpHpbbJCtI/5FSQsOi8XUt5XrKgEXwkX6zfa1YwwQAhTANgAudbsQhw3mphwjQTZ+TujHySB4Fg6zxV8VPLrgaTj

9GIa51WEYAacTYL7APeBZ+Tspm/Lx4Fw3hpC3djqLXO36IIrNadg3uJVwnsE1whUpsHeW4qffBGTdY66+/MGikImxJbEUfITmN2pUI82GxoSYCjGDjBvXW2HFPGz4MPMp61UCYCclRz6zww8GVAfYwKQUYqKoSLCtkcQwEAWeaG9VIiBOWMj7GJ0GUgkPQWua2YJkLmhsQEyyZvYFBooNoYnmECG2Q/6EbQuOQ0Q2NHd1PCKTTK/DFNLSJyQV4FD

4WgizILJwxHeWDDsZaSoQ3IHE1BQBsTIExFIJjEcAfIDkYjk4b9VjEOuCjE7NWjL1fXUGwAbUzE1LbCEnKAy4AWjGTVejEAAH3b0RSAYxy1UkxJSHyAuEGoAFsGuM+QHRA1ADbAamOHA1ACaAgmPmq+QGBguQO4oZlEHQu3H2QArwtgRMDeQCkDURUZF24FsDkgxTCgGX5EogOkGai39lYAbUTYxsR1tBIIUgonSIkAn6KCAgAjxYDoD/RSegAxM

QLkoDEBAxzIQgA4GMcG1TiXaNBAdcMGKtGhoHgxX5FyQSGPMkKGI6GoELWhPkNjAzK2wx3+VwxQlQIxGLWIxboFIx1s24xwHGoxq7HEx61XoxDGKYximJ8xlGI4xXWJ4xubwKQ4Cn0x61WExYvi6eLWNQAUmJkxcmPmqCmJYxymNUxboA0xWmLdAOmL0xxNUMxxmJPIqpATIZmIsxoZCsx8sBsxlqO/qkZAcxTmM76VlAQwHmNaivLCYcDWNt2do

OyANKLoqzINDa68IZROviZRpuVZRbP06hH6M4QIWMBQv6NKRYKEAxMWMeaL43ixiWKocUGKyc6WP8+WWMiYiGIWmFLBWhhWKOhPFmehIqwyQ4yNCi1Ultc3hCqxRdBqxrGJBA9WI5OpERgANGNJqEmLkxHWJYxvWL6QPWK4xU0AmqcX34xMACGxy1RGxE6huQ42MmxTGOmxk1VmxSmJUxamKWx2mN0xXOLdARmJKQJmJ2xiFz2x6pGsxVqFsxSyI

+aZ2OcxaSKuxySE8xMyPJxvmJRB/mM5AsMNjKfP0jBf+2jBONx0Ml8PZS7DwLo9ACmAcAHRA62TSybqwpuEwB6ucUCO0N11WAotVMu/3HmA+cXigCaUbKx1C6sYwAJ05eBsQldG8qE6KE+U6OGgIsJe+CCI0BSCIrhy6NQRVhTXRGDw3RynyVh1VQIRPv3OiR8H9+GdkqU14jPRk+XnB/cKeuexAR6RsOaERT19qm4KM6XgO6whsL5w+P2F86AH2

MaITrGzSB/a/u26ggDRhhfK3JWzzVdGx+UeeqTFwBwmQnsHLSgcBoQOYe+GsAzBT7ElW2bUfY1nQczVUAPAX/Czx14gACRYgppEjmfaiaadg0lBrY3F2upD7Ul7VtI6gGEATpB4yM0T3apJxWaKEXWaJkXuQ0EXlWcp0CAUJXZkjvXeaJMEu2glUHI4QP2M7pT7xMiIHx1jCHxmY0LqY+PTSb7SnxyIBnxQrDnxNfTfI9TULqtYyTeLhDXxT+M3x

QY0bmFLF3xH43Q47rEPxBcGPxUQFPxt+M76552vxAzgLgd+PEMD+MT0z+LhcfkTfx2rVWaR7W/xkrSI81gH/x/iwRQwBKSaoBPd64BIYYOU2GQEAFXhr2KJ272M/+7IO/+bUN/+f2KCxEAH7xl9kHxF1WHxZ2yLqncwnxLo2wAmowwJ4yCwJC+NwJy+IIJUwnXxzABIJ2+Ok2c9XXwe+KfAB+OCYtBJBwDBLYJTBKvxKTRvxARPvxQ0ifxvSDORM

oNnO+zgEJX+M2awhL/x+pHEJQBIAqIBKNAYBIAqEBOOBUBOPhcnlvWlAPPhEHXLRV8JyodgB5AygHiAlYGUAgGQbRrbwZKicTwoMnD4B8nHBAHV1BigPEIOMZle8IDzY2xfC2C7aPlqk+XzhGqji8JmBUB8CKXeC6PLhwTxQRuG2zxLvzlhw8QMBuCM4O26L/SNtTs0W3TuiWnynBrPXau0tUM+O4QqgJVU+AtJXmAI8M4kreNF67eOEBHGi3yb6

PUO0jyS0sj24eSiheJFFy2E7d12EdKNZBH2ItiW8O+xu60oK8H3YeHxK4e4YPQ+IHURhVuKm+LvlRh1bwkARgCWAMADngFACaA3iDqJtQkri6RRRoB+xjU+30qyL0U2CplUR6bH37RNoE0QAmB8BMalroSQB5uL8BGJaZmnRRcMmJYsLTxi6OQRmePmJf8nQRfez8ubvzzxisLJiB1yXKR12P4vv2DhyT0sBynRtAAtUFgsqXmUDXTNh6vFcS5xC

Dxlny42dsM+uW4KUOu8h0E7G33B0vXfRmsRvIAoKzOZEQXmzBIyQ7kIyQXGVeQljjYAVrBxxJSKC2jrk/Qvz0ogPIDnmi0UG+TyPVx55FlQAe3AUHfx6kZAH0kQzGaK4z39wmo2wcZkXrufyGFmimWURCyJlR6uMoIXLyQI9zwk2FfQDe7mwG2KugtcYQEvxzyKgM953PIUoCLQ4hF4huHH7QrSBihzeghKRLHuR9emacgQAGiEMN5QbyORaYunz

AgWOFyejnNJLF1aQ/W2tJyELtJLQLFgegGdJxSM1IbpL48HpOr63pIUoYUX9JU9EDJDNjXYh+CtAzrnDJnAUqODrxjJx+TjJO9xqQIoxJBpAHTRJKLTJVqOuemZLuegRyHEuZLF8+ZJk2RZJ6+pZLtwgkIDQLIDgxeHgKhJHFEgvh0ehjZPG2LZKCYbZMcinZMHQ3ZOCavZIX0JX3qhLxQf2bxS/+JuRg+u8PrOoJLdoZpKB2w5MtJqqzHJtpK0y

DpOnJGKNdJYngXJb4E9J5zR9JA33fYniLcIJhCfmIZKzke5L8RB5JoKR5ORAJ5I/GZ5KTJl5KlRKiJvJM1AzJtzx5emfSfJJADzJF2zfJKWOy+x2K8RZZO/Jrs3IAf5IccAFO5Q9ZJApmKCbJPTTNRrZOfIHZKRKFUM2QVUNQ48FILRaJThhxaIF+lV2oBbsKvudAJvuRgDkgwMH0AfOiXCbuPT2CvwQgVcSzAiKiMurgOzCCKhsKPwGM4iSg42Z

QD8MXmj7o73CoaPwHm6ZcUTM8gIe+sD1Fhblw72H33oOUsO7BYT10BMtwHB2703RBeJG6ReLHBJeLP4B6NlJekHhoo+VyCEGQPK56Pa4fMNOASUBvRzeOF61xMUO2Pw7x2YGsK3eJEC1BTQc0yNoIFIQ6KHhxSQm7EVyXP2p+aADjR7NDPIDbFXuh5mIEtEIrkb4PnsBX38YPcEAg9o0dIzpAZQY9npYWzXYCI+IWpycyS2lONQhjEPjIUlNz+L5

Nkp1OV+QQTD/QH4z8Ix+MkM4cH9anzGAKJ+D9Idx1GaX5EYp+BJ/UtyAb6tLFrJ27FG4CU26AA0UiGe1L2KJhH7JEAEfMUKFGp/IFSYE1JJOU1PWQM1Kp+wH1/qs5KeCS1M7QMjBqQRllSx+ZDxeW1MG+O1PgMngT02h1JmKKJVmqZ1LcIF1Oq2V1NOaN1JShd1IcmMlP2WDO1epQQHep4yE+pLUW+pWziuBJ+X+pHLVjOUGJBpEATBpxAAhpC5x

I4GLliOfg0ciCNO22VDGRpiFJXWkNzex9KLUJjKJahzKPIKP2JBJ+8NRptLXFRGEUxpvkStabiyJ4eNNGxBNKqY81JcRpNLhQ1SHGQlNPWpE0PLc21NNGe1NJWzNKrgbFwJc2ZCMJdsE5pJYyjp11NfGfNMKQ/E0Fpry2FploI8CH1L5aIBClpvyGfYstPE88tLRcitMUpX/l9YNSHBpMBkhpGtK5cWtI+QOtN2petLla86FNxfgVCyJaKKJgB1t

x/cgIo0qErASklT23lLku6uIV+VMOvgn1ibACgibo3JHbetJTphhdjDxAygM4GUH6pTVhNsigi6S2gir4NwHYwvnR40mnEFhMCJQ2on1bhwtzUB86I5JMxNXeuVJXR+VOYOApPlhg4JKpIpOMBh10UaWxJmA9aOlJFiWiuCnSU6esJhoz3Cj+WTxzhYf2DSmUDC8DdEuJ6/m6p48MfR6uE2C2BxoBgDB4RZq0iy1kDSsRlVxwNFGOJ+pWny64Gz2

2jT06WpOjEOVEWeDV0dAMwEwAmgGEYcAFqAygFqAg8lwgMMHGAFsE0AF9PTxmCIfpUT18u/YNYO2CKHBQVxPpjaOeuGUBo6TVgGurGHIaSaCp8GfB0KhUDsQVEmE+Imjo0dGlbBuqiSg2AAIomVT8Mt3AFgaeQJ08XUGudYI7gYXTu4SxEuAPMUzAgyjusBl2B4fwFKpyyXKAw4HyBPAFwAckGUARwEkARwDYA1QGcAcMDYA6ICGAkgB2JZQCmAg

ME0AEMF24wMErAlYDnggMHoAowGwAPIEkAiQFMgeEGcAXlNzAu3Gc64wEFAxABlASwCaARwEdAoTOIAygGwA4B2KZeGiwku2wtgEmwisNmnYiTTN62SSRQimIDSQagC7AELm+QHqSeBuECiIEKCBAtyBeU7EWGZ+LDGZZyT96cOmWSYAHCwpQBmAX0F8QYAAWZExAEwU/gPgqnDPiAIFKASGE4Uf6ypEmuB2ZRwFWZ+zI2ZjMHh6xjLSC5GmgYpQ

FmAaSnfhudjeA3wAuZX0A2Z2YAygrGHGMiKkB4y6RiwYAFbW4PQB4FUEEw1UCSUHzJiwGzO5huUF2+1GhHy+zOBZrGCsZs2FARR8DsZ0LLaACzKWZizNWZWEgXCW3UIkIP0AYk4Js05twfRr7yoaTJSok5nVhJyMKl6F5XzpMAH9afuXjBOVCmAckErAEMB/eTKjgA9ACyZRgH5gUv30ACez4OQfjwZGWRxE73ghZxmAmA+VQKyx8Es4lsIZELJC

6sO6XQSZOjjUaahEB7j0CM8UHqpigipEvMjEZajPxAGuDzwTb3E+JcK04pBG6AK11d+PJNY0OeP0BxGwbhapQ4QUTJiZcTISZSTJSZaTIyZWTKgSuTLKA+TJwchTOKZpTPKZlTOqZtTJlA9TIH8+OlOAmuAS6kCKKqDHXn8diDigF3iygcDIHE+43mZX0EWZyLJWZMWDWZCzOgS/OBnpNnC9SxSU/hxbKWel8CHohiANsynDWA2LNKAlbIFgYwG1

ZKbOv4jGmRZ64G5UGHTlw/XCuAnbPWZxbLxZZbNEQWEgWQiIG6ZaEDOq/TK5Ae1jsqinE3ZO2U6ohkDAAlSUOAvMMPZh7NFS4wAaZTwPaZVKgmZdIAvZw4iHyQzJGZzTnGZrTLpAUzNGZR6FMBJeLbqPeQyi5LJaMlLJfegdRpZGrLQZPdK7kjxOVALLLZZ9NA0qWjypAODjvAbkHgSo9JbefGA1+x8iGoFEgAeBWS6wkeJDWvMESU7nilUYPWgZ

i8i0Q2gj4+FgjB4c8j3Ex4ku0FImS65v1GJPjxnRfjznR7QUzWt9M++99KzxvJNdZRVJWJe10G6HCHDZkbJKZZTIqZvkDjZckDqZBPm/Z4+zVhMwFJUf9I3K64Uj8sG1J0MP0eugwBTZ7VIuJzCK32CDKpZgHM3AtLMGp9wQgAmg3KOXo2T6nBFCBDzSGKiuVRy7bj2R34V+yHf2hQrOF02V4wWQDTjTI2kPEiwIIv8k7RlykEHIADrQ4M3UltgU

LAz+vqKSRGkhMC0XM4IQBUhRkgHuQIkVfsA6ilOprTP0UkmPmN1OoI1UVRprRUohYvkgM3hBZyTSCKhsiI1YfKDHssJWaQZf2+h42xWQuyDma89liGtrQ/AUDngCylHYiCKEcA44H3MLLk9QftO7QOoNfQJSHp2z1MDQ5Uj0i6rhmK4jneEkFR4ydXOLS3LzOKAaAuKphMF0bi27UiXO/wyXOXw3Ugo8gq0g4wBNzuczCnQPt0HQglQlWHfyhKMk

VK2ETgyIMrSXaO2NnICIXGEbn3zGsqytgkXJtypu3Fmzt3+2/5jJpCKGnxL3Njkr7E62sBghQpEWHsUXLpQB3IYKIrCEqF1MnYZ5GxpaL3DkGNIpCoaApArOCqG4yFnQ2aL62R42IcmgFY4K93gCQTBTJiyKtRaKDxRq+lIIgLDxQscgH0KuLIxHrgUJRYzbpLIHC5W5IKQRrVi5+KCy5H4HSQlZO6AUDkRBe6CW56wjeQllFcxrRU2KazHEgMzD

b6kchKQ9nNhKqORRplnPouj0kuQtnNqaJmwc5pXIkgK53m5EelkiaKA85CIQbQ3nM3JClH85oZEC5agXHQmcDC5TfyiRiPJDoyPMSR3SD/Izx1kU+3LBaKPNS5JSHS5Vziy5l7SdIV7GfG+XMIChXJtgtyBK534Jy05XJcRIMOq51R2EsZvPeRvKEa5Alma5yaK3aDLXa5XUE65hvLbQlKn65EgyAiAaGG5y1LPJaR2EsU3MG2P6ACkc3IVWUdMW

5qwmW5cLnz5cJTGKl3G25EBl25IfKR5YfID5m6FO5ZrHHmHtzzuM9wLuIq3/Kvt1ocng0e53bGe5y7Nd2b3K+cglEgs9emL552wTmM23QBgPIUowPLS2ft1B5o3Iuk6BMh5753FQQJlHW8PP8IofJF5T4G8I6POq2WPNukOPIURTtOC5PSBZwPVWwAxPLAhZKKtQ/WzsAVPI2QNPJgIdPJEpXiMZ5yaOZ5yTnDQhuk55bo2XICWLPGfPK95CHCF5

uBMO5IrDF5tklUpVSJ+aVoNl5/fPl5VqEV52yGV57RVV5IYHV5jACn+2vLW5XunCBe9RYwcmFKSEfhjULCl1yQjwg+qFPUJ6FOq+v2PZRFnJMW1nKN53+Ds5zBSH5TnL8oLnMe52Hlt5hsHt5ZIW3mPnJ5mfnJchrvMBy1dOxQnvJQiq+nvwn/LIFgfPi5e3Kn5IvLS5bFjfsMfPEMcfLvQ6fVfGBXNykRXNT5kjHN56kUz5gd2z5oqNz5z4Xq51

jCL5QvKJYLXM+QbXIvcHXIAaOoVAgtfPZkA3KlejfJY8MBGb5VuzHQbfIXmMmxc2I0nKw8LiS2ffM/wA/IdQsJVOK8JVH54+J25CFEcFfvOn5KXNn5wczO5aRIu5+d0QFCFFu5N/I35BxS35syAh5u/Pic73MP5n3LeE33JlWicwv5UdMhW1/It2d/O9Q7MjGFqTGh5H9lh5/pDLACPIpgtgvD53/O9av/Mx5DEIAFUsFx5qTHx5YAqJ5FLFJ5F5

1nQcAup5Pt2QFuU2eRaApCA3vK3wmArZ52SFG4cqG55YGIIFgZKIFoExIFIqzsFMHFvO4vJ/JEjG8cH4B6BZyDl5vSAV5oQyV5GxVYFnRXYFWIE4FjO1UFOvIt5xwNG+xq27pDLIcp03xKJduNyockA8g4wE0A+gBlASHLwagSQ0Kp5SU4dyVPK3JCveIPWcAwPGpJl6MmA3wGe4nWH0EK+zfgNUAW6byVu+TfHu+56Tnovj2Lhr33Y5Unz8KOVL

mJlPF45ixNrh7v12uu70VuTcM2JCnLxhbcOSKKnONgc2BPE4xlJ0RxIcBsaEyuR4XzBqPzNuJT3j+lt2ygCwETiMmDM5LVQ4AicEVQ+oXdKDsH9FfSEDFMURoRYgrK+fxLNpn2ItpQJMRuNtL/+6AGDFFEADFaimCyJ8PG+luMwZKjyEuVb2cp/4A8gmMMrAFAFMgmnzW+EgHc6K2gTiYwGzA9pQqUkwFFqhgiEwBn1Nsk8NXAGeSlU/NQWA5hTj

hl3iYRQxKpgwmDzCXVlHFo4roS0CNmu7JNy6SotTxZcLVFT2WXw4omK6gyk2uz9OWJ7rOh0v7I7hVZXO8fcJ3CZjOPidooewp8jBZFDwA5DIku8noqny+nKbkXv1Hhz70cpQNAwZn9LOS9lMZ0/yixggKmR+FwHiABYnl4PIHpFNMGIAuYNwAG4GbA2ACNs2AGmANJDSZciAxUWoGWSV3QH8N3VVhRCJmAktj6g5KkqAWiwisGlWqAhAErAuAB98

+gFW+cv3W+GYN2IVdGPC2UEyU12iokGEA3k2hXlwrayvg1PkpEO8F9SB9Ppg9MBs83lTKsqVPlFKtUVFbJMyp73xXeXHI1FwRS1FBVIie/HM3FW6OVhO6IlJJeNc6ynJyqksHcqKgg3SOdkHWkDLLwnwAqgxmHzZ/7LdFXXWe4W8h9SPopOwTfQUgN0lOQaAG+2bi1CoKJUxW1EKkk8NSGkBxV9uPXM/AivQgWFIwcawQCgcR+UOMO6mgC+AQCIu

SELc0AT6Y2IHEY3E2RkXdW/yc7jHqE5EFm96E4IKmR7g2lGzQYVFIAf83aiK1O8I0Q0cAC/yym0oxhWHACb6p+ytGTDjKOTjVyQeOTcaXD19ImUPYhbkraBwU1XwzLEgp9eiFGTwL1We5Eyl6FDkJWkVmGQUoCIQUqogkjAilXegKQn1VWOTwLnWKejpAwKELci0tuaq5Ch2V+Q/Asdy1Gm0vP0qmVXwSujtCdLCORz2wgAzqHwFxM1/xoukOY9e

kalwKF5Wljk3wr6C3GyZBEIYk3o8hKxOl9Uz3QO0qNITfTngU9kC5SOztCfyC9I2gE6lLgCqligxIAa1IaleORDozUpNg/IEN67Ut/qMMoVinNBgI/4QNYA0tP8bU3xxMyDyGZC0CloUrtgG/TBGbpJ9I8JmLJEAHCaNrhClazw75DaHmqNMtKioRHSOIdH2MTMs48TmzWl80qpl61TBG1rx5lDMtQAgAFByOaUoRQ9iiyozZ0yqEAMy/mWRxQWV

7SoIAHShWW0y7mX0yh/CMykghqyxKVxyX/FOEE6W7bXRg5vN86yUV6UJDM3qU49mkrOCFDRzShgH2OhijSlMieEqgnpjWCDIgOdYqZHMaSzZwDIyEGVlNSN5pIKwIzjOVbK9CTL7FAYqIA3ZCpIJ8BN9XchaOau4cARNwSjIqTHU+Qls09FJuEMo5VEcgjpHRoD+ARNxv1bHGy5K/Qo02yVKwE5BMARyXd1BXEuSk6luS9yHjITyWJkP7Y383yXn

Q1hZFwSmUsysKWzSoWX4GYsmjymKWhgfaUJS8mVJS6OWDORTZ3UkFYjSsFCutPJDgwPKWDkQqWdLaTbetX1rlSqwKVS4OXSzM3q1StmYNSpqUtSu45tS76EazE2XdSkJh9SoJiEygFBDSh0YrywcjjShAaTSoeUzSisCyy1tCHS5aXPkWWUbShWWnQwGWxS6eV7ocBWA4XLGnS5aK7bdST5kfYzXS42VdS91j3SvtRBMJ6VRAF6Vnkd6WWIr6V9q

H6XY7YuX/Sy85+CF/nAy0GXmkcGXvsW2XQy08YyjY+WwrHyYIyguVpHJxrIysICoy3sDoym+VZQ7GWlQ8I74ykdgvyqADEy1ECkygKVDykWXE1TmU7MJWW8yg2XMygeWsyl3QcyxWW6y5WX6y1WWUgABWJyTaXiyvWWj1GWUTywZybSnWUXkUxWqKgWVQKzWUkWbWVcymxW6KvmWGygxWzy++XusM2UwEC2WIsK2W3nG2VnkJvoOyuOkN6F2Xvy9

2X5SmxiUE285N9X2WMsZjKBy6FasKjgChyn+rnPCOW34KOVR1GOUFbOOWHFWkKJy58ZAQFOUPI30hlyqOYQrIqS+3U6n5yuVhjoIuUnS1Uzpy8uWp1Ceoeg1pAMQZ7Gv/I2nv/RqEXqZqHM/HeHW0veFJi0Ppm9OyWZAByWJbZyUry1yVh9duW3nNdrdylYVS6fuU/y9RXDy/+WjyulCgKwZwOK+KXMhLxWjneeXUGNKV2y0KgEANeW5S9wD5S7e

WTDXeVX4feWBC2/BHy7yZny60YXy4FCoy1qUxCrGWnjX/GF0R+WlQ5+W7bN+WOkD+VjS42VbK6aVsyuOQ6BBaWwKg9ogKixXyy5apLS/SSQKqeWOKmBWYqg9jHSmAgUKpIgXSyXZoK05WwgrZhYKx6W5IfBVvSnEAfSi6FHSjSI/LchWxDAGVUKzrY0KlZjlTH3YnOGGUsKvRYcKxpXCobhUoytxr8Ki8CCKjqWnjHGWRMPGVbMAmUQqxwIyKuOQ

TSymUsTRRVKRHRUqK/RWCy+FWaKyaraqwCI0MWxX6qwxXIqglUmKtxWp1cxXRSyxXOKpRW6qlWUeK9WVxSrWUEq6xVmq21UWqylWmygErmyp4GWy75B0XDDiPnEJX2yi1rhK/FiRKqFXRKj8hey+JVm9RJX+yuAApKkZBVSjJW44LJV/+HUb9zPJV9jWOUPcngLFTJOVlKs3qpymghtK6pVJyOpV5ykVU6g5pWFtQ3g1qjyIdKyuV7OVIgd0o1Zd

0uylWdWMEx7NGFTwHgDDgMyD6AFEDVAGS7Icl+6iArMEH7cXqnEc8Ug9Yhm1i/ri1lKrDA9aKnHUCvZdWCiRI9HMQUcmGJMkgKr4gSg7W/USW3pG+kLi1a7IPPKk/fbUXro4Rlv02J7rE5cq7okvHJ2U0XnXeK4lCKNY6iLJ4J+afI9GW+Cj5EyWuix2HmS2hqfeG8X/XYdZdQ3aEX7AD4f7EwUCPJCnlnBn4xigElfYjCljKrCm20z/a37PInww

rMVKPHMUxgvMUIkgsUSADgAUANyAh5CgDKAQyr4NAx7lQAWD6Qb0y2IA+BrKNx7ZhCFQt0PIKbpXWwOVfQTU+EcUmXd6Lr7Dhr8fQSXK1PEDnqrRlXq+cX5dURp8dHjnVwx9W5459X549+lvq8UlY6b+lTpdSU7i/wwZhFTj0cxrr0wFxIKYZVk6S28Xakxcw3E7cHPcawrBGayWvlbupekNoZlHQ8nUITJASebwjdbYsbWAbzVpHXzWggfzWVOQ

LXyvX4lsmSQXm0kZUso4EnjK7QmcVTzUha8yQ+aril+anCBCVSElKVbMXINCjU4fKkX9yCNk8AYGAESIwBk3Zt6zqzhTZ5GxBrgdyo5Qfb4NgOPyXo16LSpGfwlhH64ZQVfZ18DXAyiiwSya5DbQIBTUZUpTUccm9WqanDaaijTWyShT5CMna44IwTmNwkwFoS336k+aqnAMlySCYRXiL7OiBNU9XhJQOsrA8dNRN4qz53owzkXi6nyNgSQHua12

gYjebTogO8CN9NTJyQR1YtRREBAQGUAaQQRjvDTOAIoUyCOgFyDvDBRh45JFUIAPHIKMAADc7pSe1w4Be1b2qaAH2t24X2vmkv2v+1gZKB1IOrB1EOsil0Orh1MWuUJ8ZlNp8WtjFiWqtpyWvw1EyoR1SOtSGKOs+139gx1f2rkgAOsggOOtB1+THx1wssJ1+WtPuZ8PJFZaPzFFaI0eWoSY1d4A4ATQBdWM6tY1vACYabeHr4Y1kB4DnkFg9hne

i+QVlSgLO3V5e2uAauDapCLKrCsgOG1J6sYSZ6qt+imqHKqopU1Oa2lhfJKNqgjO2ug+xEZHrINF62sIRvvxq136un2NVNU46fk0EjSSKqAmxKqB2nlZl6PA196Ju1LmqbANlwe1Ym2Z16ThKVF5FS04zEilmjBA49lGP+i4wy16fy8lNxV2Q8knCaMtG62Ceo6FyevYId/lmRBrD/IWeocIbQ2L5aZCS2BetXIRepZohtIPqAypQppcyg+GhJZ+

6r0ke2FPiQpevEcPpBT1levT1/TEz1JSOz1GcvMkDerbGMxWb1ppFb15YuspZuIjB0JMF15GutxLKRF1pRKngODgoAU6vASuECU5surZF9Ws2+B2nOIca1aJpEnqsxnE20bG0k4hHNY0a4nOI1l2r4mLKgeDHMnRTHJE+vfG4ZrHNt+Kosw2XJLEa6mtXRmmrdZWD09+a2tfFH7PQAW3RWC22oEONyVXAY133FTCl41+koFSTzPlZ3WudFdD0j1Z

ksKuFkvHePwDj1CWg+JT5lxFiqGnWNBo1WGvL6QaGv6VDUK71TUJ710gs5BbKIUCYJN4evczvQzBqLehaPIB5uM314WW31cJNG6VGtF1OVFqAODhRAwjFGApADkgv9PP11Ys0uQXjmAanHwoPIv4BmV35whHSPCbwF7oTWBI6MmHpEm4n7o6RWM+5jIVqI2qFh3fHPplusk+YBozxEBudZUBoW1rvxfpxVJ01r6qUlGxI/VSBpmAMut2J5oqLABF

HUEUaxzsEDJVJvmh+ue8AY0Eeuu1pBrKeIor91r6IPBTxPiQKYuiVSW1SlKeuQVpgQXOQzFZwAihZW8jhsRugsqNf5GKN9qOyQ2+kJxC+qjpVavNQa2zEgUSJ6Ag4AL68SAkYsZBWiGjjeQDssGkKjicGgW2r6AGDEg+xlwg6IEdAAFTRW36FlBMfM3weEQnQ6RzmNCxtHqoaHw8oxsVYV6GgCU5L7EwemSxIhrmEYJz4R+RsBQhRoXluWjhcf5E

hp5Rq1kysCqNgiPMWFRteN9RvYIw+m7aYkGaN3rUb1i+oqVy1DrVOEF6NVyH6N84EGNIz2GNVqH2N77A0pGmSmNYRFfAsxvmNixoJUyxpTqqxvC++OI2N6Ju2NqdV2N7GQRNQ0msGxxrjAfBm2F7er5kneuEeWGtMygJNw11Oo1eg+q9gIYuRKdxuKNOHCeNtRteNIY2qN5yP5N0lW+NyZF+NwQKaNCQsBNrRsQc7RtBNXRsi1UAAhNMSIGN4UU3

wRqBGNFrSZkMBHw8XiExQMxptWGJtVm2JpO2FSLWN+JpnAmxoxNOxuxQexu1NBxpcWlJtON+rXON6N3yJYe0KJQuuKJe+upFHkFqAgoBqJbkFqA+ZQ0NZnl2IBwHlJP0XFU5En9WQeLu4sZlygWUAHoACPdwGvwagpImTNn3koSP+tIO/NynFuqh5AouChU1rMvptrNANK1xm1oTwfVPhqWJLeQE5+opCu7uuLxoRpXiqBqjUdMHYw2tkPFtCIMQ

F72PFNCm1s5Sk6u9mqu1rCN1J2P0yNWiGyNxpKeJzNn8277Mv285pmZrBo717BoZN5Ouw1cYpZNCYpS1cguXNi5ozFP+1I1MJKkNjLPhJQ6sRJ6ABRA9AHRAkCXo1GsNq1cut2I6CTTU70WyyZwH9Wvqz3p+FBUEx2RwNOuuIQ4XiqgyP2riQeP+AucMbxUCJS6p9OgQRZvGAJZtcNpcKm1NurWudur45S2ud1L6rwRQRvfVKktCNZiWM1qjWegN

JBTUHwCbWnmh7NS4N3CfMMUwROlSN45rbxzmqr2TjMzAVBr/ymiOUY/kKVQmIq2KSiNfA4zWFa2gGuNkcnUiNhMje9gCmE/OWOpOIBLcZYBmZHvKWg6DlNIAyEFBH2x+aIprrQ3LHV0WXNqibABKQYqGfmN5k8sFrUEMDHmtexLVYslCuLYSpugwLfPDQfbFDJVcn8aLAtBK/pC9GJsh3ANLDSIr5hRplDDheqW30kLIBBKazH4tprSEtIlt7sYl

saYffy0Ay3OGK49jktTAAUtoaCEhylonQGsDUtFr2eNXiBIIsrGKiMETKF4wklIRlvgsJluWk/msHY5ltCInW38swlmYYl6Ak8KkHsteKEctXcvi+PFpCtnRXctr80cwl6B8taIF6VTxXQ14gsw1m5qZNOGpkFiYtS1dtJMo3ZFOhwVpV5LrDCtglrCAwlr9FqYqit9FnEtXn3itiuUSt77AZcKVosFSlsDAGVszOygBOBCFBytCKFvsdoQKtg0W

P5JVrscT4HKtfhDMt2+gsttbSstRbEatlTmat+QtvskqJS2J9kWtWItbICAA8tfVp8YA1vfsJIr7VUYLPNFIovNTlLkNtnRcgMMA0g9AAMFEcTURK2gokJMJ86KbKFg1lVSgB8GqoOti3pZWU7FKuF+Ab8Bgl+HOOy0mosEwPEjNymAyueTzjhpuvmo8FsQtE2qt17htmJ3JLm13hqfpjuqwRy2pd1CtybNCBo21JeOgO6kq1hzwCAZaBtQ5dyUS

uTVKLAZ6N0aObN4lfXU6pMfx1JTFr1JIotc0TospFY3RyN3pus6HLKngFGCWAQgGBgUADngdtSfNGhU9FwXgcKV8FzBsjJSUtiFBiRHUqsvqSwygFuGuqwDGAnJSuA7Vwb46qTlFcmt5tfv35tbhsrNtuvvVMsOgN8ktgNrupltYpK/pCnIQ6RFo1uekFX2b0W4wOdltFdCNqEK+2W6o3lvRLeMYtLRjtKlRSSguIhnhVtoJ+6AFMggoDR18BXdK

Xdp7tTwSUJI1qjFcWu71aFLBqfevahj6gmV/duEKi62I1CjxPNW+qK11uJg5uAGqATtotgMAAiZ5EvdxX63GMcQDr4m2mbAZxH2+fIsCMtOjs8TYGGASPQZh5eyIaswH2Anhhlwr0S6SwwEcNsFuElLHNnFUxOvVqFrvVfDPTttZp1FQpMMBaxNwt+ms7MCnNqJhdtSexxFFUfVgotyND7RCRtyKndA0a9PlHN9dqNtjdq8BpGgtKZD2T+O+SloT

fVnt8BRaamIE3mjSxhlaIUMtzSH6GXJxrGCEycGRuzvM0LGXQbJ2xAyBCoutoSGY74UQIyYFtcZfzGe0QyYWU0TVl8lDCw1ZFzIBcEGQCgDCAzEGIAefW7tc9rOhs61nQTfUNAA0VUtklLVWYgEKlscoca0g0utQcu8mMoFkddsHik6gDvlxsvMdImTqBu3EyA0SMjIckFwgu3GKYdQJlA3vijIUhAgIjTGr6ALRpxy1UAAyYRRkejzKW/AArLea

qCgQUB3gYFGRkOAgEEMwJrOd2W283wBbbSSz+Om57NMKJ3rVUJ2RkJUW5OqBqfHRI4NoEapMAd9gxOuJ2YRQNCdMWZyAQjRWDIGyjEzZsgN3SSLSANADGsfh0HoCgAWOjz5W6Ofk3GulyrksIBvMbJ0cXPp0ubQ/Shgy84RMX0Zg8nIAfKk+WseFPkfgDoqd9UXyD8pKHXbGx0cAWOmZjGuQzqWSg2uO1xOOtq3WASTJpIWSDAom6RmBVsisQJv4

OOdJ2SAZ0mDLHqTySKp2UBN1wuMVOmGgPVr16JZzf40YH75ZUb1IOthIQ4oYsBUMhsZFwj5gQqW9/SkA1IboBMeW8429QdAqzBMhm9WDF5bAL4S5PVab4T52YRUFBN9ItLBfLtKFS8EHNqWJ1fOmMgqxFWYvMVxblkqHbEus3rdMi0CSMQqU2OPdD/KRewnOhlziDHI6pKsx1axGYUH6dyS7O6TFC46TFR1aTFkOz2CzYyTEsKpV3Ku5V2KulV1K

utV3qulhUKurGZsuMZn0AcZDSYqWWr9aTGAAGXITXSUhpMXY6X7Pq7DXagBzXcTUjXRa6OANJitpAVJUAK66kUM4BewDi5ZkA40gINJjHHbqRsAIGhsQH7c0UI6A2AK9rZsZmq0lbXLATor4jFuiBQgNwSV7MYF+7aHyDrduxA6e00oAIjY2RpOM+rdMbXwLJEtTcrBQto/ihxnhYrUJGTGHdwRlqDXKzenK72aBQ6LxtQ715jIi6HdYwGHXo6EA

Mw7/Ph6ggOBRcuHS6AeHV0652LswhHZHERHbRCKyNkAJHbsgpHc0denURkIgAo7OAEo6vxio74CmzMi+ho6tVo5EdHU3M63fo7mHYY63JlSolnWwrrXZY7oTbs7Zhje74QY479AM47XHe474QV478HJGRfHTigxnfzkinfNV8neE6DwAB7CXW4QEnVc7knfmx8IZcK+xHDJf3apBxnSXUgnYB6oyIU6UPWy7SnRkhynX6SwPdCK6nTvhc/o07wgM

07lFlQxfUAhhOnWBxunVcgV3d7dPPoM7I5EEwRnVk7hinR7oRbX8eIaKdD2MtSr3dVKzeis7lees6Wmps6HUNs6G5TDL9nd/VDnR+oYDCc7CWmc7JURc7+1Ek6bnYp6v/FuNUAd5bYPSopXnVnIPndS6and87ECL87sPM1FaefWQgXViCQXW5iVdBC6BplC7xNrC6WAPC7hMoi678ABD/wmi6NRpi7sXURkakHi7nOVS7qncFLSkCS67MAUhyXcw

7KXXh7aQnS6OmKJZGXXKdmXWF7WXSU7ypZy6zPfyg92kEw+XQNENFqY6T5R9svuWK6ukBK6hcR665VrK7t3fK7LXVq76vZq6tXY16mvZa7dXau0QgAa7Kvca7HXfa7nXVa6LHXOtpmHa6HXZ9UnXY67WvW66qMp66mAN676HH66j8gG7ELuDB5yKG7HmoGhI3dG7CvWwrTfBBNFeh31k3XGBekGm7g9Bm6p+Vm769Dm7wYPm7CmIKEi3aiasath4

y3aKa4KCbznCWZZZkLW61VlOIJoENa6oWwbkKRuax7VIKJ7aMrWTQPrbaaQ6avS26DnlQ6QgDQ7O3SVb6HfEcmHZ30B3cJYh3Zw7ZaXGdeHcMwXGII6MZTO6xHfO61tou65gNI72PWu7p3XSBlHQPb2aLu7aWvu6tHbLypsCudjRn26z3QUqjHb1s+PU31H3VY7JAPe7zpgN6HHep6Pmm+6PHUbJvHd+6DUH46/3R2kAPZNUgPXo4InaB7DPeB7E

ndc7JUWhQ0nXB7FUKM7EPfzlkPR9VPqvk70Pcb6Fqul6mDDh7KnWr78PbZJCPTOBh5SR70FRwBWnYihKPTj6aPTI7V3Yl9kxptafbix65fYCdJnePcuPbM6N0Lx6tvfx7BPRsVhPW16xPVa1dnVJ6R8TJ6Krcc6BZac6X3ec7NaBr7okbc6aXQ87+rTp6XnYC5EXquRYvcZ6D0KZ7/nRZ6z8FJ5gXQAVQXXZ6WXRbBHPTC6Jpq57zACiAkXZ56tm

N56MXWUq/Pci6yWnyx8XTaTbfSy7SXZF7vYBS7cQRX7aXQUh6XYl6aXEy6/BCy7MPRl7+3Vl7GPBS48venoJBlH7efSK6ArOPdyvVK6qvbNIofXbAFXfV6mvbf7nAM171XTq7NnYN7OvWN7Rvb17xvS66jZAN7bXZV6RvetV3/YAGJvQNjE5NN7SALN7fXWHzFvUG6VvQn01vRG6o3R67D/VMq5fLt6k3Sm6jvYOh03d3bM3RA4DjWS4jzJWM83U

QAbvdfgLuMW6HvQ8B4TRYx5pG2RXvdW6PvZUc6HN97KQD2rQ9gVqyNSvaRtBpVIDugoPICiAjgF+qWRfL8zPMj9sgosAGoA3wzSruI1xNn5EfgVAxrK/qe6DF1VwKLgrtBg6hYJ2UoLWazE8WfTADUhbr6cprs1mha07fbrpyphaFYWA79rh/Tc7fJz0Ja7iIjRpKKfEyJeYVgbmSBBbcDXpBQLTQ04fmQy0fu4CG7YHw7Svg78DinDP3gDcTsM+

7nHc+6+Amy6+mjkBR+pWNepX06EQZlJ5uTf5EAoAFvQYNVRfaGS3XoS9LnaBploJwR5ldEqAAg5YSpYehiAGoxsXFchNSM+FcQXuZ9WmjTXyL6Nl7ErB3LEst/dpr0IMcZCccW47TnDe7nALhAFLVTlZkP31vfEkHgPFow1ULn9yAGNSdyVRi/COx7TMReBIRbXzxCIOh2Pc4B2dvI4w3ZPYjjZcgJhZ+ZnJax6ZqRe6a2BIwKwFM6nZAmQwQt0g

mojxENTdR7vfYMhTnE0BnnfXo8PWgAQZYLQFPVn62og+T5aFUcAUHmwNaZGQXwABoEKDY4spPUgxkE06X/BBiUobBA45LsbnnXBEw9IgQdQuq5IPcCjSCYChNsG8gQvR808PYC19+aZjHZQh6AnX+xVg1qMXdCPrN8KsGsgPCGqcSI5zkZDCyMgqhTnBv7DFl8x8vRIMsuQTytZOf4X7EHRgvV86G0FIRTqUqLNRjk0N8MTlBliaFypbeZ2AGVKq

oVkBBvopsCkDy6oPPb63kER6nfeax8aKVaX+a0GQpoptJuTUsBCq+AeXRrQqmMCiDKHl8w7my58QpiwUadEH4nbEG/CPEHDQIkG0ABK0KfWkHP6gqtMg3wFsgySDv8FlJAQ8EBh7AUHoYa38Sg9/gygw+h6ApUG95dUHagxNB/WI0GaPM0GTgx0sOg1kAug+0hIAqsDs5BOQ33UMGLHSMGxg480MFlMG0ADMHO2JEweqosHYABPqVgwN73ubFIuf

R+Atg28GYcnsG2XAcGpQwagCw83Lzg6NjLg/SHJGLcHXpDQZhUE8GhjeO6KfR8Gvg0Ewfg18wIpACHokcCHXaRRBwQ5kRIQ6RBIgbCGWQ3kg2QwJEkQ2lNkQKiHx0IjZdfeIQXGDiG2DHiG2ogSHFUESGrUCSH6Brb7yQ60Hm5RHMpwxM6RMrOG59IyGMkMyHw7peHvbjYjOQ5PYxADyHLfRWBfgwKGsgEKGwBbboqkeKGK/WOHjg2zTZQ8fl5Qz

kHlQ0wZxGGqH3XllItQ+1ad/bU79QzW7HfTNKJLEGgBSKaHOtuaGrQYpsKSPXKbQ3RH7Q+wxHQxplnQyB43Q9yHaTZGKWQaPbODePbt1qD7dzTTqZrZ6G2oqdjb/L6HloEkHAw6kGugekHQw8xEIw4qHcgzGHZkQS8Ew8UGEiMmHz7CvKKgyQDp6i8rMw6ixsww0H/GE0H/1BOGJhishiw7+Zug2WG+g6uRKw4MHkZMMHRg/I5xgw2HTINMHchS2

HAIQsHgBZ2GWmN2GvnL2GL3ZiGZ5jWHhw5hD6w/hGUQO5Hz7CBGw+cFFwI5wB5wx5JFw48GUIuqbwZXw7Bw1BCpdRuGYCFuG/g3nr8/UCHy5CCGxAGCHUKMeGoQ2eGOmheGEQyR6bwxTJ7w+iGnwzvpsQ/wQVPZr63CJ+G+kN+HZkL+H9Jv+Hco1/UR8fr6aQ4OGrgwyGTuUyGBvf1Grw/qj5KNzBkI1SFypWhH9/RhHbzsKHsI2KHlPXhHaMuOH

CI1l05QxkTSIyhGG0BRG18FRHNQ+rpaI7qHtWCQ4DQ0xHBtixHoOPqwFXBxHaWhaGFKN0NskHaHhaA6G2ok6HCDFvd5HGJGkI/DaCiWSKkbeyzh1ZUBgYMwAPID+8PIBQBp1SIHKgCDTolB2KWkqAwH4BcAk0pWUt4FrZ23iICzSjOCZaiWFQHnvSSbdfBbxKldBxd4G3uArx2NsQkePtzb0qSnjf7cYGl0Z4aRbY/TBOrwzBSdprhSYEbC8cpKD

NQpyzut7qortHh14jrCTojtrvgB/D1A2r9ANUl0vA6WJrPCyR4MuuCxzTg7gg3g7YMp4YANU+L0GW+iNKsIxzII6ALYG2AjgArawzTHFDxHpwCdIfIadCHa79VvA1ddrkGqMOZ68K7DQ7bUJs8l1YVwKZ1h6LHbxYy4IE7aWbZ0SAb3Log9b1V98zAxhandVYHViTYG9NXnb0Ja6lyzO3DiLbQk94HiIKYVk8kHaqSx8g1B2NeGlV/Hz9hug7HmL

d1ZdBH4DwOR3bFCZfsh7f96MNaoTxrcxUOQZoSuQXIL+dafDJDdwGqrunRwAKrAoQEfk6ng6y0AI5BoAECAsgG0QOQIz0GAL9kShnj1M4xUhL430BMBCIB0EDcdMgJthmSbAjr44Ty742+Ez465dJtR3Eb41ERloPfH9ADC6TA3eqf42/GH43LGazS2Jb43/G3wo/H+SeLaQE9AnMgERj6zZsAEEzkB/43PBsLWgmoAP/GnwquspQtgncE98TYok

UBCE2+ETICfVSE6/HEE/oBtXq+zH2U1oyE5kB9vMQB6EyubZEA+yX41An0E2+F6EwBAgoFNAuE7/GeE5kB7SVkAiMVqBi8CqAvBAKBTuOFBslFnt5A7TB99vobpE8iABQIBk3sKJhmGgRQyrFQklwLVhsUtVJJBDvGTEMgY4QNVRGxZohmiEwn9AMgnsqllVQdHakSANzJl1s4niAMKAgqCVp3E7txsCPt4+2A3Z3E/cQ6cFZj6yBTHZ4LgBIyBV

AioOZ4Yk9Em0UJGasCs6Jw7hgFwk+SAok7MA0UJ/Ask5knnxBlA89DYnqE9GhDqJgm62FkIe8gpBVhLezUAHThsgAEmSNXbQDXA0nIAEXAD44vbIcLJA8Ge0nIAH/40QKQAiJW0mxvmUBek0wB/E5hFjYM3AbE88KEBYKAB5b4mPwGMnjLBxIoQDydGALI4sQP/TR6SowV7rXgM4GLoDAPwmyru3bxEAYBTUDsmGsF3IUInmVz5usn8ACUSrpcT9

MIgy8egI46AwH7k6uHl0vwDvH3eLZAgAA===
```
%%