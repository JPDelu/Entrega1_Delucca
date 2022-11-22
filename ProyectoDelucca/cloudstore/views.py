from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from cloudstore.models import *
from cloudstore.forms import crear_consolas
from cloudstore.forms import crear_accesorios


# Create your views here.

def inicio(request):
    return render(request, 'cloudstore/inicio.html')

def consolas(request):
    return render(request, 'cloudstore/consolas.html')

def creacion_consolas(request):

    if request.method == "POST":
        formulario = crear_consolas(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            consola = Consola (nombre_consola=data["nombre_consola"], marca_consola=data["marca_consola"], precio_consola=data["precio_consola"])
            consola.save()
        return render(request, "cloudstore/inicio.html")
    else:
        formulario = crear_consolas()

    contexto = {"formulario": formulario}
    return render(request, "cloudstore/crear_consolas.html", contexto)

def juegos(request):
    return render(request, 'cloudstore/juegos.html')

def crear_juegos(request):

    if request.method == "POST":
        nom_juego = request.POST["nombre_juego"]
        gen_juego = request.POST["genero_juego"]
        pre_juego = request.POST["precio_juego"]

        juego = Juego (nombre_juego=nom_juego, genero_juego=gen_juego, precio_juego=pre_juego)

        juego.save()

    return render(request, "cloudstore/crear_juegos.html")

def accesorios(request):
    
    return render(request, 'cloudstore/accesorios.html')

def creacion_accesorios(request):

    if request.method == "POST":
        form_accesorios = crear_accesorios(request.POST)

        if form_accesorios.is_valid():
            data = form_accesorios.cleaned_data

            accesorio = Accesorio (nombre_accesorio=data["nombre_accesorio"], tipo_accesorio=data["tipo_accesorio"])
            accesorio.save()
        return render(request, "cloudstore/inicio.html")
    else:
        form_accesorios = crear_accesorios()

    contexto = {"form_accesorios": form_accesorios}
    return render(request, "cloudstore/crear_accesorios.html", contexto)




