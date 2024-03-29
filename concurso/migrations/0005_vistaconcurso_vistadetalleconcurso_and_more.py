# Generated by Django 4.2.3 on 2023-10-26 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concurso', '0004_alter_puesto_vigencia_hasta'),
    ]

    operations = [
        migrations.CreateModel(
            name='VistaConcurso',
            fields=[
                ('anho_concurso', models.IntegerField()),
                ('concurso_id', models.IntegerField(primary_key=True, serialize=False)),
                ('denominacion_conc', models.CharField(max_length=255)),
                ('cargo_id', models.IntegerField()),
                ('descripcion_cargo', models.CharField(max_length=255)),
                ('puesto_id', models.IntegerField()),
                ('descripcion_dependencia', models.CharField(max_length=255)),
                ('descripcion_area', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'vista_concurso',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VistaDetalleConcurso',
            fields=[
                ('concurso_id', models.IntegerField(primary_key=True, serialize=False)),
                ('anho_concurso', models.IntegerField()),
                ('codigo_concurso', models.CharField(max_length=255)),
                ('estado_seguimiento_concurso', models.CharField(max_length=255)),
                ('es_arancelado', models.BooleanField()),
                ('estado_concurso', models.BooleanField()),
                ('vigencia_desde', models.DateField()),
                ('vigencia_hasta', models.DateField()),
                ('denominacion_conc', models.CharField(max_length=255)),
                ('es_postulacion_multiple', models.BooleanField()),
                ('path_documento', models.CharField(max_length=255)),
                ('es_privado', models.BooleanField()),
                ('estado_documento', models.CharField(max_length=255)),
                ('vigente', models.BooleanField()),
            ],
            options={
                'db_table': 'vista_detalle_concurso',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Vis_concursos',
        ),
    ]
