from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import serializers

# Create your views here.
class SolicitudesListView(APIView):
    def get(self, request):
        try:
            # Obtener todos los registros de la tabla
            registros = models.BeneficiariosSolicitudes.objects.all()[:100]
            serializer = serializers.SolicitudesSerializer(registros, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class vwSolicitudesListView(APIView):
    def get(self, request):
        try:
            # Obtener todos los registros de la vista
            registros = models.vwSolicitudes.objects.all()
            serializer = serializers.vwSolicitudes(registros, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)