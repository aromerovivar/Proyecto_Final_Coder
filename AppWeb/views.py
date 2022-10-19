from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from AppWeb.froms import *
from AppWeb.models import *

# Create your views here.

def Inicio(request):
    return render(request,"AppWeb/inicio.html")

def aboutme(request):
    return render(request,"AppWeb/about.html")

def Blogcreado(request):
    return render(request,"AppWeb/BlogCreado.html",{"titulo":""})

def Iniciocreado(request):
    return render(request,"AppWeb/sesioncreada.html",{"nombre":""})

def formUser(request):

    if request.method == "POST":
        formu1 = userFormulario(request.POST)

        if formu1.is_valid():
            username = formu1.cleaned_data["username"]
            formu1.save()
            return render(request, "AppWeb/inicio.html",{"mensaje":"Usuario Creado."})
            
    else:
        formu1 = userFormulario()
    
    return render(request,"AppWeb/formulariosUser.html",{'formu':formu1})

@login_required
def crearBlog(request):
    if request.method == "POST":
        formu2 = blogFormulario(request.POST, request.FILES)

        if formu2.is_valid():
            info2 = formu2.cleaned_data
            Blog = blog(titulo=info2["Titulo"],descripcion=info2["Descripcion"], cuerpo=info2["Cuerpo"], imagen=info2["imagen"])
            Blog.save()
            return render(request,"AppWeb/BlogCreado.html",{"nombre":Blog.titulo,"descripcion":Blog.descripcion,"cuerpo":Blog.cuerpo,})
            
    else:
        formu2 = blogFormulario()
        
    return render(request,"AppWeb/crearblog.html",{'formulario':formu2})

def buscarblogs(request):

    return render(request,"AppWeb/BuscarBlogs.html")

def resultados(request):

    if request.GET['titulo']:
        titulo = request.GET['titulo']
        blogs = blog.objects.filter(titulo__icontains=titulo)

        return render(request, "AppWeb/resultados.html", {"titulo":titulo,"blogs":blogs})
    
    else:
        respuesta = "No enviaste Datos."

    return HttpResponse(respuesta)

#13/10 agregado
def login_request(request):

    if request.method == "POST":
        
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get('password')

            user = authenticate(username = usuario, password = contra) 
        
            if user:

                login(request, user)

                return render(request, "AppWeb/inicio.html", {"mensaje":f"Bienvenido {user}."})
        else:

            return render(request, "AppWeb/inicio.html", {"mensaje":"No encontramos el user capo."})
        
    else:

        form = AuthenticationForm()

    return render(request, "AppWeb/login.html", {"formulario":form})

@login_required
def editaruser(request):

    usuario = request.user

    if request.method == 'POST':
        form = formularioeditar(request.POST)

        if form.is_valid():
            info = form.cleaned_data

            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]

            usuario.save()

            return render(request, "AppWeb/inicio.html")
        
    else:
        form = formularioeditar(initial={
            "email":usuario.email,
            "first_name":usuario.first_name,
            "last_name":usuario.last_name,
            })
        
    return render(request, "AppWeb/editarPerfil.html",{'formulario':form,"usuario":usuario})

@login_required
def agregarAvatar(request):

    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)

        if form.is_valid():
            usuarioActual = User.objects.get(username=request.user)

            avatar = Avatar(usuario=usuarioActual, imagen=form.cleaned_data["imagen"])

            avatar.save()

            return render(request, "AppWeb/inicio.html")
        
    else:
        form = AvatarFormulario()

    return render(request, "AppWeb/agregarAvatar.html", {"formulario":form})

class listablogs(ListView):
    model = blog

class detailblogs(DetailView):
    model = blog
     

class actualizarBlog(UpdateView):
    model = blog
    success_url = "/AppWeb/blog/list"
    fields = ["titulo","descripcion", "cuerpo","imagen"]

class borrarBlog(DeleteView):
    model = blog
    success_url = "/AppWeb/blog/list"
    fields = ["titulo","descripcion", "cuerpo","imagen"]
