from django.shortcuts import render
from django.views.generic import CreateView
from .models import Usuario
from .forms import RegistrarUsuarioForm
from django.contrib.auth import login


# Create your views here.

class CrearUsuario(CreateView):
    model = Usuario
    template_name = 'usuarios/crear_usuario.html'
    form_class = RegistrarUsuarioForm

    def form_valid(self, form):
        response = super().form_valid(form)
        usuario = form.save()
        login(self.request, usuario)
        return response

    