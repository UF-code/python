# importing libraries
import numpy as np 
import pandas as pd 


# loading dataset
data= pd.read_csv('phone_data.csv')


# class specification
from sklearn.preprocessing import LabelEncoder, StandardScaler

label_encoder= LabelEncoder().fit(data.price_range)
labels= label_encoder.transform(data.price_range) 
classes= list(label_encoder.classes_)

X= data.drop(['price_range'], axis=1)
y= labels


# standardization of datasets
sc= StandardScaler()
X= sc.fit_transform(X)



# preperation of datasets for to learning and testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size= 0.2)



# categorizing the outputs
from tensorflow.keras.utils import to_categorical 
y_train= to_categorical(y_train)
y_test= to_categorical(y_test)




from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# (1) Verilen kodu inceleyerek kendi modelinizi oluşturunuz
# building Artificial Neural Network model
model = Sequential()
model.add(Dense(20, input_dim=20, activation="relu"))
model.add(Dense(16, activation="relu"))
model.add(Dense(12, activation="relu"))
model.add(Dense(8, activation="relu"))
model.add(Dense(4, activation="softmax"))
model.summary()


# (1) Verilen kodu inceleyerek kendi modelinizi oluşturunuz
# compiling the model
model.compile(loss="caterogical_crossentropy", optimizer="adam", metrics=["accuracy"])


# (1) Verilen kodu inceleyerek kendi modelinizi oluşturunuz
# training the model
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=100)