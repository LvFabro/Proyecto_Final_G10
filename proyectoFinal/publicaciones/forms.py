from django import forms
from .models import PublicarLibro, Comentarios

class CrearPublicacion(forms.ModelForm):
    class Meta:
        model = PublicarLibro
        fields = ['titulo', 'enlace', 'categoria']

class ComentariosFormulario(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields =['cuerpo']


