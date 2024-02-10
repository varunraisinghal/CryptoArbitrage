import heapq

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, edge):
        self.edges.append(edge)
        return f"Graph with {len(self.nodes)} nodes and {len(self.edges)} edges"
    
    def get_nodes(self):
        return self.nodes
    
    def get_edges(self):
        return self.edges
    

    def find_arbitrage(self, start_node):
        # Initialize the profit and path for each node
        profit = {node: 0 for node in self.nodes.values()}
        profit[start_node] = start_node.get_price()
        path = {node: [] for node in self.nodes.values()}

        # Use a priority queue to store the nodes to visit
        queue = [(-profit[start_node], start_node)]
        while queue:
            current_profit, current_node = heapq.heappop(queue)

            # Visit each adjacent node
            for adjacent_node, (rate, fee) in current_node.adjacent.items():
                new_profit = profit[current_node] * rate * (1 - fee)

                # If the new profit is higher, update the profit and path
                if new_profit > profit[adjacent_node]:
                    profit[adjacent_node] = new_profit
                    path[adjacent_node] = path[current_node] + [current_node.exchange]
                    heapq.heappush(queue, (-new_profit, adjacent_node))

        # Return the profit and path for each node
        return profit, path