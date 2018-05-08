#!/usr/bin/python3
"""
Titulo: casos_de_prueba.py

Descripcion: Implementacion de casos de prueba para la funcion calcularPrecio().
Los casos de prueba son (ordenados alfabeticamente):

    1.  test_exists_calcularPrecio: Verifica que la funcion calcularPrecio() se
    encuentre declarada.
    2.  test_periodoCorto_calcularPrecio: Verifica que la funcion
    calcularPrecio() maneje correctamente los casos de menos de una hora.
    3.  test_periodoFalso_calcularPrecio: Verifica que la funcion
    calcularPrecio() maneje correctamente periodos invalidos.
    4.  test_periodoLargo_calcularPrecio: Verifica que la funcion
    calcularPrecio() maneje correctamente los periodos mayores a una semana.
    5.  test_periodoPermitido_calcularPrecio: Verifica que la funcion
    calcularPrecio() ejecute el calculo cuando el periodo es valido.
    6.  test_periodoSemanaCompleta_calcularPrecio: Verifica que la funcion
    calcularPrecio() ejecute el calculo correspondiente a una semana completa
    correctamente.
    7.  test_periodoSemanaYFin_calcularPrecio: Verifica que la funcion
    calcularPrecio() ejecute el calculo correspondiente a un dia de fin de
    fin de semana y a un dia de semana, correctamente.
    8.  test_periodoSemanaYFin2_calcularPrecio: Verifica que la funcion
    calcularPrecio() ejecute el calculo correspondiente a un dia de fin de
    semana y a varios dias de semana, correctamente.
    9.  test_periodoVacio_calcularPrecio: Verifica que la funcion
    calcularPrecio() maneje los periodos de 0 segundos.
    10. test_tarifasNegativas_calcularPrecio: Verifica que la funcion maneje
    tarifas negativas.
    11. test_tarifasNulas_calcularPrecio: Verifica que la funcion maneje las
    tarifas nulas.
    12. test_tarifasPositivas_calcularPrecio: Verifica que la funcion maneje
    las tarifas positivas.

Autores: Daniel Francis     12-10863
         Francisco Marquez  12-11163

Equipo: Null Pointer Exception

Fecha: 07/05/2018.
"""

import unittest
from calcularPrecio import *

class FuncionTestCase(unittest.TestCase):

    #Verifica que la funcion calcularPrecio() se encuentre declarada.
    def test_exists_calcularPrecio(self):
        fare = Tarifa(1.0, 2.0)
        period = TiempoDeTrabajo("2018-05-06 06:00:00", "2018-05-06 17:00:00")
        result = calcularPrecio(fare, period)
        self.assertNotEqual(result, None)

    #Verifica que la funcion calcularPrecio() maneje correctamente los casos de
    #menos de una hora.
    def test_periodoCorto_calcularPrecio(self):
        fare = Tarifa(1.0, 2.0)
        period = TiempoDeTrabajo("2018-05-06 06:00:00", "2018-05-06 06:10:00")
        result = calcularPrecio(fare, period)
        self.assertEqual(result, 2.0)

    #Verifica que la funcion calcularPrecio() maneje correctamente periodos
    #invalidos.
    def test_periodoFalso_calcularPrecio(self):
        fare = Tarifa(1.0, 2.0)
        period = TiempoDeTrabajo("2018-05-06 06:00:00", "2018-05-06 05:59:00")
        result = calcularPrecio(fare, period)
        self.assertEqual(result, None)

    #Verifica que la funcion calcularPrecio() maneje correctamente los periodos
    #mayores a una semana.
    def test_periodoLargo_calcularPrecio(self):
        fare = Tarifa(1.0, 2.0)
        period = TiempoDeTrabajo("2018-05-06 06:00:00", "2018-05-13 17:00:00")
        result = calcularPrecio(fare, period)
        self.assertEqual(result, None)

    #Verifica que la funcion calcularPrecio() ejecute el calculo cuando el
    #periodo es valido.
    def test_periodoPermitido_calcularPrecio(self):
        fare = Tarifa(1.0, 2.0)
        period = TiempoDeTrabajo("2018-05-06 06:00:00", "2018-05-06 17:00:00")
        result = calcularPrecio(fare, period)
        self.assertEqual(result, 22.00)

    #Verifica que la funcion calcularPrecio() ejecute el calculo
    #correspondiente a una semana completa correctamente.
    def test_periodoSemanaCompleta_calcularPrecio(self):
        fare = Tarifa(1.0, 2.0)
        period = TiempoDeTrabajo("2018-05-06 06:00:00", "2018-05-13 06:00:00")
        result = calcularPrecio(fare, period)
        self.assertEqual(result, 216.00)

    #Verifica que la funcion calcularPrecio() ejecute el calculo
    #correspondiente a un dia de fin de fin de semana y a un dia de semana,
    #correctamente.
    def test_periodoSemanaYFin_calcularPrecio(self):
        fare = Tarifa(1.0, 2.0)
        period = TiempoDeTrabajo("2018-05-06 06:00:00", "2018-05-07 13:00:00")
        result = calcularPrecio(fare, period)
        self.assertEqual(result, 49.00)

    #Verifica que la funcion calcularPrecio() ejecute el calculo
    #correspondiente a un dia de fin de semana y a varios dias de semana,
    #correctamente.
    def test_periodoSemanaYFin2_calcularPrecio(self):
        fare = Tarifa(1.0, 2.0)
        period = TiempoDeTrabajo("2018-05-10 06:00:00", "2018-05-12 20:00:00")
        result = calcularPrecio(fare, period)
        self.assertEqual(result, 82.00)

    #Verifica que la funcion calcularPrecio() maneje los periodos de 0 s.
    def test_periodoVacio_calcularPrecio(self):
        fare = Tarifa(1.0, 2.0)
        period = TiempoDeTrabajo("2018-05-06 06:00:00", "2018-05-06 06:00:00")
        result = calcularPrecio(fare, period)
        self.assertEqual(result, None)

    #Verifica que la funcion maneje tarifas negativas.
    def test_tarifasNegativas_calcularPrecio(self):
        fare = Tarifa(-1.0, -2.0)
        period = TiempoDeTrabajo("2018-05-06 06:00:00", "2018-05-06 17:00:00")
        result = calcularPrecio(fare, period)
        self.assertEqual(result, None)

    #Verifica que la funcion maneje tarifas nulas.
    def test_tarifasNulas_calcularPrecio(self):
        fare = Tarifa(0.00, 0.00)
        period = TiempoDeTrabajo("2018-05-06 06:00:00", "2018-05-06 17:00:00")
        result = calcularPrecio(fare, period)
        self.assertEqual(result, None)

    #Verifica que la funcion maneje tarifas positivas.
    def test_tarifasPositivas_calcularPrecio(self):
        fare = Tarifa(1.0, 2.0)
        period = TiempoDeTrabajo("2018-05-06 06:00:00", "2018-05-06 17:00:00")
        result = calcularPrecio(fare, period)
        self.assertEqual(result, 22.0)

if __name__ == "__main__":
    unittest.main()