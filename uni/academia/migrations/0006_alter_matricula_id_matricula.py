# Generated by Django 4.0.6 on 2022-07-20 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academia', '0005_alter_docente_apellido_materno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matricula',
            name='id_matricula',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
