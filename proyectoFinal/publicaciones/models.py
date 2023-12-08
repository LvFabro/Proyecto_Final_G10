from django.db import models

# Create your models here.

class PublicarLibro(models.Model):
    fecha = models.DateField(auto_now_add=True)
    titulo = models.CharField(max_length=40)
    cuerpo = models.TextField()
    categoria = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)

    def __str__(self):
        return self.titulo

    