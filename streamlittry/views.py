''' Prueba streamlit '''
from django.shortcuts import render
from . import models
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def submit_form(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        contact = models.Contact.objects.create(
            name=data['name'], 
            email=data['email'], 
            message=data['message']
        )
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'})