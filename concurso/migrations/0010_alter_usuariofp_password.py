# Generated by Django 4.2.3 on 2023-10-25 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concurso', '0009_alter_usuariofp_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariofp',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
