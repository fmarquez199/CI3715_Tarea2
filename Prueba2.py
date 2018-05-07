def calcularPrecio(tarifa, periodo):
	pass

class TrabajoTestCase(unittest.TestCase):
# Instanciamos nuestro objeto foo antes de correr cada prueba
	#def setUp(self):
	#	self.trabajo = Trabajo()
 
	"""def test_exists_calcularPrecio(self):
		fare = (1.0, 2.0)
		period = ("05/06/2018 06:00", "05/06/2018 17:00")
		result = self.trabajo.calcularPrecio(fare, period)"""

	def test_tarifasNegativas_calcularPrecio(self):
		fare = (-1.0, -2.0)
		period = ("05/06/2018 06:00", "05/06/2018 17:00")
		result = self.trabajo.calcularPrecio(fare, period)
		self.assertEquals(result, -1)

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