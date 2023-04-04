# Example 2.21 - Plotting the Interpolant

import matplotlib.pyplot as plt
import numpy as np

f = lambda t: np.cos(t)**6 # function
M = 3
T = 2*np.pi # period
N = 2*M + 1 # samples taken over period
t = np.linspace(0,T,100) # range to plot (one period T)

x = f(np.linspace(0, T - T/float(N), N)) # sampling f, N times over T
y = np.fft.fft(x, axis = 0)/N # Fast Fourier Transform interpolant
s = np.real(y[0])*np.ones(len(t)) # IDFT interpolant, k = 0

for k in range(1, int((N+1)/2)): 
    s += 2*np.real(y[k]*np.exp(2*np.pi*1j*k*t/float(T))) # IDFT interpolants

# Plotting the results
plt.plot(t,s,'r',t, f(t), 'g')
plt.legend(['Interpolant from V_{M,T}','f'])

# The plots coincide for M => 6