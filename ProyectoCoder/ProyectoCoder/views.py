from django.http import HttpResponse
from datetime import date
from django.template import Template, Context
from django.template import loader
from AppCoder.models import Curso
#request se puede poner solo "req"
def saludo(request):
    return HttpResponse("Chanchito feliz")

def otra_vista(request):
    return HttpResponse("<h1> ¡Esto es un título!<h1><p> Y esto es un párrafo<p>")

def segunda_vista(request):
    return HttpResponse("Segunda vista actualizada")

def dia_de_hoy(request):
    hoy = date.today
    return HttpResponse(f"Hoy es {hoy}")

def muesta_nombre(self, nombre):
    return HttpResponse(f"Buenos días {nombre}, bienvenido al curso")

def probando_template(request):

    nom = "Tomas"
    ap = "Harris"

    lista_notas = [1,2,3,4,5,6,7,8,9,10]

    diccionario = {"nombre": nom, "apellido": ap, "hoy": dia_de_hoy, "notas": lista_notas}

    # mi_html = open('./Proyecto1/plantillas/index.html')
    # #Crea el template usando la clase Template
    # plantilla = Template(mi_html.read())

    # mi_html.close()
    # #Creamos un contexto
    # mi_contexto = Context()
    # #Para renderizar con su contexto (lo ensambla)
    # documento = plantilla.render(mi_contexto)

    plantilla = loader.get_template('template1.html')

    documento = plantilla.render(diccionario)
    
    return HttpResponse(documento)

def agregar_curso(request,nom,cam):
    curso = Curso(nombre = nom, camada = cam)
    curso.save()

    documento = f"Curso: {curso.nombre} Camada: {curso.camada}"

    return HttpResponse(documento)