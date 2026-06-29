from rest_framework.routers import DefaultRouter
from .views import JenisPengunjungViewSet, KuesionerViewSet

router = DefaultRouter()
router.register('jenis-pengunjung', JenisPengunjungViewSet)
router.register('kuesioner', KuesionerViewSet)

urlpatterns = router.urls