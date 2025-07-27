from django.db import models

class Machine(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    installation_date = models.DateField()
    status = models.CharField(max_length=50)
    last_maintenance = models.DateField(blank=True, null=True)
    next_maintenance = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'maquinas'
