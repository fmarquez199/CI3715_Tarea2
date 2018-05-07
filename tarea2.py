

'''
Created on May 6, 2018

@author: Francisco Marquez, Daniel Francis
'''

#!/usr/bin/python3

import time, datetime
from datetime import datetime

class Tarifa:
    
    def __init__(self,t_Dias,t_Fines):
        self.t_Dias = t_Dias
        self.t_Fines = t_Fines

class TiempoDeTrabajo:

    def __init__(self,inicioDeServicio,finDeServicio):
        self.inicioDeServicio = datetime.strptime(inicioDeServicio,'%Y-%m-%d %H:%M:%S')
        self.finDeServicio = datetime.strptime(finDeServicio,'%Y-%m-%d %H:%M:%S')


# Caso base
tarifa = Tarifa(100,120)
tiempo = TiempoDeTrabajo('2018-07-03 17:54:27','2018-07-06 20:54:27')


def calcularPrecio(tarifa, tiempoDeServicio):

# Somos una empresa eficiente que trabaja 24/7!
    
    # 1. Tiempo futuro invalido
    assert tiempo.inicioDeServicio < tiempo.finDeServicio, "Final < Inicio"

    # 2. Tarifa negativa o nula
    assert tarifa.t_Dias > 0 and tarifa.t_Fines > 0, "Tarifa <= 0"

    delta = tiempo.finDeServicio - tiempo.inicioDeServicio
    
    # 3. Limite de 7 dias
    assert delta.days <= 7, "Tiempo maximo superado"

    total = delta.days*24 + delta.seconds//3600

    if delta.seconds//60 > 0:
        total+=1;

    #print(delta.days)

    print(total)


calcularPrecio(tarifa,tiempo)