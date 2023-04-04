"""
Created on Sun Jul 24 16:54:19 2022
@author: rncru

Compute the loudness of the Krakatoa explosion.

Jesus died for sinners
"""
#%% For my computer
import sys,os

sys.path.append(os.path.join(os.getcwd(),'python'))
print(os.getcwd())

#%% Main calculation
# Variation in  air pressure
pressure_variation = 100000 # Pa

def loudness(p, p_ref = 0.00002):
    '''
    Computes the loudness of sound.
    
    Inputs:
        p - Pressure variations of sound. [Pa]
        
    Optional Inputs:
        p-ref - Reference pressure above which to measure the 
                loudness. This is commonly set at 0.00002 Pa
    
    Returns:
        L_p - Loudness of the sound. [unitless]
    '''
    import numpy as np
    
    L_p = 20*np.log10(p/p_ref)
    
    return L_p
    
Krakatoa_loudness = loudness(pressure_variation)

print(Krakatoa_loudness)