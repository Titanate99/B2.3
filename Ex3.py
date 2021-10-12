#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 11:12:57 2021

@author: nate_mac

Write a script to plot the period of a plane pendulum as a function of amplitude 
from 0 to π. Include a line showing the approximate solution for comparison.
 At what amplitude does the exact solution differ from the approximate solution by 1%?


dblquad_demo.py
This script computes the total mass of the plate described on the Numerical 
Integration webpage.
"""

# import needed libraries
from pylab import *
from scipy.integrate import dblquad

# define functions
# integrand
def sigma(y,x):            # NOTE ORDER OF ARGUMENTS! Required order for dblquad()
    return 1.3*exp(-x**2)  # gm cm^-3, doesn't actually depend on y

# lower limit of y integration
def ylower(x):             # just returns the constant value of 0
    return 0.

# upper limit of y integration
def yupper(x):
    return 2.*x/3.

# compute mass and display result
mass, error = dblquad(sigma,0.,3.,ylower,yupper)

print('The mass of the plate is %g grams' % mass)


