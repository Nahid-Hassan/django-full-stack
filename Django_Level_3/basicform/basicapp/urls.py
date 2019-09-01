from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formpage/', views.from_name_view, name='from-page')
]
