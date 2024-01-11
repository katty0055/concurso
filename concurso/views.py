# from rest_framework import viewsets
# from .models import Cargo
# from .serializers import CargoSerializer

# class CargoViewSet(viewsets.ModelViewSet):
#     serializer_class = CargoSerializer
#     queryset = Cargo.objects.all()

from rest_framework import viewsets
from .models import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import *

class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class AsignaturaViewSet(viewsets.ModelViewSet):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer

class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

class CargoDocumentoViewSet(viewsets.ModelViewSet):
    queryset = CargoDocumento.objects.all()
    serializer_class = CargoDocumentoSerializer

class CargoRequisitoViewSet(viewsets.ModelViewSet):
    queryset = CargoRequisito.objects.all()
    serializer_class = CargoRequisitoSerializer

class CarreraViewSet(viewsets.ModelViewSet):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

class CatedraViewSet(viewsets.ModelViewSet):
    queryset = Catedra.objects.all()
    serializer_class = CatedraSerializer

class ConcursoViewSet(viewsets.ModelViewSet):
    queryset = Concurso.objects.all()
    serializer_class = ConcursoSerializer

class ConcursoDocumentoViewSet(viewsets.ModelViewSet):
    queryset = ConcursoDocumento.objects.all()
    serializer_class = ConcursoDocumentoSerializer

class ConcursoRequisitoViewSet(viewsets.ModelViewSet):
    queryset = ConcursoRequisito.objects.all()
    serializer_class = ConcursoRequisitoSerializer

class DependenciaViewSet(viewsets.ModelViewSet):
    queryset = Dependencia.objects.all()
    serializer_class = DependenciaSerializer

class DiasViewSet(viewsets.ModelViewSet):
    queryset = Dias.objects.all()
    serializer_class = DiasSerializer

class DireccionViewSet(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

class DocumentoPostulacionViewSet(viewsets.ModelViewSet):
    queryset = DocumentoPostulacion.objects.all()
    serializer_class = DocumentoPostulacionSerializer

class EnfasisViewSet(viewsets.ModelViewSet):
    queryset = Enfasis.objects.all()
    serializer_class = EnfasisSerializer

class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer

class ModalidadConcursoViewSet(viewsets.ModelViewSet):
    queryset = ModalidadConcurso.objects.all()
    serializer_class = ModalidadConcursoSerializer

class ModalidadPuestoViewSet(viewsets.ModelViewSet):
    queryset = ModalidadPuesto.objects.all()
    serializer_class = ModalidadPuestoSerializer

class PostulacionViewSet(viewsets.ModelViewSet):
    queryset = Postulacion.objects.all()
    serializer_class = PostulacionSerializer

class PuestoViewSet(viewsets.ModelViewSet):
    queryset = Puesto.objects.all()
    serializer_class = PuestoSerializer

class PuestoDocumentoViewSet(viewsets.ModelViewSet):
    queryset = PuestoDocumento.objects.all()
    serializer_class = PuestoDocumentoSerializer

class PuestoRequisitoViewSet(viewsets.ModelViewSet):
    queryset = PuestoRequisito.objects.all()
    serializer_class = PuestoRequisitoSerializer

class RequisitoViewSet(viewsets.ModelViewSet):
    queryset = Requisito.objects.all()
    serializer_class = RequisitoSerializer

class SedeViewSet(viewsets.ModelViewSet):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class SubAreaViewSet(viewsets.ModelViewSet):
    queryset = SubArea.objects.all()
    serializer_class = SubAreaSerializer

class TipoCargoViewSet(viewsets.ModelViewSet):
    queryset = TipoCargo.objects.all()
    serializer_class = TipoCargoSerializer

class TipoConcursoViewSet(viewsets.ModelViewSet):
    queryset = TipoConcurso.objects.all()
    serializer_class = TipoConcursoSerializer

class TipoDocumentoViewSet(viewsets.ModelViewSet):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoSerializer

class TipoPuestoViewSet(viewsets.ModelViewSet):
    queryset = TipoPuesto.objects.all()
    serializer_class = TipoPuestoSerializer

class TurnoViewSet(viewsets.ModelViewSet):
    queryset = Turno.objects.all()
    serializer_class = TurnoSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = UsuarioFP.objects.all()
    serializer_class = UsuarioFPSerializer

class UsuarioDocumentoViewSet(viewsets.ModelViewSet):
    queryset = UsuarioDocumento.objects.all()
    serializer_class = UsuarioDocumentoSerializer

class VistaConcursoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VistaConcurso.objects.all()
    serializer_class = VistaConcursoSerializer

class VistaDetalleConcursoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VistaDetalleConcurso.objects.all()
    serializer_class = VistaDetalleConcursoSerializer

class VistaAreaPostulaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VistaAreaPostula.objects.all()
    serializer_class = VistaAreaPostulaSerializer
   
