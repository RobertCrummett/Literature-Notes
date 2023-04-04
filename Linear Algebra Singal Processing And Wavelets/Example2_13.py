# Implementing the DFT
# The functions will be able to comput the DFT or IDFT
# The function can take 2 dimensional matrix inputs
#   and it will apply the DFT/IDFT to each column

# Copied from the solution manual, because this was getting 
#   too hard for me!

import numpy as np

def DFTImpl(x, forward = True):
    """
    Compute the DFT of the vector x using standard matrix
    multiplication. To avoid out of memory situations, we do not
    allocate the entire DFT matrix, only one row of it at a time.
    Note that this function differs from the FFT in that it includes
    the normalizing factors 1/sqrt(N). The DFT is computed along axis
    0. If there is another axis, the DFT is computed for each element
    in this as well.

    Copied from solution manual 8/8/2022 by Robert Nate Crummett
    """
    y = np.zeros_like(x).astype(complex)
    N = len(x)
    sign = -(2*forward - 1) # Sign change for DFT vs IDFT

    if np.ndim(x) == 1: # For vector inputs
        for n in range(N):
            D = np.exp(sign*2*np.pi*n*1j*np.arange(float(N))/N)
            y[n] = np.dot(D,x)
    else: # For matrix inputs
        for n in range(N):
            D = np.exp(sign*2*np.pi*n*1j*np.arange(float(N))/N)
            for s2 in range(np.shape(x)[1]):
                y[n,s2] = np.dot(D,x[:,s2])

    if sign == 1: # For IDFT
        y /= float(N) # Normalizing factor

    return y