# kutuphanelerin yuklenmesi
import numpy as np 
import pandas as pd 
from sklearn.preprocessing import LabelEncoder


# verisetlerin yuklenmesi
data = pd.read_csv('phone_data.csv')


# sinif sayisinin belirlenmesi
label_encoder= LabelEncoder().fit(data.price_range)
labels= label_encoder.transform(data.price_range)
classes= list(label_encoder.classes_)

X= data.drop(['price_range'], axis=1)
y= labels



# verilerin standartlastirilmasi
from sklearn.preprocessing import StandardScaler 
sc = StandardScaler()
X= sc.fit_transform(X)