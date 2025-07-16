from django.db import models
from estacoes.models import EstacaoTrabalho

class Maquina(models.Model):
    nome = models.CharField(max_length=100)
    estacao = models.ForeignKey(EstacaoTrabalho, on_delete=models.CASCADE, related_name='maquinas')
    numero_serie = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.nome} ({self.estacao.nome})"
