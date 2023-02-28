# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 08:02:11 2023

@author: iecet
"""
#Outlier
import pandas as pd
import seaborn as sns

df = pd.read_csv("heart.csv")
df_chol = df["chol"]

df_chol.describe()

sns.boxplot(x = df_chol)

Q1 = df_chol.quantile(0.25)
Q3 = df_chol.quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR


df_chol = pd.DataFrame(df_chol)

lower_bound_filter = (df_chol < lower_bound)
upper_bound_filter = (df_chol > upper_bound)
filter = (lower_bound_filter | upper_bound_filter)

df[lower_bound_filter]

df_chol[upper_bound_filter]
aykiri_gozlemler = df_chol[filter]


clean_df = df[~filter.any(axis = 1)]
clean_df_chol = df_chol[~filter.any(axis = 1)]

cleans_df = df[~filter]


#Eksik Veri
#bazi durumlarda o sutunda nan yaziyor olmasi veri setinin kendi ozelligi olabilir yani orasinin o sutunla bir iliskisi yoktur mesela
#bu durumlarda o nan degerleri ellemiyoruz ve eksik veri olarak kabul etmiyoruz
#mesela kredi karti olmayan birinin borc bilgilerinin bos olmasi gerekir zaten, gibi


my_df = pd.read_csv("vgsales.csv")
my_df.info() #bu bilgiye baktiktan sonra non-null degerlere bakip hangi sutunlarda eksik veri oldugunu gorebilirim

my_df.columns[my_df.isnull().any()]
my_df.isnull().sum() #kac tane null degerim oldugunu veriyor

year = my_df[my_df["Year"].isnull()]
publisher = my_df[my_df["Publisher"].isnull()]

my_df.dropna()
my_df.dropna(inplace = True) #bu satiri calistirdigimda eksik olan tum veriler silinecek ama bu mantikli degil cunku neden eksik olan bir 
#yil degiskeni icin tum verilerimi kaybedeyim, o yuzden silmek yerine nan olan yil degiskenini ortalama yil ile doldurucam

mean_year = int(my_df["Year"].mean())
my_df["Year"].fillna(mean_year, inplace = True)


my_df.info()
my_df["Publisher"].unique #yila uyguladigim doldurma islemini publisher ile doldurmuyorum cunku makine ogrenmesinde boyle unique degerler kullanilmaz yani bir anlam tasimaz o yuzden burayi ellemiyorum











