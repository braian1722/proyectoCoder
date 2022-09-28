from django.shortcuts import render
from app_universidad.models import *
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"index.html") #muestro el index


def estudiantes(request): # creo una funcion para registrar estudiantes 

    if request.method == "POST":
        estudiante = Estudiante (nombre=request.POST["Nombre"],apellido=request.POST["apellido"],email=request.POST["email"])
        estudiante.save()
        return render(request,"index.html")


    return render(request,"estudiante.html")


def profesores(request):#creo una funcion para registrar profesores 

    if request.method == "POST":
        Profesor = profesor (nombre=request.POST["Nombre"],apellido=request.POST["apellido"],email=request.POST["email"],
        profecion=request.POST["profecion"])
        
        Profesor.save()
        return render(request,"index.html")


    return render(request,"profesor.html")



def materias(request): #creo una funcion para registrar materias

    if request.method == "POST":
        materias = materia (materia=request.POST["materia"],turno=request.POST["turno"],comision=request.POST["comision"])
        
        materias.save()
        return render(request,"index.html")


    return render(request,"materia.html")


## las siguientes funciones son para buscar en la base de datos con un dato en especifico el cual
## traera todos los datos ej: del estudiante buscado

def buscarEstudiante(request):
    if request.GET["email"]: 
        email = request.GET["email"] 
        estudiantes = Estudiante.objects.filter(email__icontains = email)
        return render (request,"estudiante.html",{"estudiantes":estudiantes})

    else:
        respuesta ="no enviaste datos" 
    return HttpResponse(respuesta)  


def buscarProfesor(request):
    if request.GET["email"]: 
        email = request.GET["email"] 
        profesores = profesor.objects.filter(email__icontains = email)
        return render (request,"profesor.html",{"profesores":profesores})

    else:
        respuesta ="no enviaste datos" 
    return HttpResponse(respuesta)  



def buscarMaterias(request):
    if request.GET["comision"]: 
        comision = request.GET["comision"] 
        materias = materia.objects.filter(comision__icontains = comision)
        return render (request,"materia.html",{"materias":materias})

    else:
        respuesta ="no enviaste datos" 
    return HttpResponse(respuesta) 