from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.forms.models import model_to_dict

def index(request):
    return render(request, 'homepage/index.html')