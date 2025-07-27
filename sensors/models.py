from django.db import models
from machines.models import Machine

class Sensor(models.Model):
    id = models.IntegerField(primary_key=True)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, db_column='id_maquina')
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=50)
    measurement_type = models.CharField(max_length=20)
    active = models.CharField(max_length=1)

    class Meta:
        db_table = 'sensores'
