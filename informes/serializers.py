from rest_framework import serializers
from . import models

class SolicitudesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BeneficiariosSolicitudes
        fields = '__all__'
        
class vwSolicitudes(serializers.ModelSerializer):
    class Meta:
        model = models.vwSolicitudes
        fields = '__all__'

class VwSolicitudesVigentesSerliazer(serializers.ModelSerializer):
    class Meta:
        model = models.VwSolicitudesVigentes
        fields = '__all__'