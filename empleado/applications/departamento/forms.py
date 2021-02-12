from django import forms

class NewDepaForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    departamento = forms.CharField(max_length=50)
    depa = forms.CharField(max_length=20)
