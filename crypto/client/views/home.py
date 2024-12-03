from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from ..models import *

@login_required
def home(request):
    template = "home.html"
    context = {

    }
    return render(request, template, context)
