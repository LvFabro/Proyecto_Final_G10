from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import PublicarLibro, Comentarios, Categorias
from .forms import CrearPublicacion, ComentariosFormulario
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import EsColaborador, EsAutor



# Create your views here.

#View basada en clase:


class PublicacionLibro(ListView):
    template_name = 'publicaciones/publicaciones.html'
    model = PublicarLibro
    context_object_name = 'publicarlibros'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias']=Categorias.objects.all()
        return context 
    def get_queryset(self):
        todo = super().get_queryset()
        filtro = self.request.GET.get('categoria')
        
        if filtro:
            todo = todo.filter(categoria = filtro)
        
        organizar = self.request.GET.get('ordenar')
        if organizar:
            if organizar == 'date.asc':
                todo = todo.order_by('fecha')
            elif organizar == 'date.desc':
                todo = todo.order_by('-fecha')
            elif organizar == 'alf.asc':
                todo = todo.order_by('titulo')
            elif organizar == 'alf.desc':
                todo = todo.order_by('-titulo')
        return todo


class CrearPublicacionForm(LoginRequiredMixin, EsColaborador, CreateView):
    model = PublicarLibro
    template_name = 'publicaciones/crear_publicacion.html'
    form_class = CrearPublicacion

    def form_valid(self, form):
        a = form.save(commit=False)
        a.autor_id = self.request.user.id 
        return super().form_valid(a)
    
    def get_success_url(self):
        return reverse('publicacion')

class ModificarPublicacionForm(LoginRequiredMixin, EsAutor, UpdateView):
    model = PublicarLibro
    template_name = 'publicaciones/mod_publicacion.html'
    form_class = CrearPublicacion #Se utiliza el mismo formulario para crear una publicación.
    success_url = '../libros-publicados/'

class EliminarPublicacionForm(LoginRequiredMixin, EsAutor, DeleteView):
    model = PublicarLibro
    template_name = 'publicaciones/eliminar_publicacion.html'
    success_url = '../libros-publicados/'
    

class LeerPublicacionForm(DetailView):
    model = PublicarLibro
    template_name = 'publicaciones/leer_publicacion.html'
    context_object_name = 'publicarlibros'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ComentariosFormulario()
        return context
    
    def post(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('index')

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
    
class BorrarComentario(LoginRequiredMixin, EsAutor, DeleteView):
    model = Comentarios
    template_name = 'publicaciones/eliminar_comentarios.html'
    
    def get_success_url(self):
        return reverse('leer', args=[self.object.publicacion.id])

class ModificarComentario(LoginRequiredMixin, EsAutor, UpdateView):
    model = Comentarios
    template_name = 'publicaciones/modificar_comentarios.html' 
    form_class = ComentariosFormulario

    def get_success_url(self):
        return reverse('leer', args=[self.object.publicacion.id])
    



    




