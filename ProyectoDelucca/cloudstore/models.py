from django.db import models

# Create your models here.

class Consola(models.Model):
    
    nombre_consola= models.CharField(max_length=50, default=None)
    marca_consola= models.CharField(max_length=50, default=None)
    precio_consola= models.IntegerField(default=None)

class Juego(models.Model):

    nombre_juego= models.CharField(max_length=50)
    genero_juego= models.CharField(max_length=50)
    precio_juego= models.IntegerField()

class Accesorio(models.Model):

    nombre_accesorio= models.CharField(max_length=50)
    tipo_accesorio= models.CharField(max_length=50)