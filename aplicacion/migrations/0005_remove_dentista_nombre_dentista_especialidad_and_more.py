# Generated by Django 4.2.3 on 2023-08-29 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0004_alter_avatar_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dentista',
            name='nombre',
        ),
        migrations.AddField(
            model_name='dentista',
            name='especialidad',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.AddField(
            model_name='dentista',
            name='username',
            field=models.CharField(default='', max_length=80),
        ),
    ]
