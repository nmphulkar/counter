
from django.contrib import admin
from django.urls import path
from .views import helloworld,increment,decrement,reset #importing the function names from views.py

urlpatterns = [
    path('helloworld/',helloworld), # url is created 2nd helloworld function
    path('increment/',increment),
    path('decrement/',decrement),
    path('reset/',reset),
]
