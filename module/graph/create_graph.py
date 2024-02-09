from node import Node
from graph import Graph


# Create instances of the Graph, Nodes, and Edge
crypto_graph = Graph()

# Example nodes
node_btc_exchange1 = Node("Exchange1", "BTC", 50000)
node_eth_exchange1 = Node("Exchange1", "ETH", 3000)

crypto_graph.add_node(node_btc_exchange1)
crypto_graph.add_node(node_eth_exchange1)

# Display the graph
#print(crypto_graph)
for edge in crypto_graph.edges:
    print(edge)