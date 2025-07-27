from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Company

class CompanyModelTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(
            id=1,
            name="Empresa Teste",
            cnpj="12345678000199",
            address="Rua Exemplo, 123",
            email="empresa@teste.com",
            contract_date="2023-01-01",
            active="Y"
        )

    def test_company_creation(self):
        """Testa se a empresa foi criada corretamente"""
        self.assertEqual(self.company.name, "Empresa Teste")
        self.assertEqual(self.company.cnpj, "12345678000199")
        self.assertEqual(self.company.active, "Y")

class CompanyAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.company_data = {
            "id": 2,
            "name": "Nova Empresa",
            "cnpj": "98765432000188",
            "address": "Rua Nova, 456",
            "email": "nova@empresa.com",
            "contract_date": "2023-06-01",
            "active": "Y"
        }
        self.url = reverse('company-list')  # use o nome do endpoint no seu router

    def test_create_company(self):
        """Testa se a API cria uma empresa com sucesso"""
        response = self.client.post(self.url, self.company_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Company.objects.count(), 1)
        self.assertEqual(Company.objects.get().name, "Nova Empresa")
