from django.db import models
from applications.departamento.models import Departamento

# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades empleados'
        
    def __str__(self):
        return str(self.id) + '-' + self.habilidad

class Empleado(models.Model):
    JOB_CHOICES = (
            ('0', 'CONTADOR'),
            ('1', 'ADMINISTRADOR'),
            ('2', 'ECONOMISTA'),
            ('3', 'OTRO'),
    )

    """ Modelo para tabla empleado """
    first_name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField(
            'NombreCompleto',
            max_length=120,
            blank=True,
    )
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    # la siguiente linea es una relacion de 1 a muchos
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)

    # la siguiente linea es una relacion de muchos a muchos
    habilidades = models.ManyToManyField(Habilidades)

    class Meta:
        verbose_name = 'Personal'
        verbose_name_plural = 'Personal de la empresa'
        ordering = ['first_name']
        unique_together = ('first_name', 'last_name')

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name
