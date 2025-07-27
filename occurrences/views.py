from rest_framework import viewsets
from .models import Occurrence
from .serializers import OccurrenceSerializer

class OccurrenceViewSet(viewsets.ModelViewSet):
    queryset = Occurrence.objects.all()
    serializer_class = OccurrenceSerializer
