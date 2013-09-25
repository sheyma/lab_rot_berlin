#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import numpy as np
import networkx as nx

a = np.matrix('1 2; 3 4')		# create a matrix
b = np.transpose(a)				# transpose the matrix elements
c = np.loadtxt('D.txt')			# load a file as matrix
d = np.loadtxt('D.txt', unpack=True)
e = np.transpose(np.loadtxt('D.txt', unpack=True))
g = np.zeros( (len(c),len(c) ))
h = np.zeros( (2,3) )

print(a)
print(b)
print(c)
print(' ')
print(d)
print(' ')
print(e)
print(' ')
print(g)
print(' ')
print(h)
print('')


def get_my_threshold_matrix(filename,threshold_value) :	
	
	A = np.transpose(np.loadtxt(filename, unpack=True)) 

	B = np.zeros((len(A),len(A)))
	for row in range(len(A)):
		for item in range(len(A)):
			if row != item:
				if A[row,item] >= threshold_value:
					B[row,item] = 1
				else:
					B[row,item] = 0
	
	print(B)
	G = nx.from_numpy_matrix(B,create_using=nx.Graph())   # ???
	return G

if __name__ == '__main__':
  import sys
  usage = 'Usage: %s correlation_matrix threshold' % sys.argv[0]
  try:
    infilename_data = sys.argv[1]
    value = float(sys.argv[2])
  except:
    print usage; sys.exit(1)

G = get_my_threshold_matrix(infilename_data, value)

n_nodes = nx.number_of_nodes(G)
n_edges = nx.number_of_edges(G)
n_components = nx.number_connected_components(G)
print 'number of nodes:', n_nodes
print 'number of edges:', n_edges
print 'number of components:', n_components
print("Nodes: ", G.nodes())
print("Edges: ", G.edges())
print("Degree of node 0: ", G.degree(0) )
print("Degree of node 1: ", G.degree(1))
print("Degree of node 2: ", G.degree(2))
print("Degree of node 3: ", G.degree(3))
print(G[1])

print 'degree histogram'
check_sum = 0.
degree_hist = {}

for node in G:
	if G.degree(node) not in degree_hist:
		degree_hist[G.degree(node)] = 1
	else:
		degree_hist[G.degree(node)] += 1

print(degree_hist)

keys = degree_hist.keys()
keys.sort()

for item in keys:
	print item, degree_hist[item]		# items and values in dictionary
	check_sum += float(degree_hist[item])/float(n_nodes)

print "check sum: %f" % check_sum
print 'clustering coefficient of full network', nx.average_clustering(G)


# GET NUMBER OF EDGES FOR DIFFERENT THRESHOLDS
def get_my_number_of_edges(filename):
	f = open(filename[:-4]+'_edges.dat','w')
	
	threshold = 0
	
	for i in range(0,101):
		
		threshold = float(i)/100
		G = get_my_threshold_matrix(filename,threshold) 

		N = nx.number_of_nodes(G) 
		max_number_edges = N * (N-1.) / 2
		E = nx.number_of_edges(G)	
		f.write("%f\t%d\t%f\n" % (threshold, E, E/max_number_edges))
	f.close()
	

get_my_number_of_edges(infilename_data)






# GET CLUSTER COEFFICIENTS FOR DIFFERENT THRESHOLDS
threshold = 0
filename = 'D.txt'
f = open(filename[:-4]+'_cc.dat', 'w')
print (f)

for i in range(0,101) :
	threshold = float(i)/100
	A = np.transpose(np.loadtxt(filename, unpack=True)) 
	B = np.zeros((len(A),len(A)))

	for row in range(len(A)):
		for item in range(len(A)):
		  if row != item:
			if A[row,item] >= threshold:
			  B[row,item] = 1
			else:
			  B[row,item] = 0

	G = nx.from_numpy_matrix(B,create_using=nx.Graph()) 
	for node in G :
		f.write('%d\t%f\t%f\n' % (node, threshold, nx.clustering(G, node)))
	f.write("\n")
f.close()

# GET AVERAGE CLUSTER COEFFICIENT
threshold = 0
filename = 'D.txt'
f = open(filename[:-4]+'_average_cc.dat', 'w')
print (f)

for i in range(0,101) :
	threshold = float(i)/100
	A = np.transpose(np.loadtxt(filename, unpack=True)) 
	B = np.zeros((len(A),len(A)))

	for row in range(len(A)):
		for item in range(len(A)):
		  if row != item:
			if A[row,item] >= threshold:
			  B[row,item] = 1
			else:
			  B[row,item] = 0

	G = nx.from_numpy_matrix(B,create_using=nx.Graph()) 
	
	f.write('%f\t%f\t\n' % (threshold, nx.average_clustering(G)))
f.close()






