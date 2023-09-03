from django.shortcuts import render, redirect
from .models import Cita, Avatar, Dentista, Comentario
from django.utils.decorators import method_decorator
from .forms import RegistroUsuariosForm, citaForm, UserEditForm, AvatarFormulario, ComentarioForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth       import authenticate, login,update_session_auth_hash, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from django.shortcuts import get_object_or_404
from django.forms import ModelForm
from django.http import Http404


@login_required
def yo(request):
    return render(request, "aplicacion/yo.html")


def volver(request):
    return render(request, "aplicacion/home2.html")

def home(request):
    return render(request, "aplicacion/inicio1.html" )

#_____________________ APARTADO DE CITAS _____________________#
@login_required
def ver_citas(request):
    citas = Cita.objects.filter(paciente=request.user)
    return render(request, 'aplicacion/ver_citas.html', {'citas': citas})

@login_required
def editar_cita(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id)
    form = citaForm(instance=cita)
    
    if request.method == 'POST':
        form = citaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect(reverse('ver_citas'))
    
    return render(request, 'aplicacion/editar_cita.html', {'form': form})

@login_required
def eliminar_cita(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id)
    
    if request.method == 'POST':
        cita.delete()
        return redirect(reverse('ver_citas'))
    
    return render(request, 'aplicacion/eliminar_cita.html', {'cita': cita})


@login_required
def agendar_cita(request):
    if request.method == 'POST':
        form = citaForm(request.POST)
        if form.is_valid():
            cita_instance = form.save(commit=False)
            cita_instance.paciente = request.user
            cita_instance.save()
            return redirect(reverse('ver_citas'))

    else:
        form = citaForm()

    return render(request, 'aplicacion/agendar_cita.html', {'form': form})
#_____________________ APARTADO DE CITAS _____________________#

#_____________________  LOGIN, REGISTRO Y EDIT  _____________________#
def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)

                
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.png"
                finally:
                    request.session["avatar"] = avatar


                return render(request, "aplicacion/home2.html", {'mensaje': f'Bienvenido a nuestro sitio {usuario}'})
            else:
                return render(request, "aplicacion/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})
        else:
            return render(request, "aplicacion/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})

    miForm =   AuthenticationForm()      

    return render(request, "aplicacion/login.html", {"form":miForm})    


def register(request):
    if request.method == 'POST':
        form = RegistroUsuariosForm(request.POST)
        if form.is_valid():
            
            user = form.save()
            
            login(request, user)

            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:

                request.session["avatar"] = avatar
            
            return render(request, "aplicacion/home2.html")
    else:
        miForm =   RegistroUsuariosForm()      
    return render(request, "aplicacion/registro.html", {"form":miForm})

@login_required
def borrar_cuenta(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        logout(request)
        return redirect('base')

@login_required
def editUser(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')

            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password1 and password1 == password2:
                usuario.set_password(password1)  
                usuario.save()
                update_session_auth_hash(request, usuario) 
                return render(request, "aplicacion/home2.html")
            else:
                form.add_error('password1', "Las contraseñas no coinciden")

        return render(request, "aplicacion/editUser.html", {'form': form, 'usuario': usuario.username })
    else:
        form = UserEditForm(instance=usuario)
        return render(request, "aplicacion/editUser.html",  {'form': form, 'usuario': usuario.username })
         


#_____________________ LOGIN, REGISTRO Y EDIT _____________________#

#_____________________ AVATARES _____________________#
@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES) 
        if form.is_valid():
            u = User.objects.get(username=request.user)

            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request,"aplicacion/home2.html")
    else:
        form = AvatarFormulario()
    return render(request, "aplicacion/cambiarAvatar.html", {'form': form })


#_____________________ AVATARES _____________________#

#_____________________ DENTISTAS _____________________#
class lista_dentistas(LoginRequiredMixin, ListView):
    model = Dentista
    template_name = 'dentista_list.html'  # Asegúrate de que sea el nombre correcto
    context_object_name = 'dentistas' 

class agregar_dentista(LoginRequiredMixin, CreateView):
    model = Dentista
    fields = ['nombre', 'especialidad']
    success_url = reverse_lazy('lista_dentistas')

class editarDentista(LoginRequiredMixin, UpdateView):
    model = Dentista
    fields = ['nombre', 'especialidad']
    success_url = reverse_lazy('lista_dentistas')

class eliminar_dentista(LoginRequiredMixin, DeleteView):
    model = Dentista
    success_url = reverse_lazy('lista_dentistas')
    

#_____________________ DENTISTAS _____________________#

#_____________________ COMENTARIOS _____________________#

class ComentarioCreateView(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = ComentarioForm  # Especifica el formulario de modelo aquí
    success_url = reverse_lazy('lista_comentarios')
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
class ComentarioListView(LoginRequiredMixin, ListView):
    model = Comentario
    context_object_name = 'comentarios'

class ComentarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Comentario
    fields = ['texto']
    success_url = reverse_lazy('lista_comentarios')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(autor=self.request.user)  # Filtrar por autor

class ComentarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Comentario
    success_url = reverse_lazy('lista_comentarios')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.autor != self.request.user:
            raise Http404("No tiene permisos para eliminar este comentario.")
        return obj

#_____________________ COMENTARIOS _____________________#