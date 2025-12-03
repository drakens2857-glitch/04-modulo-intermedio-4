from django.db import models
from django.contrib.auth.models import User
class Categoria(models.Model):

    nombre = models.CharField(max_length=100, unique=True)

descripcion = models.TextField(blank=True)

creado = models.DateTimeField(auto_now_add=True)

def __str__(self):

    return self.nombre

class Meta:

    verbose_name = "Categoría"
    verbose_name_plural = "Categorías"
    ordering = ['nombre'] 
class Post(models.Model):

    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

autor = models.ForeignKey(User, on_delete=models.CASCADE)

categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL,
null=True)

contenido = models.TextField()
publicado = models.BooleanField(default=False)


creado = models.DateTimeField(auto_now_add=True)
actualizado = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.titulo

class Meta:
    ordering = ['-creado'] 
    verbose_name = "Post"
    verbose_name_plural = "Posts"