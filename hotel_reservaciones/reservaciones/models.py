from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Habitacion(models.Model):
    numero_habitacion = models.CharField(max_length=10)
    tipo_habitacion = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio_por_noche = models.DecimalField(max_digits=10, decimal_places=2)
    disponibilidad = models.BooleanField(default=True)

    def __str__(self):
        return f'Habitacion {self.numero_habitacion} - {self.tipo_habitacion}'

class Reservacion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'Reservation {self.id} by {self.user.username}'