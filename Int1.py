#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 14:36:55 2021

@author: nate_mac

quad_demo.py
Demonstrates using the arg parameter to 
pass parameters to the integrand function 
when using the quad() function.
"""

# import the needed modules
from pylab import *
from scipy.integrate import quad

# define the integrand function 
def func(x, alpha):
	return alpha*exp(-alpha*x**3)

# set the parameters
a = 1   # lower limit of integration
b = 3   # upper limit of integration
N = 100 # number of alpha values to use in integrations

alpha_ary = linspace(0,1,N) # create an array of values of alpha
value = zeros(N)            # create an array to store results of integrations

# do the integrations
idx = 0
for alpha in alpha_ary:
    value[idx],error = quad(func,a,b,args=alpha) # note use of the args optional argument
    idx = idx + 1
	
# plot the result
figure(1)
clf()
plot(alpha_ary,value)

# note the new syntax for the xlabel() and title() commands
# that allows the use of LaTeX commands
xlabel(r'$\alpha$') 
ylabel('Integral')
title(r"Plot of $\int^3_1 \alpha \exp(-\alpha x^3) dx$")