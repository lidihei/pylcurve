import numpy as np
import os
from pylcurve.lightcurve import lcurve


time = np.array([0,1], dtype=np.float)
expose = np.array([0,0], dtype=np.float)
ndiv = np.array([0,0], dtype=np.float)


_lcurve = lcurve()
_lcurve.lc(time, expose=expose, ndiv=ndiv)
