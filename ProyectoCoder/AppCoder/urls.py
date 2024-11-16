from django.urls import path, include
from AppCoder import views
from Proyecto1.views import saludo, segunda_vista, dia_de_hoy, muesta_nombre, probando_template

urlpatterns= [
    #pego sin el admin
    path('saludo/', saludo),
    path('segunda_vista/', segunda_vista),
    path('hoy/', dia_de_hoy),
    path('elnombre/<nombre>/', muesta_nombre),
    path('probando_template', probando_template),
    path('AppCoder/',include('AppCoder.urls')),
    path('inicio/',views.inicio ),
    path('cursos/',views.cursos ),
    path('profesores/',views.profesores ),
    path('estudiantes/',views.estudiantes ),
    path('entregables/',views.entregables ),


]