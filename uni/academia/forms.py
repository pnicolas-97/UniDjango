from django import forms
from academia.models import *

# Estuden fomrm

class EstudentForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'
