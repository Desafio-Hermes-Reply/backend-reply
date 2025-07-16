from rest_framework import serializers
from .models import Industria

class IndustriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Industria
        fields = '__all__'
