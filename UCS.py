import heapq
from path_construction import *


def ucs(graph, start, goal):
    queue = [(0, start)]
    visited = set()
    path = {start: None}
    cost_so_far = {start: 0}
    nodes_explored = 0

    while queue:
        current_cost, node = heapq.heappop(queue)

        if node == goal:
            return reconstruct_path(path, start, goal), cost_so_far[goal], nodes_explored

        if node in visited:
            continue

        visited.add(node)
        nodes_explored += 1

        for neighbor, cost in graph.get(node, []):
            new_cost = cost_so_far[node] + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                heapq.heappush(queue, (new_cost, neighbor))
                path[neighbor] = node

    return None, float('inf'), nodes_explored
