from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cita, Dentista, Comentario
from django.forms import ModelForm


class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']


class DentistaForm(forms.ModelForm):
    class Meta:
        model = Dentista 
        fields = ['nombre', 'especialidad']

class RegistroUsuariosForm(UserCreationForm):    
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class citaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['fecha', 'motivo']

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput)
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=True)
    last_name = forms.CharField(label="Apellidos/s", max_length=80, required=True)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)

