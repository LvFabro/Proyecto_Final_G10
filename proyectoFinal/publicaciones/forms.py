from django import forms
from .models import PublicarLibro

class CrearPublicacion(forms.ModelForm):
    class Meta:
        model = PublicarLibro
        fields = ['titulo', 'enlace', 'categoria', 'autor']


