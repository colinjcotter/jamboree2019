import pandas

dfx = pandas.read_csv('../velocity_x_full.csv',header=None)
dfy = pandas.read_csv('../velocity_y_full.csv',header=None)

u = dfx.values
v = dfy.values

dfxp = pandas.read_csv('group2_velocity_x_prediction.csv')
dfyp = pandas.read_csv('group2_velocity_y_prediction.csv')

up = dfxp.values
vp = dfyp.values

print(up)

uvar = 0.0027484808563318208
vvar = 0.0032466907292199158

import numpy as np

error = 0.
for i in range(3):
    upi = up[i,1:]
    ui = u[int(up[i,0])]
    vpi = vp[i,1:]
    vi = v[int(up[i,0])]
    eu = (upi-ui)**2/uvar
    ev = (vpi-vi)**2/vvar
    error += np.sqrt(np.sum(ev) + np.sum(eu))/up[i,0]

error = np.array(error)
error.tofile('error.txt',sep=' ')
