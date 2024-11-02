import networkx as nx
import matplotlib.pyplot as plt


def visualize_graph(graph, path=None):
    G = nx.Graph()  # Use DiGraph for directed graphs

    # Add edges to the graph
    for node, neighbors in graph.items():
        for neighbor, cost in neighbors:
            G.add_edge(node, neighbor, weight=cost)

    pos = nx.spring_layout(G)  # Position nodes using spring layout

    # Draw the graph
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightblue', font_size=5, font_weight='bold')

    # Draw edge labels
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # If a path is provided, highlight it
    if path:
        path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

    plt.title("Graph Visualization")
    plt.axis('off')  # Turn off the axis
    plt.show()
