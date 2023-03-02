# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 16:28:58 2023

@author: iecet
"""

import seaborn as sns
import pandas as pd

df = pd.DataFrame({"gruplar": ["A", "B", "C", "A", "B", "C"],
                   "veri": [10, 11, 52, 23, 43, 55]}, columns = ["gruplar", "veri"])

df.groupby("gruplar") #bunu soyledigimde gruplara ayirir ama ne yapacagini da henuz bilemez
#ayrica, bu cok onemli, gruplama yapabilmek icin benim kategorik degiskenlere ihtiyacim var

df_planets = sns.load_dataset("planets")

df_planets.groupby("method")["orbital_period"].mean()

bombe = df_planets.groupby("method")["orbital_period"].describe() #bombee
