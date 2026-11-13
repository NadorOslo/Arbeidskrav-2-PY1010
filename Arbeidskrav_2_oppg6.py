# -*- coding: utf-8 -*-
"""
Arbeidskrav 2

Oppgave 6

"""

import numpy as np
import matplotlib.pyplot as plt

# Lager 200 x-verdier jevnt fordelt mellom -10 og 10
x = np.linspace(-10, 10, 200)

# Beregner funksjonsverdiene
y = -x**2 - 5

# Tegner grafen
plt.plot(x, y)

# Legger til tittel, navn på aksene og rutenett
plt.title('Grafen til f(x) = -x² - 5')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xlim(-10, 10)
plt.grid(True)

# Viser grafen
plt.show()