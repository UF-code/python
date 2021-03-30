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


# egitim ve test verilerinin hazirlanmasi
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2)


# cikti degerlerinin kategorilestirilmesi
from tensorflow.keras.utils import to_categorical
y_train= to_categorical(y_train)
y_test= to_categorical(y_test)