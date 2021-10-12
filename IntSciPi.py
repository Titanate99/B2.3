#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 11:07:01 2021

@author: nate_mac

"""

"""
Write a script to plot the period of a plane pendulum as a function of 
amplitude from 0 to π. Include a line showing the approximate solution for 
comparison. At what amplitude does the exact solution differ from the 
approximate solution by 1%?
"""

from pylab import *

from scipy.integrate import quad

def gaus(x):
    return exp(-x**2)


print(quad(gaus,-inf,inf))
