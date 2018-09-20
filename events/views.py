from django.shortcuts import render, get_object_or_404
from .models import Event, Comment
from django.utils.timezone import localdate
from django.core.paginator import Paginator, InvalidPage
from django.http import HttpResponse
from django.views.defaults import bad_request, server_error
from datetime import datetime, timedelta

ITEMS_PER_PAGE = 5

# Create your views here.
def index(request):
    """ exibe a pagina principal de aplicações"""
    context= {
        'hide_new_button': True,
        'priorities': Event.priorities_list,
        'today': localdate()
    }
    return render(request, 'index.html', context)
"""Exibe todos os eventos de uma pagina, recebe o número da pagina a ser visualizada via GET"""
def all(resquest):
    page = resquest.GET.get('page', 1)
    paginator = Paginator(Event.objects.all (), ITEMS_PER_PAGE)
    total = paginator.count

    try:
        events = paginator.page(page)
    except InvalidPage:
        events = paginator.page(1)

    context = {
        'events': events,
        'total': total,
        'priorities': Event.priorities_list,
        'today': localdate(),

    }
    return render(resquest, 'events.html', context)

"""Vizualização dos eventos de um determinado dia, recebe a data um formato ano/mes/dia como perimetro"""

def day(request, yaer:int, month:int, day:int):
    day = datetime(yaer, month, day)
    events = Event.objects.filter(date ='%y-%m_%d'.format(day)).order_by('-priority', 'event')
    context ={
        'today': localdate(),
        'day': day,
        'next': day + timedelta(days=1),
        'previous': day - timedelta(days=1),
        'priorities': Event.priorities_list,
    }
    return render(request, 'day.html', context)