from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
html = '<em>Now I am in views.py</em>'

def index(request):
    return HttpResponse(html)


def help(request):
    help_dict = {
        'help_insert':'Help Page'
    }
    
    return render(request, 'index.html', context=help_dict)