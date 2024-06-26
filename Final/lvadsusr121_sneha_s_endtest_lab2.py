# -*- coding: utf-8 -*-
"""LVADSUSR121_SNEHA S_ENDTEST_LAB2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QwC254A4KHT1VnU5yhZcCEIfdRcayJGo
"""

import pandas as pd
data = pd.read_csv('/content/drive/MyDrive/Predictive analytics Practice/auto-mpg.csv')
print(data)

data.info()

data.describe()

data.shape

data.isnull().sum()

data.fillna(data.mean(), inplace=True)

data.isnull().sum()

from matplotlib import pyplot as plt
import seaborn as sns
def _plot_series(series, series_name, series_index=0):
  palette = list(sns.palettes.mpl_palette('Dark2'))
  xs = series['weight']
  ys = series['mpg']

  plt.plot(xs, ys, label=series_name, color=palette[series_index % len(palette)])

fig, ax = plt.subplots(figsize=(10, 5.2), layout='constrained')
df_sorted = data.sort_values('weight', ascending=True)
_plot_series(df_sorted, '')
sns.despine(fig=fig, ax=ax)
plt.xlabel('weight')
_ = plt.ylabel('mpg')

duplicates = data.duplicated(keep=False)
data['dup_bool'] = duplicates
print(data[data['dup_bool'] == True].count())
data.drop('dup_bool',axis=1)
data.head(1)

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

from sklearn.model_selection import train_test_split

x = data.drop(['car name','origin','mpg'],axis=1)
y = data['mpg']

X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.33, random_state=42)

from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
import xgboost as xgb
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import numpy as np

dtr = DecisionTreeRegressor()
dtr.fit(X_train,y_train)
y_pred = dtr.predict(X_test)
MSE = mean_squared_error(y_test, y_pred)
RMSE = np.sqrt(MSE)
r2 = r2_score(y_test, y_pred)
print("Decision tree \nMSE:", MSE)
print("RMSE:", RMSE)
print("R2 score:", r2)



lr = LinearRegression()
lr.fit(X_train,y_train)
y_pred = lr.predict(X_test)
MSE = mean_squared_error(y_test, y_pred)
RMSE = np.sqrt(MSE)
r2 = r2_score(y_test, y_pred)
print("Linear regression \nMSE:", MSE)
print("RMSE:", RMSE)
print("R2 score:", r2)



rfr = RandomForestRegressor()
rfr.fit(X_train,y_train)
y_pred = rfr.predict(X_test)
MSE = mean_squared_error(y_test, y_pred)
RMSE = np.sqrt(MSE)
r2 = r2_score(y_test, y_pred)
print("Random Forest \nMSE:", MSE)
print("RMSE:", RMSE)
print("R2 score:", r2)



xgbr = xgb.XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
xgbr.fit(X_train, y_train)
y_pred = xgbr.predict(X_test)
MSE = mean_squared_error(y_test, y_pred)
RMSE = np.sqrt(MSE)
r2 = r2_score(y_test, y_pred)
print("XGB \nMSE:", MSE)
print("RMSE:", RMSE)
print("R2 score:", r2)