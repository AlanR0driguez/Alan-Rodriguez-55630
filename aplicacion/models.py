from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario por {self.autor.username}"

    def foto_perfil(self):
        return self.autor.profile.avatar.url

class Dentista(models.Model):
    nombre = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} especialista en {self.especialidad}"


class paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    ci = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.ci}"
    

class Cita(models.Model):
    paciente = models.ForeignKey(User, related_name='citas', on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    motivo = models.TextField()

    def __str__(self):
        return f"Cita de {self.paciente} el {self.fecha}"
    

class RegistroUsuariosForm(UserCreationForm): 
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    ci = models.PositiveIntegerField(unique=True)
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput)


class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"