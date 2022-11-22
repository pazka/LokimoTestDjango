from django.urls import path, include
from rest_framework import routers

from LokimoTest.LokimoTest.controllers import ad_controller

base_router = routers.DefaultRouter()
base_router.register(r'', ad_controller.AdCRUD)

urls = [
    path('', include(base_router.urls)),
]
