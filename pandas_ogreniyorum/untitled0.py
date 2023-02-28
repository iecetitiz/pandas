# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 11:03:54 2023

@author: iecet
"""

import pandas as pd

dict = {"ece" : [90, 89, 92],
        "mert": [70, 69, 40],
        "hasan": [90, 60, 40]}

df = pd.DataFrame(dict)

print(df.shape)

vg = pd.read_csv("vgsales.csv")
print(vg.shape)

head5 = vg.head()
tail5 = vg.tail()

print(vg.columns)
print(vg.info())
print(vg.dtypes)

describe = vg.describe()
describeT = vg.describe().T

