# Development Log – The Torchbearer

**Student Name:** Adrian Serrano
**Student ID:** 132350007

---

## Entry 1 – 5/5/26: Initial Plan

_The goal of the program is to find the most fuel-efficient path to all relic nodes and exit node. My initial plan is to implement Dijsktra's algorithm to map out all the nodes in the set. In order to find the optimal path, we need to search through k! relic orderings possible, as different paths can result in different fuel costs. Doing this for even a small set of nodes would take an extremely long time to compute, which is where pruning comes in. A baseline best path found will be established after our first search iteration, and all subsequent search paths will be compared to this baseline. If at any point in a subsequent iteration the path cost becomes greater than the current best path found, it will be pruned, saving us a ton of time in searching for the optimal path. This recursive search and pruning will definitely be the most challenging part of this algorithm. And I plan to test my implementation using the provided test cases._

---

## Entry 2 – 5/7/26: Part 2a and select_sources() questions

_Working on part 2a in the README.md and implementation of select_sources() in torchbearer.py. I'm a bit confused why exit_node is included in the parameters. If select_sources() is finding the nodes we need to run Dijsktra's from, I don't know why we would need to know the distances FROM the target node, since that is the exit node. I feel like including that node in the sources would just introduce unnecessary computation cost, for now I'm not going to include it and see how the tests check out once my implementation is complete._

---

## Entry 3 – 5/10/26: Implementing find_optimal_route()

`find_optimal_route()` _is responsible for returning the minimum fuel cost to visit all relic nodes as well as the specific order in which the nodes were visited. In the case that no relic nodes needed to be visited, we returned the cost from the spawn to exit node and an empty list. In order to find the optimal relic order, we need to make a call to_ `_explore()`. _If a valid path has been found, we return it. This one wasn't too bad, toughest part was passing correct args to_ `_explore()`._

---

## Entry 4 - 5/10/26: Implementing _explore()

`_explore()` _is our recursive helper function that utilizes best-so-far cost tracking and pruning to keep track of the best relic ordering while quickly cutting branching paths if they are >= than our current best path. Realizing I had to implement copies to_ `relics_remaining` _and_ `relics_visited_order` _because they kept getting mutated throughout the recursive loop was the most painful part. God I hate recursion, it makes my brain hurt._

---

## Entry 5 – 5/11/26: Post-Implementation Reflection

_I am finally free._

---

## Final Entry – 5/13/26: Time Estimate

_Updated my time estimate table based on Discord messages but still not sure if I'm doing it correctly. Parts 2, 5, and 6 were coding heavy but relied a lot on my answers in the README, so I'm not sure if I was supposed to add those times together for Implementation estimate. I'm just going to add together Part 7 and README and DEVLOG writing and put that as the cumulative total._

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | 2 |
| Part 2: Precomputation Design | 3 |
| Part 3: Algorithm Correctness | 2 |
| Part 4: Search Design | 1 |
| Part 5: State and Search Space | 3 |
| Part 6: Pruning | 3 |
| Part 7: Implementation | 9 |
| README and DEVLOG writing | 13 |
| **Total** | 22 |
