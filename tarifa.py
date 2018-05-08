#!/usr/bin/python3
"""
Titulo: tarifa.py

Descripcion: Implementacion de la clase Tarifa.

Autores: Daniel Francis     12-10863
         Francisco Marquez  12-11163

Equipo: Null Pointer Exception

Fecha:06/05/2018.
"""

"""
La clase Tarifa representa un par ordenado donde se muestra el monto a cobrar
de un servicio prestado por hora, en dia de semana (Lunes a Viernes) y en fines
de semana. Contiene dos atributos y 3 metodos.

Los atributos son objetos float t_Dias y t_Fines.

Los metodos son de inicializacion (init) y representacion como cadena (str y 
repr).
"""
class Tarifa:
	#Metodo de inicializacion de la clase.
    def __init__(self,t_Dias,t_Fines):
        self.t_Dias = t_Dias
        self.t_Fines = t_Fines

    #Metodo de representacion como cadena.
    def __str__(self):
        return "(%f,%f)" % (self.t_Dias,self.t_Fines)

    #Metodo de representacion de la clase por salida estandar.
    def __repr__(self):
        return self.__str__