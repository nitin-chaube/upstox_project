from django.contrib import admin
from django.urls import path, include
from trading.views import home  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('trading.urls')),  # Include the trading app URLs
    path('', home),  # Define the root URL
]
