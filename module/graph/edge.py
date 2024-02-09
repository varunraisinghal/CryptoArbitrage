class Edge:
    def __init__(self, from_node, to_node, fee, exchange_rate):
        self.from_node = from_node
        self.to_node = to_node
        self.fee = fee
        self.exchange_rate = exchange_rate

    def __repr__(self):
        return f"Edge(from {self.from_node} to {self.to_node}, Fee: {self.fee}, Rate: {self.exchange_rate})"
    
    def get_fee(self):
        return self.fee
    
    def get_exchange_rate(self):
        return self.exchange_rate
