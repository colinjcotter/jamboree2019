import pandas
import numpy as np

df_pred = pandas.read_csv('predictions.csv')
df_meas = pandas.read_csv('../measurements.csv')

Predictions = df_pred.Predicted.values
Variances = df_pred.Variance.values
#switch order
Predictions = np.concatenate((Predictions[0:3],[Predictions[6]],Predictions[3:6]))
Variances = np.concatenate((Variances[0:3],[Variances[6]],Variances[3:6]))
Measurements = df_meas.values[1].astype(float)[2:]

error = np.sqrt(np.sum((Predictions-Measurements)**2/Variances))
error = np.array([error])
error.tofile('error.txt')
