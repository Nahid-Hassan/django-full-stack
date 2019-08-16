from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
html = '<em>My Second App</em>'

def index(request):
    return HttpResponse(html)