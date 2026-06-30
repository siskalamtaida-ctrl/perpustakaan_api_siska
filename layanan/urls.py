from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import JenisPengunjungViewSet, KuesionerViewSet, LaporanBulananView

router = DefaultRouter()
router.register('jenis-pengunjung', JenisPengunjungViewSet)
router.register('kuesioner', KuesionerViewSet)

urlpatterns = router.urls + [
    path('laporan/', LaporanBulananView.as_view(), name='laporan-bulanan'),
]