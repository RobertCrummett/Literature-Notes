"""
Created on Tue Jul 26 19:18:31 2022
@author: rncru

Figure 1.6. Fourier series approximation of a square wave with 10 nonzero
coefficients in the left panel. In the right panel, the magnitude of the first
100 non zero coefficients of the Fourier approximation.

Jesus died for sinners
"""

import sys,os

sys.path.append(os.path.join(os.getcwd(),'python'))
print(os.getcwd())

import numpy as np
import matplotlib.pyplot as plt

N = 20
f = 440
T = 1/f
t = np.linspace(0,T,100)
x = np.zeros(len(t))

# Fourier series calculation
for k in range(1,N+1,2):
    x += (4/(k*np.pi))*np.sin(2*np.pi*k*t/T)

plt.figure()
plt.subplot(1,2,1)
plt.plot(t,x,'g-',lw = 2)
plt.title('Fourier Approximation of Square Wave')


b = np.zeros(100,)

# Fourier series coefficient approximation
for k in range(1,201,2):
    i = int((k-1)/2)
    b[i] = 4/(k*np.pi)
    
plt.subplot(1,2,2)
plt.plot(b,'r-',lw = 2)
plt.title('Coefficent Sizes 1 - 100')
plt.ylim(0,1)
plt.xlim(0,100)
plt.tight_layout()