# The Torchbearer

**Student Name:** Adrian Serrano
**Student ID:** 132350007
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

- **Why a single shortest-path run from S is not enough:**
  _A single shortest-path solution from_ `S` _will only find the shortest path to one target, but our problem requires us to visit all relic nodes. Our shortest-path run isn't able to decide which relic to visit first if multiple relic locations must be visited later on in the path._

- **What decision remains after all inter-location costs are known:**
  _After all inter-location costs are known our algorithm still needs to decide what order to visit the relics in that is the most fuel efficient._

- **Why this requires a search over orders (one sentence):**
  _Different relic orderings produce different fuel costs, so we need to search over all possible orderings rather than perform a single shortest-path computation._

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

> List the source node types as a bullet list. For each, one-line reason.

| Source Node Type | Why it is a source |
|---|---|
| _Spawn (S)_ | _This is our starting point, so it is always a source node._ |
| _Relic (R)_ | _We must visit all relics, for each relic we visit we must compute the shortest distance to all other nodes as well as the target node_ `T`. |

### Part 2b: Distance Storage

> Fill in the table. No prose required.

| Property | Your answer |
|---|---|
| Data structure name | Nested python dictionary |
| What the keys represent | A node in the graph |
| What the values represent | Neighbor nodes from key node and their distance |
| Lookup time complexity | O(1) |
| Why O(1) lookup is possible | Python dictionaries use a hash table internally, so key lookups are O(1). |

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** `k + 1` _(starting node is the +1)_
- **Cost per run:** `O(m log n)` _for a min-heap priority queue._
- **Total complexity:** `O((k + 1) * m log n) = O(km log n)`.
- **Justification (one line):** _We run Dijkstra's algorithm for each source node in the graph. And there are_ `k + 1` _source nodes._

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  _Their stored distance is the true shortest-path cost from the source node_ `x`, _no other route can perform better._

- **For nodes not yet finalized (not in S):**
  _Their stored distance is the shortest path found so far using only finalized nodes in_ `S` _as the intermediate steps._

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  `S` _is empty, source node initialized to have_ `dist = 0` _and all other nodes_ `dist = inf`. _Since source node is not in_ `S`, `dist[source]` _is equal to shortest path found so far using finalized nodes as intermediate steps, but since_ `S` _is empty_ `dist[source] = 0`, _thus the invariant holds._

- **Maintenance : why finalizing the min-dist node is always correct:**
  _Let_ `u` _be a node not in_ `S`. _Any alternative path to_ `u` _must leave the finalized set at some point. Because edge weights are nonnegative, the alternative path found to_ `u` _can only ever increase the cost, so no other path is cheaper than_ `dist[u]`. _Therefore,_ `dist[u]` _is the true shortest path and_ `u` _can be finalized and added to_ `S`.

- **Termination : what the invariant guarantees when the algorithm ends:**
  _Every reachable node has been finalized, and their stored distance equals the true shortest-path cost from the source node._

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

_If any distance is wrong, the route planner will compare orderings using wrong costs and may pick a route that is not actually the cheapest._

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** _Greedily picking the closest relic can lead us to a node where any remaining relics are very expensive to reach._
- **Counter-example setup:** 

  | From \ To | B   | C   | D   | T   |
  |-----------|-----|-----|-----|-----|
  | S         | 1   | 2   | 3   | --  |
  | B         | --  | 100 | 1   | 2   |
  | C         | 1   | --  | 100 | 1   |
  | D         | --  | 100 | --  | 1   |

- **What greedy picks:** _Greedy chooses to go to node_ `B` _first since it is the cheapest, then to node_ `D`. _It is at node_ `D` _where we see why greedy fails. We are required to visit **all** nodes, so we must go to node_ `C`, _and are now forced to pay a cost of 100 to reach the final node._
- **What optimal picks:** `S -> C -> B -> D -> T` _with a total cost of_ `2 + 1 + 1 + 1 = 5`.
- **Why greedy loses:** _Greedy fails in our scenario because locally optimal choices do not lead to the globally optimal solution. In this scenario, the future cost of our first move is unknown._

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _Our algorithm needs to search through all possible relic orderings in order to find the optimal solution._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Lecture notes_
- _https://www.geeksforgeeks.org/python/time-complexities-of-python-dictionary/_
- _https://www.geeksforgeeks.org/python/heap-queue-or-heapq-in-python/_
- _https://www.geeksforgeeks.org/dsa/time-and-space-complexity-of-dijkstras-algorithm/_