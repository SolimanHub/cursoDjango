# Generated by Django 3.1.5 on 2021-02-05 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_empleado_habilidades'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='full_name',
            field=models.CharField(blank=True, max_length=120, verbose_name='NombreCompleto'),
        ),
        migrations.AlterField(
            model_name='habilidades',
            name='habilidad',
            field=models.CharField(max_length=50, verbose_name='Habilidad'),
        ),
    ]
