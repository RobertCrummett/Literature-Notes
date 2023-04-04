"""
Created on Sun Jul 24 22:15:45 2022
@author: rncru

Excercizwe 1.10: Create the triangle wave form Example 1.5

Jesus died for sinners
"""

import sys,os

sys.path.append(os.path.join(os.getcwd(),'python'))
print(os.getcwd())

from sound import *
import numpy as np
import matplotlib.pyplot as plt

antsec = 3
fs = 44100
f = 440
T = 1/f
t = np.linspace(0,antsec,fs*antsec)

samples_per_period = fs/f

t_first_half = t[0:int(samples_per_period/2)]
t_second_half = t[int(samples_per_period/2):int(samples_per_period)]

x = np.concatenate((4*t_first_half/T  - 1, 3 - 4*t_second_half/T))

x = tile(x,f*antsec)

play(x, fs)
audiowrite('triangle440.wav',x,fs)