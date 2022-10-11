import numpy as np
import os
from pylcurve.lightcurve import lcurve
import ctypes
lib = ctypes.CDLL('../pylcurve/lib/libpylcurve.so')



times = np.array([0,1], dtype=np.float)
expose = np.array([0,0], dtype=np.float)
ndiv = np.array([0,0], dtype=np.float)


llcurve = lcurve()
smodel = 'example_model_file'
llcurve.lc_from_smodel(smodel, times, expose=expose, ndiv=ndiv)


