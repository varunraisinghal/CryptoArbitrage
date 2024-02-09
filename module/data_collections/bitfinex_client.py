#!/usr/bin/env python
# coding: utf-8

# In[7]:


import requests

def get_bitfinex_symbols():
    url = 'https://api.bitfinex.com/v1/symbols'
    response = requests.get(url)
    return response.json() if response.status_code == 200 else []

def get_recent_price(symbol):
    url = f'https://api.bitfinex.com/v1/pubticker/{symbol}'
    response = requests.get(url)
    return response.json()['last_price'] if response.status_code == 200 else 'N/A'


# In[8]:


symbols = get_bitfinex_symbols()
for symbol in symbols:
	price = get_recent_price(symbol)
	print(f'{symbol.upper()}: {price}')

