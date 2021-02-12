"""empleado URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'persona_app'

urlpatterns = [
    #path(
    #    '/', 
    #    views.as_view()
    #),
    path(
        #para el inicio se deja vacia la direccion
        'administrar/', 
        views.ListAdministrador.as_view(),
        name='pag_administrador'
    ),
    path(
        #para el inicio se deja vacia la direccion
        '', 
        views.InicioView.as_view(),
        name='pag_home'
    ),
    path(
        'delete/<pk>/', 
        views.EmpleadoDeleteView.as_view(),
        name='eliminar-registro'
    ),
    path(
        'update/<pk>/', 
        views.EmpleadoUpdateView.as_view(),
        name='modificar_empleado'
    ),
    path('success/', views.SuccessView.as_view(), name='correcto'),
    path(
        'add/', 
        views.EmpleadoCreateView.as_view(),
        name='add_emp'
        ),
    path(
        'ver-empleado/<pk>', 
        views.EmpleadoDetailView.as_view(),
        name='empleado_detail',
    ),
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view()),
    path(
        'listar-empleados-area/<shorname>/', 
        views.ListByAreaEmpleado.as_view(),
        name='emp_depa',
    ),
    path('listar-empleados-trabajo/<job_name>/', views.ListByJob.as_view()),
    path('buscar-empleado/', views.ListEmpByKWord.as_view()),
    path('lista-paginada-empleados/', 
        views.ListPaginacion.as_view(),
        name = 'empleados_all',
    ),
    path('lista-habilidades/', views.ListHabilidadesEmpleado.as_view()),
]
