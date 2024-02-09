#!/usr/bin/env python
# coding: utf-8


import requests

def get_gemini_symbols():
    url = 'https://api.gemini.com/v1/symbols'
    response = requests.get(url)
    return response.json() if response.status_code == 200 else []

def get_recent_price(symbol):
    url = f'https://api.gemini.com/v1/pubticker/{symbol}'
    response = requests.get(url)
    return response.json()['last'] if response.status_code == 200 else 'N/A'


symbols = get_gemini_symbols()
for symbol in symbols:
	price = get_recent_price(symbol)
	print(f'{symbol.upper()}: {price}')

