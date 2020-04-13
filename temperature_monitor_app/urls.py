from django.urls import path
from . import views
# This is the root of a path

urlpatterns = [
    path('', views.index, name='index')
]