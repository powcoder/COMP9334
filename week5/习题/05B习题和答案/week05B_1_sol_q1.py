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
COMP9334 Revision problem 5B_1 

Solution 

"""

# import 
import numpy as np
from scipy.stats import t

#%% The given data 
# store the mean response times in 2-D numpy arrays
# Each column is for a system
mrt_sys = np.array([ [13.64,   12.78,   12.21],
                     [13.09,   13.98,   13.64],
                     [13.84,   13.58,   13.09],
                     [12.28,   14.59,   13.84],
                     [14.55,   12.72,   12.28] ])
# The required significance
p = 0.95 

#%% Solution

# Compute the following differenes
# System 0 - System 1
dt01 = mrt_sys[:,0]- mrt_sys[:,1]
# System 0 - System 2
dt02 = mrt_sys[:,0]- mrt_sys[:,2]
# System 1 - System 2
dt12 = mrt_sys[:,1]- mrt_sys[:,2]

# multiplier for confidence interval
num_tests = mrt_sys.shape[0]
mf = t.ppf(1-(1-p)/2,num_tests-1)/np.sqrt(num_tests)

# To compute the confidence interval
pm1 = np.array([-1,1])

# confidence interval for dt01
ci01 = np.mean(dt01) + pm1 * np.std(dt01, ddof=1) * mf

# confidence interval for dt02
ci02 = np.mean(dt02) + pm1 * np.std(dt02, ddof=1) * mf

# confidence interval for dt12
ci12 = np.mean(dt12) + pm1 * np.std(dt12, ddof=1) * mf

