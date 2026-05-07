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

pop_type_indice = {
    'enfants': {
        'indice': 1,
        'tranche': [0,18],
        'population': init_population / 0.18,
        'tc': 0, # haut
        'tg': 0 # faible
    },
    'adultes': {
        'indice': 2,
        'tranche': [18,67],
        'population': init_population / 0.49,
        'tc': 0, # haut
        'tg': 0 # moyen
    },
    'seniors': {
        'indice': 3,
        'tranche': [67,100],
        'population': init_population / 0.33,
        'tc': 0, # faible
        'tg': 0 # faible
    }
}

def change_scenario(mtc: int, mtg: int):
    def decorator(func):
        def my_inner(*args, **kwargs):
            # Applique un multiplicateur au taux de conta (mtc) et de guerison (mtg)
            args = list(args)
            args[1] = args[1] * mtc  # tc
            args[2] = args[2] * mtg  # tg
            return func(*args, **kwargs)
        return my_inner
    return decorator

def scenario_by_age():
    

def limit_check(func):
    def my_inner(*args, **kwargs):
        # fait en sorte que somme des SIR = 1000 et infectes <= 1000
        result = func(*args, **kwargs)
        popu = args[3] if len(args) > 3 else kwargs.get('popu', 1000)
        result['infectes'] = [min(v, popu) for v in result['infectes']]
        return result
    return my_inner


# x de taux de conta, x de taux de guer
@change_scenario(1, 1)
@limit_check
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

    sir = {
        "susceptibles": s,
        "infectes": i,
        "retrait": r,
        "d_saturation": d_saturation
    }

    return sir

sir = simulation(30, taux_contamination, taux_guerison, init_population, S, I, R)
print(sir["d_saturation"])
