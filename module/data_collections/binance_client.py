import requests
api_key = 'HQEyig9ozNbtx9o4oXlrMoZRVaoFP5NVN3MsyiKSkTflVBNIoFZzbDy4Kxhgz8w9'

def get_markets(api_key, currencies):
    """Fetches markets for specified currencies, excluding pairs containing 'USD4'."""
    url = "https://api.binance.us/api/v3/exchangeInfo"
    headers = {'X-MBX-APIKEY': api_key}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return [pair['symbol'] for pair in data['symbols'] 
                if any(currency in pair['symbol'] for currency in currencies) 
                and 'USD4' not in pair['symbol']]
    except requests.RequestException as e:
        return f"Error: {e}"

# Usage of the updated function
eth_markets = get_markets(api_key, ['ETH'])
usdt_usdc_markets = get_markets(api_key, ['USDT', 'USDC'])

def get_price(api_key, symbol):
    url = f"https://api.binance.us/api/v3/ticker/price?symbol={symbol}"
    headers = {'X-MBX-APIKEY': api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['price']
        
    else:
        return "Error: " + response.text

def format_and_print_price(symbol, price):
    # Improved method to identify base and quote currencies
    # Assume last 3 or 4 characters as quote currency based on known currencies
    known_currencies = ['USDT', 'USDC', 'BTC', 'ETH', 'BUSD', 'DAI', 'ADA', 'MATIC', 'SOL']
    quote_currency = None
    for currency in known_currencies:
        if symbol.endswith(currency):
            quote_currency = currency
            break

    if quote_currency:
        base_currency = symbol[:-len(quote_currency)]
    else:
        # Fallback to a default assumption if quote currency is not in the known list
        base_currency = symbol[:-3]
        quote_currency = symbol[-3:]

    # Ensure that both base and quote currencies are identified
    if base_currency and quote_currency:
        print(f"Price of {base_currency} in {quote_currency}: {price} {quote_currency} for 1 {base_currency}. Conversion rate: 1 {base_currency} = {price} {quote_currency}")
    else:
        print(f"Unable to determine base and quote currencies for symbol: {symbol}")



# Count the total number of markets
total_markets = len(eth_markets) + len(usdt_usdc_markets)
print(f"Total markets to fetch: {total_markets}")

# Counter for successfully fetched prices
fetched_prices_count = 0

# Fetching prices and printing information
for symbol in eth_markets + usdt_usdc_markets:
    price = get_price(api_key, symbol)
    if "Error" not in price:
        format_and_print_price(symbol, price)
        fetched_prices_count += 1
    else:
        print(f"Failed to fetch price for {symbol}")

# Check if all prices were successfully fetched
if fetched_prices_count == total_markets:
    print("Successfully fetched prices for all markets.")
else:
    print(f"Prices fetched for {fetched_prices_count} markets out of {total_markets}.")

# Optionally, you can also print how many markets failed
failed_markets = total_markets - fetched_prices_count
if failed_markets > 0:
    print(f"Failed to fetch prices for {failed_markets} markets.")

