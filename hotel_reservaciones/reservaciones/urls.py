from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoomViewSet, ReservationViewSet, occupancy_statistics
from .views import index

router = DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'reservations', ReservationViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('', include(router.urls)),
]

urlpatterns += [
    path('statistics/', occupancy_statistics),
]