from maquinas.models import Maquina
from maquinas.serializers import MaquinaSerializer
from rest_framework import viewsets


class MaquinaViewSet(viewsets.ModelViewSet):
    queryset = Maquina.objects.all()
    serializer_class = MaquinaSerializer
