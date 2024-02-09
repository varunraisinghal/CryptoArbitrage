
api_key = 'HQEyig9ozNbtx9o4oXlrMoZRVaoFP5NVN3MsyiKSkTflVBNIoFZzbDy4Kxhgz8w9'


import requests

def get_all_eth_markets(api_key):
    url = "https://api.binance.us/api/v3/exchangeInfo"
    headers = {'X-MBX-APIKEY': api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        eth_markets = [pair['symbol'] for pair in data['symbols'] if 'ETH' in pair['symbol']]
        return eth_markets
    else:
        return "Error: " + response.text


# Fetching all ETH markets
eth_markets = get_all_eth_markets(api_key)
print("ETH Markets on Binance:", eth_markets)

def get_all_usdt_usdc_markets(api_key):
    url = "https://api.binance.us/api/v3/exchangeInfo"
    headers = {'X-MBX-APIKEY': api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        usdt_usdc_markets = [pair['symbol'] for pair in data['symbols'] if 'USDT' in pair['symbol'] or 'USDC' in pair['symbol']]
        return usdt_usdc_markets
    else:
        return "Error: " + response.text

# Fetching all USDT and USDC markets
usdt_usdc_markets = get_all_usdt_usdc_markets(api_key)
print("USDT and USDC Markets on Binance:", usdt_usdc_markets)

