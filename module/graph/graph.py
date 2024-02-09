class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, edge):
        self.edges.append(edge)

    def __repr__(self):
        return f"Graph with {len(self.nodes)} nodes and {len(self.edges)} edges"
