from django.db import models
from .choices import empleos_wta
from applications.departamento.models import Departamento
# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField("Nombres", max_length=50)
    apellido = models.CharField("Apellidos", max_length=50)
    trabajo = models.CharField("Trabajo", max_length=1, choices= empleos_wta)
    imagen= models.ImageField("Imagen", upload_to=None, height_field=None, width_field=None, max_length=None)
    departamento = models.ForeignKey(Departamento, verbose_name= "Cargo del empleado", on_delete=models.CASCADE, default=1)
    

    def __str__(self):
        return self.nombre + "-" + self.apellido  +  "-" + str(self.id)
    