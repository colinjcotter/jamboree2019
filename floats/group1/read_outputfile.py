import numpy as np
# =============================================================================
# GET DATA
# =============================================================================

output = np.loadtxt('output_prediction_all.csv',delimiter=",")
print(output.shape)


pred_lon = output[0,:]
pred_lat = output[1,:]
err_lon = output[2,:]
err_lat = output[3,:]

latmean = np.fromfile('../latmean.txt', sep=' ')
lonmean = np.fromfile('../lonmean.txt', sep=' ')

print(pred_lon.shape)
print(pred_lat.shape)
print(err_lon.shape)
print(err_lat.shape)
print(latmean.shape)
print(lonmean.shape)

prediction_error = np.sqrt(np.sum((pred_lon-lonmean)**2/err_lon + (pred_lat-latmean)**2/err_lat))

prediction_error = np.array([prediction_error])
prediction_error.tofile('error.txt',sep=' ')

