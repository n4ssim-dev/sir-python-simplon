import random
import time
import math
import matplotlib.pyplot as plt
import pandas as pd

taux_contamination: float = 0.1
taux_guerison: float = 0.1
init_population: float = 1000

S = [init_population - 1]
I = [1]
R = [0]

pop_types = {
    'enfants': {
        'indice': 1,
        'tranche': [0,18],
        # %de la pop
        'population': init_population * 0.18,
        # taux de contamination
        'tc': 0.3, # haut
        # taux de guérison
        'tg': 0.05, # faible
        # dict qui stock les sir de ce groupe
        'sir': {}
    },
    'adultes': {
        'indice': 2,
        'tranche': [18,67],
        'population': init_population * 0.49,
        'tc': 0.15, # moyen
        'tg': 0.1, # moyen
        'sir': {}
    },
    'seniors': {
        'indice': 3,
        'tranche': [67,100],
        'population': init_population * 0.33,
        'tc': 0.05, # faible
        'tg': 0.05, # faible
        'sir': {}
    }
}


def simulation(day_nb: int, tc: float, tg: float, popu: int, s: list, i: list, r: list):
    d_saturation_achieved = False
    d_saturation = None

    for d in range(0, day_nb):

        nouveauxInfectes = tc * float(i[d]) * (s[d] / popu)
        nouveauxRetablis = tg * float(i[d])

        s.append(s[d] - nouveauxInfectes)
        i.append(i[d] + nouveauxInfectes - nouveauxRetablis)
        r.append(r[d] + nouveauxRetablis)

        if i[d] >= 15 and not d_saturation_achieved:
            d_saturation = d
            d_saturation_achieved = True

    return {
        "susceptibles": s,
        "infectes": i,
        "retrait": r,
        "d_saturation": d_saturation
    }

def simulation_by_age_id(nb_day: int, id_age: int):
    # Cible la cat avec l'indice age
    groupe = next(g for g in pop_types.values() if g['indice'] == id_age)

    # Init le sir de cette cat
    pop = groupe['population']
    s = [pop - 1]
    i = [1]
    r = [0]

    # Fais une simulation et assigne les valeurs en param
    groupe['sir'] = simulation(nb_day, groupe['tc'], groupe['tg'], pop, s, i, r)
    return groupe['sir']

def simulation_all_age(func):
    nb_of_age = len(pop_types)
    for i in range(nb_of_age):
        func()

sir = simulation(30, taux_contamination, taux_guerison, init_population, S, I, R)
sir_by_age = simulation_by_age_id(300, 1)

# Imprime la dict sir dans la dict avec l'indice correspondant au 2eme arg
print(sir_by_age)
