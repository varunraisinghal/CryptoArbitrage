#!/usr/bin/env python
# coding: utf-8


import requests

def get_okex_instruments():
    url = 'https://www.okex.com/api/v5/market/tickers?instType=SPOT'
    response = requests.get(url)
    return response.json() if response.status_code == 200 else []

def get_recent_price(instrument_id):
    url = f'https://www.okex.com/api/v5/market/ticker?instId={instrument_id}'
    response = requests.get(url)
    return response.json()['data'][0]['last'] if response.status_code == 200 else 'N/A'


instruments = get_okex_instruments()['data']
for instrument in instruments:
	instrument_id = instrument['instId']
	price = get_recent_price(instrument_id)
	print(f'{instrument_id}: {price}')

