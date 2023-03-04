# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 10:23:07 2023

@author: iecet
"""

import numpy as np
import pandas as pd

dicti = {"name: ": ["ali", "veli", "hasan"],
         "age": [12, 34, 56],
         "salary": [1200, 1500, 1600]}


#bu yapiyla birlikte key'ler sutun olarak geldi, valuelar da bu sutun isimlerinin degerleri olarak geldi
#yani excell dosyasina benzer bir yapi olusturdum
#DataFrama yapisi da bu zaten
# bu yapiyi df degiskenine atiyorum
df = pd.DataFrame(dicti)
print(df.shape)


#simdi, yukaridaki benim kendi olusturdugum datanin DataFrame'iydi, ben simdi disardan dosya cekip onun DataFrame'ini yaraticam
vg = pd.read_csv("vgsales.csv")

#bir data frame'in boyutlarini alabilirim, sutun sayisi kadar degiskenim olmus oluyor yani, fiyat, marka falan
print(vg.shape)




#elindeki veri setini oncelikle taniman lazim
head5 = vg.head() #default olarak ilk 5 tanesini getiriyor
head10 = vg.head(10)

tail5 = vg.tail() #default olarak ilk 5 tanesini getiriyor
tail10 = vg.tail(10)

# Pandas 2
#mesela Year column'unda eksik veri varmis bunu gorebilirim burdan
#ve Dtype kismindan bu sutunlarin icindeki verilerin tipini ogrenebilirim

print(vg.columns) #bana veri setimdeki sutunlarin isimlerini getiriyor, copy paste yapip kullanmak istedigimde kullanabilirim

print(vg.info()) # bu sonuc geldiginde non-null degerlere bakarak hangi sutunalrda eksik veri var mesela bunu gorebilirim
#ve burda dtype ksiminda yazan object string demek aslinda
#ayrica eksik verileri ayrica isleyecegiz

#yukardaki bilgiyi yalnizca sutunlarin data type'lari seklinde de alabiliridim
print(vg.dtypes)


#simdi cok cok cok onemli bir method, hatta o kadar onemli ki baska bir degiskene aktarip kullanicam
describe = vg.describe() #bu method sadece sayisal olan sutunlari aliyor
describeT = vg.describe().T #boyle gormek daha kolay
eksikleri_sil = vg.dropna().describe().T #nan degerleri goz ardi ederek istatistik sunuyor
# %50 olarak verilen medyani gosteriyor

# Pandas 3
#Indexleme ve parcalama yapicaz ve bu cok siklikla yaptigimiz bir sey olacak

Platform = vg["Platform"] #bir sutunun tamamini boyle getirebilirim
Year = vg.Year #istersem de boyle getiririm, ama bu sefer column isminde bosluk olursa hata alirim o yuzden ustteki gibi yazmak daha iyi olabilir

print(vg.loc[:, "Global_Sales"]) #stop degerleri bu sefer dahil bilgin olsun, ayrica yine sol taraf satir sag taraf sutun
print(vg.loc[2:5, "Name":"Genre"])
print(vg.loc[::-1, "Global_Sales"]) #istersem tersten de yazdirabilirim

#istersem fancy index loc icinde de kullanabilirim
#istersem kosullu islem de yapabilirim

print(vg.iloc[:, 2:4]) #iloc oldugunda fark yine ayni numpy gibi olmasi, indexlerle ve numaralariyla bir dilimleme yapiyorum
#yine ayni numpyda ogrendigim gibi baslangiclar dahil bitisler dahil degil

# Pandas 4
# Filtreleme
#Aslinda burda yaptigim sey sql'de where kosulunu kullanmak

filter = vg["Year"] > 2000 #bu filtre bana True ve False'lardan olusan bir yapi dondurecek
yeni = vg[filter] #butun csv file icindeki degerleri getirecek ve bunlar icinden ayiklayacak

eski = vg[vg["Year"] < 1990] #istersem bu filtrelemeyi abstraction olmadan boyle de yapabilirim

#birden fazla sart da saglayabilirim

sales = vg[(vg["Publisher"] == "Nintendo") & (vg["Global_Sales"] > 0.50) ] #kosullari ayri ayri parantezlere almak onemli

# Pandas 5 
# List Comprehension ile yeni bir sutun eklemek

vg2 = pd.read_csv("vgsales.csv")
vg2["trend"] = ["eski" if i < 2010 else "yeni" for i in vg2.Year] #olmayan bir sutuna erisiyormus gibi davrandigimda yeni bir sutun olusturuyorum

vg2["deneme"] = [i+2 for i in vg2.index]

for i in vg2.Year:
    print(i)


ort_global_sales = vg2["Global_Sales"].mean()

vg2["satis_degeri"] = ["dusuk" if i < ort_global_sales else "yuksek" for i in vg2["Global_Sales"]]

# Pandas 6
# Birlestirme ve Silme

vg2.drop(["deneme"], axis = 1, inplace = True )

head3 = vg2.head(3)
tail3 = vg2.tail(3)

concat = pd.concat([head3, tail3]) #defaultu axis = 0

Genre = vg2["Genre"]

concat2 = pd.concat([Genre, Platform], axis = 1)


# Pandas 7
# Group by

vg2["Genre"].unique() 
vg2.groupby("Genre").sum()
vg2.groupby("Genre")["Global_Sales"].sum()
vg2.groupby("Genre")["Global_Sales"].max()
vg2.groupby("Genre")["Global_Sales"].min()

vg2["Platform"].unique()
vg2.groupby("Platform")["JP_Sales"].count()
vg2.groupby("Platform")["JP_Sales"].max()
vg2.groupby("Platform")["JP_Sales", "Rank"].max()

# Pandas 8
# value_counts(), apply(), data types

vg2["Genre"].unique()
vg2["Genre"].value_counts() # her bir unique degerin kac kez gozlemlendigini sayiyor
vg2["trend"].value_counts()

vg2["trend"] = ["eski" if i < 2010 else "yeni" for i in vg2.Year]

vg2["yeni_trend"] = ["eski" if i < 2010 else "yeni" for i in vg2.Year] #yeni bir sutun ekliyorum

def hello(i):
    if i < 2010:
        return "old"
    else:
        return "new"



vg2["hello"] = vg2["Year"].apply(hello)


def ikikat(i):
    return i*2

vg2["ikikatsatis"] = vg2["Global_Sales"].apply(ikikat)

vg2.dtypes

vg2.NA_Sales = vg2.NA_Sales.astype("int")


vg2.dtypes

#-----------------------------------------------------------------------

# Pandas Series

seri = pd.Series([10, 33, 88, 9]) #numpy arraylerinden farki index numaralariyla gelmis olmasi
print(seri.shape)
print(type(seri))
print(seri.axes)
print(seri.dtype)
print(seri.size)
print(seri.ndim)
print(seri.values)
print(seri.head())
print(seri.tail())

pd.Series([12, 45, 6, 78, 9], index = [2, 5, 7, 8, 9]) #istersem indexleri kendim belirleyebilirim

seri2 = pd.Series([12, 45, 6, 78, 9], index = ["a", "b", "c", "d", "e"]) #istersem stringleri de index yapabilirim
print(seri2["a"])
print(seri2["a":"c"]) #istersem boyle bir slice da yapabilirim

sozluk = pd.Series({"reg": 10, "log":11, "cart": 12, "ece": 30}) #istersem bir dictionary'i Series icine direkt de atabilirim
#ustte yaptigim dilimleme islemini aynen burda da yapabilirim
#gercek hayatta bir pandas serisiyle calisiyorsak genelde elimizde boyle bir yapi olur


sozluk["reg": "cart"]

pd.concat([seri, seri]) #istersem serileri birlestirerek de bir pandas serisi olusturabilirim

# Eleman islemleri

a = np.array([1, 2, 33, 444, 75])
serim = pd.Series(a)

print(serim[1])
print(serim[1:3])

print(serim.index) #serimin index numaralarini alabilirim
print(seri.index)
print(sozluk.index) #ayni sekilde burdan da indexlere ulasirim
print(sozluk.keys) #keylere ulasiyorum
print(list(sozluk.items())) #itemlara ulasiyorum
print(sozluk.values)

#eleman sorgulama

"reg" in serim
"reg" in sozluk

#fancy index

sozluk[["log", "reg"]]

#DataFrame
#makine ogrenmesindeki kilit rol pandas islemlerindedir
#istersem python listlerden de DataFrame yaratabilirim

l = [1, 2, 39, 12, 67, 90]
pd.DataFrame(l, columns=["degisken_ismi"])

m = np.arange(1, 10).reshape((3, 3))
pd.DataFrame(m, columns=["var1", "var2", "var3"])

df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df1.head()
df1.columns

#istersem degiskenlerin ismini degistirebilirim
df1.columns = ("deg1", "deg2", "deg3")

#DataFrame hakkinda bilgi alabilirim
df.axes
type(df)
df1.shape
df1.ndim
df1.size
df1.values #degisken isimleri olmadan sadece degerleri veriyor, type olarak da ndarray

type(df1.values) #value degerlerini aldigimda numpy arrayine ceviriyor

#Numpy arrayi uzerinden de DataFrame olusturabilirim, ki yukarida da olusturdum zaten

a = np.array([1, 2, 3, 4])
pd.DataFrame(a, columns = ["dgisken1"])

#Eleman Islemleri
s1 = np.random.randint(10, size = 5)
s2 = np.random.randint(10, size = 5)
s3 = np.random.randint(10, size = 5)

dictionary = {"var1": s1, "var2": s2, "var3": s3}

df_dictionary = pd.DataFrame(dictionary) #dictionary'yi direkt iceri atip da kullanabilirim

df_dictionary.index #boyle ulasabildigim gibi istersem degistire de bilirim

df_dictionary.index = ["a", "b", "c", "d", "e"] #boyle de degistiririm

df["c":"e"] #bunu soyleyebilirim artik, ama bunu loc/iloc mantigiyla yaparim


#istersem bir sutunu istersem de bir satiri silerim, satir sileceksem axis = 0, sutun sileceksem axis = 1
df_dictionary.drop("a", axis = 0, inplace = True) #indexi a olan satiri siler
#eger inplace'i True olarak degistirmezsem yaptigim degisiklik kalici olmaz


#fancy index ile birden fazla satiri secip tum o satirlari sutlayabilirim

fancy_filter = ["c", "b"]
df_dictionary.drop(fancy_filter, axis = 0) 

#bir degisken isminin olup olmadigini sorgulayabilirim

"var1" in df_dictionary

#aaaaaaaaaa ama bu cok guzel bi sorgu
h = ["melis", "mert", "hakan"]
for i in h:
    print(i in df_dictionary) #ic ice iki for dongusu gibi aslinda


#elimde var olan iki tane sutunu kullanarak yeni bir sutun yaratabilirim
df_dictionary["fark"] = df_dictionary["var1"] - df_dictionary["var2"]

#degisken silmek
df_dictionary.drop("fark", axis = 1, inplace = True)

#fancy index'i yine kullanabilirim ve istedigim sutunlari sutlarim
filter_again = ["var1", "var3"]
df_dictionary.drop(filter_again, axis = 1) #inplace eklesem kalici olurdu


df.drop(index = [3], axis = 0, inplace = True)





