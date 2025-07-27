from django.contrib import admin
from .models import Machine

@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'model', 'status')
