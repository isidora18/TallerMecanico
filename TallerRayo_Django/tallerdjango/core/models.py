from django.db import models
from django.db.models.base import Model
# Create your models here.

class Perfiltrabajador(models.Model):
    id_Perfiltrabajador = models.IntegerField(primary_key=True, verbose_name="ID Trabajador")
    Perfiltrabajador = models.CharField(max_length=60, verbose_name="Perfil del Trabajador")
    
    def __str__(self):
        return self.Perfiltrabajador

class Vehiculo(models.Model):
    id_Vehiculo = models.IntegerField(primary_key=True, verbose_name="ID Vehiculo")
    Vehiculo = models.CharField(max_length=60, verbose_name="Vehiculo")
    
    def __str__(self):
        return self.Vehiculo