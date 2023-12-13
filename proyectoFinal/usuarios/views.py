from django.shortcuts import render
from django.views.generic import CreateView
from .models import Usuario
from .forms import RegistrarUsuarioForm


# Create your views here.

class CrearUsuario(CreateView):
    model = Usuario
    template_name = 'crear_usuario.html'
    form_class = RegistrarUsuarioForm

    