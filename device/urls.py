from rest_framework import routers
from .api import EscanearRedViewSet
router = routers.DefaultRouter()

router.register('escanear-red', EscanearRedViewSet, 'escanear_red')
# router.register('ping-check', PingCheckViewSet, 'ping_check')

urlpatterns = router.urls