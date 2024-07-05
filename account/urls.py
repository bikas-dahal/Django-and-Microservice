from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register(r'users', views.AddressViewset)

urlpatterns = [
    path('', include(router.urls))
]