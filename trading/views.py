from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import UpstoxService
from django.conf import settings
from django.http import HttpResponse

# Initialize UpstoxService with the credentials from settings
upstox_service = UpstoxService(
    api_key=settings.UPSTOX_API_KEY,
    api_secret=settings.UPSTOX_API_SECRET,
    access_token=settings.UPSTOX_ACCESS_TOKEN
)

def home(request):
    return render(request, 'trading/base.html')

class HoldingsView(APIView):
    def get(self, request):
        data = upstox_service.fetch_current_holdings()
        return Response(data)

class PlaceOrderView(APIView):
    def post(self, request):
        transaction_type = request.data.get('transaction_type')
        prouct = request.data.get('product')
        quantity = request.data.get('quantity')
        price = request.data.get('price')
        data = upstox_service.get_brokerage_details(transaction_type, product, quantity, price)
        return Response(data)

class GetBrokerageView(APIView):
    def post(self, request):
        transaction_type = request.data.get('transaction_type')
        symbol = request.data.get('symbol')
        quantity = request.data.get('quantity')
        price = request.data.get('price')
        data = upstox_service.place_order(transaction_type, symbol, quantity, price)
        return Response(data)

class PostbackView(APIView):
    def post(self, request):
        data = request.data
        upstox_service.handle_postback(data)
        return Response({"status": "received"}, status=status.HTTP_200_OK)

class PricesView(APIView):
    def get(self, request, symbol):
        data = upstox_service.get_prices(symbol)
        return Response(data)
