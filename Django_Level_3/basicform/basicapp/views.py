from django.shortcuts import render
from . import forms

# Create your views here.


def index(request):
    my_dict = {'insert_me': 'this is a simle form    '}
    return render(request, 'basicapp/index.html', my_dict)


def from_name_view(request):
    form = forms.FromName()

    if request.method == 'POST':
        form = forms.FromName(request.POST)

        if form.is_valid():
            print()
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email']) 
            print(form.cleaned_data['text'])
            print()

    return render(request, 'basicapp/form_page.html', {'form_insert': form})
