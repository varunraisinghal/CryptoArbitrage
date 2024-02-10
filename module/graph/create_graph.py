import pandas as pd
from node import Node
from graph import Graph

# Read the DataFrame
df = pd.read_csv('market_prices.csv')

# Create an instance of the Graph
crypto_graph = Graph()

# Initialize an empty list for edges
edge_list = []

# Iterate through the DataFrame and add nodes or edges to the graph
for index, row in df.iterrows():
    quote_currency = row['Quote']

    # Check if the quote currency is USDC or USDT
    if quote_currency in ['usdc', 'usdt', 'USDC', 'USDT']:
        # Create a Node for each row with USDC or USDT as quote
        node = Node(row['Exchange'], row['Crypto'], row['Price'])
        crypto_graph.add_node(node)
    else:
        # Add other quotes to the edge list
        edge_list.append(row)

# # Display the nodes in the graph
# print("Nodes in the Graph:")
# for node in crypto_graph.get_nodes():
#     print(node)

# Display the edge list
print("\nEdge List:")
for edge in edge_list:
    print(edge)
