# -*- coding: utf-8 -*-
"""
Arbeidskrav 2

Oppgave 3

@author: benmo
"""

import numpy as np

v_grad = float(input('Skriv inn gradtallet:' ))

v_rad = v_grad*np.pi/180

print(f'Verdien av {v_grad:g} grader er {v_rad:.2f} radianer')

# {v_grad:g} viser for eksempel 90.0 som 90, men beholder desimaler i et tall som 90.5. Standardformatet g bruker opptil seks gjeldende sifre.

# {v_rad:.2f} viser nøyaktig to desimaler. Tallet avrundes, så 1.570796... blir 1.57.

# f foran anførselstegnet gjør at du kan sette variablene direkte inn i teksten med {}.
