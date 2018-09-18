from django.shortcuts import render

# Create your views here.
def index(request):
    """ exibe a pagina principal de aplicações"""
    context={
        'hide_new_button': True,
        'priorities': event.priorities_list,
        'today': localdate()
    }

     return render(request, 'index.html', context)