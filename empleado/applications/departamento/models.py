from django.db import models

# Create your models here.
 
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50, blank=True)
    shor_name = models.CharField('Nombre corto', max_length=20, unique=True)
    anulate = models.BooleanField('Anulado', default=False) # con este atrivuto sabemos si este departamento esta activo o no
    
    def __str__(self):
       return str(self.id) + '-' + self.name + '-' + self.shor_name
       #return self.name
