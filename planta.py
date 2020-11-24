#!/usr/bin/python3.7



import numpy as np

import numpy.random as ra


class Planta:

    def __init__(self, pos, color, radio_exclusion, radio_alcance):

        self.pos = pos
        self.color = color
        self.radio_exclusion = radio_exclusion
        self.radio_alcance = radio_alcance


    def bloquea_crecimiento(self, pos):#retorna true si bloquea el crecimiento

        bloqueo = True
        
        x = pos[0]
        y = pos[1]
        
        x_mayor = self.pos[0] + self.radio_exclusion
        x_menor = self.pos[0] - self.radio_exclusion
        y_mayor = self.pos[1] + self.radio_exclusion
        y_menor = self.pos[1] - self.radio_exclusion

        if x > x_mayor or x < x_menor or y > y_mayor or y < y_menor:#Si se encuentra entre esto
            bloqueo = False 
    
        return bloqueo

    def lanza_espora(self):
        #color varia a lo mucho 0.15
        posicion = ra.normal(self.pos, self.radio_alcance)
        color = np.clip(ra.normal(self.color,  0.15), 0, 1)
        
        radio_alcance = ra.normal(self.radio_alcance, self.radio_alcance * 0.1)
        radio_exclusion = ra.normal(self.radio_exclusion, self.radio_exclusion * 0.1)
        hija_random = Planta(posicion, color, radio_exclusion, radio_alcance)
        return hija_random
        

    def caja_bajo_bloqueo(self):

        """Devuelve un np.array de 2 x 4 con las coordenadas de las 4 esquinas de la caja. Para el plot."""

        r = self.radio_exclusion

        return self.pos + np.vstack([

            [-r, -r],

            [r, -r],

            [r, r],

            [-r, r],

        ])



    def __repr__(self):

        return f"<Planta ({self.pos}) | {self.color} | {self.radio_exclusion:0.4f} | {self.radio_alcance:0.4f}>"
"""
choice = ra.normal(100, 10)
print(choice)
color=np.array([1.0, 0.0, 0.0])
color_chance = ra.normal(color, 0.12)
print(color_chance)

planta = Planta(pos=np.array([-3.254, 6.25]), color=np.array([1.0, 0.0, 0.0]), radio_exclusion=0.48, radio_alcance=1.39)
planta2 = planta.lanza_espora()
print(f"{planta.bloquea_crecimiento((7.812, 2.25))} noo lo bloquea")
print(planta.pos)
print(False * False)
color=np.array([1.0, 0.3, 0.0])
color_1 = np.clip(ra.normal(color, 0.15), 0, 1)
print(color_1)"""