from django.urls import path
from . import views

urlpatterns = [
    path('solicitudes/', views.SolicitudesListView.as_view(), name='solicitudes_list'),
    path('vwsolicitudes/', views.vwSolicitudesListView.as_view(), name='solicitudes_list'),
    path('solicitudes-vigentes/', views.vwSolicitudesVigentestView.as_view(), name='Solicitudes_vigentes'),
]