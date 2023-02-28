# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 18:04:06 2023

@author: iecet
"""

import numpy as np
import pandas as pd

dict = {"age": [12, 34, 56, 34, 35, 23, 67, 89, 67, 12, 13],
         "salary": [1200, 1500, 1600, 1700, 2000, 3000, 4000, 1200, 1500, 1700, 4000]}

df = pd.DataFrame(dict)
print(df.shape)

vg = pd.read_csv("vgsales.csv")
print(vg.shape)

head = vg.head()
tail = vg.tail()


print(vg.columns)
print(vg.info())
print(vg.dtypes)

describe = vg.describe()
describeT = vg.describe().T

Year = vg["Year"]
Publisher = vg.Publisher

print(vg.loc[:2, "Rank":"Platform"])
print(vg.iloc[1:5, 2:5]) #baslangiclar dahil bitisler dahil degil


normal = df[(df["age"] < 50) & (df["salary"] > 1000)]

df["yas durumu"] = ["yasli" if i > 40 else "genc" for i in df["age"]]


for i in df["age"]:
    print(i)
    
    
































