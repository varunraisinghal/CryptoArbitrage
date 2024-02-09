from node import Node
from graph import Graph
from edge import Edge
import networkx as nx
import matplotlib.pyplot as plt


# Create instances of the Graph, Nodes, and Edge
crypto_graph = Graph()

# Example nodes
node_btc_exchange1 = Node("Exchange1", "BTC")
node_eth_exchange1 = Node("Exchange1", "ETH")

crypto_graph.add_node(node_btc_exchange1)
crypto_graph.add_node(node_eth_exchange1)

# Example edge
edge_btc_to_eth = Edge(node_btc_exchange1, node_eth_exchange1, fee=0.001, exchange_rate=20)
crypto_graph.add_edge(edge_btc_to_eth)

# Display the graph
print(crypto_graph)
for edge in crypto_graph.edges:
    print(edge)

# Create a new networkx graph
G = nx.DiGraph()

# Add nodes to the graph
G.add_node(node_btc_exchange1)
G.add_node(node_eth_exchange1)

# Add edges to the graph
G.add_edge(node_btc_exchange1, node_eth_exchange1, weight=edge_btc_to_eth.fee)

# Draw the graph
pos = nx.spring_layout(G)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, edge_color='r', edge_cmap=plt.cm.Blues, pos=pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()