from django.db import models
from companies.models import Company
from profiles.models import Profile

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, db_column='id_empresa')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, db_column='id_perfil')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password_hash = models.CharField(max_length=255)
    access_level = models.CharField(max_length=50)
    registration_date = models.DateField()
    last_login = models.DateTimeField()
    active = models.CharField(max_length=1)

    class Meta:
        db_table = 'usuarios'
