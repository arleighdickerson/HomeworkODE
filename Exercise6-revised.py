'''
@author: Arleigh Dickerson
'''
import numpy as np
from concurrent.futures.thread import ThreadPoolExecutor
from os import cpu_count

###############################################################################
#### INITIALIZATION PARAMS ####################################################
###############################################################################
sigma = 10
rho = 28
beta = 8 / 3

x0 = 1
y0 = -1
z0 = 10
r0 = np.array((x0, y0, z0))  # position vector

t0 = 0
tMax = 40

stepSizes = list((10 ** -i for i in range(1, 6)))
EXECUTOR = ThreadPoolExecutor(cpu_count())

compareStepSize = 0.1
tol = 5e-14
###############################################################################
###############################################################################
###############################################################################

def f(t, r):
    (x, y, z) = r  # unpacking position vector
    
    # all derivatives taken with respect to time
    Dx = sigma * (y - x)
    Dy = x * (rho - z) - y
    Dz = x * y - beta * z
    
    return np.array((Dx, Dy, Dz))
def rk4(t, k, y, f):
    k1 = k * f(t, y)
    k2 = k * f(t + 0.5*k, y + 0.5*k1)
    k3 = k * f(t + 0.5*k, y + 0.5*k2)
    k4 = k * f(t + k, y + k3)
    return y + (k1 + 2*(k2 + k3) + k4)/6.0
def precision(stepSize):
     return abs(int(np.log10(stepSize)))

def evaluate(stepSize):
    rNext = lambda t,r:rk4(t,stepSize,r,f)
        
    i = 0
    ti = t0  # time
    ri = r0  # 3 dimensional space
    p = 10 ** (precision(stepSize) - 1)
    while ti <= tMax:
        i +=1
        ti += stepSize
        ri = rNext(ti, ri)
        if i == p:
            i = 0
            yield ri
    print("done with " + str(stepSize))
    
def maxDifference(res1,res2):
    def difference(r1,r2):return np.max(np.abs(r1 - r2))
    res = zip(res1,res2)
    return max([difference(r[0],r[1]) for r in res])
    

def timestepDependent(res0):
    return lambda res1: maxDifference(res0, res1) < tol

def run():
    results = EXECUTOR.map(lambda s:(s,list(evaluate(s))),stepSizes)
    for (stepSize,result) in results:
        dependent = timestepDependent(result)
        for (compareToSize,compareToResult) in results:
            if compareToSize != stepSize:
                if maxDifference(result, compareToResult) < tol:
                    print("result with step size " + str(stepSize) +
                          " is time step independent on result with step size " + str(compareToSize))