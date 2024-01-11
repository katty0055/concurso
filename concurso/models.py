from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .validators import *
from .managers import UsuarioFPManager
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group as AuthGroup, Permission as AuthPermission
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission



class Direccion(models.Model):
    direccion_id = models.BigAutoField(primary_key=True)
    descripcion_direccion = models.CharField(max_length=100, null=False, blank=True, db_comment='Descripcion de la direccion.')

    def __str__(self) -> str:
        return str(self.direccion_id) + " - " + str(self.descripcion_direccion)

    class Meta:
        db_table = 'direccion'
        db_table_comment = 'Direccion'


class Dependencia(models.Model):
    dependencia_id = models.BigAutoField(primary_key=True)
    direccion = models.ForeignKey('Direccion', on_delete=models.SET_DEFAULT, default=None,blank=True, null=True, db_comment='Identificador de direccion.')
    tipo_dependencia = models.CharField(max_length=100, db_comment='Identifica si es departamento, division, coordinacion, etc.')
    descripcion_dependencia = models.CharField(max_length=100, null=False, blank=True, db_comment='Descripcion de la dependencia.')

    def __str__(self) -> str:
        return str(self.dependencia_id) + " - " + str(self.descripcion_dependencia)

    class Meta:
        db_table = 'dependencia'
        db_table_comment = 'Tabla de dependencias.'


class Area(models.Model):
    area_id = models.BigAutoField(primary_key=True)
    dependencia = models.ForeignKey('Dependencia', on_delete=models.SET_DEFAULT, default=None, blank=True, null=True, db_comment='Identificador de dependencia.')
    descripcion_area = models.CharField(max_length=100, null=False, blank=True, db_comment='Descripcion de modulo/area.')

    def __str__(self) -> str:
        return str(self.area_id) + " - " + str(self.descripcion_area)

    class Meta:
        db_table = 'area'
        db_table_comment = 'Area (Modulos, Division)'


class SubArea(models.Model):
    sub_area_id = models.BigAutoField(primary_key=True)
    area = models.ForeignKey('Area', on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True, db_comment='Idenficador de area/modulo.')
    descripcion_sub_area = models.CharField(max_length=100, null=False, blank=True, db_comment='Descripcion del subarea')

    def __str__(self) -> str:
        return str(self.sub_area_id) + " - " + str(self.descripcion_sub_area)

    class Meta:
        db_table = 'sub_area'
        db_table_comment = 'Tabla de asignaturas/subareas.'


class TipoCargo(models.Model):
    tipo_cargo_id = models.BigAutoField(primary_key=True)
    descripcion_tipo_cargo = models.CharField(max_length=100, null=False, blank=True, db_comment='Descripcion del tipo de cargo.')

    def __str__(self) -> str:
        return str(self.tipo_cargo_id) + " - " + str(self.descripcion_tipo_cargo)


    class Meta:
        db_table = 'tipo_cargo'
        db_table_comment = 'Tabla de tipos de cargos.'


class Cargo(models.Model):
    cargo_id = models.BigAutoField(primary_key=True)
    tipo_cargo = models.ForeignKey('TipoCargo', on_delete=models.SET_DEFAULT, default=None, blank=True, null=True, db_comment='Idetificador de tipo cargo.')
    descripcion_cargo = models.CharField(max_length=100, null=True, blank=True, db_comment='Descripcion del cargo.')

    def __str__(self) -> str:
        return str(self.cargo_id) + " - " + str(self.descripcion_cargo)

    class Meta:
        db_table = 'cargo'
        db_table_comment = 'Tabla de cargos.'


class TipoDocumento(models.Model):
    tipo_documento_id = models.BigAutoField(primary_key=True)
    descripcion_tipo_documento = models.CharField(db_comment='Descripcion del tipo documento.')

    def __str__(self) -> str:
        return str(self.descripcion_tipo_documento)

    class Meta:
        db_table = 'tipo_documento'
        db_table_comment = 'Tabla de los tipos de documentos.'


