#!/usr/bin/python3.7



import numpy as np

import numpy.random as ra

import matplotlib.pyplot as plt

from planta import Planta



class Jardin(object):

    def __init__(self, radio, plantas=[]):#He puesto [] en lugar de None porque es muchoo más simple

        self.radio = radio
        self.plantas = plantas
        

    def intenta_plantar(self, pl):

        pos = pl.pos
        x = pos[0]
        y = pos[1]

        longitud = len(self.plantas)
        #Si solo pongo el radio no tiene sentido, porque estaria teniendo plantas con radio_alcanze fuera del jardin, quitar pl.radio_alcance si igualmente podemos
        if x > self.radio or x < -self.radio  or y > self.radio  or y < -self.radio:#Si se encuentra entre esto
            apta = False 
            return apta
        else: 
            apta = True
            if longitud == 0:
                self.plantas.append(pl)
                return apta
            else:
                for planta in self.plantas:
                    if  planta.bloquea_crecimiento(pos) == True:
                        apta = False
                        return apta
                self.plantas.append(pl)
                return apta 

                    
            
        #true si lo consigue y añadirla: comprobar que esta dentro del radio, comprobar #false si no



    def crecimiento_total(self, nintentos=1000):

        contador = 0
        while contador < nintentos:
            try:
                perdida = self.intenta_plantar(self.plantas[ra.randint(0,len(self.plantas))].lanza_espora())
                if perdida == False:
                    contador += 1
            except: 
                print("Cambia el valor del radio del jardin a uno mas grande por favor")
                break


    def mapa_aereo(self, filename):

        fig, ax = plt.subplots(1, 1, figsize=(6, 6))



        # Borde del mapa en negro

        ax.plot([-self.radio, -self.radio, self.radio, self.radio, -self.radio],

                [self.radio, -self.radio, -self.radio, self.radio, self.radio], 'k', linewidth=2)



        # Cada planta

        for pl in self.plantas:

            caja = pl.caja_bajo_bloqueo()

            caja = np.vstack([caja, caja[0, :]])  # Para que este cerrada, el primer punto se copia el ultimo

            ax.plot(caja[:, 0], caja[:, 1], color=pl.color, linewidth=1, alpha=0.5)

            ax.plot(caja[:, 0], caja[:, 1], color=pl.color, linewidth=1, alpha=0.5)



        fig.savefig(filename, bbox_inches="tight")

        plt.close()



    def __repr__(self):

        lines = ["JARDIN:"]

        for (i, pl) in enumerate(self.plantas):

            lines.append(f"    {i:04d} --> {pl}")

        lines.append('-' * 40)

        return '\n'.join(lines)