from node import Node
from graph import Graph
from edge import Edge


# Create instances of the Graph, Nodes, and Edge
crypto_graph = Graph()

# Example nodes
node_btc_exchange1 = Node("Exchange1", "BTC", 50000)
node_eth_exchange1 = Node("Exchange1", "ETH", 3000)

crypto_graph.add_node(node_btc_exchange1)
crypto_graph.add_node(node_eth_exchange1)

# Example edge
edge_btc_to_eth = Edge(node_btc_exchange1, node_eth_exchange1, fee=0.001, exchange_rate=20)
crypto_graph.add_edge(edge_btc_to_eth)

# Display the graph
#print(crypto_graph)
for edge in crypto_graph.edges:
    print(edge)