from django.urls import path
from . import views

urlpatterns = [
    path('libros-publicados/', views.PublicacionLibro.as_view(), name = 'publicacion' ),
]