import random
import time
import matplotlib.pyplot as plt
import pandas as pd
from typing import TypedDict

class SIR_TYPE(TypedDict):
    susceptibles: int
    infectes: int
    retablis: int

taux_contamination: float = 0.1
taux_guerison: float= 0.1
init_population: float = 1000
 
init_sir : SIR_TYPE = {
    'susceptibles': init_population,
    'infectes': 0,
    'retablis': 0,
}

def simulation(day_nb: int,tc: float,tg: float, sir: dict, population: int):

    for d in range(day_nb):
        nouveauxInfectes = tc * sir['infectes'] * (sir['susceptibles'] / population)
        nouveauxRetablis = tg * sir['infectes']

        sir['susceptibles'] = sir['susceptibles'] - nouveauxInfectes
        sir['infectes'] = sir['infectes'] + nouveauxInfectes - nouveauxRetablis
        sir['retablis'] = sir['retablis'] + nouveauxRetablis

        print(f'Le nombre de s aujd est de : {sir['susceptibles']}')

    return sir;

sir = simulation(30,taux_contamination, taux_guerison, init_sir,init_population);

