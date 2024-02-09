class Node:
    def __init__(self, exchange, cryptocurrency, price):
        self.exchange = exchange
        self.cryptocurrency = cryptocurrency
        self.price = price

    def __repr__(self):
        return f"Node(exchange:{self.exchange}, crypto:{self.cryptocurrency}, price:{self.price})"
