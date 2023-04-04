# Example 2.23
# Implementing the FFT with different algorithms

import numpy as np
import math

#%% Dr. Ryan's Bit Reversal Functions

def bit_reversal(x):
    """
    Alters vector x in bit-reversed order

    Made by Øyvind Ryan (January 24th, 2017 12:10 AM)
    Copied by Robert Nate Crummett 8/8/2022
    """
    N = len(x)
    j = 0
    for i in range(0,int(N/2),2):
        if (j > i):
            temp = x[j] 
            x[j] = x[i]
            x[i] = temp
            temp = x[N-j-1]
            x[N-j-1] = x[N-i-1]
            x[N-i-1] = temp
        temp = x[i+1]
        x[i+1] = x[j+int(N/2)]
        x[j+int(N/2)]

        m = int(N/4)
        while (m >= 1 and j >= m):
            j -= m
            m = int(m/2)
        j += m

def bit_reversal_arr(x):
    """
    Alters array x in bit-reversed order

    Made by Øyvind Ryan
    Copied by Robert Nate Crummett 8/8/2022
    """
    N, n = np.shape(x)
    temp = np.zeros(x).astype(complex)
    j = 0
    for i in range(0,int(N/2),2):
        if (j > i):
            temp[:] = x[j]
            x[j,:] = x[i]
            x[i,:] = temp
            temp[:] = x[N-j-1]
            x[N-j-1,:] = x[N-i-1]
            x[N-i-1,:] = temp
        temp[:] = x[i+1]
        x[i+1,:] = x[j+int(N/2)]
        x[j+int(N/2),:] = temp

        m = int(N/4)
        while (m >= 1 and j >= m):
            j -= m
            m = int(m/2)
        j += m

#%% FFT Implementation

def FFTImpl(x, FFTKernel, forward = True):
    """
    Compute the FFT or IFFT of the vector x. Note that this function
    differs from the DFT in that the normalizing factor 1/sqrt(N) is
    not included. The FFT is computed along axis 0. If there is
    another axis, the FFT is computed for each element in this as
    well. This function calls a kernel for computing the FFT. The
    kernel assumes that the input has been bit-reversed, and contains 
    only one axis. This function is where the actual bit reversal and
    the splitting of the axes take place.
    
    x: a vector
    FFTKernel: can be any of FFTKernelStandard, FFTKernelNonrec, and
    FFTKernelSplitradix. The kernel assumes that the input has been
    bit-reversed, and contains only one axis.
    forward: Whether the FFT or the IFFT is applied
    """
    if np.ndim(x) == 1:
        bit_reversal(x)
        FFTKernel(x, forward)
    else:
        bit_reversal_arr(x)
        for s2 in math.xrange(np.shape(x)[1]):
            FFTKernel(x[:,s2], forward)

    if not forward:
        x /= len(x)

#%% Defining FFT Kernels

def FFTKernelStandard(x, forward):
    """
    Compute the FFT of x, using a standard FFT algorithm
    
    x: a bit-reversed version of the input. Should have only one axis
    forward: Whether the FFT or the IFFT is applied
    """
    N = len(x)
    sign = -1
    if not forward:
        sign = 1

    if N > 1:
        xe, xo = x[0:int(N/2)], x[int(N/2):]
        FFTKernelStandard(xe, forward)
        FFTKernelStandard(xo, forward)
        D = np.exp(sign*2*np.pi*1j*np.arange(float(N/2))/N)
        xo = xo*D
        x[:] = np.concatenate([xe + xo, xe - xo])

def FFTKernelNonrec(x, forward):
    """
    Compute the FFT of x, using a non recusive FFT algorithm.
    
    x: a bit-reversed version of the input. Should have only one axis
    forward: Whether the FFT or the IFFT is applied
    """
    N = len(x)
    sign = -1
    if not forward:
        sign = 1
    
    D = np.exp(sign*2*np.pi*1j*np.arange(float(N/2))/N)
    nextN = 1
    while nextN < N:
        k = 0
        while k < N:
            xe, xo = x[k:(k+nextN)], x[(k+nextN):(k+2*nextN)]
            xo = xo*D[0::(int(N/(2*nextN)))]
            x[k:(k+2*nextN)] = np.concatenate([xe + xo, xe - xo])
            k += 2*nextN
        nextN *= 2

def FFTKernelSplitradix(x, forward):
    """
        Compute the FFT of x, using a split radix FFT algorithm.

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
        xe = x[0:int(N/2)]
        xo1 = x[int(N/2):int(3*N/4)]
        xo2 = x[int(3*N/4):N]
        FFTKernelSplitradix(xe, forward)
        FFTKernelSplitradix(xo1, forward)
        FFTKernelSplitradix(xo2, forward)
        G = np.exp(sign*2*np.pi*1j*np.arange(float(N/4))/N)
        H = G*np.exp(sign*2*np.pi*1j*np.arange(float(N/4))/(N/2))
        xo1 = xo1*G
        xo2 = xo2*H
        xo = np.concatenate([xo1 + xo2, -sign*1j*(xo1 - xo2)])
        x[:] = np.concatenate([xe + xo, xe - xo])