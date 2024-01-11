# from rest_framework import serializers
# from .models import Cargo

# class CargoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cargo
#         fields = ['id','descripcion','anho','convocatoria','catedra_id','departamento_id','area_id','plazas']

from rest_framework import serializers
from .models import *


class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = '__all__'

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'

class CargoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CargoDocumento
        fields = '__all__'

class CargoRequisitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CargoRequisito
        fields = '__all__'

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = '__all__'

class CatedraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catedra
        fields = '__all__'    

class ConcursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concurso
        fields = '__all__'      

class ConcursoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConcursoDocumento
        fields = '__all__'  

class ConcursoRequisitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConcursoRequisito
        fields = '__all__'

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'        

class DependenciaSerializer(serializers.ModelSerializer):
    direccion = DireccionSerializer()

    class Meta:
        model = Dependencia
        fields = '__all__'

class AreaSerializer(serializers.ModelSerializer):
    dependencia = DependenciaSerializer()

    class Meta:
        model = Area
        fields = '__all__'

class SubAreaSerializer(serializers.ModelSerializer):
    area = AreaSerializer()

    class Meta:
        model = SubArea
        fields = '__all__'

class DiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dias
        fields = '__all__'
        
class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = '__all__'

class DocumentoPostulacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentoPostulacion
        fields = '__all__'

class EnfasisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfasis
        fields = '__all__'

class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = '__all__'

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = '__all__'

class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = '__all__'

class ModalidadConcursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModalidadConcurso
        fields = '__all__'

class ModalidadConcursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModalidadConcurso
        fields = '__all__'

class ModalidadPuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModalidadPuesto
        fields = '__all__'

class PostulacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postulacion
        fields = '__all__'

class PuestoSerializer(serializers.ModelSerializer):
    direccion = DireccionSerializer()
    dependencia = DependenciaSerializer()
    area = AreaSerializer()
    sub_area = SubAreaSerializer()
    catedra = CatedraSerializer()
    turno = TurnoSerializer()
    cargo = CargoSerializer()
    sede = SedeSerializer()
    concurso = ConcursoSerializer()

    class Meta:
        model = Puesto
        fields = '__all__'

class PuestoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PuestoDocumento
        fields = '__all__'

class PuestoRequisitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PuestoRequisito
        fields = '__all__'

class RequisitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requisito
        fields = '__all__'

class TipoCargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCargo
        fields = '__all__'

class TipoConcursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoConcurso
        fields = '__all__'

class TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento
        fields = '__all__'

class TipoPuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPuesto
        fields = '__all__'


class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = '__all__'

class UsuarioFPSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioFP
        fields = '__all__'

class UsuarioDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioDocumento
        fields = '__all__'

class VistaConcursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VistaConcurso
        fields = '__all__'

class VistaDetalleConcursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VistaDetalleConcurso
        fields = '__all__'

class VistaAreaPostulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = VistaAreaPostula
        fields = '__all__'