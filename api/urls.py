from django.urls import path, include
from rest_framework.routers import DefaultRouter

from companies.views import CompanyViewSet
from machines.views import MachineViewSet
from occurrences.views import OccurrenceViewSet
from sensor_readings.views import SensorReadingViewSet
from sensors.views import SensorViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='company')
router.register(r'machines', MachineViewSet, basename='machine')
router.register(r'occurrences', OccurrenceViewSet, basename='occurrence')
router.register(r'sensor-readings', SensorReadingViewSet, basename='sensorreading')
router.register(r'sensors', SensorViewSet, basename='sensor')

urlpatterns = [
    path('', include(router.urls)),
]
