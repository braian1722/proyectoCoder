from django import forms

class form_estudiantes(forms.Form):
    nonbre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class form_profesores(forms.Form):
    nonbre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profecion = forms.CharField(max_length=30)


class form_materias(forms.Form):
    materia = forms.CharField(max_length=30)
    turno =  forms.CharField(max_length=30)
    comision = forms.IntegerField()   

    