import pandas
import numpy as np

df_meas = pandas.read_csv('../measurements.csv')

#1. Dry bulb temperature: 8.0388 degrees Celsius
#2. Relative humidity: 70.8324%
#3. Accumulated sunshine in the past hour: 1420.1 seconds
#4. Accumulated rainfall since 00:00UTC: 0.7434 millimetres
#5. Station pressure: 1011.9 hPa
#6. 10m wind speed: 3.3166 metres per second
#7. 100cm soil temperature: 6.9535 degrees Celsius

Predictions = np.array([8.0388, 70.8324, 1420.1, 0.7434, 1011.9, 3.3166, 6.9535])
df_cov = pandas.read_csv('group2_covariances.csv', header=None)
Covariances = df_cov.values
Sigma = np.linalg.inv(Covariances)

#switch order
Measurements = df_meas.values[1].astype(float)[2:]
Measurements = np.concatenate((Measurements[0:3],Measurements[4:], [Measurements[3]]))
Error = Predictions - Measurements

error = np.dot( Error, np.dot(Sigma, Error))
np.array([error]).tofile('error.txt', sep=' ')
