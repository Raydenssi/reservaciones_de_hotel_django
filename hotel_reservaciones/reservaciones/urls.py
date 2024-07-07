from django.urls import path
from .views import (
    index, CustomLoginView, CustomLogoutView, CustomSignupView, 
    profile, RoomListView, RoomCreateView, RoomUpdateView, RoomDeleteView, make_reservation, ReservationListView
)

urlpatterns = [
    path('', index, name='index'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', CustomSignupView.as_view(), name='register'),
    path('profile/', profile, name='profile'),
    path('rooms/', RoomListView.as_view(), name='rooms_list'),
    path('rooms/create/', RoomCreateView.as_view(), name='room_create'),
    path('rooms/update/<int:pk>/', RoomUpdateView.as_view(), name='room_edit'),
    path('rooms/delete/<int:pk>/', RoomDeleteView.as_view(), name='room_delete'),
    path('rooms/reserve/<int:room_id>/', make_reservation, name='make_reservation'),
    path('reservations/', ReservationListView.as_view(), name='list_reservations'),
]
