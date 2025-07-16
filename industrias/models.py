from django.db import models

class Industria(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True)

    def __str__(self):
        return self.nome
