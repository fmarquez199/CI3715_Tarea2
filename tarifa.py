"""
Titulo: tarifa.py

Descripcion: Implementacion de la clase Tarifa.

Autores: Daniel Francis     12-10863
         Francisco Marquez  12-11163

Fecha:06/05/2018.
"""

#!/usr/bin/python3

class Tarifa:
    def __init__(self,t_Dias,t_Fines):
        self.t_Dias = t_Dias
        self.t_Fines = t_Fines

    def __str__(self):
        return "(%f,%f)" % (self.t_Dias,self.t_Fines)

    def __repr__(self):
        return self.__str__