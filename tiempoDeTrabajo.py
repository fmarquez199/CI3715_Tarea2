"""
Titulo: tiempoDeTrabajo.py

Descripcion: Implementacion de la clase TiempoDeTrabajo.

Autores: Daniel Francis     12-10863
         Francisco Marquez  12-11163

Fecha:06/05/2018.
"""

class TiempoDeTrabajo:
    def __init__(self,inicioDeServicio,finDeServicio):
        self.inicioDeServicio = datetime.strptime(
            inicioDeServicio,'%Y-%m-%d %H:%M:%S')
        self.finDeServicio = datetime.strptime(
            finDeServicio,'%Y-%m-%d %H:%M:%S')

    def __str__(self):
        return "(%s,%s)" % (self.inicioDeServicio,self.finDeServicio)

    def __repr__(self):
        return self.__str__