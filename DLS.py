import random
from path_construction import *


def dls(graph, start, goal, limit):
    stack = [(start, 0, 0)]
    visited = set()
    path = {start: None}
    nodes_explored = 0

    while stack:
        node, depth, cumulative_cost = stack.pop()

        if node == goal:
            return reconstruct_path(path, start, goal), cumulative_cost, nodes_explored

        if depth < limit:
            if node not in visited:
                visited.add(node)
                nodes_explored += 1

                neighbors = graph.get(node, [])
                random.shuffle(neighbors)

                for neighbor, cost in neighbors:
                    if neighbor not in visited:
                        stack.append((neighbor, depth + 1, cumulative_cost + cost))
                        path[neighbor] = node

    return None, float('inf'), nodes_explored
