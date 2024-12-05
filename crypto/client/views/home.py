from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count
import requests
from ..models import *

@login_required
def home(request):
<<<<<<< Updated upstream
    template = "home.html"
    stef = "igorneuker"
=======
    # Fetch trending tokens from CoinGecko API

    top_coins = get_highest_coins()
    trending_tokens = get_trending_tokens()
    template = "home/home.html"
>>>>>>> Stashed changes
    context = {
    }
    return render(request, template, context)
