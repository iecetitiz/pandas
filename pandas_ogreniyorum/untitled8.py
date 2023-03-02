# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 18:55:14 2023

@author: iecet
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({"gruplar": ["A", "B", "C", "A", "B", "C"],
                   "degisken1": [10, 23, 33, 22, 11, 99], 
                  "degisken1": [10, 23, 33, 22, 11, 99],
                  "degisken2": [100, 253, 333, 262, 111, 969]}, 
                  columns = ["gruplar", "degisken1", "degisken2"])

df.groupby("gruplar").mean() #bunu dedigim zaman meani alinabilecek tum degiskenlerin meanini hesapliyor
df.groupby("gruplar").aggregate(["min", np.median, max]) #describe deseydim istemesem de tum diger functionlar da gelecekti

df.groupby("gruplar").aggregate({"degisken1" : "min","degisken2" : "max" }) #abi yok artik ama ya
#her bir degisken icin farkli bir sey bulduruyorum su an


#Filter
def filter_func(x):
    return x["degisken1"].std() > 9

print(df.groupby("gruplar").filter(filter_func))

#transform
#degiskenler uzerinde bir donusturme islemi yapmak istedigimde bunun adi transform olmus olacak

df["degisken1"] * 9
df_a = df.iloc[:, 1:3] #amacim gruplar sutunundan kurtulmak cunku azsonra uygulayacagim islemi kategorik degiskenlere uygulayacagi zaman hata alirim

df_a.transform(lambda x: x-x.mean())
df_s = df.iloc[:, 1:3]
df_s.transform(lambda x: (x - x.mean()) / x.std())

#apply
#aggregation amaciyla kullanacagim tum degiskenler uzerinde dolasan tipki filter ve transform gibi bir method

df_s.apply(np.sum) #np.sum yerine baska herhangi bir function da yazmis olabilirdim mesela kendi yazdigim bir function
df_s.apply(np.mean)

#peki gruplar degiskeni de olsaydi nasil olurdu
df.groupby("gruplar").apply(np.sum)

#aggregate, filter, transform va apply ileri toplulastirma islemleri
































