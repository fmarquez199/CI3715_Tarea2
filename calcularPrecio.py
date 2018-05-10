#!/usr/bin/python3
"""
Titulo: calcularPrecio.py

Descripcion: Implementacion de la clase TiempoDeTrabajo.

Autores: Daniel Francis     12-10863
         Francisco Marquez  12-11163

Equipo: Null Pointer Exception

Fecha:06/05/2018.
"""

from datetime import datetime
from tiempoDeTrabajo import TiempoDeTrabajo
from tarifa import Tarifa

"""
Funcion que toma un objeto datetime y retorna un float que representa la
fraccion del dia que refleja el objeto datetime.
"""
def fraccionDia(dia: datetime) -> float:
    return dia.hour + dia.minute / 60 + dia.second / 3600

"""
Funcion que toma un objeto Tarifa y un objeto TiempoDeServicio y retorna el
valor a pagar por un servicio prestado.
"""
def calcularPrecio(tarifa: Tarifa, tiempoDeServicio: TiempoDeTrabajo) -> float:
    try:
        precio = 0.00 #Variable donde se retornara el resultado de la funcion.
        total = 0.00 #Variable auxiliar para conocer la duracion del servicio.
        
        #Las tarifas en el objeto Tarifa deben ser positivas.
        assert(tarifa.t_Dias > 0 and tarifa.t_Fines > 0)

        #Las tarifas en semana no coinciden con tarifas de fin de semana.
        assert(tarifa.t_Dias != tarifa.t_Fines)

        #La fecha de inicio del servicio debe ser menor que la fecha de fin.
        assert(tiempoDeServicio.inicioDeServicio 
               < tiempoDeServicio.finDeServicio)

        #La fecha de inicio se calcula para máximo 10 años atrás
        assert(tiempo.DeServicio.inicioDeServicio > datetime.datetime.now - datetime.timedelta(days=10*365))

        delta = (
            tiempoDeServicio.finDeServicio - tiempoDeServicio.inicioDeServicio)

        total = delta.days * 24 + delta.seconds / 3600
        
        #El tiempo total del servicio no puede exceder de 7 dias (168 horas).
        assert(total <= 168.00)

        #Las fracciones de hora se cobran como una hora adicional.
        if delta.seconds % 3600 > 0:
            total = float(int(total)) + 1.000
        
        #inicio es una variable auxiliar para marcar el comienzo del servicio.
        inicio = datetime.weekday(tiempoDeServicio.inicioDeServicio)

        if delta.days > 0: #El servicio duro un dia o mas.
            #fin, igual que inicio, marca el fin del servicio.
            fin = datetime.weekday(tiempoDeServicio.finDeServicio)

            if inicio in (5,6): #Comienzo en fin de semana.
                precio += tarifa.t_Fines * (24.00 - fraccionDia(
                    tiempoDeServicio.inicioDeServicio))
            else: #Comienzo en dia de semana.
                precio += tarifa.t_Dias * (24.00 - fraccionDia(
                    tiempoDeServicio.inicioDeServicio))

            #Acumulamos las horas de los dias.
            for x in range(delta.days):
                #next_day tiene el dia siguiente en la semana.
                next_day = (inicio + x + 1) % 7
                #fin_de_semana indica si next_day es fin de semana.
                fin_de_semana = next_day in (5,6)

                if fin_de_semana: #Si sigue un fin de semana.

                    if next_day != fin: #Si es el fin del servicio.
                        precio += tarifa.t_Fines * 24
                    else: #Si no es el fin del servicio.
                        precio += tarifa.t_Fines * fraccionDia(
                            tiempoDeServicio.finDeServicio)
                else: #Si sigue un dia de semana.

                    if next_day != fin: #Si es el fin del servicio.
                        precio += tarifa.t_Dias * 24
                    else: #Si no es el fin del servicio.
                        precio += tarifa.t_Dias * fraccionDia(
                            tiempoDeServicio.finDeServicio)
        else: #Si el servicio duro un menos de un dia.
        
            if inicio in (5,6): #Si fue fin de semana.
                precio = tarifa.t_Fines * total
            else: #Si fue dia de semana.
                precio = tarifa.t_Dias * total
        
        #El monto a pagar debe ser positivo.
        assert(precio > 0.00)

        return precio
    except:
        #Si se recibe algo anormal, no se hace nada.
        pass