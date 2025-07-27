from rest_framework import viewsets
from .models import Sensor
from .serializers import SensorSerializer

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
