from django import urls
from django.urls import path
from . import views

# url confi
urlpatterns = [
    path('',views.home, name='home')
]