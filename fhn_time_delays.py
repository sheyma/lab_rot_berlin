#!/usr/bin/python2.7 

# -*- coding: utf-8 -*-

from __future__ import division

import numpy as np

import sys

from netpy import simnet

import random

import numpy as np

import math
import os


#gfilename = 'allzeros.dat'
#dfilename = 'allzeros.dat'

#gfilename = 'NKI705197sc.dat'
#dfilename = 'pathdistance_zeros.dat'



gfilename = sys.argv[1]
dfilename = sys.argv[2]

print gfilename[:-4]

"""Attention: alphabethical order of equation advised!!! """

eqns = {r'x{i}': '(y{i} + gamma * x{i} - pow(x{i},3.0)/3.0) * TAU',

        r'y{i}': '- (x{i} - alpha + b * y{i}) / TAU'}

#for parameter in range(1, 10):
	#params[sigma] = parameter * 0.01


params = { # Fitzhugh-Nagumo parameters...

        'gamma': 1.0, 

        'alpha': 0.85,  #'alpha': 1.05, 

        'b': 0.2,

        'TAU': 1.25, 

	'sigma': float(sys.argv[3]),  #float(sys.argv[3]), # 0.1 # 0.005 # global coupling constant

	'D' : float(sys.argv[4]),   # noise # 0.05

	'v' : 70.0, # velocity in 0.1 m/s ???
	#'tau' : 1.0, 

}


noise = {'x': 'D * gwn()', 'y': 'D * gwn()'}  # this is for the noise for the first system only if noise = {'x': 'D * gwn()', 'y': 'D * gwn()'} it is for all nodes

#noise = { 'x': '0' }



""" Topology """

G = np.loadtxt(gfilename) # weight matrix

C = params['sigma'] 

H = [ [C, 0],

      [0, 0] ]

print 'H', H



"""Delay-Matrix. """

#simple version: all delay identical => specily 'tau' in params-array

#T = params['tau'] * np.ones_like(G)



try:

	D_matrix = np.loadtxt(dfilename)

except:

	print 'File not found:', dfilename

T  = D_matrix/params['v']


print 'maximum delay', T.max(), '=> smallest largest integer:', math.ceil(T.max())

max_tau = math.ceil(T.max())



""" coupling term """

#diffusive coupling: \dot var_i = ... (var_j - var_i)

#coupling = '+{G:.12f}*{H}*({var}-{self})'

#direct coupling: \dot var_i = ... var_j

coupling = '-{G:.1f}*{H}*{var}(t-{tau})'



"""Let's go """

neuronetz = simnet(eqns, G, H, T, params, coupling, noise)

#print neuronetz.eqnsN

random.seed()

  

# generate history function/initial conditions: 

#100 specifies the number of points in the history array

thist = np.linspace(0, max_tau, 10000)

xhist = np.zeros(len(thist))

yhist = np.zeros(len(thist)) + 0.5

dic = {'t' : thist}

for i in range(len(G)):

  # all elements identical

  dic['x'+str(i)] = xhist

  # constant shift added

  #dic['x'+str(i)] = xhist + i / len(G)

  # random values added

  #dic['x'+str(i)] = xhist + 1.*random.random()

  dic['y'+str(i)] = yhist



neuronetz.ddeN.hist_from_arrays(dic)



""" Start simulation with t = [0,tmax] """

tmax = 70000
neuronetz.run(tmax)




# alternative way to generate history function/initial conditions

#initial_conditions = {'x0': -0.95, 'y0': -0.95+ pow(0.95,3.0)/3.0,

                      #'x1': -0.95, 'y1': -0.95+ pow(0.95,3.0)/3.0}

#neuronetz.run(initial_conditions, tmax=600)

series = neuronetz.sol



#sample solution for output starting at t=-max_tau

solution = neuronetz.ddeN.sample(0, dt=0.1)



t = solution['t']

#print only last 10% of time series

#tpre = solution['t']

#t = tpre[int(0.9*len(tpre)):]



print "starting print-out of data..."



t=solution['t'][0:]



x = {}

y = {}



for i in range(0,len(G[0])):


  x[i] =  solution['x'+str(i)][0:]

  y[i] =  solution['y'+str(i)][0:]


f = open(gfilename[:-4]+'_sigma='+str(params['sigma'])+'_D='+str(params['D'])+'_v='+str(params['v'])+'_tmax='+str(tmax)+'.dat', 
'w')
#f = open('data.dat', 'w')


for i, t0 in enumerate(t):

  f.write('%s\t' % (t0))

  for j in range(0, len(x)):

    f.write('%.2f\t%.2f\t' % (float(x[j][i]), float(y[j][i])))

  f.write('\n')

  

f.close()



print "done!"



