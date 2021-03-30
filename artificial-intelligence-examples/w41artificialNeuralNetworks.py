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



# YSA modelinin olusturulmasi
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model= Sequential()
model.add(Dense(16, input_dim=20, activation="relu"))
model.add(Dense(12, activation="relu"))
model.add(Dense(4, activation="softmax"))
model.summary()


# modelin derlenmsi
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics="accuracy")


# modelin egitilmesi
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs= 50)


# gerekli degerlerin gosterilmesi
print('Ortalama egitim kaybi: ', np.mean(model.history.history["loss"]))
print('Ortalama egitim basarimi: ', np.mean(model.history.history["accuracy"]))
print('Ortalama dogrulama kaybi: ', np.mean(model.history.history["val_loss"]))
print('Ortalama dogrulama basarimi: ', np.mean(model.history.history["val_accuracy"]))


# egitim ve dogrulama basarimlarinin gosterilmesi
import matplotlib.pyplot as plt 
plt.plot(model.history.history["accuracy"])
plt.plot(model.history.history["val_accuracy"])
plt.title("Model Basarim")
plt.ylabel(" Basarim")
plt.xlabel("Epok")
plt.legend(["Egitim", "Test"], loc="upper left")
plt.show


# egitim ve dogrulama basarimlarinin gosterilmesi
plt.plot(model.history.history["loss"])
plt.plot(model.history.history["val_loss"])
plt.title("Model Kaybi")
plt.ylabel(" Kaybi")
plt.xlabel("Epok")
plt.legend(["Egitim", "Test"], loc="upper left")
plt.show