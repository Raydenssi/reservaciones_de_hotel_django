from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoomViewSet, ReservationViewSet, estadisticas_de_reserva

router = DefaultRouter()
router.register(r'Habitaciones', RoomViewSet)
router.register(r'Reservaciones', ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += [
    path('statistics/', estadisticas_de_reserva),
]