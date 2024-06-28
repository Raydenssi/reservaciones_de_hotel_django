from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoomViewSet, ReservationViewSet, estadisticas_de_reserva

router = DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'reservations', ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += [
    path('statistics/', estadisticas_de_reserva),
]