from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from sensors.models import Sensor
from .models import SensorReading
from datetime import datetime

class SensorReadingAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Criar sensor para FK
        self.sensor = Sensor.objects.create(
            id=1,
            nome="Sensor Teste",
            modelo="Modelo A",
            tipo_medicao="Temperatura",
            sensor_ativo='Y',
            id_maquina=1
        )
        self.valid_payload = {
            "reading_id": 1,
            "sensor": self.sensor.id,
            "value": 100,
            "value_type": "temperatura",
            "datetime": datetime.now().isoformat()
        }
        self.invalid_payload = {
            "reading_id": 2,
            # sensor faltando (obrigatório)
            "value": 100,
            "value_type": "temperatura",
            "datetime": datetime.now().isoformat()
        }

    def test_create_valid_sensor_reading(self):
        response = self.client.post(reverse('sensorreading-list'), data=self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_sensor_reading(self):
        response = self.client.post(reverse('sensorreading-list'), data=self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_sensor_reading_list(self):
        SensorReading.objects.create(**self.valid_payload)
        response = self.client.get(reverse('sensorreading-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_get_sensor_reading_detail(self):
        reading = SensorReading.objects.create(**self.valid_payload)
        response = self.client.get(reverse('sensorreading-detail', kwargs={'pk': reading.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['reading_id'], reading.reading_id)

    def test_update_sensor_reading(self):
        reading = SensorReading.objects.create(**self.valid_payload)
        updated_data = self.valid_payload.copy()
        updated_data['value'] = 120
        response = self.client.put(reverse('sensorreading-detail', kwargs={'pk': reading.pk}), data=updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['value'], 120)

    def test_partial_update_sensor_reading(self):
        reading = SensorReading.objects.create(**self.valid_payload)
        patch_data = {'value': 130}
        response = self.client.patch(reverse('sensorreading-detail', kwargs={'pk': reading.pk}), data=patch_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['value'], 130)

    def test_delete_sensor_reading(self):
        reading = SensorReading.objects.create(**self.valid_payload)
        response = self.client.delete(reverse('sensorreading-detail', kwargs={'pk': reading.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
