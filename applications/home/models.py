from django.db import models

# Create your models here.

class prueba(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)
    cantidad = models.IntegerField(default=0)

    
    def __str__(self):
        return self.titulo + "-" + self.subtitulo
    
    
    


  