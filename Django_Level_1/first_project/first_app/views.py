from django.shortcuts import render
from django.http import HttpResponse

#python file read
# html = open(
#     '/media/nahid/New Volume/Web-Developer/Full-Stack-Web-Developer/Capstone_Project_One/project.html', 'r')

# Create your views here.
def index(request):
    #return HttpResponse(html)
    return HttpResponse('First Django Web Application.')


