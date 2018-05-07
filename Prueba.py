from datetime import datetime, time, timedelta
import calendar

# Primero escribiremos una clase vacía a probar
class Trabajo(object):
	def fechasInvalidas(self):
		print("La fecha de inicio debe ser previa a la de fin.")
		print("El programa terminara.")
		return -1
	def explotacion(self):
		print("El periodo de trabajo no puede exceder de una semana.")
		print("El programa terminara.")
		return -1
	def calcularPrecio(self, tarifa, periodo):
		precio = 0
		for monto in tarifa:
			if monto <= 0.00:
				print("Tarifa debe ser positiva.")
				print("El programa terminara.")
				return -1
		if periodo[1] < periodo[0]:
			return fechasInvalidas()
		if periodo[1] - periodo[0] < 0.25:
			precio = tarifa[0]
		if periodo[1] - periodo[0] > 168.00:
			return explotacion()
		return precio

# Después escribiremos el código de nuestra prueba
import unittest

class TrabajoTestCase(unittest.TestCase):
# Instanciamos nuestro objeto foo antes de correr cada prueba
	def setUp(self):
		self.trabajo = Trabajo()
 
	"""def test_exists_calcularPrecio(self):
		fare = (1.0, 2.0)
		period = ("05/06/2018 06:00", "05/06/2018 17:00")
		result = self.trabajo.calcularPrecio(fare, period)"""

	"""def test_tarifasNegativas_calcularPrecio(self):
		fare = (-1.0, -2.0)
		period = ("05/06/2018 06:00", "05/06/2018 17:00")
		result = self.trabajo.calcularPrecio(fare, period)
		self.assertEquals(result, -1)"""

	"""def test_tarifasNulas_calcularPrecio(self):
		fare = (0.00, 0.00)
		period = ("05/06/2018 06:00", "05/06/2018 17:00")
		result = self.trabajo.calcularPrecio(fare, period)
		self.assertEquals(result, -1)"""

	"""def test_tarifasPositivas_calcularPrecio(self):
		fare = (1.0, 2.0)
		period = ("05/06/2018 06:00", "05/06/2018 17:00")
		result = self.trabajo.calcularPrecio(fare, period)
		self.assertEquals(result, -1)"""

	"""def test_periodoFalso_calcularPrecio(self):
		fare = (1.0, 2.0)
		period = ("05/06/2018 06:00", "05/06/2018 05:59")
		result = self.trabajo.calcularPrecio(fare, period)
		self.assertEquals(result, -1)"""

	"""def test_periodoVacio_calcularPrecio(self):
		fare = (1.0, 2.0)
		period = ("05/06/2018 06:00", "05/06/2018 06:00")
		result = self.trabajo.calcularPrecio(fare, period)
		self.assertEquals(result, -1)"""

	"""def test_periodoCorto_calcularPrecio(self):
		fare = (1.0, 2.0)
		period = ("05/06/2018 06:00", "05/06/2018 06:10")
		result = self.trabajo.calcularPrecio(fare, period)
		self.assertEquals(result, 2.0)"""

	"""def test_periodoPermitido_calcularPrecio(self):
		fare = (1.0, 2.0)
		period = ("05/06/2018 06:00", "05/06/2018 17:00")
		result = self.trabajo.calcularPrecio(fare, period)
		self.assertEquals(result, 22.00)"""

	"""def test_periodoLargo_calcularPrecio(self):
		fare = (1.0, 2.0)
		period = ("05/06/2018 06:00", "05/06/2018 17:00")
		result = self.trabajo.calcularPrecio(fare, period)
		self.assertEquals(result, -1)"""


if __name__ == "__main__":
	unittest.main()