# -*- coding: utf-8 -*-
"""
Arbeidskrav 2

Oppgave 2

@author: benmo
"""
import math


antall_elever = int(input('Skriv inn antall elever:' ))

antall_pizza = math.ceil(antall_elever / 4) # math.ceil() runder resultatet opp til et helt tall. Er resultatet allerede et helt tall, beholdes det.

print("Det skal kjøpes" , antall_pizza , "pizza")

