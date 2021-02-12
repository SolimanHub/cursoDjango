from django.db import models

# Create your models here.
 
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50, blank=True)
    shor_name = models.CharField('Nombre corto', max_length=20, unique=True)
    anulate = models.BooleanField('Anulado', default=False) # con este atrivuto sabemos si este departamento esta activo o no
    
    class Meta:
        #investigar mas metodos de esta clase Meta
        verbose_name = 'Mi departamento'
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['shor_name']
        unique_together = ('name', 'shor_name')

    def __str__(self):
       return str(self.id) + '-' + self.name + '-' + self.shor_name
       #return self.name
