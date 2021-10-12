#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 10:47:34 2021

@author: nate_mac

Imagine that you have a molecular dynamics simulation of atoms in thermal equilibrium. 
The ideal distribution of each velocity component will be normal.  In order to
determine how likely a particular interaction will take place, like ionization, 
you need to know the probability that an individual atom will have a given velocity.  
For simplicity, we'll just look at one component of the velocity.

Write a function to return the integrated probability over a specified interval 
of 𝑥 values (which here are velocities). For now, set the mean to zero and the 
variance to one in your distribution (feel free to use keyword arguments so that
you can set these at run time).
What's the probability that the velocity of a given atom lies in the interval [−𝜎,𝜎]?
"""

#N(x | mu, sigma, n) := (n/(sigma*sqrt(2*pi))) * exp((-(x-mu)^2)/(2*sigma^2))

import random as r
import math 
import numpy as np
from pylab import *
from scipy.integrate import quad

#rand_vx = r.sample(range(10, 60), 50)
"""
Attempt #1
def gauss(x):
    return exp(np.random.normal(0,1,x))

def make_gauss(N, sigma, mu,f):
    
    k = N / (sigma * math.sqrt(2*math.pi))
    s = -1.0 / (2 * sigma * sigma)
    def f():
        return k * math.exp(s * (x - mu)*(x - mu))
    return f

x = make_gauss(10,1,1,r_v)

"""


"""
Attempt #2
# Integrating a random set of int velocities (x)
np.random.seed(42)
def gaussian(x, mu, sigma):
    return ((1/(sigma*sqrt(2*pi))) * np.exp((-(x-mu)^2)/(2*sigma^2)))


# Define mu and sigma
mu = 0
sigma = 1

# Define bounds of integral
a = -3
b = 3
# Generate function values
x_range = np.linspace(-5,5,100)
fx = gaussian(x_range, mu, sigma)
out = (quad(x_range,a,b))
print(out)
"""

v = np.linspace(-10,10,50)


def make_gauss(N, sigma, mu):
    k = N / (sigma * math.sqrt(2*math.pi))
    s = -1.0 / (2 * sigma * sigma)
    def f(x):
        return k * math.exp(s * (x - mu)*(x - mu))
    return f
lit = np.arange(0,10)

print(quad(make_gauss(lit, 1, 0), -inf, inf))
