from django.db import models

class Usuario(models.Model):
    NOM_USUARIO = models.CharField(max_length=100, unique=True)
    CONTRASENA = models.CharField(max_length=100)