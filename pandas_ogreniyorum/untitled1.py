# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 12:33:46 2023

@author: iecet
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Line Plot
x = np.arange(1, 6)
y = 2 * x + 4

plt.plot(x, y, color = "blue", label = "y = 2 * x + 4")
plt.legend() #bunu eklemezsem ust satirda yazdigim label gorunmez

plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("y = 2 * x + 4 graphic")
plt.show()


#Scatter Plot
#dagilimsal bir grafiktir ve iki seyi birbiriyle karsilastirmak icin kullanilir
df = sns.load_dataset("tips")
df.info()
df.describe().T

df["sex"].value_counts()
df["day"].value_counts()
df["smoker"].value_counts()
df["size"].value_counts()

#aykiri degerleri gozlemleyebilirim mesela bu grafikten ama genel olarak anliyorum ki arada dogrusal bir iliski var
plt.scatter(df["total_bill"], df["tip"], color = "green", label = "tip-total_bill")
plt.legend()
plt.xlabel("total_bill")
plt.ylabel("tip")
plt.title("tip-total_bill graphic")
plt.show()


plt.scatter(df["day"], df["tip"], color = "green", label = "tip-total_bill")
plt.legend()
plt.xlabel("day")
plt.ylabel("tip")
plt.title("day-total_bill graphic")
plt.show()

#Histogram and Bar
#Kategorik degiskenlerin frekanslari icin kullaniyoruz

plt.hist(df["size"])
plt.xlabel("size")
plt.ylabel("siklik")
plt.title("hist plot")

plt.hist(df["sex"])
plt.hist(df["smoker"])
plt.hist(df["day"])

plt.bar(df["size"], df["tip"])
plt.bar(df["sex"], df["tip"])

# Subplot
# Bir pencere birden fazla grafik gostermek icin kullaniliyor

plt.subplot(2, 1, 1) #2 satirdan ve bir sutundan olusan bir pencere yaraticak ve bunun ilk kutucugunu alacak
plt.scatter(df["total_bill"], df["tip"], color = "green", label = "tip-total_bill")
plt.legend()
plt.xlabel("total_bill")
plt.ylabel("tip")
plt.title("tip-total_bill graphic")
plt.show()

plt.subplot(2, 1, 2)
plt.scatter(df["day"], df["tip"], color = "green", label = "tip-total_bill")
plt.legend()
plt.xlabel("day")
plt.ylabel("tip")
plt.title("day-total_bill graphic")
plt.show()
plt.tight_layout()

#veya istersem 2 satirdan ve 2 sutundan olusan bir yapi da kullanabilirim
#plt.subplot(2, 2, 1) deyip altina grafigi yazarsam ilk kutucuga verdigim grafigi koyar

#Figure Olusturma
fig, axes = plt.subplots(2, 1, figsize = (5,5))
axes[0].scatter(df["tip"], df["total_bill"])
axes[1].plot(df["tip"], df["total_bill"])

fig2, axes2 = plt.subplots(2, 2, figsize = (8,8))
axes2[0,0].bar(df["size"], df["tip"])
axes2[0,1].bar(df["size"], df["tip"])
axes2[1,0].bar(df["size"], df["tip"])
axes2[1,1].bar(df["size"], df["tip"])

#fig burdaki tum gorselin ismi
#mesela kaydetmeme yariyor

fig2.savefig("graphic1.png")
fig2.savefig("graphic1.pdf")









