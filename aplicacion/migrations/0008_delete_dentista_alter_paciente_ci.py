# Generated by Django 4.2.3 on 2023-08-30 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0007_profesional'),
    ]

    operations = [
        migrations.DeleteModel(
            name='dentista',
        ),
        migrations.AlterField(
            model_name='paciente',
            name='ci',
            field=models.PositiveIntegerField(max_length=20, unique=True),
        ),
    ]