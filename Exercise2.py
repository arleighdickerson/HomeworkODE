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
    yi = 0
    while ti <= 1:
        yield (ti, yi)
        yi += k * f(ti, yi)
        ti += k 

#derp backward(k): our differential equation is linear, we don't need an iterative method

for euler in [forward]:
    for k in ks:
        (t, y) = zip(*euler(k))
        pl.plot(t, y)
        pl.show()
