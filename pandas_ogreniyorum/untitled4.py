# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 07:28:30 2023

@author: iecet
"""

import numpy as np
import pandas as pd


matrix = np.arange(1, 81).reshape(10, 8)
df = pd.DataFrame(matrix, columns = ["var1", "var2","var3","var4","var5","var6","var7","var8"])

df.head()
df.columns

df_copy = pd.DataFrame(matrix, columns = ["var1", "var2","var3","var4","var5","var6","var7","var8"])
df_copy.columns = ("deg1", "deg2","deg3","deg4","deg5","deg6","deg7","deg8")


df.axes
type(df)
df.shape
df.ndim
df.values


df_copy.index = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
df_copy["c":"f"]
df_copy["c":"f"]["c":"e"]
df[0:3]
df_copy[0:3]


me = (df_copy.loc[["c","h"], ["deg2","deg6"]])
print(type(me))
print(me)

df_copy.loc[["c","h"], ["deg2","deg6"]]

vg = pd.read_csv("vgsales.csv")

print(vg.loc[(vg["Year"] > 2000), ["Name", "Platform"]])

print(vg.loc[(vg["Year"] > 2000), "Name": "Publisher"])

vg[vg["Year"] > 2000]


elliveyuz = vg.loc[50:100, "Name": "Publisher"]
sart = vg.loc[(vg["Name"] == "Super Mario 64") | (vg["Name"] == "Tetris") ,"Name": "Publisher"]

#sart.drop(labels = [], axis = 0, inplace = True)

df_copy = df_copy.loc["a":"g", "deg1":"deg8"]

m = np.random.randint(1, 30, size = (10, 3))
joker = pd.DataFrame(m, columns = ["var1", "deg2", "var3"])
df1 = pd.DataFrame(m, columns = ["var1", "var2", "var3"])
df2 = pd.DataFrame(m, columns = ["var1", "var2", "var3"])


df3 = pd.concat([df1, df2])
df4 = pd.concat([df1, df2], ignore_index= True)
df7 = pd.concat([df_copy, joker])



df5 = pd.concat([df2, joker])
df6 = pd.concat([df2, joker], join = "inner")

















