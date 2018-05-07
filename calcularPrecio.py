"""
Titulo: calcularPrecio.py

Descripcion: Implementacion de la clase TiempoDeTrabajo.

Autores: Daniel Francis     12-10863
         Francisco Marquez  12-11163

Fecha:06/05/2018.
"""

from datetime import datetime
from tiempoDeTrabajo import TiempoDeTrabajo
from tarifa import Tarifa

def fraccionDia(dia):
    return dia.hour + dia.minute / 60 + dia.second / 3600

def calcularPrecio(tarifa, tiempoDeServicio):
# Somos una empresa eficiente que trabaja 24/7!
    precio = 0

    if tarifa.t_Dias <= 0 or tarifa.t_Fines <= 0:
        return -1

    if tiempoDeServicio.inicioDeServicio >= tiempoDeServicio.finDeServicio:
        return -1

    delta = tiempoDeServicio.finDeServicio - tiempoDeServicio.inicioDeServicio

    total = delta.days * 24 + delta.seconds / 3600

    if total > 168.00:
        return -1

    if delta.seconds % 3600 > 0:
        total = float(int(total)) + 1.000

    inicio = datetime.weekday(tiempoDeServicio.inicioDeServicio)
    if delta.days > 0:
        fin = datetime.weekday(tiempoDeServicio.finDeServicio)
        if inicio in (5,6):
            precio += tarifa.t_Fines * (24.00 - fraccionDia(
                tiempoDeServicio.inicioDeServicio))
        else:
            precio += tarifa.t_Dias * (24.00 - fraccionDia(
                tiempoDeServicio.inicioDeServicio))
        for x in range(delta.days):
            if (inicio + x + 1) % 7 in (5,6):
                if (inicio + x + 1) % 7 != fin:
                    precio += tarifa.t_Fines * 24
                else:
                    precio += tarifa.t_Fines * fraccionDia(
                        tiempoDeServicio.finDeServicio)
            else:
                if (inicio + x + 1) % 7 != fin:
                    precio += tarifa.t_Dias * 24
                else:
                    precio += tarifa.t_Dias * fraccionDia(
                        tiempoDeServicio.finDeServicio)
    else:
        if inicio in (5,6):
            precio = tarifa.t_Fines * total
        else:
            precio = tarifa.t_Dias * total

    assert(precio > 0.00)

    return precio