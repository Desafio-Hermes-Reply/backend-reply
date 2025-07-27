from django.db import models

class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14)
    address = models.CharField(max_length=500)
    email = models.CharField(max_length=255, blank=True, null=True)
    contract_date = models.DateField()
    active = models.CharField(max_length=1)

    class Meta:
        db_table = 'empresas_cliente'