class Documento(models.Model):
    documento_id = models.BigAutoField(primary_key=True)
    tipo_documento = models.ForeignKey('TipoDocumento', on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True, db_comment='Identificador de tipo documento.')
    path_documento = models.CharField(db_comment='Direccion de donde se almacena el documento.')
    es_privado = models.BooleanField(db_comment='Identifica si es privado o no el documento.')
    estado_documento = models.CharField(db_comment='Estado del documento.')
    vigente = models.BooleanField(blank=True, null=True, db_comment='Vigencia del documento.')

    def __str__(self) -> str:
        return str(self.documento_id)

    class Meta:
        db_table = 'documento'
        db_table_comment = 'Tabla que almacenara a los documentos de todas las entidades.'


class CargoDocumento(models.Model):
    documento_cargo_id = models.BigAutoField(primary_key=True)
    cargo = models.ForeignKey('Cargo', on_delete=models.SET_DEFAULT, default=None, blank=True, null=True, db_comment='Identificador de cargo.')
    documento = models.ForeignKey('Documento', on_delete=models.SET_DEFAULT, default=None, blank=True, null=True, db_comment='Identificador de documento.')

    def __str__(self) -> str:
        return str(self.documento_cargo_id)

    class Meta:
        db_table = 'cargo_documento'
        db_table_comment = 'Tabla que relaciona documento con cargo.'


class Requisito(models.Model):
    requisito_id = models.BigAutoField(primary_key=True)
    descripcion_requisito = models.CharField(db_comment='Descripcion del requisito.')

    def __str__(self) -> str:
        return str(self.requisito_id) + " - " + str(self.descripcion_requisito)

    class Meta:
        db_table = 'requisito'
        db_table_comment = 'Requisitos para la postulacion al concurso.'


class CargoRequisito(models.Model):
    cargo_requisito_id = models.BigAutoField(primary_key=True)
    cargo = models.ForeignKey('Cargo', on_delete=models.SET_DEFAULT, default=None, blank=True, null=True, db_comment='Identificador de cargo.')
    requisito = models.ForeignKey('Requisito', on_delete=models.SET_DEFAULT, default=None, blank=True, null=True, db_comment='Identificador de requisito.')

    def __str__(self) -> str:
        return str(self.cargo_requisito_id)

    class Meta:
        db_table = 'cargo_requisito'
        db_table_comment = 'Tabla que relaciona los requisitos con el cargo.'


class Carrera(models.Model):
    carrera_id = models.BigAutoField(primary_key=True)
    descripcion_carrera = models.CharField(max_length=100, null=True, blank=True, db_comment='Descripcion de carrera.')

    def __str__(self) -> str:
        return str(self.carrera_id) + " - " + str(self.descripcion_carrera)

    class Meta:
        db_table = 'carrera'
        db_table_comment = 'Tabla de carreras.'


class Enfasis(models.Model):
    enfasis_id = models.BigAutoField(primary_key=True)
    carrera = models.ForeignKey('Carrera', on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True, db_comment='Identificacion de Carrera.')
    descripcion_enfasis = models.CharField(db_comment='Descripcion de enfasis.')

    def __str__(self) -> str:
        return str(self.enfasis_id) + " - " + str(self.descripcion_enfasis)

    class Meta:
        db_table = 'enfasis'
        db_table_comment = 'Tabla de enfasis.'


class Asignatura(models.Model):
    asignatura_id = models.BigAutoField(primary_key=True)
    sub_area = models.ForeignKey('SubArea', on_delete=models.SET_DEFAULT, default=None, blank=True, null=True, db_comment='Identificador de asignatura.')
    codigo = models.CharField(max_length=10, null=False, blank=True)
    descripcion_asignatura = models.CharField(max_length=200, null=False, blank=True)

    def __str__(self) -> str:
        return str(self.asignatura_id) + " - " + str(self.descripcion_asignatura)

    class Meta:
        db_table = 'asignatura'
        db_table_comment = 'Tabla de asignaturas.'


class Catedra(models.Model):
    catedra_id = models.BigAutoField(primary_key=True)
    asignatura = models.ForeignKey('Asignatura', on_delete=models.SET_DEFAULT, default=None, blank=True, null=True, db_comment='Identificador de asignatura.')
    seccion = models.CharField(db_comment='Seccion de la catedra.')
    carrera = models.ForeignKey('Carrera', on_delete=models.SET_DEFAULT, default=None,blank=True, null=True, db_comment='Identificacion de Carrera.')
    enfasis = models.ForeignKey('Enfasis', on_delete=models.SET_DEFAULT, default=None,blank=True, null=True, db_comment='Idenficacion de enfasis.')

    def __str__(self) -> str:
        return str(self.catedra_id)

    class Meta:
        db_table = 'catedra'
        db_table_comment = 'Tabla de catedra.'


