# Generated by Django 4.0.6 on 2022-07-20 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academia', '0003_alter_carrera_codigo_alter_carrera_duracion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='sexo',
            field=models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], max_length=1),
        ),
    ]
