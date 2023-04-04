"""
Created on Sat Aug  6 20:40:49 2022
@author: rncru

Direct implementation of the DFT, the discrete Fourier transform.

Jesus died for sinners
"""

import sys,os

sys.path.append(os.path.join(os.getcwd(),'python'))
print(os.getcwd())

import numpy as np

def dft_impl(x, forward = True):
    '''
    The DFT or IDFT of a vector input.
    
    Inputs:
        x - A vector in either the frequency or time domain
        forward - True corresponds to DFT implementation
                  False corresponds to IDFT implementation
                  True (DFT) is assumed as default
    Outputs:
        y - The transformed x vector
    '''
    if np.size(x.shape) == 1:
        if not(forward):
            # This is the condition for IDFT computation
            y = np.zeros_like(x).astype(complex)
            N = len(x)
            for n in range(N):
                D = (1/N)*np.exp(2*np.pi*n*1j*np.arange(float(N))/N)
                y[n] = np.dot(D,x)
        else:
            # This is the default DFT calculation
            y = np.zeros_like(x).astype(complex)
            N = len(x)
            for n in range(N):
                D = np.exp(-2*np.pi*n*1j*np.arange(float(N))/N)
                y[n] = np.dot(D,x)
    else:
        # for a 2x2 matrix input
        n_col = x.shape[1] # the number of collumns
        y = np.zeros_like(x).astype(complex)
        
        if not(forward):
            for col in range(n_col):
                # This is the condition for IDFT computation
                x_col = x[:,col]
                y_col = np.zeros_like(x_col).astype(complex)
                N = len(x_col)
                for n in range(N):
                    D = (1/N)*np.exp(2*np.pi*n*1j*np.arange(float(N))/N)
                    y_col[n] = np.dot(D,x_col)
                y[:,col] = y_col
        else:
            for col in range(n_col):
                # This is the condition for IDFT computation
                x_col = x[:,col]
                y_col = np.zeros_like(x_col).astype(complex)
                N = len(x_col)
                for n in range(N):
                    D = np.exp(-2*np.pi*n*1j*np.arange(float(N))/N)
                    y_col[n] = np.dot(D,x_col)
                y[:,col] = y_col
                    
    return y


# Testing the DFT algorithm on known data
x = np.arange(1,5)
x = np.tile(x,(2,1))
x = np.array([[1, 2 + 1j, 4, 5],[3, 4.5, 6, 9]])
print(x)
y = dft_impl(x, forward = True)
print(y)
x = dft_impl(y, forward = False)
print(x)