from django.urls import path
from cloudstore import views

urlpatterns = [
    path('', views.inicio),
    path('consolas', views.consolas),
    path('juegos', views.juegos),
    path('accesorios', views.accesorios),
]
