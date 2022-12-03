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
COMP9334

Fork-join MVA example
"""

import numpy as np

# MVA for closed single-class queueing networks with 
# fork-join subsystems 

# These are the input parameters
I = 3 # number of subsystems
# subsystem 1 = processor
# subsystem 2 = disk array 1
# subsystem 3 = disk array 2
# service demand D
D = np.array([0.01, 0.02, 0.03])  # D1, D2, D3 
# Number of parallel stations per subsystem
K = np.array([1,2,3])   # K1, K2, K3

# The corresponding harmonic numbers
H = []
for k in K:
    H.append(np.sum(1 / np.arange(1,k+1)))
H = np.array(H)

# number of transactions N
N = 50  

# The MVA code
nbar = np.zeros((N+1,I))
Rzero = np.zeros((N+1,))
Xzero = np.zeros((N+1,))

for n in range(1,N+1):  # For each customers
    Rzero[n] = np.sum(D * (H + nbar[n-1,:]))
    Xzero[n] = n / Rzero[n]
    nbar[n,:] = Xzero[n] * D * (H + nbar[n-1,:])


   
