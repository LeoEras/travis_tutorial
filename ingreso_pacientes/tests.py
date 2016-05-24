from django.test import TestCase

# Create your tests here.
from ingreso_pacientes.models import Paciente
#ABABABABAB

class CrearPaciente(TestCase):
	def setUp(self):
		self.Cliente = Client()
    def crear_paciente(self):
        self.paciente = Paciente.objects.create(nombres='Juan',apellidos='Vargas',cedula='0955555555')

    def test_crear_paciente(self):
        self.crear_paciente()
        self.assertIsInstance(self.paciente,Paciente,'paciente creado exitosamente')

	def test_crear_paciente_view(self):
		respuesta = self.cliente.post('/pacientes/', ("nombres":"John","apellidos":"Connor","cedula":"0955555555"))
		self.assertContains(respuesta, "guardado correctamente")