# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 12:52:28 2023

@author: iecet
"""

import pandas as pd

#ileri birlestirme islemleri
df1 = pd.DataFrame({"calisanlar": ["Ali", "Veli", "Ayse", "Fatma"],
                    "grup": ["Muhasebe", "Muhendislik", "Muhendislik", "IK"]})

df2 = pd.DataFrame({"calisanlar": ["Ali", "Veli", "Ayse", "Fatma"],
                    "ilk_giris": [2010, 2009, 2014,2019]})


df3 = pd.merge(df1, df2) #bir kosul ya da parametre belirtmememe ragmen her iki data frame'de de ortak olan calisanlar sutununa gore bir birlestirme yapti
df5 = pd.DataFrame({"calisanlar": ["Murat", "Veli", "Ayse", "Fatma"],
                    "grup": ["Muhasebe", "Muhendislik", "Muhendislik", "IK"]})

df6 = pd.merge(df5, df2) #farkli bir satir oldugunda onu es gecerek digerlerini eslestiriyor


df3 = pd.merge(df1, df2, on = "calisanlar") #boyle yazarsam da kendim belirtmis oluyorum

df4 = pd.DataFrame({"grup": ["Muhasebe", "Muhendislik","IK"], 
    "mudur": ["Caner", "Mustafa", "Berkcan"]})


df7 = pd.merge(df3, df4)

df8 = pd.DataFrame({"grup": ["Muhasebe", "Muhasebe", "Muhendislik", "Muhendislik","IK", "IK"], 
    "yetenekler": ["matematik", "excel", "kodlama", "linux", "excel", "yonetim"]})


df9 = pd.merge(df1, df8)
