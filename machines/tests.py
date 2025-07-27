from django.test import TestCase
from .models import Machine
from datetime import date

class MachineModelTest(TestCase):
    def test_create_machine(self):
        machine = Machine.objects.create(
            id=1,
            name="Máquina Teste",
            serial_number="ABC123456",
            model="X1000",
            manufacturer="Fabrica XYZ",
            location="Setor 1",
            installation_date=date.today(),
            status="Ativa"
        )
        self.assertEqual(machine.name, "Máquina Teste")
