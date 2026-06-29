from rest_framework import serializers
from .models import JenisPengunjung, Kuesioner

class JenisPengunjungSerializer(serializers.ModelSerializer):
    class Meta:
        model = JenisPengunjung
        fields = '__all__'

class KuesionerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kuesioner
        fields = '__all__'