from node import Node
from graph import Graph
import random


# Create instances of the Graph, Nodes, and Edge
crypto_graph = Graph()

exchanges = ['Exchange A', 'Exchange B', 'Exchange C', 'Exchange D', 'Exchange E']
cryptocurrencies = ['Bitcoin', 'Ethereum', 'Litecoin', 'Ripple', 'Cardano']



# Example nodes
#create nodes of every coin
node_btc_exchange1 = Node("Exchange1", "BTC", 50000, )
node_eth_exchange1 = Node("Exchange1", "ETH", 3000)


#loop through bitcoin add edges from bitcoin to every other
node_eth_exchange1.add_edge(node_btc_exchange1, 0.01, 0.06)
node_btc_exchange1.add_edge(node_eth_exchange1, 0.01, 17)

crypto_graph.add_node(node_btc_exchange1)
crypto_graph.add_node(node_eth_exchange1)
# Display the graph
#print(crypto_graph)

arbs = []
for node in crypto_graph.nodes:
	arbs.append("start: ", node, "arb:, ", crypto_graph.find_arbitrage(node))

