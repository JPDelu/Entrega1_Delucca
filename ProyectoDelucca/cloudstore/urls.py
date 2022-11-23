from django.urls import path
from cloudstore.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('consolas', consolas, name="Consolas"),
    path('juegos', juegos, name="Juegos"),
    path('accesorios', accesorios, name="Accesorios"),
    path('crear_juegos/', crear_juegos, name="Form_juegos"),
    path('crear_consolas/', creacion_consolas, name="Form_consolas"),
    path('busqueda_consolas/', buscar_consola, name="Buscador_consolas"),
    path('busqueda_consolas_resultado/', resultado_busqueda, name="Resultado_busqueda_consolas"),
    path('crear_accesorios/', creacion_accesorios, name="Form_accesorios")
]
