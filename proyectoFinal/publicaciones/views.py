from django.shortcuts import render
from django.views.generic import ListView
from .models import PublicarLibro


# Create your views here.

#View basada en clase:

class PublicacionLibro(ListView):
    template_name = 'publicaciones.html'
    model = PublicarLibro
    context_object_name = 'publicarlibros'

