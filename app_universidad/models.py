
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=40) 
    apellido = models.CharField(max_length=30) 
    email = models.EmailField()

class profesor(models.Model):
    nombre = models.CharField(max_length=30) 
    apellido = models.CharField(max_length=30) 
    email = models.EmailField()
    profecion = models.CharField(max_length=30) 

class materia(models.Model):
    materia = models.CharField(max_length=30)
    turno =  models.CharField(max_length=30)
    comision = models.IntegerField()   