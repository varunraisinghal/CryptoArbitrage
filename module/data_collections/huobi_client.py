#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests

def get_huobi_tickers():
    url = 'https://api.huobi.pro/market/tickers'
    response = requests.get(url)
    return response.json()['data'] if response.status_code == 200 else []


# In[4]:


tickers = get_huobi_tickers()
for ticker in tickers:
	symbol = ticker['symbol']
	price = ticker['close']
	print(f'{symbol.upper()}: {price}')

