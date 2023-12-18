from django.contrib import admin
from .models import PublicarLibro, Categorias, Comentarios


# Register your models here.

admin.site.register(PublicarLibro)
admin.site.register(Categorias)
admin.site.register(Comentarios)

