import pandas as pd

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


