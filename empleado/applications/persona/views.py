# Nota general: para declarar una vista se agrega en el archivo urls.py

#Requerimientos con ListView
# 1 Lista todos los empleados de la empresa
# 2 Lista todos los empleados que pertenecen a un area especifica de la empresa
# 3 Listar empleados por trabajo
# 4 Listar empleados por palabra clave
# 5 Listar habilidades de un empleado

from django.shortcuts import render
# nota: lo primero que se hace para trabajar con listview es importar el listview
# con reverse_lazy declaramos urls 'redireccion'
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    TemplateView,
    CreateView,
    DeleteView,
)

#importar el modelo con el que se va a trabajar
from .models import Empleado
# forms
from .forms import EmpleadoForm

class ListAdministrador(ListView):
    template_name = 'persona/administrar.html'
    paginate_by = 10
    ordering = 'first_name'
    def get_queryset(self):
        palabraClave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
                first_name__icontains=palabraClave
        )
        return lista


class InicioView(TemplateView):
    """Vista que carga la pagina de inicio"""
    template_name = 'persona/home.html'
    

# 1 Lista todos los empleados de la empresa
class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    model = Empleado

# 2 Lista todos los empleados que pertenecen a un area especifica de la empresa

class ListByAreaEmpleado(ListView):
    template_name = 'persona/empleados_depa.html'
    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
                departamento__shor_name=area
        )
        return lista


# 3 Listar empleados por trabajo

class ListByJob(ListView):
    template_name = 'persona/list_by_job.html'
    def get_queryset(self):
        trabajo = self.kwargs['job_name']
        lista = Empleado.objects.filter(
                job=trabajo
        )
        return lista

# 4 Listar empleados por palabra clave

class ListEmpByKWord(ListView):
    template_name = 'persona/list_by_kw.html'
    context_object_name = 'empleadosKW'
    def get_queryset(self):
        palabraClave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
                first_name=palabraClave
        )
        print('_+++++++++++++_')
        print('Lista resultado: ', lista)
        return lista

# Lista todos los empleados con paginacion
class ListPaginacion(ListView):
    template_name = 'persona/list_paginacion.html'
    paginate_by = 10
    ordering = 'first_name'
    def get_queryset(self):
        palabraClave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
                first_name__icontains=palabraClave
        )
        return lista

# 5 Listar habilidades de un empleado
class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'
    def get_queryset(self):
        '''modificar esta lista para no meter el id directo en el codigo '''
        empleado = Empleado.objects.get(id=10)
        print(empleado.habilidades.all())
        return empleado.habilidades.all()

# Trabajando con DetailView

class  EmpleadoDetailView(DetailView):
    model = Empleado# este parametro es obligatorio
    template_name = 'persona/detail_empleado.html'
    

# CreateView

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = 'persona/add.html'
    #fields = ('__all__')
    # el atributo fields tambien se puede declarar de la siguente manera
    '''fields = [
            'first_name',
            'last_name',
            'job',
            'departamento',
            'avatar',
            'habilidades',
    ]'''
    form_class = EmpleadoForm
    # para ser mas especifico con los parametros deseados
    success_url = reverse_lazy('persona_app:pag_home')
    def form_valid(self, form):
        #logica del proceso
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class SuccessView(TemplateView):
    template_name = 'persona/success.html'

class EmpleadoUpdateView(UpdateView):
    template_name = 'persona/update.html'
    model = Empleado
    fields = [
            'first_name',
            'last_name',
            'job',
            'departamento',
            'habilidades',
    ]
    success_url = '.'
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('======Metodo POST========')
        print('=========================')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print('======Form Valid==========')
        print('===========================')
        return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'persona/delete.html'    
    success_url = reverse_lazy('persona_app:correcto')
