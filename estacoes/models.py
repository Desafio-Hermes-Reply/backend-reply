from django.db import models
from industrias.models import Industria

class EstacaoTrabalho(models.Model):
    nome = models.CharField(max_length=100)
    industria = models.ForeignKey(Industria, on_delete=models.CASCADE, related_name='estacoes')

    def __str__(self):
        return f"{self.nome} ({self.industria.nome})"
