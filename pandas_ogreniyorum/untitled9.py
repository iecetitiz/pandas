# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 09:58:31 2023

@author: iecet
"""

import pandas as pd

#mesela github'dan bir veri seti almak isteyebilirsin
ornek_csv = pd.read_csv("reading_data/ornekcsv.csv", sep = ";") #sep'i koymasaydim istedigim gibi olmayacakti
duz_metin = pd.read_csv("reading_data/duz_metin.txt") #sep kullanmadim ama sorun cikarmadi cunku bosluklari txt'de sorun etmedi
excel = pd.read_excel("reading_data/ornekx.xlsx")
# bu 3 yapi da artik dataframe

data = pd.read_csv("reading_data/data.txt")
