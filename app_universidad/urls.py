from universidad.urls import path
from app_universidad.views import *

urlpatterns = [
    path('', index),
    path('estudiantes/', estudiantes),
    path('profesores/', profesores),
    path('materias/', materias),
    path('buscarEstudiante/', buscarEstudiante),
    path('buscarProfesor/', buscarProfesor),
    path('buscarMaterias/', buscarMaterias), 

    
    


   
]