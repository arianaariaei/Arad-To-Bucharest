from path_construction import *


def bfs(graph, start, goal):
    queue = [(start, 0)]
    visited = set()
    path = {start: None}
    nodes_explored = 0

    while queue:
        node, cumulative_cost = queue.pop(0)

        if node == goal:
            return reconstruct_path(path, start, goal), cumulative_cost, nodes_explored

        if node in visited:
            continue

        visited.add(node)
        nodes_explored += 1

        for neighbor, cost in graph.get(node, []):
            if neighbor not in visited:
                queue.append((neighbor, cumulative_cost + cost))
                path[neighbor] = node

    return None, float('inf'), nodes_explored
