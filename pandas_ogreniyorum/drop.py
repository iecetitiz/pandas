# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 22:04:00 2023

@author: iecet
"""

import pandas as pd
import numpy as np

data = {"product_name":["Keyboard","Mouse", "Monitor", "CPU","CPU", "Speakers",pd.NaT],
        "Unit_Price":[500,200, 5000.235, 10000.550, 10000.550, 250.50,None],
        "No_Of_Units":[5,5, 10, 20, 20, 8,pd.NaT],
        "Available_Quantity":[5,6,10,"Not Available","Not Available", pd.NaT,pd.NaT],
        "Available_Since_Date":['11/5/2021', '4/23/2021', '08/21/2021','09/18/2021','09/18/2021','01/05/2021',pd.NaT]
       }

df = pd.DataFrame(data)

df.drop(index = [5, 6], axis = 0, inplace = True) #yapi bu

df.drop(df.index[2:4], inplace=True) #delete rows by index range, 4 exclusive

mydf = pd.read_csv("vgsales.csv")

df = df.iloc[:2]

df[df['Unit_Price'] >400] #bunu yazdigimda butun dataframe'i donduruyor

drops = (df[(df['Unit_Price'] >400) & (df['Unit_Price'] < 600)])
drpdf = pd.DataFrame(drops)

df.drop(df[(df['Unit_Price'] >400) & (df['Unit_Price'] < 600)].index, inplace=True) #silmek icin bir secenek de bu

