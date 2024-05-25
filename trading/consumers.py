import json
from channels.generic.websocket import WebsocketConsumer

class PriceConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data = json.loads(text_data)
        symbol = data.get('symbol')

        # Simulate getting price from Upstox (you need to implement actual Upstox WebSocket here)
        price_data = {"symbol": symbol, "price": 100.0}  # Dummy data
        self.send(text_data=json.dumps(price_data))
