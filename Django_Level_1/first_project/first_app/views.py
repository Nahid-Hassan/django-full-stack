from django.shortcuts import render
from django.http import HttpResponse

#python file read
# html = open(
#     '/media/nahid/New Volume/Web-Developer/Full-Stack-Web-Developer/Capstone_Project_One/project.html', 'r')

# Create your views here.
def index(request):
    my_dict = {
        #key: value
        'insert_me': 'Hello I am from views.py'
    }

    return render(request, 'first_app/index.html', context=my_dict)
    
    #return HttpResponse(html)
    #return HttpResponse('First Django Web Application.')


