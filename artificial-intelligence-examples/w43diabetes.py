# importing essential libraries
import numpy as np 
import pandas as pd 
from sklearn.preprocessing import LabelEncoder 


# reading data's
data = pd.read_csv('diabetes.csv')


# class specification
label_encoder= LabelEncoder().fit(data.output)
labels= label_encoder.transform(data.output)
classes= list(label_encoder.classes_)

X= data.drop(['output'], axis=1)   
y= labels


# data standartization
from sklearn.preprocessing import StandardScaler 
sc= StandardScaler()
X= sc.fit_transform(X)


# preparing dataset for Training and Testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size= 0.2)


# categorizin outputs 
from tensorflow.keras.utils import to_categorical
y_train= to_categorical(y_train)
y_test= to_categorical(y_test)


# creating Artificial Neural Network for diabetes data
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense 

model= Sequential()
model.add(Dense(8, input_dim=8, activation="sigmoid"))
model.add(Dense(6,  activation="sigmoid"))
model.add(Dense(4,  activation="sigmoid"))
model.add(Dense(2,  activation="softmax"))
model.summary()


#  compiling model
model.compile(loss="binary_crossentropy", optimizer="adam", metrics="accuracy")