from django import forms
from ..models.carrera import Carrera 

class FormCarrera(forms.ModelForm):
    class Meta: 
        model = Carrera
        fields = ['name', 'description']