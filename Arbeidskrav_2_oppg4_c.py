# -*- coding: utf-8 -*-
"""
Arbeidskarv 2

Oppgave 4_c
"""

data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
}

land = input('Skriv inn et nytt land: ').strip().capitalize()

while land in data:
    print('Dette landet finnes allerede i dictionaryet.')
    land = input('Skriv inn et annet land: ').strip().capitalize()

hovedstad = input(f'Skriv inn hovedstaden i {land}: ').strip().capitalize()

innbyggere = float(input(
    f'Skriv inn antall innbyggere i {hovedstad}, i millioner: '
).replace(',', '.'))

data[land] = [hovedstad, innbyggere]

print('\nOppdatert dictionary:')
print(data)

"""
while land in data: gjør at brukeren må skrive inn et annet land dersom landet allerede finnes. 
Slik unngår man å overskrive en eksisterende oppføring.

hovedstad og innbyggere lagrer den nye informasjonen. .replace(',', '.') lar brukeren skrive desimaltallet med enten komma eller punktum.

data[land] = [hovedstad, innbyggere] legger landet inn som en ny nøkkel, med hovedstaden og innbyggertallet i en liste.

print(data) skriver ut hele det oppdaterte dictionaryet.
"""