import random
from path_construction import *


def dfs(graph, start, goal):
    stack = [(start, 0)]
    visited = set()
    path = {start: None}
    nodes_explored = 0

    while stack:
        node, cumulative_cost = stack.pop()
        if node == goal:
            return reconstruct_path(path, start, goal), cumulative_cost, nodes_explored

        if node not in visited:
            visited.add(node)
            nodes_explored += 1

            neighbors = graph.get(node, [])
            random.shuffle(neighbors)

            for neighbor, cost in neighbors:
                if neighbor not in visited:
                    stack.append((neighbor, cumulative_cost + cost))
                    path[neighbor] = node

    return None, float('inf'), nodes_explored
