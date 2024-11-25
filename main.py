from Ciudad import *
from Persona import *
from Establecimiento import *
from RutaOptima import *
import networkx as nx

def main():
    ciudad = Ciudad() 
    javier = Persona("Javier", (54, 14), 'weight') 
    andreina = Persona("Andreína", (52, 13), 'andreina') 
    establecimiento = Establecimiento("The Darkness", (50, 14)) 
    ruta_optima = RutaOptima(javier, andreina, ciudad) 

    ruta_javier, ruta_andreina, mensaje = ruta_optima.calcular_rutas_y_tiempos(establecimiento.location)
    print("Ruta de Javier:", ruta_javier) 
    print("Ruta de Andreína:", ruta_andreina) 
    print(mensaje)
main()