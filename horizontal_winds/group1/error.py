import pandas

dfx = pandas.read_csv('../velocity_x_full.csv',header=None)
dfy = pandas.read_csv('../velocity_y_full.csv',header=None)

u = dfx.values
v = dfy.values

dfxp = pandas.read_csv('predictions_x.csv',header=None)
dfyp = pandas.read_csv('predictions_y.csv',header=None)

up = dfxp.values
vp = dfyp.values

dfxvar = pandas.read_csv('variances_x.csv',header=None)
dfyvar = pandas.read_csv('variances_y.csv',header=None)

uvar = dfxvar.values
vvar = dfyvar.values

import numpy as np

uvar[np.where(uvar==0)] = 1.0e-12
vvar[np.where(vvar==0)] = 1.0e-12

maskv = np.where(v[35,:] != 0)
masku = np.where(u[35,:] != 0)

error = 0.
for i in range(3):
    upi = up[i,1:]
    ui = u[int(up[i,0])]
    vpi = vp[i,1:]
    vi = v[int(up[i,0])]
    uvari = uvar[i,1:]
    vvari = vvar[i,1:]
    eu = (upi-ui)**2/uvari
    ev = (vpi-vi)**2/vvari
    error += np.sqrt(np.sum(ev) + np.sum(eu))/up[i,0]

error = np.array(error)
error.tofile('error.txt',sep=' ')
