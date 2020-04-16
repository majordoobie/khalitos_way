from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='monitor_index'),

    # The braces will take whatever string is in base/here/ and assign it to <device_name>
    path('all', views.all, name='monitor_all'),
    path('<device_name>', views.history, name='monitor_history'),
]