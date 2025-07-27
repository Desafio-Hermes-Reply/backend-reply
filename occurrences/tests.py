from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Occurrence
from sensor_readings.models import SensorReading
from datetime import datetime

class OccurrenceAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Criar uma leitura de sensor para usar na FK
        self.sensor_reading = SensorReading.objects.create(
            id=1,
            id_sensor=1,
            valor=100,
            tipo_valor="temperatura",
            data_hora=datetime.now()
        )
        self.valid_payload = {
            "id": 1,
            "sensor_reading": self.sensor_reading.id,
            "sensor_id": 1,
            "occurrence_number": 1,
            "anomaly_type": "Teste Anomalia",
            "severity": "Alta",
            "description": "Descrição teste",
            "status": "Aberta"
        }
        self.invalid_payload = {
            "id": 2,
            # faltando sensor_reading, obrigatório
            "sensor_id": 1,
            "occurrence_number": 1,
            "anomaly_type": "Teste Anomalia",
            "severity": "Alta",
            "description": "Descrição teste",
            "status": "Aberta"
        }

    def test_create_valid_occurrence(self):
        response = self.client.post(reverse('occurrence-list'), data=self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_occurrence(self):
        response = self.client.post(reverse('occurrence-list'), data=self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_occurrence_list(self):
        Occurrence.objects.create(**self.valid_payload)
        response = self.client.get(reverse('occurrence-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_occurrence_detail(self):
        occurrence = Occurrence.objects.create(**self.valid_payload)
        response = self.client.get(reverse('occurrence-detail', kwargs={'pk': occurrence.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], occurrence.id)

    def test_update_occurrence(self):
        occurrence = Occurrence.objects.create(**self.valid_payload)
        updated_data = self.valid_payload.copy()
        updated_data['status'] = 'Fechada'
        response = self.client.put(reverse('occurrence-detail', kwargs={'pk': occurrence.pk}), data=updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'Fechada')

    def test_partial_update_occurrence(self):
        occurrence = Occurrence.objects.create(**self.valid_payload)
        patch_data = {'status': 'Em análise'}
        response = self.client.patch(reverse('occurrence-detail', kwargs={'pk': occurrence.pk}), data=patch_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'Em análise')

    def test_delete_occurrence(self):
        occurrence = Occurrence.objects.create(**self.valid_payload)
        response = self.client.delete(reverse('occurrence-detail', kwargs={'pk': occurrence.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
