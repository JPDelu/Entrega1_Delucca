from django.urls import path
from cloudstore import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('consolas', views.consolas, name="Consolas"),
    path('juegos', views.juegos, name="Juegos"),
    path('accesorios', views.accesorios, name="Accesorios"),
]
