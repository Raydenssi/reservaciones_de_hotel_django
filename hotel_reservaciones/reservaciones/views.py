import datetime
from rest_framework import viewsets
from .models import Habitacion, Reservacion
from .serializers import RoomSerializer, ReservationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Habitacion.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservacion.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

@api_view(['GET'])
def estadisticas_de_reserva(request):
    total_habitaciones = Habitacion.objects.count()
    habitaciones_ocupadas = Reservacion.objects.filter(check_out__gte=datetime.now()).count()
    porcentaje_de_ocupacion = habitaciones_ocupadas / total_habitaciones * 100

    return Response({
        'total_habitaciones': total_habitaciones,
        'habitaciones_ocupadas': habitaciones_ocupadas,
        'porcentaje_de_ocupacion': porcentaje_de_ocupacion,
    })