def straight_line_distance(city1, city2, coordinates):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]

    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
