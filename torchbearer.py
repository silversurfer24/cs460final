"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: ___________________________
Student ID:   ___________________________

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.
        
    TODO
    """
    return ("A single shortest-path solution from S will only find the shortest path to one target, but our problem requires us to visit all relic nodes."
    "Our shortest-path run isn't able to decide which relic to visit first if multiple relic locations must be visited later on in the path.\n"
    
    "After all inter-location costs are known our algorithm still needs to decide what order to visit the relics in that is the most fuel efficient.\n"
    
    "Different relic orderings produce different fuel costs, so we need to search over all possible orderings rather than perform a single shortest-path computation."
    )


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    Returns a list of nodes to run Dijkstra from.
    
    TODO
    """
    visited = set()
    sources = []
    for node in [spawn] + list(relics):
        if node not in visited:
            visited.add(node)
            sources.append(node)
    return sources


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    TODO
    """
    # init every node to infinity; source node starts at 0
    dist = {node: float('inf') for node in graph}
    dist[source] = 0
 
    # min-heap of (current_distance, node)
    # if we pop a stale entry whose distance is worse than dist[u], we skip it
    pq = [(0, source)]
 
    while pq:
        curr, u = heapq.heappop(pq)
 
        # skip stale heap entries left behind by earlier improvements
        if curr > dist[u]:
            continue
 
        # relax every outgoing edge from u
        for v, weight in graph[u]:
            new_dist = curr + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))
 
    return dist


def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    Run Dijkstra once per source node. Result: dist_table[u][v] is the cheapest
    cost from u to v.

    TODO
    """
    sources = select_sources(spawn, relics, exit_node)
    dist_table = {}
    for source in sources:
        dist_table[source] = run_dijkstra(graph, source)
    return dist_table


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    TODO
    """
    return ("Their stored distance is the true shortest-path cost from the source node `x`, no other route can perform better.\n"
            
    "Their stored distance is the shortest path found so far using only finalized nodes in `S` as the intermediate steps.\n"
    
    "`S` is empty, source node initialized to have `dist = 0` and all other nodes `dist = inf`. Since source node is not in `S`, `dist[source]`"
    "is equal to shortest path found so far using finalized nodes as intermediate steps, but since `S` is empty `dist[source] = 0`, thus the invariant holds.\n"
    
    "Let `u` be a node not in `S`. Any alternative path to `u` must leave the finalized set at some point."
    "Because edge weights are nonnegative, the alternative path found to `u` can only ever increase the cost, so no other path is cheaper than `dist[u]`."
    "Therefore, `dist[u]` is the true shortest path and `u` can be finalized and added to `S`.\n"

    "Every reachable node has been finalized, and their stored distance equals the true shortest-path cost from the source node.\n"

    "If any distance is wrong, the route planner will compare orderings using wrong costs and may pick a route that is not actually the cheapest.\n"
    )


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    TODO
    """
    return ("Greedily picking the closest relic can lead us to a node where any remaining relics are very expensive to reach.\n"
    
    "| From \ To | B   | C   | D   | T   |\n"
    "|-----------|-----|-----|-----|-----|\n"
    "| S         | 1   | 2   | 3   | --  |\n"
    "| B         | --  | 100 | 1   | 2   |\n"
    "| C         | 1   | --  | 100 | 1   |\n"
    "| D         | --  | 100 | --  | 1   |\n"
    
    "Greedy chooses to go to node `B` first since it is the cheapest, then to node `D`. It is at node `D` where we see why greedy fails."
    "We are required to visit **all** nodes, so we must go to node `C`, and are now forced to pay a cost of 100 to reach the final node.\n"
    
    "`S -> C -> B -> D -> T` with a total cost of `2 + 1 + 1 + 1 = 5`.\n"
    
    "Greedy fails in our scenario because locally optimal choices do not lead to the globally optimal solution. In this scenario, the future cost of our first move is unknown.\n"
    
    "Our algorithm needs to search through all possible relic orderings in order to find the optimal solution.\n"
    )


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    pass


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
