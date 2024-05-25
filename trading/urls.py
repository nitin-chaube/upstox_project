from django.urls import path
from .views import HoldingsView, PlaceOrderView, PostbackView, PricesView, GetBrokerageView

urlpatterns = [
    path('holdings/', HoldingsView.as_view(), name='holdings'),
    path('brokerage/', GetBrokerageView.as_view(), name='get-brokerage'),
    path('order/', PlaceOrderView.as_view(), name='place-order'),
    path('postback/', PostbackView.as_view(), name='postback'),
    path('prices/<str:symbol>/', PricesView.as_view(), name='prices'),
]
