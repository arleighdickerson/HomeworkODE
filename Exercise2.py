'''
@author: Arleigh Dickerson
'''
import numpy as np
from matplotlib import pyplot as pl
ks = [0.01, 0.0125, 0.02, 0.025]
y0 = 0
h = 0.019
def F(t, y):return - 100 * (y - np.cos(t)) - np.sin(t)

def explicit(k):
    ti = 0
    yi = 0
    while ti <= 1:
        yield (ti, yi)
        yi += k * F(ti, yi)
        ti += k 

def implicit(k):
    ti = 1
    yi = 1
    while ti >= 0:
        yield (ti, yi)
        yi -= yi + h * F(ti, yi)
        ti -= k 

for euler in [implicit, explicit]:
    for k in ks:
        (t, y) = zip(*euler(k))
        pl.plot(t, y)
        pl.show()
