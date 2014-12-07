from pylab import *
import numpy as np
from scipy.integrate import odeint
from mpl_toolkits.mplot3d.axes3d import Axes3D

def f(t, r):
    (x, y, z) = r
    
    # The Lorenz equations
    dx_dt = sigma*(y - x)
    dy_dt = x*(rho - z) - y
    dz_dt = x*y - beta*z
    
    return array([dx_dt, dy_dt, dz_dt])  
    
# Initial position in space
r0 = [1.0, -1.0, 10.0]

# Constants sigma, rho and beta
sigma = 10.0
rho   = 28.0
beta  = 8.0/3.0

# Time grid
tf = 40.0
t0=0.0
qinit = 3
qmax = 4
k = 1 * 10**-qinit
#t = linspace(0, tf, tf*100)

#pos = odeint(f, r0, t) #BUILT-IN RK4 METHOD to NUMPY
def rk4(t, k, y, f):
	k1 = k * f(t, y)
	k2 = k * f(t + 0.5*k, y + 0.5*k1)
	k3 = k * f(t + 0.5*k, y + 0.5*k2)
	k4 = k * f(t + k, y + k3)
	return t + k, y + (k1 + 2*(k2 + k3) + k4)/6.0

#
rp = []
rp.append(r0)
tp = []
tp.append(t0)
t = t0
r = r0
xlog = []

q = qinit
while q <= qmax:
	xtemp = []
	count = 0
	t=0
	r=r0
	xtemp.append(r0[0])
	while t<tf:
		t,r = rk4(t,k,r,f)
		tp.append(t)
		rp.append(r)
		count += 1
		if(count == 10**(q-1)):
			count = 0
			print(t)
			xtemp.append(r[0])
	xlog.append(xtemp)
	q += 1
	k = k = 1 * 10**-q
	
#########################################################xlog configured

rp = array(rp)
x = rp[:, 0]
y = rp[:, 1]
z = rp[:, 2]

fig = figure(figsize=(16,10))
ax = fig.gca(projection='3d')
ax.plot(x, y, z)

fig, ax = subplots(1, 3, sharex=True, sharey=True, figsize=(16,8))

ax[0].plot(x, y)
ax[0].set_title('X-Y cut')

ax[1].plot(x, z)
ax[1].set_title('X-Z cut')

ax[2].plot(y, z)
ax[2].set_title('Y-Z cut')

show()

