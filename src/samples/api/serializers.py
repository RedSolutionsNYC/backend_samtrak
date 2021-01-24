from rest_framework import serializers
from samples.models import Sample

class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = ('id', 'serialNo', 'cylinderSize' )