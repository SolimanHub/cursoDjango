from django.contrib import admin
from .models import Empleado, Habilidades

admin.site.register(Habilidades)

# Ordenar los datos que se muestran en empleado
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
    )
    #funcion para full_name dado que no existe en db
    def full_name(self,obj):
        print(obj)
        return obj.first_name + ' ' + obj.last_name

    # A;adimos un buscador  
    search_fields = ('first_name','last_name',)
    # a;adimos filtros
    list_filter = ('job','habilidades',)
    filter_horizontal = ('habilidades',)
admin.site.register(Empleado, EmpleadoAdmin)
