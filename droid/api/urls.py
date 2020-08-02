from rest_framework import routers
from droid.api.views import AnuncianteViewSet, DemandaDePecasViewSet

"""
Registration of urls available in the application
"""
app_name = 'api'
router = routers.DefaultRouter(trailing_slash=True)

router.register('anunciante', AnuncianteViewSet)
router.register('demanda_peca', DemandaDePecasViewSet)

urlpatterns = router.urls
