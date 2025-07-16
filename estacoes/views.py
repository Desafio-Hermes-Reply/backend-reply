from rest_framework import viewsets
from .models import EstacaoTrabalho
from .serializers import EstacaoTrabalhoSerializer

class EstacaoTrabalhoViewSet(viewsets.ModelViewSet):
    queryset = EstacaoTrabalho.objects.all()
    serializer_class = EstacaoTrabalhoSerializer
