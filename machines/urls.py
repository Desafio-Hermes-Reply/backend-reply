from rest_framework import routers
from django.urls import path, include
from .views import MachineViewSet

router = routers.DefaultRouter()
router.register(r'machines', MachineViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
