"""
Created on Tue Jul 26 21:53:29 2022
@author: rncru

Exercise 1.17 - Listen to the Fourier series of the triangle wave.

Jesus died for sinners
"""

import sys,os

sys.path.append(os.path.join(os.getcwd(),'python'))
print(os.getcwd())

from sound import play
import numpy as np
import matplotlib.pyplot as plt

N = 10
f = 440
T = 1/f
t = np.linspace(0,T,100)
x = np.zeros(len(t))

for k in range(1,N+1,2):
    x += (-8/(k**2*np.pi**2))*np.cos(2*np.pi*k*t/T)
    
plt.figure()
plt.plot(t,x)

antsec = 3
fs = 44100

x_play = np.tile(x,f*antsec)
play(x_play,fs)