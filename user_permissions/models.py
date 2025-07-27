from django.db import models
from machines.models import Machine
from users.models import User

class UserMachinePermission(models.Model):
    id = models.IntegerField()
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, db_column='id_maquina')
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='id_usuario')
    concession_date = models.DateTimeField()
    active = models.CharField(max_length=1)

    class Meta:
        db_table = 'permissoes_maquina_usuario'
        unique_together = (('machine', 'user', 'id'),)
