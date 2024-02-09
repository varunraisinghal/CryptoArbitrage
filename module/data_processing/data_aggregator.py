import pandas as pd
from collections import deque

# Create a DataFrame to represent the graph
graph = pd.DataFrame(columns=['Source Exchange', 'Target Exchange', 'Source Coin', 'Target Coin', 'Fee'])

# Add edges to the graph
graph = graph.append({'Source Exchange': 'Exchange A', 'Target Exchange': 'Exchange A', 'Source Coin': 'Bitcoin', 'Target Coin': 'Ethereum', 'Fee': 0.01}, ignore_index=True)
graph = graph.append({'Source Exchange': 'Exchange A', 'Target Exchange': 'Exchange B', 'Source Coin': 'Bitcoin', 'Target Coin': 'Bitcoin', 'Fee': 0.02}, ignore_index=True)
graph = graph.append({'Source Exchange': 'Exchange B', 'Target Exchange': 'Exchange B', 'Source Coin': 'Bitcoin', 'Target Coin': 'Litecoin', 'Fee': 0.015}, ignore_index=True)
graph = graph.append({'Source Exchange': 'Exchange B', 'Target Exchange': 'Exchange C', 'Source Coin': 'Litecoin', 'Target Coin': 'Litecoin', 'Fee': 0.03}, ignore_index=True)
graph = graph.append({'Source Exchange': 'Exchange C', 'Target Exchange': 'Exchange C', 'Source Coin': 'Ethereum', 'Target Coin': 'Litecoin', 'Fee': 0.025}, ignore_index=True)
graph = graph.append({'Source Exchange': 'Exchange C', 'Target Exchange': 'Exchange A', 'Source Coin': 'Ethereum', 'Target Coin': 'Ethereum', 'Fee': 0.035}, ignore_index=True)


graph['Source Coin Price'] = [50000, 50000, 2000, 150, 3000, 3000]
graph['Target Coin Price'] = [3000, 50000, 150, 150, 200, 3000]


def bfs(graph, start_exchange, start_coin):
    # Create a queue for BFS
    queue = deque([(start_exchange, start_coin)])

    # Create a set to store visited nodes
    visited = set()

    while queue:
        exchange, coin = queue.popleft()
        print(f'Exchange: {exchange}, Coin: {coin}, Price: {graph[(graph["Source Exchange"] == exchange) & (graph["Source Coin"] == coin)]["Source Coin Price"].values[0]}')

        # Get all the neighbors of the current node
        neighbors = graph[(graph['Source Exchange'] == exchange) & (graph['Source Coin'] == coin)][['Target Exchange', 'Target Coin']].values

        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append(tuple(neighbor))
                visited.add(tuple(neighbor))

# Call the bfs function
bfs(graph, 'Exchange A', 'Bitcoin')