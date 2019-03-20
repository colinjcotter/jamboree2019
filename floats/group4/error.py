import numpy as np
lon = np.array([0,-67,-3])
lat = np.array([-30,39,-19])
lonvar = np.array([2, 2, 10])
latvar = np.array([5, 2, 10])

latmean = np.fromfile("../latmean.txt",sep=' ')
lonmean = np.fromfile("../lonmean.txt",sep=' ')

error = np.sqrt(np.sum((lat-latmean)**2/latvar + (lon-lonmean)**2/lonvar))
print(error)

error = np.array([error])
error.tofile('error.txt',sep=' ')

