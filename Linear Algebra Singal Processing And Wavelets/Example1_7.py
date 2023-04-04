"""
Created on Sun Jul 24 21:50:55 2022
@author: rncru

Example 1.7
Recreate the right hand side of figure 1.1 with two pure tones.

Jesus died for sinners
"""

import sys,os

sys.path.append(os.path.join(os.getcwd(),'python'))
print(os.getcwd())

import numpy as np
import matplotlib.pyplot as plt

def two_pure_tones(a,b,t, frequency_1 = 440, frequency_2 = 4400):
    
    f = a*np.sin(2*np.pi*frequency_1*t) + b*np.sin(2*np.pi*frequency_2*t)
    
    return f

fs = 44100
antsec = 0.01125
t = np.linspace(0,antsec,int(fs*antsec))
x = two_pure_tones( a = 1, b = 0.5, t = t)

plt.figure(1)
plt.plot(t,x,'k-')
plt.tight_layout()
plt.title(label = 'Audio Signal. Figure 1.1, Right. Example 1.7')