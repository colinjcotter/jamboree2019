import numpy as np
lat = np.array([-12,15,-12])
lon = np.array([41,-35,41])

latmean = np.fromfile("../latmean.txt",sep=' ')
lonmean = np.fromfile("../lonmean.txt",sep=' ')

error = np.sqrt(np.sum((lat-latmean)**2 + (lon-lonmean)**2))

error = np.array([error])
error.tofile('error.txt',sep=' ')