class ModalidadConcurso(models.Model):
    modalidad_concurso_id = models.BigAutoField(primary_key=True)
    descripcion_modalidad_concurso = models.CharField(db_comment='Descripcion de la modalidad del concurso.')

    def __str__(self) -> str:
        return str(self.modalidad_concurso_id) + " - " + str(self.descripcion_modalidad_concurso)

    class Meta:
        db_table = 'modalidad_concurso'
        db_table_comment = 'Modalidades del concurso. Ejemplo(Externo, Abreviado, Interno)'


class TipoConcurso(models.Model):
    tipo_concurso_id = models.BigAutoField(primary_key=True)
    descripcion_tipo_concurso = models.CharField(db_comment='Descripcion del tipo concurso.')

    def __str__(self) -> str:
        return str(self.tipo_concurso_id) + " - " + str(self.descripcion_tipo_concurso)

    class Meta:
        db_table = 'tipo_concurso'
        db_table_comment = 'Tabla de tipos de concursos.'


class Concurso(models.Model):
    concurso_id = models.BigAutoField(primary_key=True)
    anho_concurso = models.SmallIntegerField(db_comment='Anho del concurso.')
    codigo_concurso = models.CharField(db_comment='Codigo del concurso.')
    estado_seguimiento_concurso = models.CharField(blank=True, null=True, db_comment='Estado de seguimiento del concurso.')
    estado_concurso = models.BooleanField(default=True,null=False, db_comment='Borrado logico del concurso.')
    tipo_concurso = models.ForeignKey('TipoConcurso', on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True, db_comment='Identificador de tipo concurso.')
    modalidad_concurso = models.ForeignKey('ModalidadConcurso', on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True, db_comment='Columna que identifica a la tabla modalidad.')
    es_arancelado = models.BooleanField(blank=True, null=True, db_comment='Identificador de si es arancelado o no.')
    vigencia_desde = models.DateField(null=True, blank=True, db_comment='Fecha de inicio de concurso.')
    vigencia_hasta = models.DateField(null=True, blank=True, db_comment='Fecha de fin de concurso.')
    denominacion_conc = models.CharField(db_comment='Denominacion del concurso')
    es_postulacion_multiple = models.BooleanField(blank=True, null=True, db_comment='Identifica si en el concurso se admiten mas de una postulacion')

    def __str__(self) -> str:
        return self.denominacion_conc + " - " + str(self.anho_concurso)

    class Meta:
        db_table = 'concurso'
        db_table_comment = 'Tabla de concursos.'


class ConcursoDocumento(models.Model):
    id_concurso_documento = models.BigAutoField(primary_key=True)
    documento = models.ForeignKey('Documento', on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True, db_comment='Identificador de documento.')
    concurso = models.ForeignKey('Concurso', on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True, db_comment='Identificador de concurso.')

    def __str__(self) -> str:
        return str(self.id_concurso_documento)

    class Meta:
        db_table = 'concurso_documento'
        db_table_comment = 'Tabla que relaciona concurso  y documento.'


class ConcursoRequisito(models.Model):
    concurso_requisito_id = models.BigAutoField(primary_key=True)
    requisito = models.ForeignKey('Requisito', on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True, db_comment='Identificador de requisito.')
    concurso = models.ForeignKey('Concurso', on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True, db_comment='Identificador de concurso.')

    def __str__(self) -> str:
        return str(self.concurso_requisito_id)

    class Meta:
        db_table = 'concurso_requisito'
        db_table_comment = 'Tabla donde se relacionan los requisitos con el concurso.'



class Dias(models.Model):
    dia_id = models.BigAutoField(primary_key=True)
    descripcion_dia = models.CharField(db_comment='Descripcion de dia.')

    def __str__(self) -> str:
        return self.descripcion_dia

    class Meta:
        db_table = 'dias'
        db_table_comment = 'Tabla de dias.'


