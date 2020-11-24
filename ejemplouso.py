#!/usr/bin/python3.7



# Importamos definiciones desde los otros ficheros. Deben estar en la misma ruta.
import numpy as np
import numpy.random as ra

from planta import Planta

from jardin import Jardin





if __name__ == "__main__":

    jardin = Jardin(radio=10)  # Creo el jardin
    jardin.intenta_plantar(Planta(pos=np.array([-3.254, 6.25]), color=np.array([1.0, 0.0, 0.0]), radio_exclusion=0.48, radio_alcance=1.39))
    jardin.intenta_plantar(Planta(pos=np.array([7.812, 2.25]), color=np.array([0.0, 1.0, 0.0]), radio_exclusion=0.60, radio_alcance=1.16))
    jardin.intenta_plantar(Planta(pos=np.array([-2.98, -8.25]), color=np.array([0.0, 0.0, 1.0]), radio_exclusion=0.52, radio_alcance=1.28))
    jardin.crecimiento_total()  

    jardin.mapa_aereo("hola.jpg")

    # Falta poblarlo con las 3 plantas descritas, dejarlo crecer y hacer el mapa

