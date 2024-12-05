from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count
import requests
from ..models import *

@login_required
def home(request):
    template = "home.html"
    stef = "igorneuker"
    context = {
    }
    return render(request, template, context)
