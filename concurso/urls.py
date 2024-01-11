from rest_framework import routers
from .views import *
from django.urls import path, include
from djoser.views import TokenCreateView

router = routers.DefaultRouter()
router.register(r'area',AreaViewSet)
router.register(r'asignatura',AsignaturaViewSet)
router.register(r'cargo',CargoViewSet)
router.register(r'cargodocumento',CargoDocumentoViewSet)
router.register(r'cargorequisito',CargoRequisitoViewSet)
router.register(r'carrera',CarreraViewSet)
router.register(r'catedra',CatedraViewSet)
router.register(r'concurso',ConcursoViewSet)
router.register(r'concursodocumento',ConcursoDocumentoViewSet)
router.register(r'concursorequisito',ConcursoRequisitoViewSet)
router.register(r'dependencia',DependenciaViewSet)
router.register(r'dia',DiasViewSet)
router.register(r'direccion',DireccionViewSet)
router.register(r'documento',DocumentoViewSet)
router.register(r'documentopostulacion',DocumentoPostulacionViewSet)
router.register(r'enfasis',EnfasisViewSet)
router.register(r'horario',HorarioViewSet)
router.register(r'modalidadconcurso',ModalidadConcursoViewSet)
router.register(r'modalidadpuesto',ModalidadPuestoViewSet)
router.register(r'postulacion',PostulacionViewSet)
router.register(r'puesto',PuestoViewSet)
router.register(r'puestodocumento',PuestoDocumentoViewSet)
router.register(r'puestorequisito',PuestoRequisitoViewSet)
router.register(r'requisito',RequisitoViewSet)
router.register(r'sede',SedeViewSet)
router.register(r'subarea',SubAreaViewSet)
router.register(r'tipocargo',TipoCargoViewSet)
router.register(r'tipoconcurso',TipoConcursoViewSet)
router.register(r'tipodocumento',TipoDocumentoViewSet)
router.register(r'tipopuesto',TipoPuestoViewSet)
router.register(r'turno',TurnoViewSet)
router.register(r'vistaconcurso',VistaConcursoViewSet)
router.register(r'vistadetalleconcurso',VistaDetalleConcursoViewSet)
router.register(r'vistaareapostula',VistaAreaPostulaViewSet)
router.register(r'usuarioFp',UsuarioViewSet)
urlpatterns = router.urls



urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),  # incluye las rutas para crear y refrescar tokens
]

urlpatterns += router.urls