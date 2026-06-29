from rest_framework import viewsets
from .models import JenisPengunjung, Kuesioner
from .serializers import JenisPengunjungSerializer, KuesionerSerializer

class JenisPengunjungViewSet(viewsets.ModelViewSet):
    queryset = JenisPengunjung.objects.all()
    serializer_class = JenisPengunjungSerializer

class KuesionerViewSet(viewsets.ModelViewSet):
    queryset = Kuesioner.objects.all()
    serializer_class = KuesionerSerializer