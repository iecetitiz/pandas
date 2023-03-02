# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 14:11:39 2023

@author: iecet
"""

import numpy as np
import pandas as pd

m = np.random.randint(1, 30, size = (10, 3))
df = pd.DataFrame(m, columns = ["var1", "var2", "var3"])
df

# ?np.random.randint yazip calistirdigimda docstringi aciyor

#devam

df.loc[0:3, "var3"]

#df.iloc[0:3, "var3"] #iloc kullanacagim zaman degisken ismi kullanamiyorum
df.iloc[0:3]["var3"] #ama boyle kullanmamda bir sakinca yok


df["var1"]
print(type(df["var1"]))

df["var1"][4:7] #boyle kullanmamda hicbir sakinca yok

df[1:7][2:5] #bunun buncusunu aliyorum(satirlari aliyorum, aldiklarimdan yine satirlari aliyorum)

df[1:7][["var1", "var3"]] #fancy index burda da isliyor

#kosullu eleman islemleri
df.var1 > 15 #butun df'yi degil sadece var1'i getiriyor
df[df.var1 > 15]
df[df.var1 > 15]["var1"] #boyle yaptigimda da butun df'yi degil yalnizca istedigim sutunu almis oldum

df[df.var1 > 15][["var1", "var3"]]
df.loc[(df.var1 > 15), ["var1", "var2"]] #her iki satirda yaptiklarim da ayni seyi yapiyor

df.loc[(df.var1 > 15), "var1":"var3"] #boyle yaparsam da loc mantigini kullanmis oluyorum

#Birlestirme Islemleri
df2 = df + 99 #ya yuh artik ama ya, df'nin butun elemanlarina 99 ekledim ve yeni bir df olusturdum
df2

pd.concat([df, df2])

df3 = pd.concat([df, df2]) #dikkat edersen indexler de oldugu gibi geldi
#bu yuzden boyle bir sorun yasadiginda fonksiyonun detaylarina git ve bu sorunu cozup cozemeyecegine bi bak

df2.columns = ["var1", "var1", "var3"]
df3 = pd.concat([df, df2], ignore_index= True)
#burda bir noktaya deginmek istiyorum, fark ettiysen her iki df'mde de sutun isimleri ayniydi
#simdi degistiriyorum ve tekrar birlestirmeyi denicem

#df2.columns = ["var1", "var1", "degisken3"]


pd.concat([df, df2], join = "inner", ignore_index=True)





















