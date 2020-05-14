from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.forms.models import model_to_dict
from background_task import background
# User models in current app
from .models import TemperatureRead, TemperatureSensors

@background(schedule=1)
def doit():
    print("hellow")

def index(request):    
    logs = TemperatureRead.objects.all().order_by('-sample_date')
    return render(request, 'monitor/index.html', {'logs': logs, 'title': 'All Temperature Sensors'})

def all(requests):
    logs = TemperatureRead.objects.all().order_by('-sample_date')
    return render(requests, 'monitor/all.html', {'logs': logs, 'title': 'All Temperature Sensors'})

def history(request, device_name):
    device = get_object_or_404(TemperatureSensors, device_name=device_name)
    history_data = TemperatureRead.objects.filter(device_name=device.device_name)
    return render(request, 'monitor/index.html', {'logs': history_data, 'title': f'{device.device_name} sensor'})




