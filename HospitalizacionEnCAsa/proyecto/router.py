from aplicacion.viewsets import AuxiliarViewset, EntidadViewset, FamiliarViewset, HistoriaViewset, PacienteViewset, PersonViewset, VitalesViewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register('entidad', EntidadViewset)

router.register('historia', HistoriaViewset)


router.register('person', PersonViewset)


router.register('paciente', PacienteViewset)


router.register('familiar', FamiliarViewset)


router.register('auxiliar', AuxiliarViewset)


router.register('vitales', VitalesViewset)


