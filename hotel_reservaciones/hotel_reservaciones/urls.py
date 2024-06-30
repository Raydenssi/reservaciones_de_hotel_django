"""
URL configuration for hotel_reservaciones project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.authtoken.views import obtain_auth_token
from reservaciones import views

urlpatterns = [
    path('', include('reservaciones.urls')),
    re_path('login', views.login),
    re_path('register', views.register),
    re_path('profile', views.profile),
    path('admin/', admin.site.urls),
    path('api/', include('reservaciones.urls')),
]

urlpatterns += [
    path('api-token-auth/', obtain_auth_token),
]