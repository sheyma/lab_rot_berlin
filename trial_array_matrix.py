#!/usr/bin/python2.7

import numpy

from array import*


a=array('i',[1,2,3,4,5])
for i in a:
	print(a)

a.insert(0,6)
print(a)
a.append(7)
print(a)

b=array('i',[9,10,11])
a.extend(b)
print(a)

a.remove(2)
print(a)

a.reverse()
print(a)

c=numpy.matrix([ [1,2], [3,4]   ])
print(c) 
