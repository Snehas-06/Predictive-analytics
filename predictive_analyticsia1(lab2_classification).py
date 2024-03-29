# -*- coding: utf-8 -*-
"""Predictive_analyticsIA1(LAB2-CLASSIFICATION).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QtXCEMuv8-FXXzafJeuLASvkiX2-dGMJ
"""

import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/Predictive analytics Practice/booking.csv')
#print(data)

d1 = df.isnull().sum()
d2 = df.duplicated().sum()
#print(d1)
#print(d2)

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
outliers = ((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)

cleaned_df = df[~outliers]
cleaned_df.to_csv('cleaned_dataset.csv', index=False)

from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

x = df.drop(columns=['booking status'])
y = df['booking status']

X_train,X_test,Y_train,Y_test = train_test_split(x,y,test_size=.3,random_state=42)

model1 = LabelEncoder()
m1 = model1.fit_transform(df[['room type']])
m2 = model1.fit_transform(df[['type of meal']])
m3 = model1.fit_transform(df[['booking status']])

model2 = DecisionTreeClassifier()
model2.fit(X_train,Y_train)
result = model2.predict(X_test)

accuracy = accuracy_score(Y_test,result)

print(accuracy)

if result == 0 :
  print("your booking is cancelled")
else :
  print("your booking is not cancelled")