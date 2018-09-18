from django.urls import path
from . import views

urlpattens = [
    path('', views.index, name="agenda-events-index")
]
