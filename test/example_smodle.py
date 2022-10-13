import numpy as np
import os
from pylcurve import lcurve
import matplotlib.pyplot as plt
from ctypes import *
import time

#lib = ctypes.CDLL('../pylcurve/lib/libpylcurve.so')

tt = time.time()

times = np.array([0,1], dtype=np.float)
expose = np.array([2,2], dtype=np.float)/24/3600
ndiv = np.array([1,1], dtype=np.float)
data = np.loadtxt('example_data_file')
times = data[:, 0]
expose = data[:, 1]
#times = np.arange(0, 1, 0.1)
#Tsize = len(times)
#c_times = times.ctypes.data_as(POINTER(c_double*Tsize))
#c_expose = expose.ctypes.data_as(POINTER(c_double*Tsize))
#cc_expose = np.array(c_expose.contents)


llcurve = lcurve()
smodel = 'example_model_file'
calc = llcurve.lc_from_smodel(smodel, times, expose=expose, ndiv=7)

print('calculated time', time.time()- tt)
fig, ax = plt.subplots(1,1,figsize=(8.5, 4))
plt.plot(times, llcurve.calc)
plt.show()
