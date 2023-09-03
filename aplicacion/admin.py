from django.contrib import admin
from .models import Comentario, Dentista, paciente, Cita

admin.site.register(Comentario)
admin.site.register(Dentista)
admin.site.register(paciente)
admin.site.register(Cita)