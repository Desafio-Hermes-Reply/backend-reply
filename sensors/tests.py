from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from machines.models import Machine
from .models import Sensor

class SensorAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.machine = Machine.objects.create(
            id=1,
            name="Máquina A",
            serial_number="123ABC",
            model="X1000",
            manufacturer="Fábrica X",
            location="Setor 1",
            installation_date="2024-01-01",
            status="Operacional"
        )
        self.sensor_data = {
            "id": 1,
            "machine": self.machine.id,
            "name": "Sensor Temperatura",
            "model": "TMP-01",
            "measurement_type": "temperatura",
            "active": "Y"
        }
        self.sensor = Sensor.objects.create(**self.sensor_data)

    def test_list_sensors(self):
        response = self.client.get(reverse('sensor-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_sensor(self):
        new_sensor = {
            "id": 2,
            "machine": self.machine.id,
            "name": "Sensor Pressão",
            "model": "PRS-02",
            "measurement_type": "pressão",
            "active": "Y"
        }
        response = self.client.post(reverse('sensor-list'), new_sensor, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Sensor.objects.count(), 2)

    def test_get_sensor_detail(self):
        response = self.client.get(reverse('sensor-detail', kwargs={'pk': self.sensor.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.sensor.name)

    def test_update_sensor(self):
        updated_data = self.sensor_data.copy()
        updated_data['name'] = 'Sensor Atualizado'
        response = self.client.put(
            reverse('sensor-detail', kwargs={'pk': self.sensor.id}),
            updated_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.sensor.refresh_from_db()
        self.assertEqual(self.sensor.name, 'Sensor Atualizado')

    def test_delete_sensor(self):
        response = self.client.delete(reverse('sensor-detail', kwargs={'pk': self.sensor.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Sensor.objects.count(), 0)
