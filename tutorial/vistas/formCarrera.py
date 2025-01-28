from django import forms
from ..models import Carrera

class FormCarrera(forms.ModelForm):
    class meta:
        model=Carrera
        fiels = ["nombre", "descripcion"]
    #fields='__all__'  => esto es para mostrar todos los campos