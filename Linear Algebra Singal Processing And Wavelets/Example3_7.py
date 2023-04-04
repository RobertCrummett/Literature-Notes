# Example 3.7
# Implementation of convolution three different ways
# The plots compare the computation times

#%% Module import
import sys, os

sys.path.append(os.path.join(os.getcwd(),'python'))
print(os.getcwd())

from sound import *
from time import *
import numpy as np
import matplotlib.pyplot as plt

# sample sound to convolve
x, fs = audioread('sounds/castanets.wav')
x = x[:,0]
N = len(x)

kmax = 100
# preallocation
vals1 = np.zeros(int(kmax/10))
vals2 = np.zeros(int(kmax/10))
vals3 = np.zeros(int(kmax/10))
ind = 0

# three different convolution methods
for k in range(10,kmax+1,10):
    t = np.random.random(k)
    start = time()
    np.convolve(t, x)
    vals1[ind] = time() - start

    z = np.zeros(N)
    start = time()
    for s in range(k):
        z[(k-1):N] += t[s]*x[(k-1-s):(N-s)]
    vals2[ind] = time() - start

    z = np.zeros(N)
    start = time()
    for n in range(k-1,N):
        for s in range(k):
            z[n] += t[s]*x[n-s]
    vals3[ind] = time() - start

    ind += 1

# plotting timed results
plt.plot(range(10,kmax+1,10),np.log(vals1),'r-', \
    range(10,kmax+1,10),np.log(vals2),'g-', \
    range(10,kmax+1,10),np.log(vals3),'b-')
plt.legend(['conv','simple for','double for'])
plt.show()