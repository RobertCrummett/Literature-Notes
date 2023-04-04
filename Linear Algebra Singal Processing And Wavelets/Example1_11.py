"""
Created on Tue Jul 26 18:57:39 2022
@author: rncru

Exercise 1.11 - Make a program that plays all pure tones in an octave.

Jesus died for sinners
"""

import sys,os

sys.path.append(os.path.join(os.getcwd(),'python'))
print(os.getcwd())

from sound import *
import numpy as np
import matplotlib.pyplot as plt

def Octave_Maker(f_0):
    '''
    This function makes a ground of pure tones out of an original input 
    frequency. The final tone, f_12, is double the frequency of f_0. 
    
    Inputs:
        f_0 - the base frequency
        
    Ouputs:
        octave - the octave resulting from f_0
    '''
    f_1 = f_0 * 2**(1/12)
    f_2 = f_0 * 2**(2/12)
    f_3 = f_0 * 2**(3/12)
    f_4 = f_0 * 2**(4/12)
    f_5 = f_0 * 2**(5/12)
    f_6 = f_0 * 2**(6/12)
    f_7 = f_0 * 2**(7/12)
    f_8 = f_0 * 2**(8/12)
    f_9 = f_0 * 2**(9/12)
    f_10 = f_0 * 2**(10/12)
    f_11 = f_0 * 2**(11/12)
    f_12 = f_0 * 2**(12/12)
    
    octave = [f_0, f_1, f_2, f_3, f_4, f_5, f_6, f_7, \
              f_8, f_9, f_10, f_11, f_12]
    
    return octave

frequencies = Octave_Maker(440)
fs = 44100
antsec = 3

t = np.linspace(0,antsec,antsec*fs)

# playing the octave
for freq in frequencies:
    octave_to_play = np.sin(2*np.pi*freq*t);
    play(octave_to_play,fs)