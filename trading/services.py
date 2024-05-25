import requests
import json

class UpstoxService:
    # BASE_URL = 'https://api.upstox.com/v2'

    def __init__(self, api_key, api_secret, access_token):
        self.api_key = api_key
        self.api_secret = api_secret
        self.access_token = access_token

    def get_headers(self):
        return {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }

    def fetch_current_holdings(self):
        # url = f'{self.BASE_URL}portfolio/long-term-holdings'
        url = 'https://api.upstox.com/v2/portfolio/long-term-holdings'
        headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer {your_access_token}'
        }

        response = requests.get(url, headers=headers)
        return response

    def get_brokerage_details(self, transaction_type, product, quantity, price):
        url = 'https://api.upstox.com/v2/charges/brokerage'
        headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer {your_access_token}'
        }

        params = {
            'instrument_token': 'NSE_EQ|INE669E01016',
            'quantity': quantity,
            'product': product,
            'transaction_type': transaction_type,
            'price': price,
        }

        response = requests.get(url, headers=headers, params=params)

        print(response.json())

    def place_order(self, transaction_type, symbol, quantity, price):
        url = 'https://api.upstox.com/v2/order/place'
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer {your_access_token}',
        }

        data = {
            'quantity': quantity,
            'product': 'D',
            'validity': 'DAY',
            'price': 0,
            'tag': 'string',
            'instrument_token': 'NSE_EQ|INE669E01016',
            'order_type': 'MARKET',
            'transaction_type': transaction_type,
            'disclosed_quantity': 0,
            'trigger_price': price,
            'is_amo': False,
            'symbol': symbol,
        }

        try:
            # Send the POST request
            response = requests.post(url, json=data, headers=headers)

            # Print the response status code and body
            return response

        except Exception as e:
            # Handle exceptions
            print('Error:', str(e))

    def handle_postback(self, data):
        # Process postback data received from Upstox
        pass

    def get_prices(self, symbol):
        url = 'https://api.upstox.com/v2/market-quote/ltp?instrument_key=NSE_EQ%7CINE848E01016'
        headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer {your_access_token}'
        }

        response = requests.get(url, headers=headers)

        return response
