# -*- coding: utf-8 -*-
"""
Arbeidskrav 2

Oppgave 4_a
"""

data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]
        }

print('Du kan velge mellom: Norge, England, Frankrike og Italia.')

land = input('Skriv inn ønsket land: ').strip().capitalize()

if land in data:
    hovedstad = data[land][0]
    innbyggere = data[land][1]

    print(f'Hovedstaden i {land} er {hovedstad}, '
          f'som har {innbyggere} millioner innbyggere.')
else:
    print('Landet finnes ikke i listen.')
    
"""
Hvis brukeren skriver Norge, henter data[land] listen som tilhører Norge:

["Oslo", 0.634]

Deretter hentes de to verdiene med plasseringen deres i listen. 
Python teller fra 0:


hovedstad = data[land][0]   Henter "Oslo"
innbyggere = data[land][1]  Henter 0.634

if land in data: sjekker først om landet finnes i dictionaryet. 
Dermed får brukeren en forklarende melding i stedet for en feilmelding dersom landet ikke finnes.

I inntastingen fjerner .strip() ekstra mellomrom før og etter teksten, mens .capitalize() gjør første bokstav stor og resten små. 
Dermed kan brukeren også skrive for eksempel norge eller NORGE.
"""