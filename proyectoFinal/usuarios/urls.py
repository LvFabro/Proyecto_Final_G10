from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('register/', views.CrearUsuario.as_view(), name = 'registrar'),
    path('login/', LoginView.as_view(template_name='usuarios/iniciar_sesion.html'), name = 'login'),
    path('logout/', LogoutView.as_view(next_page='index'), name = 'logout'),
]

