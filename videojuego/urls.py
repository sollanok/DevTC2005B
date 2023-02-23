from django.urls import path
from . import views


# estos son los paths como "1000.800/pathwanted"
urlpatterns = [
    path('', views.index, name = 'index'),
    path('proceso', views.proceso, name = 'proceso'),
    path('datos', views.datos, name = 'datos'),
    path('multiplicacion', views.multiplicacion, name = 'multiplicación'),
    path('division', views.division, name = 'division'),
]