from rest_framework import viewsets
from .models import Machine
from .serializers import MachineSerializer

class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
