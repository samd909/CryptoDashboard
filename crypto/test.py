import requests

def get_bitcoin_price():
    # URL for CoinGecko's Bitcoin price endpoint
    url = "https://api.coingecko.com/api/v3/simple/price"
    
    # Parameters for the API call
    params = {
        'ids': 'bitcoin',
        'vs_currencies': 'usd'
    }
    
    try:
        # Make the GET request to fetch Bitcoin's current price
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception if there is an HTTP error

        # Extract the price data from the JSON response
        data = response.json()
        bitcoin_price = data['bitcoin']['usd']
        
        # Print the current price
        print(f"Current Bitcoin Price: ${bitcoin_price}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Call the function to get and print the Bitcoin price
get_bitcoin_price()
