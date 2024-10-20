import matplotlib.pyplot as plt
import networkx as nx

# Visualize the graph
def visualize_and_save(graph, filename="metro_graph.png", labels=True):
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(graph, seed=42)
    nx.draw(graph, pos, with_labels=labels, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold', edge_color='gray')
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.savefig(filename)
    plt.show()


# Visualize the transport network with weights
def visualize_weighted_graph(graph,filename="metro_graph_weights.png", labels=True):
    plt.figure(figsize=(24, 16))
    pos = nx.spring_layout(graph, seed=42)
    nx.draw(graph, pos, with_labels=True, node_color='skyblue', node_size=300, edge_color='gray', font_size=6, font_weight='bold')
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.title("Transport Network Graph with Weights")
    plt.savefig(filename)
    plt.show()
