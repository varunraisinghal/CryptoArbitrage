import requests
import pandas as pd

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

def get_price(api_key, symbol):
    url = f"https://api.binance.us/api/v3/ticker/price?symbol={symbol}"
    headers = {'X-MBX-APIKEY': api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['price']
    else:
        return "Error: " + response.text

def format_price_data(symbol, price):
    known_currencies = ['USDT', 'USDC', 'BTC', 'ETH', 'BUSD', 'DAI', 'ADA', 'MATIC', 'SOL']
    quote_currency = None
    for currency in known_currencies:
        if symbol.endswith(currency):
            quote_currency = currency
            break

    if quote_currency:
        base_currency = symbol[:-len(quote_currency)]
    else:
        base_currency = symbol[:-3]
        quote_currency = symbol[-3:]

    if base_currency and quote_currency:
        return {
            "Exchange": "Binance",
            "Crypto": base_currency,
            "Quote": quote_currency.lower(),
            "Price": float(price),
            "Conversion_Rate": f"1 {base_currency} = {price} {quote_currency}"
        }
    else:
        return None

api_key = 'HQEyig9ozNbtx9o4oXlrMoZRVaoFP5NVN3MsyiKSkTflVBNIoFZzbDy4Kxhgz8w9'

# Fetching market data
eth_markets = get_markets(api_key, ['ETH'])
usdt_usdc_markets = get_markets(api_key, ['USDT', 'USDC'])

if isinstance(eth_markets, str) or isinstance(usdt_usdc_markets, str):
    print("Failed to fetch market data.")
else:
    combined_markets = eth_markets + usdt_usdc_markets
    price_data = []

    for symbol in combined_markets:
        price = get_price(api_key, symbol)
        if "Error" not in price:
            data = format_price_data(symbol, price)
            if data:
                price_data.append(data)

    # Creating DataFrame
    df = pd.DataFrame(price_data)

    # Sorting DataFrame by Crypto
    df = df.sort_values(by='Crypto')

    # Checking if all pairs are in the DataFrame
    if len(df) == len(combined_markets):
        print("All market pairs are included in the DataFrame.")
    else:
        print("Some market pairs may be missing in the DataFrame.")
        missing_pairs = set(combined_markets) - set(df['Crypto'])
        print("Missing pairs:", missing_pairs)

    # Printing DataFrame
    print(df.to_string(index=False))

    # Saving DataFrame to CSV
    csv_filename = "market_prices.csv"
    df.to_csv(csv_filename, index=False)
    print(f"DataFrame saved to {csv_filename}")
