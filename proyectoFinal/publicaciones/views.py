from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import PublicarLibro
from .forms import CrearPublicacion, ComentariosFormulario
from django.urls import reverse

# Create your views here.

#View basada en clase:


class PublicacionLibro(ListView):
    template_name = 'publicaciones/publicaciones.html'
    model = PublicarLibro
    context_object_name = 'publicarlibros'


class CrearPublicacionForm(CreateView):
    model = PublicarLibro
    template_name = 'publicaciones/crear_publicacion.html'
    form_class = CrearPublicacion

    def form_valid(self, form):
        a = form.save(commit=False)
        a.autor_id = self.request.user.id 
        return super().form_valid(a)
    
    def get_success_url(self):
        return reverse('publicacion')

class ModificarPublicacionForm(UpdateView):
    model = PublicarLibro
    template_name = 'publicaciones/mod_publicacion.html'
    form_class = CrearPublicacion #Se utiliza el mismo formulario para crear una publicación.
    success_url = '../../crear-publicacion/libros-publicados/'

class EliminarPublicacionForm(DeleteView):
    model = PublicarLibro
    template_name = 'publicaciones/eliminar_publicacion.html'
    success_url = '../../crear-publicacion/libros-publicados/'

class LeerPublicacionForm(DetailView):
    model = PublicarLibro
    template_name = 'publicaciones/leer_publicacion.html'
    context_object_name = 'publicarlibros'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ComentariosFormulario()
        return context
    
    def post(self, request, *args, **kwargs):

        publicacion = self.get_object()
        form =ComentariosFormulario(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor_id = self.request.user.id
            comentario.publicacion = publicacion
            comentario.save()
            return super().get(request)
        else:
            return super().get(request)


    




