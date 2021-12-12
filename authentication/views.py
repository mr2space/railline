from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def account():
    return HttpRequest("Hello world")
