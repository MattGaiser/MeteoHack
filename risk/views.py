from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        'payload': 0
    }
    return render(request, 'risk/index.html', context)

def risk(request, type=0):
    context = {
        'payload': 0
    }
    return render(request, 'risk/risk.html', context)
