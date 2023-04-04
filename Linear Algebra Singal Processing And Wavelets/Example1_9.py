"""
Created on Sun Jul 24 22:01:56 2022
@author: rncru

Exercise 1.9
Adding random noise to sound file.

Jesus died for sinners
"""

import sys,os

sys.path.append(os.path.join(os.getcwd(),'python'))
print(os.getcwd())

from sound import *
import numpy as np

x, fs = audioread(r'sounds/castanets.wav')

# Add random noise
c = 0.4 # dampening factor
z = x + c*(2*np.random.random(shape(x)) - 1) # rescale [0,1] -> [-1,1]

# Play sound file with added random noise
play(z,fs)