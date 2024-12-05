import requests
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import *


@login_required
def dashboard(request):
    template = 'dashboard/dashboard.html'
    context = {

    }
    return render(request, template, context)