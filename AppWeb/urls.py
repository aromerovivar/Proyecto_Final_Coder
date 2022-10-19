from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path

from AppWeb.views import *

urlpatterns = [
    path('',Inicio, name="Inicio"),
    path('accounts/RegisterUser/', formUser, name="RegistrarUsuario"),
    path('crearblog/',crearBlog, name="CrearBlogs"),
    path("blogcreado/",Blogcreado, name="blogcreado"),
    path('buscarBlogs/',buscarblogs, name="Buscarblogs"),
    path('resultados/',resultados,name="resultadoBlogs"),
    #13/10 agregado
    path('accounts/login/',login_request,name="login"),
    path('accounts/SesionCreada/',Iniciocreado),
    path('logout', LogoutView.as_view(template_name="AppWeb/logout.html"), name="Logout"),
    path('accounts/editarUser/',editaruser,name='EditUser'),
    path("accounts/ChangeAvatar/",agregarAvatar,name="AgregarAvatar"),
    path("aboutme/AlejoRomeroVivar",aboutme,name="Abotme"),

    #CRUD Blogs

    path('blog/list/', listablogs.as_view(),name="BlogLeer"),
    path('blog/<int:pk>/', detailblogs.as_view(),name="BlogDetalle"),
    path('blog/editar/<int:pk>', actualizarBlog.as_view(),name="Blogeditar"),
    path('blog/eliminar/<int:pk>', borrarBlog.as_view(),name="eliminarBlog"),
]
