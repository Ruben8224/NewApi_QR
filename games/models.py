from django.db import models
from django.conf import settings

# Create your models here.
class Game(models.Model):
    juego = models.TextField(default='', blank=False)
    fecha_de_lanzamiento = models.TextField(default='', blank=False)
    descripcion = models.TextField(default='', blank=False)
    tipo = models.TextField(default='', blank=False)
    creador = models.TextField(default='', blank=False)
    personajes = models.TextField(default='', blank=False)
    enemigos = models.TextField(default='', blank=False)
    precio = models.IntegerField(default=0)
    musica = models.TextField(default='', blank=False)
    version = models.TextField(default='', blank=False) 
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)