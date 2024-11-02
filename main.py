import time

from AStar import *
from BFS import *
from DFS import *
from DLS import *
from Greedy import *
from UCS import *
from graph import *
from heuristic import *
from visualization import *


def get_algorithm_choice():
    print("Choose a search algorithm:")
    print("1. Breadth-First Search (BFS)")
    print("2. Depth-First Search (DFS)")
    print("3. Uniform Cost Search (UCS)")
    print("4. Depth-Limited Search (DLS)")
    print("5. A* Search")
    print("6. Greedy Search")

    choice = int(input("Enter the number of the algorithm: "))
    return choice


def execute_algorithm(choice, graph, start, goal, heuristic, depth_limit=10):
    if choice == 1:
        return bfs(graph, start, goal)
    elif choice == 2:
        return dfs(graph, start, goal)
    elif choice == 3:
        return ucs(graph, start, goal)
    elif choice == 4:
        return dls(graph, start, goal, depth_limit)
    elif choice == 5:
        return astar(graph, start, goal, heuristic)
    elif choice == 6:
        return greedy_search(graph, start, goal, heuristic)
    else:
        print("Invalid choice.")
        return None


def run_program(graph, coordinates):
    start_city = input("Enter the start city: ")
    goal_city = input("Enter the goal city: ")

    choice = get_algorithm_choice()

    heuristic = None
    if choice in [5, 6]:
        heuristic = lambda x, y: straight_line_distance(x, y, coordinates)

    start_time = time.perf_counter()

    result = execute_algorithm(choice, graph, start_city, goal_city, heuristic)

    end_time = time.perf_counter()

    if result is not None:
        path, total_cost, nodes_explored = result

        print(f"\nPath from {start_city} to {goal_city}: {path}")
        print(f"Total cost: {total_cost}")
        print(f"Nodes explored: {nodes_explored}")
        print(f"Time elapsed: {end_time - start_time:.12f} seconds")
        visualize_graph(graph, path)
    else:
        print("No path found.")


run_program(graph, coordinates)
