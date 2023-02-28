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

df.iloc[0:3, "var3"] #iloc kullanacagim zaman degisken ismi kullanamiyorum
df.iloc[0:3]["var3"] #ama boyle kullanmamda bir sakinca yok


