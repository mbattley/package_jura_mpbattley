#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 09:07:09 2023

JURA coding tutorial

@author: matthewbattley
"""

import numpy as np
import matplotlib.pylab as plt

# Based on example code from Oscar Barragan

t0 = 0. #days but typically Barycentre Julian Date (BJD) 
p  = 10. #days
e  = 0.5 
w  = np.pi/3
k  = 10 #m/s
t_init = 0 #days
t_end = 25 #days

#time to create the function that computes the true anomaly from the mean anomaly
#This function calculates the true anomaly
#input parameters: t (float), t0 (float), 
#    p (float), e(float)
#output: true (array) --> The true anomaly of the planetary orbit
def true_anomaly(t,t0,e,p):
    mean = 2.*np.pi * ( t - t0) / p                       #mean anomaly
    true = mean + e * np.sin(mean)                        #guess
    f = true - e * np.sin(true) - mean                    #first value of function f
    for i in range(len(t)):                               #iterate for all the values
        while np.abs(f[i]) > 1e-6:                        #Newton-Raphson condition
            f[i] = true[i] - e*np.sin(true[i]) - mean[i]  #calculate  f
            df   = 1. - e * np.cos(true[i])               #Calculate df
            true[i] = true[i] - f[i]/df                   #Update the eccentric anomaly
    eimag = np.sqrt(1. - e*e)*np.sin(true)                #Time to calculate true anomaly
    ereal = np.cos(true) - e
    true  = np.arctan2(eimag,ereal)                       #Get True anomaly from ecc anomaly
    return true

#Create a function that computes the Radial Velocity curve
#input parameters: t_init(float), t_end(float), t0 (float), 
#    p (float), e(float), w(float), k(float), npts (integer,optional) 
#output: t_vector, rv (array) --> The time and RV of the curve we want to plot 
def rv_curve(t_init,t_end,t0,p,e,w,k,npts=1000):
    t_vector = np.linspace(t_init,t_end,npts)
    #Get the true a nomaly from the true_anomaly function
    nu =  true_anomaly(t_vector,t0,e,p)
    #Compute the RV curve
    rv = k * np.cos(nu + w) + e * np.cos(w)
    return t_vector, rv

t, rv = rv_curve(t_init,t_end,t0,p,e,w,k)

# plot the RV curve
plt.plot(t, rv)
plt.xlabel("Time [d]")
plt.ylabel("RV [m/s]")
plt.show()