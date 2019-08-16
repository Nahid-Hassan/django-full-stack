# from django.conf.urls import url
# from first_app import views

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