class Postulacion(models.Model):
    postulacion_id = models.BigAutoField(primary_key=True)
    concurso = models.ForeignKey('Concurso', on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True, db_comment='Identificador de concurso.')
    cargo = models.ForeignKey('Cargo', on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True, db_comment='Identificador de cargo.')
    anho = models.SmallIntegerField(db_comment='Anho de la postulacion.')
    usuario = models.ForeignKey('UsuarioFP', on_delete=models.SET_DEFAULT, default=None, blank=True, null=True, db_comment='Identificador de usuario.')
    fecha_postulacion = models.DateTimeField(null=False, db_comment='Fecha de la postulacion.')
    puesto = models.ForeignKey('Puesto', on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True)

    def __str__(self):
        return str(self. postulacion_id) + " - " + "Postulacion a " + self.concurso.denominacion_conc

    class Meta:
        db_table = 'postulacion'
        db_table_comment = 'Tabla de postulacion.'


class DocumentoPostulacion(models.Model):
    documento_postulacion_id = models.BigAutoField(primary_key=True)
    postulacion = models.ForeignKey('Postulacion', on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True, db_comment='Identificador de postulacion')
    documento = models.ForeignKey('Documento', on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True, db_comment='Identificador de documento.')
    aprobado = models.BooleanField(blank=True, null=True, db_comment='Verificacion de la aprobacion del documento.')

    def __str__(self) -> str:
        return str(self.documento_postulacion_id)

    class Meta:
        db_table = 'documento_postulacion'
        db_table_comment = 'Tabla que relaciona documento con postulacion.'



class ModalidadPuesto(models.Model):
    modalidad_puesto_id = models.BigAutoField(primary_key=True)
    descripcion_modalidad = models.CharField(db_comment='Descripcion modalidad.')

    def __str__(self) -> str:
        return str(self.modalidad_puesto_id) + " - " + str(self.descripcion_modalidad)

    class Meta:
        db_table = 'modalidad_puesto'
        db_table_comment = 'Tabla de modalidades de puestos.'


class Sede(models.Model):
    sede_id = models.BigAutoField(primary_key=True)
    descripcion_sede = models.CharField(db_comment='Descripcion de sede.')

    def __str__(self) -> str:
        return str(self.sede_id) + " - " + str(self.descripcion_sede)

    class Meta:
        db_table = 'sede'
        db_table_comment = 'Tabla de sede.'


class Turno(models.Model):
    turno_id = models.BigAutoField(primary_key=True)
    descripcion_turno = models.CharField(db_comment='Descripcion de turno.')
    horario_referencial = models.CharField(blank=True, null=True, db_comment='Horario referencial del turno')

    def __str__(self) -> str:
        return str(self.turno_id) + " - " + str(self.descripcion_turno)

    class Meta:
        db_table = 'turno'
        db_table_comment = 'Tabla de turnos.'       


class TipoPuesto(models.Model):
    tipo_puesto_id = models.BigAutoField(primary_key=True)
    descripcion_puesto = models.CharField(db_comment='Descripcion del puesto.')

    def __str__(self) -> str:
        return str(self.tipo_puesto_id) + " - " + str(self.descripcion_puesto)

    class Meta:
        db_table = 'tipo_puesto'
        db_table_comment = 'Tipo de puesto (nombrado, contratado, nombrado temporal)'


class Puesto(models.Model):
    puesto_id = models.BigAutoField(primary_key=True)
    direccion = models.ForeignKey('Direccion', on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True, db_comment='Identificador de direccion.')
    dependencia = models.ForeignKey('Dependencia', on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True, db_comment='Identificador de dependencia.')
    area = models.ForeignKey(Area, on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True, db_comment='Idenficador de area/modulo.')
    perodicidad = models.CharField(blank=True, null=True, db_comment='Frecuencia de asistencia. (Lunes a viernes)')
    sub_area = models.ForeignKey('SubArea', on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True, db_comment='Identificador de asignatura.')
    catedra = models.ForeignKey('Catedra', on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True, db_comment='Identificacion de la catedra.')
    turno = models.ForeignKey('Turno', on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True, db_comment='Identificador de turno.')
    cargo = models.ForeignKey('Cargo', on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True, db_comment='Identificador de cargo.')
    vigencia_hasta = models.DateField(validators=[validate_future_date], blank=True, null=True, db_comment='Fecha de fin de puesto.')
    vigencia_desde = models.DateField(blank=True, null=True, db_comment='Fecha de inicio del puesto.')
    sede = models.ForeignKey('Sede', on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True, db_comment='Identificacion de sede.')
    periodo_contrato = models.CharField(blank=True, null=True)
    tipo_puesto = models.ForeignKey('TipoPuesto', on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True, db_comment='Identificador de tipo de puesto.')
    remuneracion = models.IntegerField(blank=True, null=True, db_comment='Remuneracion del puesto.')
    modalidad_puesto = models.ForeignKey('ModalidadPuesto', on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True, db_comment='Modalidad del puesto(Traslado Permanente)')
    estado_puesto = models.BooleanField(default=True, null=False, db_comment='Estado del puesto.')
    convocatoria = models.SmallIntegerField(db_comment='Convocatoria del puesto.(periodo academico: primer o segundo semestre)')
    anho_puesto = models.SmallIntegerField(db_comment='Anho del puesto.')
    concurso = models.ForeignKey(Concurso, on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True)
    categoria_salarial = models.CharField(blank=True, null=True, db_comment='Categoria salarial.')
    cantidad_puestos = models.BigIntegerField(validators=[validate_positive_number], blank=True, null=True)

    def __str__(self) -> str:
        return "Puesto para " + self.direccion.descripcion_direccion + ", Dependencia: " + self.dependencia.descripcion_dependencia

    class Meta:
        db_table = 'puesto'
        db_table_comment = 'Tabla de puestos(catedras).'


