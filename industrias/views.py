from rest_framework import viewsets
from .models import Industria
from .serializers import IndustriaSerializer

class IndustriaViewSet(viewsets.ModelViewSet):
    queryset = Industria.objects.all()
    serializer_class = IndustriaSerializer
