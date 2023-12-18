from django.db import models
from django.urls import reverse
from usuarios.models import Usuario

# Create your models here.

class Categorias(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class PublicarLibro(models.Model):
    fecha = models.DateField(auto_now_add=True)
    titulo = models.CharField(max_length=50)
    enlace = models.TextField()
    categoria = models.ForeignKey(Categorias, related_name = 'publicaciones', on_delete = models.SET_NULL, null=True)
    autor = models.ForeignKey(Usuario, related_name = 'publicaciones', on_delete = models.CASCADE)

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('publicacion')

class Comentarios(models.Model):
    fecha = models.DateField(auto_now_add=True)
    cuerpo = models.TextField()
    publicacion = models.ForeignKey(PublicarLibro, on_delete = models.CASCADE, related_name = 'comentario')
    autor = models.ForeignKey(Usuario, on_delete = models.CASCADE, related_name = 'comentario')

    def __str__(self):
        return self.publicacion.titulo + "-" + self.autor.username 

    