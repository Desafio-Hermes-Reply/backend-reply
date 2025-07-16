from rest_framework import serializers
from .models import EstacaoTrabalho

class EstacaoTrabalhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstacaoTrabalho
        fields = '__all__'
