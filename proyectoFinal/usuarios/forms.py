from .models import Usuario
from django.contrib.auth.forms import UserCreationForm

class RegistrarUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'email', 'telefono']

        

