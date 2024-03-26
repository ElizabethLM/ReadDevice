from django.db import models
from rest_framework import serializers
from .models import Dispositivo, PingResult

class DispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
        fields = ('id', 'ip', 'estado', 'nombre', 'puertos')
        
class PingResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = PingResult
        fields = ('id', 'ip', 'estado')