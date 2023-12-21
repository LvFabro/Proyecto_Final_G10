from django.urls import path
from . import views


urlpatterns = [
    path('libros-publicados/', views.PublicacionLibro.as_view(), name = 'publicacion' ),
    path('crear-publicacion/', views.CrearPublicacionForm.as_view(), name = 'publicar' ),
    path('editar-publicacion/<int:pk>', views.ModificarPublicacionForm.as_view(), name = 'editar'),
    path('eliminar-publicacion/<int:pk>', views.EliminarPublicacionForm.as_view(), name = 'eliminar'),
    path('leer-publicacion/<int:pk>', views.LeerPublicacionForm.as_view(), name = 'leer'),
    path('eliminar-comentarios/<int:pk>', views.BorrarComentario.as_view(), name = 'eliminar-comentario'),
    path('modificar-comentarios/<int:pk>', views.ModificarComentario.as_view(), name = 'modificar-comentario'),
]
