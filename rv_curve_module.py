#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 09:07:09 2023

JURA coding tutorial

@author: matthewbattley
"""

import numpy as np
import matplotlib.pylab as plt

t0 = 0. #days but typically Barycentre Julian Date (BJD) 
p  = 10. #days
e  = 0.5 
w  = np.pi/3
k  = 10 #m/s
t_init = 0 #days
t_end = 25 #days


# Based on example code from Oscar Barragan

#Create a function that computes the Radial Velocity curve
#input parameters: t_init(float), t_end(float), t0 (float), 
#    p (float), e(float), w(float), k(float), npts (integer,optional) 
#output: t_vector, rv (array) --> The time and RV of the curve we want to plot 
def rv_curve(t_init,t_end,t0,p,e,w,k,npts=1000):
    t_vector = np.linspace(t_init,t_end,npts)
    rv = k * np.cos(nu + w) + e * np.cos(w)
    return t_vector, rv

time, rv = rv_curve(t_init,t_end,t0,p,e,w,k)