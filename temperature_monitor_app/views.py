from django.shortcuts import render
from django.http import HttpResponse
from django.forms.models import model_to_dict

# User models in current app
from .models import TemperatureRead

def index(request):    
    last_read = TemperatureRead.objects.latest('sample_date')
    last_read_dict = {
        'device': last_read.device_name.device_name,
        'date': last_read.sample_date.strftime("%d%b%y %H:%M").upper(),
        'temp': f"{last_read.temperature}\N{DEGREE SIGN}",
        'humid': f"{last_read.humidity}%",
        'online': last_read.device_online
    }
    return render(request, 'index.html', {'temp_devices': last_read_dict})



