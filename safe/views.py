from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.
def index(request):
    return render( request, 'safe/index.html')
def about(request):
    return render( request, 'safe/about.html')
def contact(request):
    return render( request, 'safe/contact.html')

