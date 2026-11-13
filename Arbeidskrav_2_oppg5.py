# -*- coding: utf-8 -*-
"""
Arbeidskrav 2

Oppgave 5

"""

import numpy as np


def beregn_areal_og_omkrets(a, b):
    radius = a / 2

    # Arealet av trekanten og halvsirkelen
    areal_trekant = a * b / 2
    areal_halvsirkel = np.pi * radius**2 / 2
    areal = areal_trekant + areal_halvsirkel

    # Den skrå siden i trekanten beregnes med Pytagoras
    skraa_side = np.sqrt(a**2 + b**2)

    # Ytre omkrets: loddrett side + skrå side + halvsirkelbue
    omkrets = b + skraa_side + np.pi * radius

    return areal, omkrets


a = float(input('Skriv inn lengden a: '))
b = float(input('Skriv inn lengden b: '))

areal, omkrets = beregn_areal_og_omkrets(a, b)

print(f'Arealet av figuren er {areal:.2f} kvadratenheter.')
print(f'Den ytre omkretsen er {omkrets:.2f} lengdeenheter.')