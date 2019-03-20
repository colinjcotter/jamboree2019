import json
with open('lagrangian.json') as infile:
    d = json.load(infile)

import json
with open('lagrangian_extra_with_means.json') as infile:
    d = json.load(infile)

import numpy
latmean = numpy.zeros(3)
lonmean = numpy.zeros(3)
for i in range(3):
    latmean[i] = numpy.mean(d[i]['lat'])
    lonmean[i] = numpy.mean(d[i]['lon'])

latmean.tofile('latmean.txt', sep=' ')
lonmean.tofile('lonmean.txt', sep=' ')
