from django.shortcuts import render
from django.http import HttpResponse
from django.forms.models import model_to_dict

# User models in current app
from .models import TemperatureRead

def index(request):    
    last_read = TemperatureRead.objects.latest('sample_date')
    last_read_dict = {
        'Device': last_read.device_name,
        'Date': last_read.sample_date,
        'Temperature:': last_read.temperature,
        'Humidity': last_read.humidity,
        'Online': last_read.device_online
    }
    return render(request, 'index.html', last_read_dict)



