from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def inicio(request):
    return render(request, 'cloudstore/inicio.html')

def consolas(request):
    return render(request, 'cloudstore/consolas.html')

def juegos(request):
    return render(request, 'cloudstore/juegos.html')

def accesorios(request):
    return render(request, 'cloudstore/accesorios.html')

