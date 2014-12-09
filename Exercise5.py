'''
@author: Arleigh Dickerson
'''
import numpy as np

A = np.array([
              [-21, 19, -20],
              [19, -21, 20],
              [40, -40, -40]
            ])
x0 = np.array([1,0,-1])

(v,S) = np.linalg.eig(A * x0)
