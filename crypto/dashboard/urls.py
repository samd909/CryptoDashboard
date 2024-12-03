# crypto_price/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('coin/<str:coin_id>/', views.coin_graph, name='coin_graph'),  # For the main page of the coin graph (no timeframe)
    path('coin/<str:coin_id>/<str:timeframe>/', views.coin_graph, name='coin_graph_timeframe'),  # For coin graph with timeframe
]
