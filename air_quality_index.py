# -*- coding: utf-8 -*-
"""air quality index

Automatically generated by Colaboratory.


"""
#Importing the modules required.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from fbprophet import Prophet

#Reading the input data
data = pd.read_csv("AirQualityUCI.csv",delimiter=';')

print(data.head())

#Dropping the unwanted columns.
data.drop(['Unnamed: 15','Unnamed: 16'],axis =1, inplace = True)

print(data.head())

data = data.dropna()

print(data)

#Converting the date and time in a format to be recognised by the fbprophet.
data['Date'] = pd.to_datetime(data['Date'],format="%d/%m/%Y")

print(data.head())

#To print the number of readings recorded per day.
print(data['Date'].value_counts())

data.index = pd.DatetimeIndex(data['Date'])

#Getting the average of data per day.

data = data.resample('D').mean()
#Sorting the values based on the date index.
data = data.sort_values('Date')

#Renaming all the columns in the dataset.
data = data.rename(columns={'Date	':'ds','PT08.S1(CO)':'y','NMHC(GT)':'y1','PT08.S2(NMHC)':'y2','NOx(GT)':'y3','PT08.S3(NOx)':'y4','NO2(GT)':'y5','PT08.S4(NO2)':'y6','PT08.S5(O3)':'y7'})

data = data.reset_index()

data = data.rename(columns= {'Date':'ds'})

m = Prophet()

#Iterating through each column and creating a df sepeately and plotting the result.
column = ['y','y1','y2','y3','y4','y5','y6','y7']
for col in column:
  df_new = data[['ds',col]]
  df_new = df_new.rename(columns = {col:'y'})
  m = Prophet()
  m.fit(df_new)
  x = m.make_future_dataframe(periods = 400)
  y = m.predict(x)
  m.plot(y)
  m.plot_components(y)