class Horario(models.Model):
    horario_id = models.BigAutoField(primary_key=True)
    puesto = models.ForeignKey('Puesto', on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True, db_comment='Identificador de puesto.')
    dia = models.ForeignKey(Dias, on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True, db_comment='Identificador de dia.')
    hora_desde = models.DateTimeField(null=True, blank=True, db_comment='Horario de inicio.')
    hora_hasta = models.DateTimeField(null=True, blank=True, db_comment='Horario de finalizacion.')

    def __str__(self) -> str:
        return str(self.horario_id)

    class Meta:
        db_table = 'horario'
        db_table_comment = 'Tabla de horarios.'


class PuestoDocumento(models.Model):
    id_puesto_documento = models.BigAutoField(primary_key=True)
    documento = models.ForeignKey('Documento', on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True, db_comment='Identificador de documento.')
    puesto = models.ForeignKey('Puesto', on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True, db_comment='Identificador de puesto.')
    fecha_agregada = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.id_puesto_documento)

    class Meta:
        db_table = 'puesto_documento'
        db_table_comment = 'Tabla que relaciona puesto y documento.'


class PuestoRequisito(models.Model):
    puesto_requisito_id = models.BigAutoField(primary_key=True)
    puesto_id = models.ForeignKey('Puesto', on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True, db_comment='Identificador de puesto.')
    requisito_id = models.ForeignKey('Requisito', on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True, db_comment='Identificador de requisito.')

    def __str__(self) -> str:
        return str(self.puesto_requisito_id)

    class Meta:
        db_table = 'puesto_requisito'
        db_table_comment = 'Tabla que relaciona los requisitos con el puesto.'


# class Usuario(models.Model):
#     usuario_id = models.BigAutoField(primary_key=True)
#     telefono = models.CharField(db_comment='Telefono de la persona.')
#     direccion_particular = models.CharField(db_comment='Direccion particular.')
#     fecha_nacimiento = models.DateField(blank=True, null=True, db_comment='Fecha de nacimiento de la persona.')
#     lugar_nacimiento = models.CharField(blank=True, null=True, db_comment='Lugar de nacimiento de la persona.')
#     nro_documento = models.CharField(max_length=15, db_comment='Numero de documento.')
#     apellido = models.CharField(max_length=150, db_comment='Apellido de la persona.')
#     nombre = models.CharField(max_length=150, db_comment='Nombre de la persona.')
#     correo = models.CharField(db_comment='Correo de la persona.')
#     usuario_nombre = models.CharField(max_length=50, db_comment='Nombre de usuario.')
#     password = models.CharField(db_comment='Contrasenha del usuario.')
#     estado_usuario = models.BooleanField(default=True, null=False, db_comment='Estado de la cuenta (True, False)')
#     sexo = models.CharField(max_length=1, blank=True, null=True)
#     documento_duplicado = models.CharField(max_length=3, blank=True, null=True)

#     def __str__(self) -> str:
#         return self.usuario_id

#     class Meta:
#         db_table = 'usuario'
#         db_table_comment = 'Tabla de usuarios'

