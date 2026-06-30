from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import JenisPengunjung, Kuesioner
from .serializers import JenisPengunjungSerializer, KuesionerSerializer

class JenisPengunjungViewSet(viewsets.ModelViewSet):
    queryset = JenisPengunjung.objects.all()
    serializer_class = JenisPengunjungSerializer

class KuesionerViewSet(viewsets.ModelViewSet):
    queryset = Kuesioner.objects.all()
    serializer_class = KuesionerSerializer

class LaporanBulananView(APIView):
    def get(self, request):
        bulan = request.query_params.get('bulan')
        tahun = request.query_params.get('tahun')

        kuesioner = Kuesioner.objects.all()

        if bulan:
            kuesioner = kuesioner.filter(tanggal_kunjungan__month=bulan)
        if tahun:
            kuesioner = kuesioner.filter(tanggal_kunjungan__year=tahun)

        total = kuesioner.count()

        if total == 0:
            return Response({
                'pesan': 'Tidak ada data untuk periode ini',
                'bulan': bulan,
                'tahun': tahun,
                'total_kuesioner': 0
            })

        rata_kualitas = sum(k.kualitas_layanan for k in kuesioner) / total
        rata_fasilitas = sum(k.fasilitas for k in kuesioner) / total
        rata_kebersihan = sum(k.kebersihan for k in kuesioner) / total

        return Response({
            'bulan': bulan,
            'tahun': tahun,
            'total_kuesioner': total,
            'rata_rata_kualitas_layanan': round(rata_kualitas, 2),
            'rata_rata_fasilitas': round(rata_fasilitas, 2),
            'rata_rata_kebersihan': round(rata_kebersihan, 2),
        })