# Generated by Django 4.2.3 on 2023-10-25 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concurso', '0006_usuariofp_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariofp',
            name='email',
            field=models.EmailField(default='email@pol.una.py', max_length=254, unique=True),
        ),
    ]