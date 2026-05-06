# Development Log – The Torchbearer

**Student Name:** Adrian Serrano
**Student ID:** 132350007

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – 5/5/26: Initial Plan

> Required. Write this before writing any code. Describe your plan: what you will
> implement first, what parts you expect to be difficult, and how you plan to test.

_The goal of the program is to find the most fuel-efficient path to all relic nodes and exit node. My initial plan is to implement Dijsktra's algorithm to map out all the nodes in the set. In order to find the optimal path, we need to search through k! relic orderings possible, as different paths can result in different fuel costs. Doing this for even a small set of nodes would take an extremely long time to compute, which is where pruning comes in. A baseline best path found will be established after our first search iteration, and all subsequent search paths will be compared to this baseline. If at any point in a subsequent iteration the path cost becomes greater than the current best path found, it will be pruned, saving us a ton of time in searching for the optimal path. This recursive search and pruning will definitely be the most challenging part of this algorithm. And I plan to test my implementation using the provided test cases._

---

## Entry 2 – [Date]: [Short description]

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

_Your entry here._

---

## Entry 3 – [Date]: [Short description]

_Your entry here._

---

## Entry 4 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | |
| Part 2: Precomputation Design | |
| Part 3: Algorithm Correctness | |
| Part 4: Search Design | |
| Part 5: State and Search Space | |
| Part 6: Pruning | |
| Part 7: Implementation | |
| README and DEVLOG writing | |
| **Total** | |
