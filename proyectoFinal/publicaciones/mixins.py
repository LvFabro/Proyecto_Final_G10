from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Comentarios, PublicarLibro

class EsColaborador(UserPassesTestMixin):
    def test_func(self):
        usuario = self.request.user
        return usuario.es_colaborador or usuario.is_superuser

class EsAutor(UserPassesTestMixin):
    def test_func(self):
        usuario = self.request.user
        publicacion_comentario = self.get_object()

        if isinstance(publicacion_comentario, PublicarLibro):
            return usuario == publicacion_comentario.autor or usuario.is_superuser
        elif isinstance(publicacion_comentario, Comentarios):
            return usuario == publicacion_comentario.autor or usuario == publicacion_comentario.publicacion.autor or usuario.is_superuser
            
