from django.shortcuts import render, redirect
from .models import Evento

# Create your views here.

# def index(request):
#    return redirect('/agenda/')

def lista_eventos(request):
    try:
        evento = Evento.objects.get(id=1)
        if evento:
            response = {'evento' : evento}
            return render(request, 'agenda.html', response)
    finally:
        return render(request, 'agenda.html')
