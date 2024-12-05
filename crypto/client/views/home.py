import requests
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import *

@login_required
def home(request):
    # Fetch trending tokens from CoinGecko API

    top_coins = get_highest_coins()
    trending_tokens = get_trending_tokens()
    template = "home/home.html"
    context = {
        "top_coins": top_coins,
        "trending_tokens": trending_tokens
    }
    return render(request, template, context)

@login_required
def update_trending_tokens(request):
    trending_tokens = get_trending_tokens()
    return render(request, "partials/trending_tokens.html", {"trending_tokens": trending_tokens})

@login_required
def update_highest_coins(request):
    top_coins = get_highest_coins()
    return render(request, "partials/highest_coins.html", {"top_coins": top_coins})



def get_trending_tokens():
    trending_url = "https://api.coingecko.com/api/v3/search/trending"
    price_url = "https://api.coingecko.com/api/v3/simple/price"
    
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
    return trending_tokens


    
def get_highest_coins():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    
    # Parameters for the request
    params = {
        "vs_currency": "usd",  # Convert to USD
        "order": "market_cap_desc",  # Order by market cap (descending)
        "per_page": 8,  # Limit the results to 8
        "page": 1,  # Get the first page of results
    }
    
    # Fetch the top 8 highest value coins
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an exception if the request fails
    coins_data = response.json()

    # Combine data into a list of dictionaries for the top 8 coins
    highest_coins = [
        {
            "name": coin["name"],
            "symbol": coin["symbol"],
            "market_cap_rank": coin["market_cap_rank"],
            "price": coin["current_price"],  # Get price in USD
            "thumb": coin["image"] if isinstance(coin["image"], str) else coin["image"].get("thumb", None)
        }
        for coin in coins_data
    ]

    return highest_coins
