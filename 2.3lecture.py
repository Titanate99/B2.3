#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 14:58:41 2021

@author: nate_mac

tasks: int sin(x) analitically
    thene calc using trap rule
    then using simpson's rule

"""

import random as r
import math 
import numpy as np
from pylab import *
from scipy.integrate import quad, simpson
import matplotlib.pyplot as plt

check = 2

a = 0   # lower limit of integration
b = np.pi   # upper limit of integration
N=10
x = linspace(0,np.pi,N)

y = np.sin(x)

value = zeros(N) 

idx = 0
for i in y:
    value[idx],error = quad(func,a,b,args=i) # note use of the args optional argument
    idx = (idx + 1)



figure(1)
clf()
plot(x,value)

#diff between exact answer and alg. answer is the ERROR
# so see how error changes with increase in N

#take the int of sin(x) using Trapazoid method
def TrapTest(N,check):
    x = linspace(0,np.pi,N)
    y = np.sin(x)
    approx = trapz(y,x)
    error = check - approx
    figure(2)
    clf()
    plot(x,y)
    return "Your error using Trapazoids is " + str(error)
#take the int of sin(x) using Simpson method
    

def SimpTest(N,check):
    x = linspace(0,np.pi,N)
    y = np.sin(x)
    approx = simpson(y,x)
    error = check - approx
    return error
    #return "Your error using Simpson is " + str(error)
#Perform many Simpson checks over a range of N-Sample values
#Plot against N to show progression of error
def NTest(N_min,N_max):
    ns = arange(N_min+1,N_max+2,1)
    errors = zeros(N_max-N_min)
    for n in (ns-1):
        
        error = SimpTest(n,check)
       
        errors[n-(N_min+1)] = error
        print("Your error using Simpson for N = " + str(n) + " is " + str(error))
    figure(3)
    clf()
    plot(ns[1:],errors,'-.r')
    #print(ns.shape)
    #print(errors.shape)
    return
        

print(TrapTest(10,2))
print(SimpTest(10,2))
    
NTest(10,100)
