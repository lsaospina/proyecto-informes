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