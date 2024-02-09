#!/usr/bin/env python
# coding: utf-8


import requests

def get_all_assets():
    url = 'https://api.kraken.com/0/public/Assets'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['result']
    else:
        return {}


def get_recent_price(pair):
    url = f'https://api.kraken.com/0/public/Ticker?pair={pair}'
    response = requests.get(url)
    if response.status_code == 200 and 'result' in response.json():
        data = response.json()['result']
        # Assuming the first key in the result is the pair we're interested in
        first_key = list(data.keys())[0]
        # Extracting the last trade closed price
        last_trade_price = data[first_key]['c'][0]
        return last_trade_price
    else:
        return 'N/A'


assets = get_all_assets()
for asset, details in assets.items():
	# Kraken uses 'X' or 'Z' prefixes for crypto and fiat currencies respectively in their API
	# We'll strip those prefixes to try and get the USD pair. This is a simplification and might not work for all assets.
	asset_code = details['altname']
	if 'X' in asset_code or 'Z' in asset_code:
		asset_code = asset_code.replace('X', '').replace('Z', '')
	pair = f'{asset_code}USD'  # Assuming you want to get the USD pair
	price = get_recent_price(pair)
	print(f'{asset} ({pair}): {price}')


