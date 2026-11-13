# -*- coding: utf-8 -*-
"""
Arbeidskrav 2
Oppgave 1
"""

from datetime import date

alder = int(input('Hvilket år er du født? ') )

ny_alder = date.today().year - alder # Beregning av alder

print("Du blir" , ny_alder , " i år ")

