import pandas
import numpy as np

df_meas = pandas.read_csv('../measurements.csv')
df_pred = pandas.read_csv('estimate.csv')

pred = df_pred.values[:,1:].astype(float)
Predictions = pred[:,0]
Variances = (pred[:,2]-pred[:,1])**2

Measurements = df_meas.values[1].astype(float)[2:]

error = np.sqrt(np.sum((Measurements-Predictions)**2/Variances))
np.array([error]).tofile('error.txt', sep=' ')
