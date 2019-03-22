import pandas
import numpy as np

df_meas = pandas.read_csv('../measurements.csv')
df_pred = pandas.read_csv('weather_forecast.txt')
df_var = pandas.read_csv('weather_variance.txt')

Measurements = df_meas.values[1].astype(float)[2:]
Predictions = df_pred.values
Variances = df_var.values

error = np.sqrt( np.sum((Predictions-Measurements)**2/Variances))
np.array([error]).tofile('error.txt', sep=' ')
