from tokenize import blank_re
from unittest.util import _MAX_LENGTH

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Usuario(models.Model):

    nombre = models.CharField(max_length=60)
    email = models.EmailField()
    contra = models.CharField(max_length=150)

class blog(models.Model):

    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    cuerpo = models.CharField(max_length=500)
    imagen = models.ImageField(upload_to="imagenblogs",null=True,blank=True)
    


class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares",null=True,blank=True)

