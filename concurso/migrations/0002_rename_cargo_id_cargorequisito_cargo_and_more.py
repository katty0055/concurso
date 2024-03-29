# Generated by Django 4.2.3 on 2023-10-11 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('concurso', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cargorequisito',
            old_name='cargo_id',
            new_name='cargo',
        ),
        migrations.RenameField(
            model_name='cargorequisito',
            old_name='requisito_id',
            new_name='requisito',
        ),
        migrations.RenameField(
            model_name='catedra',
            old_name='asignatura_id',
            new_name='asignatura',
        ),
        migrations.RenameField(
            model_name='catedra',
            old_name='carrera_id',
            new_name='carrera',
        ),
        migrations.RenameField(
            model_name='catedra',
            old_name='enfasis_id',
            new_name='enfasis',
        ),
        migrations.RenameField(
            model_name='concurso',
            old_name='modalidad_concurso_id',
            new_name='modalidad_concurso',
        ),
        migrations.RenameField(
            model_name='concurso',
            old_name='tipo_concurso_id',
            new_name='tipo_concurso',
        ),
        migrations.RenameField(
            model_name='concursodocumento',
            old_name='concurso_id',
            new_name='concurso',
        ),
        migrations.RenameField(
            model_name='concursodocumento',
            old_name='documento_id',
            new_name='documento',
        ),
        migrations.RenameField(
            model_name='concursorequisito',
            old_name='concurso_id',
            new_name='concurso',
        ),
        migrations.RenameField(
            model_name='concursorequisito',
            old_name='requisito_id',
            new_name='requisito',
        ),
        migrations.RenameField(
            model_name='dependencia',
            old_name='direccion_id',
            new_name='direccion',
        ),
        migrations.RenameField(
            model_name='documentopostulacion',
            old_name='documento_id',
            new_name='documento',
        ),
        migrations.RenameField(
            model_name='documentopostulacion',
            old_name='postulacion_id',
            new_name='postulacion',
        ),
        migrations.RenameField(
            model_name='enfasis',
            old_name='carrera_id',
            new_name='carrera',
        ),
        migrations.RenameField(
            model_name='horario',
            old_name='dia_id',
            new_name='dia',
        ),
        migrations.RenameField(
            model_name='horario',
            old_name='puesto_id',
            new_name='puesto',
        ),
        migrations.RenameField(
            model_name='postulacion',
            old_name='cargo_id',
            new_name='cargo',
        ),
        migrations.RenameField(
            model_name='postulacion',
            old_name='concurso_id',
            new_name='concurso',
        ),
        migrations.RenameField(
            model_name='postulacion',
            old_name='puesto_id',
            new_name='puesto',
        ),
        migrations.RenameField(
            model_name='postulacion',
            old_name='usuario_id',
            new_name='usuario',
        ),
        migrations.RenameField(
            model_name='puesto',
            old_name='area_id',
            new_name='area',
        ),
        migrations.RenameField(
            model_name='puesto',
            old_name='cargo_id',
            new_name='cargo',
        ),
        migrations.RenameField(
            model_name='puesto',
            old_name='catedra_id',
            new_name='catedra',
        ),
        migrations.RenameField(
            model_name='puesto',
            old_name='concurso_id',
            new_name='concurso',
        ),
        migrations.RenameField(
            model_name='puesto',
            old_name='dependencia_id',
            new_name='dependencia',
        ),
        migrations.RenameField(
            model_name='puesto',
            old_name='direccion_id',
            new_name='direccion',
        ),
        migrations.RenameField(
            model_name='puesto',
            old_name='modalidad_puesto_id',
            new_name='modalidad_puesto',
        ),
        migrations.RenameField(
            model_name='puesto',
            old_name='sede_id',
            new_name='sede',
        ),
        migrations.RenameField(
            model_name='puesto',
            old_name='sub_area_id',
            new_name='sub_area',
        ),
        migrations.RenameField(
            model_name='puesto',
            old_name='tipo_puesto_id',
            new_name='tipo_puesto',
        ),
        migrations.RenameField(
            model_name='puesto',
            old_name='turno_id',
            new_name='turno',
        ),
        migrations.RenameField(
            model_name='puestodocumento',
            old_name='documento_id',
            new_name='documento',
        ),
        migrations.RenameField(
            model_name='puestodocumento',
            old_name='puesto_id',
            new_name='puesto',
        ),
        migrations.RenameField(
            model_name='subarea',
            old_name='area_id',
            new_name='area',
        ),
    ]
