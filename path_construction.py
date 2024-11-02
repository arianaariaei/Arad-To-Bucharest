def reconstruct_path(path, start, goal):
    current_node = goal
    reversed_path = []

    while current_node is not None:
        reversed_path.append(current_node)
        current_node = path[current_node]

    reversed_path.reverse()

    if reversed_path[0] == start:
        return reversed_path
    else:
        return None