class UsuarioFP(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    telefono = models.CharField(max_length=255, db_comment='Telefono de la persona.')
    direccion_particular = models.CharField(max_length=255, db_comment='Direccion particular.')
    fecha_nacimiento = models.DateField(blank=True, null=True, db_comment='Fecha de nacimiento de la persona.')
    lugar_nacimiento = models.CharField(max_length=255, blank=True, null=True, db_comment='Lugar de nacimiento de la persona.')
    documento = models.CharField(max_length=20, unique=True, db_comment='Numero de documento.')
    apellido = models.CharField(max_length=150, db_comment='Apellido de la persona.')
    nombre = models.CharField(max_length=150, db_comment='Nombre de la persona.')
    correo = models.EmailField(db_comment='email')
    email = models.EmailField(unique=True, default="email@pol.una.py")
    usuario_nombre = models.CharField(max_length=50, db_comment='Nombre de usuario.')
    #password = models.CharField(max_length=128, db_comment='Contrasenha del usuario.')
    estado_usuario = models.BooleanField(default=True, null=False, db_comment='Estado de la cuenta (True, False)')
    sexo = models.CharField(max_length=1, blank=True, null=True)
    documento_duplicado = models.CharField(max_length=3, blank=True, null=True)
    groups = models.ManyToManyField(Group, related_name='usuarios', blank=True,db_table='usuariofp_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='usuariofp_set', blank=True, verbose_name='user permissions', db_table='usuariofp_user_permissions')
    idsistema = models.IntegerField(null=True, blank=True, default=1, db_comment='Identificador del sistema que se autentica')
    USERNAME_FIELD = 'documento'
    REQUIRED_FIELDS = ['email','telefono','direccion_particular','fecha_nacimiento'
                       ,'lugar_nacimiento','nombre','apellido','email','sexo'] 
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioFPManager()

    def __str__(self):
        return  self.documento
    class Meta:
        db_table = 'usuariofp'
        db_table_comment = 'Tabla de usuarios FPUNA'

class Group(AuthGroup):
    class Meta:
        proxy = True
        db_table = 'auth_group'
        db_table_comment = 'Tabla de grupos de usuarios'

class Permission(AuthPermission):
    class Meta:
        proxy = True
        db_table = 'auth_permission'
        db_table_comment = 'Tabla de permisos de usuarios'
class UsuarioDocumento(models.Model):
    usuario_documento_id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey('UsuarioFP', on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True, db_comment='Identificador de usuario.')
    fecha_subida = models.DateField(null=True, blank=True, db_comment='Fecha de subida del documento.')
    documento = models.ForeignKey('Documento', on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True, db_comment='Identificador de documento.')

    def __str__(self) -> str:
        return str(self.usuario_documento_id)

    class Meta:
        db_table = 'usuario_documento'
        db_table_comment = 'Tabla en donde se relacionan los documentos con los usuarios.'


class VistaConcurso(models.Model):
    anho_concurso = models.IntegerField()
    concurso_id = models.IntegerField(primary_key=True)
    denominacion_conc = models.CharField(max_length=255)
    cargo_id = models.IntegerField()
    descripcion_cargo = models.CharField(max_length=255)
    puesto_id = models.IntegerField()
    descripcion_dependencia = models.CharField(max_length=255)
    descripcion_area = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'vista_concurso'


class VistaDetalleConcurso(models.Model):
    concurso_id = models.IntegerField(primary_key=True)
    anho_concurso = models.IntegerField()
    codigo_concurso = models.CharField(max_length=255)
    estado_seguimiento_concurso = models.CharField(max_length=255)
    es_arancelado = models.BooleanField()
    estado_concurso = models.BooleanField()
    vigencia_desde = models.DateField()
    vigencia_hasta = models.DateField()
    denominacion_conc = models.CharField(max_length=255)
    es_postulacion_multiple = models.BooleanField()
    path_documento = models.CharField(max_length=255)
    es_privado = models.BooleanField()
    estado_documento = models.CharField(max_length=255)
    vigente = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'vista_detalle_concurso'


class VistaAreaPostula(models.Model):
    puesto_id = models.IntegerField(primary_key=True)
    dependencia_id = models.IntegerField()
    descripcion_dependencia = models.CharField(max_length=255)
    area_id = models.IntegerField()
    descripcion_area = models.CharField(max_length=255)
    sub_area_id = models.IntegerField()
    descripcion_sub_area = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'vista_area_postula'