from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# This function can be named anything, but convention is to name it index
def index(requests):
    return HttpResponse("Hellow world")
