from django.db import models

class Dispositivo(models.Model):
    ip = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    nombre = models.CharField(max_length=200)
    puertos = models.CharField(max_length=200)
    
class PingResult(models.Model):
    ip = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)