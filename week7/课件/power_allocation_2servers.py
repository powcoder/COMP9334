https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Week 7A_2 

Power allocation 

"""

import numpy as np
import matplotlib.pyplot as plt 

# Impact of power allocation to mean response time 

## Problem parameters 
# Linear scaling 
# DVFS parameters 
alpha = 0.008 # DVFS, in GHz/W
s_b = 2.5     # GHz
b = 180       # W 
# s = s_b + alpha * (P - b), where 
# s = server speed
# P = server allocated to server 

# Total power 
power_total = 400 

# Job arrival rate 
lamb = 0.8  

# Mean service time at 1 GHz = 1

## Two server case 
# Can do a simple search for the answer 
# Vary the power allocation for Server 1
power1_vec = np.arange(0.1,0.95,0.025)*power_total

# Mean response time for a given power allocation 
mrt = np.zeros_like(power1_vec) 
 
# Parameters
n_q = 100 # Number of searches 
gap_factor = 0.001 # To avoid dividing by zero in searching for job allocation

for k in range(len(power1_vec)):
    power1 = power1_vec[k] 
    # power allocation to server 2 = power_total - power1_vec
    power2 = power_total - power1
    
    # speed of the server
    s1 = s_b + alpha * (power1 - b) 
    s2 = s_b + alpha * (power2 - b) 
    
    # To determine the fraction of jobs going to each server
    # q = fraction of jobs going to server 1
    # upper and lower limit of q 
    q_max = (1-gap_factor)*lamb/s1
    q_min = (1+gap_factor)*(1-lamb/s2)   
    
    # Search for the minimum response time 
    q_vec = np.linspace(q_min,q_max,n_q) 
    
    # mean response time for a given power allocation
    mrt_1 = q_vec / (s1 - lamb*q_vec) 
    mrt_1[mrt_1 < 0] = np.inf 
    mrt_2 = (1 - q_vec) / (s2 - lamb*(1-q_vec))
    mrt_2[mrt_2 < 0] = np.inf 
    mrt[k] = np.min(mrt_1 + mrt_2) 
    
    

# Plot the graph
plt.plot(power1_vec,mrt)
plt.xlabel('Power allocated to server 1')
plt.ylabel('Mean response time') 


