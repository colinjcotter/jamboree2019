import numpy as np
lon = np.array([-12,-64,-35])
lat = np.array([38,38,42])
lonvar = np.array([1.5, 15.8, 3.3])
latvar = np.array([0.3, 1.1, 1.3])

latmean = np.fromfile("../latmean.txt",sep=' ')
lonmean = np.fromfile("../lonmean.txt",sep=' ')

error = np.sqrt(np.sum((lat-latmean)**2/latvar + (lon-lonmean)**2/lonvar))
print(error)

error = np.array([error])
error.tofile('error.txt',sep=' ')

