# crypto_price/views.py
from django.shortcuts import render
import requests

def home(request):
    template = "home.html"
    
    # Define the CoinGecko API URL to fetch all coins' market data
    url_all_coins = "https://api.coingecko.com/api/v3/coins/markets"
    
    # Parameters to get all coins data (price, name, and symbol)
    params_all_coins = {
        'vs_currency': 'usd',  # Prices in USD
        'order': 'market_cap_desc',  # Sort by market cap in descending order
        'per_page': 250,  # Fetch up to 250 coins per page
        'page': 1  # Start from the first page
    }

    try:
        # Fetch all coins' data
        response_all_coins = requests.get(url_all_coins, params=params_all_coins)
        response_all_coins.raise_for_status()  # Check for errors in the response
        all_coins_data = response_all_coins.json()

        # Create a dictionary 'data' where each coin is a key and the value is its price
        data = {coin['id']: coin['current_price'] for coin in all_coins_data}
        
    except requests.exceptions.RequestException as e:
        data = {}  # In case of an error, set an empty dictionary
    
    context = {
        'data': data,  # Pass the dictionary to the template
    }
    
    return render(request, template, context)

def coin_graph(request, coin_id, timeframe='1d'):
    template = "coin_graph.html"
    
    # API URL to fetch historical data for a specific coin
    url_historical_data = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    
    # Prepare parameters to fetch historical data (prices)
    params = {
        'vs_currency': 'usd',
        'days': timeframe,  # 1d, 7d, or 30d
    }

    try:
        # Fetch historical data for the selected coin
        response = requests.get(url_historical_data, params=params)
        response.raise_for_status()
        historical_data = response.json()
        
        # Extract the timestamps and prices
        timestamps = [entry[0] for entry in historical_data['prices']]
        prices = [entry[1] for entry in historical_data['prices']]
        
    except requests.exceptions.RequestException as e:
        timestamps = []
        prices = []
    
    # Pass the data to the template
    context = {
        'coin_id': coin_id,
        'timestamps': timestamps,
        'prices': prices,
        'timeframe': timeframe
    }

    return render(request, template, context)

