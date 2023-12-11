from django.urls import path
from . import views

urlpatterns = [
    path('libros-publicados/', views.PublicacionLibro.as_view(), name = 'publicacion' ),
    path('crear-publicacion/', views.CrearPublicacionForm.as_view(), name = 'publicar' ),
]