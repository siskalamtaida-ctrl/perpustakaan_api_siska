from django.db import models

class JenisPengunjung(models.Model):
    nama = models.CharField(max_length=100)  # contoh: Mahasiswa, Dosen, Umum

    def __str__(self):
        return self.nama

class Kuesioner(models.Model):
    jenis_pengunjung = models.ForeignKey(JenisPengunjung, on_delete=models.CASCADE)
    nama_pengunjung = models.CharField(max_length=100)
    tanggal_kunjungan = models.DateField()
    kualitas_layanan = models.IntegerField()  # rating 1-5
    fasilitas = models.IntegerField()
    kebersihan = models.IntegerField()
    saran = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama_pengunjung