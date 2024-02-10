import pandas as pd
import heapq

class Node:
	def __init__(self, exchange, cryptocurrency, price, rel_value=0):
		self.exchange = exchange
		self.cryptocurrency = cryptocurrency
		self.price = price
		self.rel_value = rel_value
		self.adjacent = {}  # New attribute to store adjacent nodes

	def __repr__(self):
		return f"Node(exchange:{self.exchange}, crypto:{self.cryptocurrency}, price:{self.price})"

	def add_edge(self, node, fee, exchange_rate):
		self.adjacent[node] = (fee, exchange_rate)  # Add an edge to the adjacent nodes dictionary

	def set_edges(self, edges):
		self.adjacent = edges # Set the adjacent nodes dictionary

	def get_edges(self):
		return self.adjacent  # Return the adjacent nodes dictionary
	
	def get_price(self):
		return self.price
	
	def get_cryptocurrency(self):
		return self.cryptocurrency
	
	def get_rel_value(self):
		return self.rel_value
