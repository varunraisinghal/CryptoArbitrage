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
