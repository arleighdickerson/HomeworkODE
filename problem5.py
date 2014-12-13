from pylab import *
import numpy as np
import scipy.optimize as op
from scipy.integrate import odeint
from mpl_toolkits.mplot3d.axes3d import Axes3D

epsilon = 0.9    
# Initial position in space
r0 = [0.0, 1-epsilon, np.sqrt((1+epsilon)/(1-epsilon)), 0.0]

def f(t, r):
    (w, x, y, z) = r
    dw_dt = -x/(x**2+z**2)**1.5
    dx_dt = w
    dy_dt = -z/(x**2+z**2)**1.5
    dz_dt = y
    return array([dw_dt, dx_dt, dy_dt, dz_dt])

def function(u):
	return u-epsilon*sin(u)-t
    
def realF(t):
	u = op.fsolve(function, 0)
	w = sin(u)/(1-epsilon*cos(u))
	x = cos(u)-epsilon
	y = (np.sqrt(1-epsilon**2)*cos(u))/(1-epsilon*cos(u))
	z = np.sqrt(1-epsilon**2)*sin(u)    
	return array([w,x,y,z])
    
tf = 50
t0=0.0
k = 0.005

def rk4(t, k, y, f):
	k1 = k * f(t, y)
	k2 = k * f(t + 0.5*k, y + 0.5*k1)
	k3 = k * f(t + 0.5*k, y + 0.5*k2)
	k4 = k * f(t + k, y + k3)
	return t + k, y + (k1 + 2*(k2 + k3) + k4)/6.0

count = 0
t=t0
r=r0
rp = []
rp.append(r0)
tp = []
tp.append(t0)
realpoints = []
realpoints.append(r0)
u=0

while t<tf:
	realpoints.append(realF(t))
	t,r = rk4(t,k,r,f)
	tp.append(t)
	rp.append(r)

rp = array(rp)
x = rp[:, 1]
y = rp[:, 2]
z = rp[:, 3]
realpoints = array(realpoints)
xExact = realpoints[:, 1]
yExact = realpoints[:, 2]
zExact = realpoints[:, 3]

fig, ax = subplots(1, 3, sharex=True, sharey=True, figsize=(16,8))

ax[0].plot(tp, x, 'r', tp, xExact, 'b')
ax[0].set_title('x vs t')

ax[1].plot(tp, z, 'r', tp, zExact, 'b')
ax[1].set_title('z vs t')

ax[2].plot(x, z, 'r', xExact, zExact, 'b')
ax[2].set_title('X-Z cut')

show()
