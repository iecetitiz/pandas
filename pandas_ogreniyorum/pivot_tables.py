# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 07:51:37 2023

@author: iecet
"""

import pandas as pd
import seaborn as sns
titanic = sns.load_dataset("titanic")
titanic.head()

titanic.groupby("sex")[["survived"]].mean() #ic ice iki koseli parantez yapinca bir dataframe yapmis oldum
titanic.groupby(["sex", "class"])[["survived"]].aggregate("mean").unstack()
#yukarda kullandigim unstack() methodu yan yana daha net bir sekilde gormemi sagladi 

#ama bunun cok daha kolay bir yolu var
titanic.pivot_table("survived", index = "sex", columns = "class")

#peki cok boyutlu bir pivot olusturmak istersem
age = pd.cut(titanic["age"], [0, 18, 90]) #surekli bir degiskeni kategorik bir degiskene donusturmus oldum

age.head(10)

titanic.pivot_table("survived", ["sex", age], "class") #sex'i tirnaksiz, age'i de tirnakli yazamam
#sebebi, sex'i tablonun kendisinden almam, age'i de kendim olusturmam


