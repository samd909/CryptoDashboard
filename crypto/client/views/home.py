import requests
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import *

@login_required
def home(request):
    # Fetch trending tokens from CoinGecko API
    trending_url = "https://api.coingecko.com/api/v3/search/trending"
    price_url = "https://api.coingecko.com/api/v3/simple/price"
    
    try:
        # Get trending tokens
        response = requests.get(trending_url)
        response.raise_for_status()
        trending_data = response.json()
        
        # Extract IDs of the top 5 tokens
        token_ids = [coin["item"]["id"] for coin in trending_data.get("coins", [])[:8]]
        
        # Fetch prices for the tokens
        price_params = {
            "ids": ",".join(token_ids),  # Comma-separated list of token IDs
            "vs_currencies": "usd",  # Fetch prices in USD
        }
        price_response = requests.get(price_url, params=price_params)
        price_response.raise_for_status()
        prices = price_response.json()
        
        # Combine data into a list of dictionaries
        trending_tokens = [
            {
                "name": coin["item"]["name"],
                "symbol": coin["item"]["symbol"],
                "market_cap_rank": coin["item"].get("market_cap_rank", "N/A"),
                "thumb": coin["item"].get("thumb"),  # URL for the thumbnail image
                "price": prices.get(coin["item"]["id"], {}).get("usd", "N/A"),  # Get price in USD
            }
            for coin in trending_data.get("coins", [])[:8]
        ]
    except requests.RequestException as e:
        trending_tokens = []  # Fallback to an empty list on error
        print(f"Error fetching data: {e}")
    top_coins = get_top_8_highest_value_coins()

    template = "home.html"
    context = {
        "top_coins": top_coins,
        "trending_tokens": trending_tokens
    }
    return render(request, template, context)


def get_top_8_highest_value_coins():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    
    # Parameters for the request
    params = {
        "vs_currency": "usd",  # Convert to USD
        "order": "market_cap_desc",  # Order by market cap (descending)
        "per_page": 8,  # Limit the results to 8
        "page": 1,  # Get the first page of results
    }
    
    # Send GET request to the CoinGecko API
    response = requests.get(url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        coins_data = response.json()
        
        # Extract the top 8 coins and create a list of relevant data (name and price)
        top_8_coins = [
            {
                "name": coin["name"],
                "symbol": coin["symbol"],
                "price": coin["current_price"]
            }
            for coin in coins_data
        ]
        return top_8_coins
    else:
        print("Error fetching data from CoinGecko")
        return []
