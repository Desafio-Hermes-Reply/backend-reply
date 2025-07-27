from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cnpj', 'email', 'active', 'contract_date')
    search_fields = ('name', 'cnpj', 'email')
    list_filter = ('active', 'contract_date')
