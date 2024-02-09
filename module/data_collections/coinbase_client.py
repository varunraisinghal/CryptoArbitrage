#!/usr/bin/env python
# coding: utf-8

import requests

def get_coinbase_products():
    url = 'https://api.pro.coinbase.com/products'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch products")
        return []



def get_recent_price(product_id):
    url = f'https://api.pro.coinbase.com/products/{product_id}/ticker'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['price']
    else:
        return 'N/A'


products = get_coinbase_products()
for product in products:
	product_id = product['id']
	price = get_recent_price(product_id)
	print(f'{product_id}: {price}')

