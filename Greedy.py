import heapq
from path_construction import *


def greedy_search(graph, start, goal, heuristic):
    queue = [(0, start, 0)]
    visited = set()
    path = {start: None}
    nodes_explored = 0

    while queue:
        _, node, cumulative_cost = heapq.heappop(queue)

        if node == goal:
            return reconstruct_path(path, start, goal), cumulative_cost, nodes_explored

        if node in visited:
            continue

        visited.add(node)
        nodes_explored += 1

        for neighbor, cost in graph.get(node, []):
            if neighbor not in visited:
                priority = heuristic(neighbor, goal)
                heapq.heappush(queue, (priority, neighbor, cumulative_cost + cost))
                path[neighbor] = node

    return None, float('inf'), nodes_explored
