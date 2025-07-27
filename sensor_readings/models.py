from django.db import models
from sensors.models import Sensor

class SensorReading(models.Model):
    reading_id = models.IntegerField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, db_column='id_sensor')
    value = models.IntegerField()
    value_type = models.CharField(max_length=50)
    datetime = models.DateTimeField()

    class Meta:
        db_table = 'leitura_sensores'
        unique_together = (('reading_id', 'sensor'),)
