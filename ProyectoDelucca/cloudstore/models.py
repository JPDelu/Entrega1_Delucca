from django.db import models

# Create your models here.

class Consola(models.Model):
    
    nombre_consola: models.CharField()
    marca_consola: models.CharField()