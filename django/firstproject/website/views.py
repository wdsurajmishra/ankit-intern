from django.shortcuts import render
from django.http import HttpResponse
from ankit.xyz import faltu

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
