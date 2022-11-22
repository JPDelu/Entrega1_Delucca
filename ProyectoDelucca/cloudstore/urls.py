from django.urls import path
from cloudstore import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('consolas', views.consolas, name="Consolas"),
    path('juegos', views.juegos, name="Juegos"),
    path('accesorios', views.accesorios, name="Accesorios"),
    path('crear_juegos/', views.crear_juegos, name="Form_juegos"),
    path('crear_consolas/', views.creacion_consolas, name="Form_consolas"),
    path('crear_accesorios/', views.creacion_accesorios, name="Form_accesorios")
]
