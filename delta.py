from bsm_model import BsmModel

from math import log 
from math import exp
from math import sqrt

from scipy.stats import norm 

import numpy as np

from numpy import shape 

# stock prices range from 10 to 70
# choose 60*23 call options contracts

s = np.array([range(10, 70, 1) for i in range(23)])
I = np.ones((np.shape(s)))
time = np.arange(1, 12.5, 0.5) / 12
T = np.array([ele for ele in time for i in range(np.shape(s)[1])]).reshape(np.shape(s))

contracts = []

for i in range(np.shape(s)[0]):
    for j in range(np.shape(s)[1]):
        contracts.append(BsmModel('c', s[i,j],40*I[i,j], 0.1*I[i,j], T[i,j], 0.5*I[i,j]))

theta = [x.theta() for x in contracts]
gamma = [x.gamma() for x in contracts]
delta = [x.delta() for x in contracts]
vega = [x.vega() for x in contracts]
rho = [x.rho() for x in contracts]

gamma = np.array(gamma).reshape(shape(s))
delta = np.array(delta).reshape(shape(s))
theta = np.array(theta).reshape(shape(s))
vega = np.array(vega).reshape(shape(s))
rho = np.array(rho).reshape(shape(s))

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import animation

z = delta
fig = plt.figure(figsize=(20,11))
ax = fig.add_subplot(111, projection='3d')
ax.view_init(40,290)
ax.plot_wireframe(s, T, z, rstride=1, cstride=1)
ax.plot_surface(s, T, z, facecolors=cm.jet(delta),linewidth=0.001, rstride=1, cstride=1, alpha = 0.75)
ax.set_zlim3d(0, z.max())
ax.set_xlabel('stock price')
ax.set_ylabel('Time to Expiration')
ax.set_zlabel('delta')
m = cm.ScalarMappable(cmap=cm.jet)
m.set_array(z)
cbar = plt.colorbar(m)