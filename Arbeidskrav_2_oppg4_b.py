# -*- coding: utf-8 -*-
"""
Arbeidskarv 2

Oppgave 4_b

"""

data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
}

print('Du kan velge mellom: Oslo, London, Paris og Roma.')

by = input('Skriv inn en hovedstad: ').strip().capitalize()

for land, info in data.items():
    hovedstad = info[0]
    innbyggere = info[1]

    if by == hovedstad:
        print(f'{hovedstad} er hovedstaden i {land} '
              f'og det er {innbyggere} millioner innbyggere i London.')
        break
else:
    print('Hovedstaden finnes ikke i listen.')
    
"""
by lagrer hovedstaden brukeren skriver inn.

for land, info in data.items(): går gjennom hvert land og den tilhørende listen i dictionaryet. 
For Norge blir land lik "Norge" og info lik ["Oslo", 0.634]. Metoden .items() lar deg hente nøkkelen og verdien sammen.

if by == hovedstad: sjekker om byen brukeren skrev inn stemmer med hovedstaden i denne runden.

break avslutter løkken når programmet finner et treff. 
else kjøres bare dersom hele løkken fullføres uten et treff og dermed uten break. 

"""