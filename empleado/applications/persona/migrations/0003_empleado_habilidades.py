# Generated by Django 3.1.5 on 2021-02-03 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_auto_20210203_0301'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='habilidades',
            field=models.ManyToManyField(to='persona.Habilidades'),
        ),
    ]
