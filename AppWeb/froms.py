from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from AppWeb.models import Avatar, blog


class userFormulario(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField( label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField( label = "Repita la contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField( label = "Nombre")
    last_name = forms.CharField( label = "Apellido")

    class Meta:
        model = User
        fields = ["username", "email", "first_name","last_name", "password1", "password2"]


class blogFormulario(forms.ModelForm):

    Titulo = forms.CharField()
    Descripcion = forms.CharField()
    Cuerpo = forms.CharField()
    class Meta:
        model = blog
        fields = ["imagen"]

    
class formularioeditar(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField( label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField( label = "Repita la contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ["email", "first_name","last_name", "password1", "password2"]

class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ["imagen"]
