from rest_framework import serializers
from .models import Habitacion, Reservacion

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservacion
        fields = '__all__'