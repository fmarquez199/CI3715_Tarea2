#!/usr/bin/python3
"""
Titulo: tiempoDeTrabajo.py

Descripcion: Implementacion de la clase TiempoDeTrabajo.

Autores: Daniel Francis     12-10863
         Francisco Marquez  12-11163

Equipo: Null Pointer Exception

Fecha:06/05/2018.
"""
from datetime import datetime

"""
La clase TiempoDeTrabajo representa un par ordenado donde se muestra la fecha
de inicio y finalizacion de un servicio prestado. Contiene dos atributos y 3
metodos.

Los atributos son objetos datetime inicioDeServicio y finDeServicio.

Los metodos son de inicializacion (init) y representacion como cadena (str y 
repr).
"""
class TiempoDeTrabajo:
    #Metodo de inicializacion de la clase.
    def __init__(self, inicioDeServicio: str, finDeServicio: str) -> 'void':
        try:
            self.inicioDeServicio = datetime.strptime(
                inicioDeServicio,'%Y-%m-%d %H:%M:%S')
            self.finDeServicio = datetime.strptime(
                finDeServicio,'%Y-%m-%d %H:%M:%S')
        except:
            self.inicioDeServicio = None
            self.finDeServicio = None

    #Metodo de representacion como cadena.
    def __str__(self) -> str:
        return "(%s,%s)" % (self.inicioDeServicio,self.finDeServicio)

    #Metodo de representacion de la clase por salida estandar.
    def __repr__(self) -> str:
        return self.__str__