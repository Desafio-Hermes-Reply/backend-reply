from django.db import models
from sensor_readings.models import SensorReading

class Occurrence(models.Model):
    id = models.IntegerField()
    sensor_reading = models.ForeignKey(SensorReading, on_delete=models.CASCADE, db_column='id_leitura')
    sensor_id = models.IntegerField()
    occurrence_number = models.IntegerField()
    anomaly_type = models.CharField(max_length=100)
    severity = models.CharField(max_length=20)
    description = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=50)

    class Meta:
        db_table = 'ocorrencias'
        unique_together = (('id', 'sensor_reading'),)
