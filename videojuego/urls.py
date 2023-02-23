from django.urls import path
from . import views


# estos son los paths como "IPAdress/pathwanted"
urlpatterns = [
    path('', views.index, name = 'index'),
    path('proceso', views.proceso, name = 'proceso'),
    path('datos', views.datos, name = 'datos'),

    # Creación de calculadora de fracciones
    path('suma', views.suma, name = 'suma'),
    path('resta', views.resta, name = 'resta'),
    path('multiplicacion', views.multiplicacion, name = 'multiplicación'),
    path('division', views.division, name = 'división'),
]