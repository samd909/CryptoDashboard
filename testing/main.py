import requests

base_url = "https://api.coingecko.com/api/v3/coins/markets"

def get_top_5_coins(vs_currency="usd"):
    params = {
        "vs_currency": vs_currency,
        "order": "market_cap_desc",
        "per_page": 5,  
        "page": 1,
        "sparkline": False
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        coins_data = response.json()
        return coins_data
    else:
        print(f"Fout bij het ophalen van gegevens: {response.status_code}")
        return None

top_coins = get_top_5_coins()

if top_coins:
    print("Top 5 cryptocurrencies:")
    for coin in top_coins:
        print(f"Naam: {coin['name']} ({coin['symbol'].upper()})")
        print(f"Prijs: {coin['current_price']} USD")
        print(f"Marktwaarde: {coin['market_cap']} USD")
        print("-" * 30)
else:
    print("Geen data beschikbaar.")
