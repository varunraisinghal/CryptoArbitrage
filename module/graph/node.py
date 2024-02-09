class Node:
    def __init__(self, exchange, cryptocurrency):
        self.exchange = exchange
        self.cryptocurrency = cryptocurrency

    def __repr__(self):
        return f"Node({self.exchange}, {self.cryptocurrency})"
