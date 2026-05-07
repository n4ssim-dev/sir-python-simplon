import random
import time
import matplotlib.pyplot as plt
import pandas as pd
from typing import TypedDict

taux_contamination: float = 0.1
taux_guerison: float= 0.1
init_population: float = 1000

S = [init_population-1]
I = [1]
R = [0]

def simulation(day_nb: int,tc: float,tg: float,popu: int, s=list,i=list,r=list):
    d_saturation = None

    for d in range(0,day_nb):

        nouveauxInfectes = tc * float(i[d]) * (s[d] / popu)
        nouveauxRetablis = tg * float(i[d])

        s.append(s[d] - nouveauxInfectes)
        i.append(i[d] + nouveauxInfectes - nouveauxRetablis)
        r.append(r[d] + nouveauxRetablis)

        if i[d] >= 15:
            if d_saturation is not None:
                d_saturation = d

    sir = {
        "susceptibles": s,
        "infectes": i,
        "retrait": r,
        "d_saturation": d_saturation
    }

    return sir;

sir = simulation(30,taux_contamination,taux_guerison, init_population, S,I,R);
print(sir)