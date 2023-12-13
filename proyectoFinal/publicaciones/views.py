from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
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

class ModificarPublicacionForm(UpdateView):
    model = PublicarLibro
    template_name = 'mod_publicacion.html'
    form_class = CrearPublicacion #Se utiliza el mismo formulario para crear una publicación.
    success_url = '../../crear-publicacion/libros-publicados/'

class EliminarPublicacionForm(DeleteView):
    model = PublicarLibro
    template_name = 'eliminar_publicacion.html'
    success_url = '../../crear-publicacion/libros-publicados/'

