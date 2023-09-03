from .views import *
from django.urls import path, include
from django.contrib.auth.views import LogoutView


urlpatterns = [
 path('yo/', yo, name='yo'),
 path('', home, name='base'),
 path('volver/', volver, name='volver'),

#_____________________ CITAS _____________________#

 path('agendar_cita/', agendar_cita, name='agendar_cita'),
 path('ver_citas/', ver_citas, name='ver_citas'),
 path('editar_cita/<int:cita_id>/', editar_cita, name='editar_cita'),
 path('eliminar_cita/<int:cita_id>/', eliminar_cita, name='eliminar_cita'),

#_____________________ CITAS _____________________#

#_____________________ LOGIN _____________________# 

 path('login/', login_request, name="login" ),
 path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout" ),
 path('registro/', register, name="registro" ),
 path('editUser/', editUser, name='editUser'),
 path('borrar_cuenta/',borrar_cuenta, name='borrar_cuenta'),

#_____________________ LOGIN _____________________# 
 
#_____________________ AVATAR _____________________# 

 path('agregaAvatar/', agregarAvatar, name="agregarAvatar" ),

#_____________________ AVATAR _____________________# 

#_____________________ DENTISTA _____________________# 

path('dentistas/', lista_dentistas.as_view(), name="lista_dentistas" ),
path('agregar_dentista/', agregar_dentista.as_view(), name="agregar_dentista" ),
path('dentista/<int:pk>/update/', editarDentista.as_view(), name='editarDentista'),
path('dentista/<int:pk>/delete/', eliminar_dentista.as_view(), name='eliminar_dentista'),

#_____________________ DENTISTA _____________________# 

#_____________________ COMENTARIOS _____________________# 

path('comentarios/nuevo/', ComentarioCreateView.as_view(), name='nuevo_comentario'),
path('comentarios/', ComentarioListView.as_view(), name='lista_comentarios'),
path('comentarios/<int:pk>/editar/', ComentarioUpdateView.as_view(), name='editar_comentario'),
path('comentarios/<int:pk>/eliminar/', ComentarioDeleteView.as_view(), name='eliminar_comentario'),


#_____________________ COMENTARIOS _____________________# 


]