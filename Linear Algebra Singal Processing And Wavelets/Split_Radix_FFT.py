"""
Created on Mon Aug  8 10:23:59 2022
@author: rncru

Information regarding the purpose of the file.

Jesus died for sinners
"""

import sys,os

sys.path.append(os.path.join(os.getcwd(),'python'))
print(os.getcwd())

import numpy as np

def FFTKernelSplitradix(x, forward):
    """
    Compute the FFT of x, using the split-radix FFT algorithm.
        
    x: a bit-reversed version of the input. Should have only one axis
    forward: Whether the FFT or the IFFT is applied
    """
    N = len(x)
    sign = -1
    if not forward:
        sign = 1
    if N == 2:
        x[:] = [x[0] + x[1], x[0] - x[1]]
    elif N > 2:
        xe, xo1, xo2 = x[0:(N/2)], x[(N/2):(3*N/4)], x[(3*N/4):N]
        FFTKernelSplitradix(xe, forward)
        FFTKernelSplitradix(xo1, forward)
        FFTKernelSplitradix(xo2, forward)
        G = np.exp(sign*2*np.pi*1j*np.arange(float(N/4))/N)
        H = G*np.exp(sign*2*np.pi*1j*np.arange(float(N/4))/(N/2))
        xo1 *= G
        xo2 *= H
        xo = np.concatenate( [xo1 + xo2, -sign*1j*(xo2 - xo1)] )
        x[:] = np.concatenate([xe + xo, xe - xo])
    return x

