from django.db import models

# Create your models here.
class Persona(models.Model): 
    nombre = models.CharField(max_length=100)
    fecha_ingreso=  models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre