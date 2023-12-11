from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import PublicarLibro
from .forms import CrearPublicacion

# Create your views here.

#View basada en clase:


class PublicacionLibro(ListView):
    template_name = 'publicaciones.html'
    model = PublicarLibro
    context_object_name = 'publicarlibros'


class CrearPublicacionForm(CreateView):
    model = PublicarLibro
    template_name = 'crear_publicacion.html'
    form_class = CrearPublicacion
    

