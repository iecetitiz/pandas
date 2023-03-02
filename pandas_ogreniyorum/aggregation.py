# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 16:12:20 2023

@author: iecet
"""

import seaborn as sns

df = sns.load_dataset("planets")

#?sns.load_dataset bu sorguyu sag tarafta konsolda calistirdigim zaman hangi datasetleri kullanabilecegimi bana soyleyecek

mean = df.mean() #bu fonksiyon tum data frame icindeki tum sutunlarin mean degerlerini getirecek
print(type(mean))

df.head() #veriyi hizli ve daha kolay bir sekilde tanimak icin kullaniyorum
df["mass"].mean()
df["mass"].count() #nan degerleri saymiyor




