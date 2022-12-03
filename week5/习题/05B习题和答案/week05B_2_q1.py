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
COMP9334 Week 4B, Solution to revision problem

Generate Weibull distributed random numbers 


"""

import numpy as np 
import matplotlib.pyplot as plt 
import pickle

# Save state of the random number generator  
# rand_state = np.random.get_state()
# pickle.dump( rand_state, open( "rand_state.p", "wb" ) )

# If you want to reproduce the results in the solution, 
# you will need to uncomment the following 2 lines 
# rand_state = pickle.load( open( "rand_state.p", "rb" ) )
# np.random.set_state(rand_state)
# Notes: the state was saved by using Lines 16-17

# Generate 10,000 random numbers that are uniformly
# distributed in (0,1)
n = 10000
u = np.random.random((n,))

# To produce 10,000 numbers with Weibull distribution with parameters
# alpha = 5
# beta = 6
n = 10000;
alpha = 5;
beta = 6;
x = (-np.log(1-u)/alpha)**(1/beta);

# To check the numbers are really Weibull distributed
# Plot an histogram of the number 
nb = 50 # Number of bins in histogram 
freq, bin_edges = np.histogram(x, bins = nb, range=(0,np.max(x)))

# Lower and upper limits of the bins
bin_lower = bin_edges[:-1]
bin_upper = bin_edges[1:]
# expected number of exponentially distributed numbers in each bin
y_expected = n*(np.exp(-alpha*bin_lower**beta)-np.exp(-alpha*bin_upper**beta))

bin_center = (bin_lower+bin_upper)/2
bin_width = bin_edges[1]-bin_edges[0]

plt.bar(bin_center,freq,width=bin_width)
plt.plot(bin_center,y_expected,'r--',label = 'Expected',Linewidth =3)
plt.legend()
plt.title('Histogram of 10^4 Weibull distributed psuedo-random numbers')
# plt.savefig('week05B_2_sol/fig/week05B_2_q1.png')
