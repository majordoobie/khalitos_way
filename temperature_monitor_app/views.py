from django.shortcuts import render
from django.http import HttpResponse
from django.forms.models import model_to_dict

# User models in current app
from .models import TemperatureRead, TemperatureSensors

def index(request):    
    logs = TemperatureRead.objects.all().order_by('-sample_date')
    return render(request, 'monitor/index.html', {'logs': logs})


def history(request, device_name):
    device = TemperatureSensors.objects.get(device_name=device_name)
    history_data = TemperatureRead.objects.filter(device_name=device.device_name)
    return render(request, 'monitor/index.html', {'logs': history_data})

