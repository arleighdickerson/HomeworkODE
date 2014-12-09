'''
@author: Arleigh Dickerson
'''
import numpy as np
from matplotlib import pyplot as pl
ks = [0.01, 0.0125, 0.02, 0.025]
y0 = 0
def f(t, y):return - 100 * (y - np.cos(t)) - np.sin(t)

def forward(k): #explicit
    ti = 0
    yi = y0
    while ti <= 1:
        yield (ti, yi)
        yi += k * f(ti, yi)
        ti += k 

def backward(k): # implicit
    k100 = 100 * k
    k100Inc = k100 + 1
    def yNext(tNext,yCurrent):
        return  (yCurrent + 
                 (k100 * np.cos(tNext)) - 
                 (k * np.sin(tNext))
                ) / k100Inc
    ti = 0
    yi = y0
    while ti <= 1:
        yield (ti, yi)
        ti += k 
        yi = yNext(ti,yi)

for euler in [forward,backward]:
    for k in ks:
        (t, y) = zip(*euler(k))
        pl.plot(t, y)
        pl.show()
