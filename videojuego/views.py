from django.shortcuts import render
from django.http import HttpResponse
from .models import Reto
# excentar la necesidad de un token con POST
from django.views.decorators.csrf import csrf_exempt
# importar json
from json import loads, dumps

class Fraccion:
    def __init__(self, num, den):
        self.num = num
        self.den = den
    def toJSON(self):
        return dumps(self, default=lambda o:o.__dict__, sort_keys=False, indent=4)

# Create your views here.
def index(request):
    #return HttpResponse('<h1>se logra</h1>')
    return render(request, 'index.html')

def proceso(request):
    nombre = request.POST['nombre']
    nombre = nombre.upper()
    return render(request, 'proceso.html',{'name':nombre})

def datos(request):
    jugadores = Reto.objects.all()
    return render(request, 'datos.html', {'lista_jugadores':jugadores})

# http://127.0.0.1:8000/multiplicacion?p=10.3&q=20
def multiplicacion(request):
    p = request.GET['p']
    q = request.GET['q']
    r = float(p) * float(q)
    return HttpResponse("Multiplicación: " + p + " x " + q + " = " + str(r))

# serialization: mandar un objeto por medio de la red, generar un json con dump
# deserialization: traducir la info que está en el json con load
# @ se llama anotación
@csrf_exempt
def division(request):
    body_unicode = request.body.decode('utf-8')
    body = loads(body_unicode)
    p = body['p']
    q = body['q']
    resultado = Fraccion(p,q)
    json_resultado = resultado.toJSON()
    return HttpResponse(json_resultado, \
        content_type = "text/json-comment-filtered")