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
	
	G = nx.from_numpy_matrix(B,create_using=nx.Graph())   # ???
	return G

def get_my_characteristics(G, filename) :
	n_nodes = nx.number_of_nodes(G)
	n_edges = nx.number_of_edges(G)
	n_components = nx.number_connected_components(G)
	print 'number of nodes:', n_nodes
	print 'number of edges:', n_edges
	print 'number of components:', n_components
	print("Nodes: ", G.nodes())
	print("Edges: ", G.edges())

	for node in G :
		print 'Degree of node ', node, " : ", G.degree(node)

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
	return 0  ##?



# GET NUMBER OF EDGES FOR DIFFERENT THRESHOLDS

def get_my_number_of_edges(filename):
	f = open(filename[:-4]+'_edges.dat','w')
	threshold = 0
	print(f)	
	for i in range(0,101):
		threshold = float(i)/100
		G = get_my_threshold_matrix(filename,threshold) 
		N = nx.number_of_nodes(G) 
		max_number_edges = N * (N-1.) / 2
		E = nx.number_of_edges(G)	
		f.write("%f\t%d\t%f\n" % (threshold, E, E/max_number_edges))
	f.close()
	
# GET CLUSTER COEFFICIENTS OF SINGLE NODES FOR DIFFERENT THRESHOLDS
def get_my_cluster_coefficients(filename) :
	threshold = 0
	f = open(filename[:-4]+'_cc.dat', 'w')
	print (f)
	for i in range(0,101) :
		threshold = float(i)/100	
		G = get_my_threshold_matrix(filename,threshold) 
		for node in G :
			f.write('%d\t%f\t%f\n' % (node, threshold, nx.clustering(G, node)))
		f.write("\n")
	f.close()

# GET AVERAGE CLUSTER COEFFICIENT OF THE WHOLE NETWORK
def get_my_average_cluster_coefficient(filename) :
	threshold = 0
	f = open(filename[:-4]+'_average_cc.dat', 'w')
	print (f)	
	f.write('threshold \t average_cluster_coefficient \n')		
	for i in range(0,101) :
		threshold = float(i)/100
		G = get_my_threshold_matrix(filename,threshold) 
		f.write(' %f\t %f\t\n' % (threshold, nx.average_clustering(G)))
	f.close()

# PROB OF ONE NODE TO HAVE k' NUMBER OF DEGREES/NEIGBORS CONNECTED
def get_my_degree_distribution(filename) :
	threshold = 0
	f = open(filename[:-4]+'_degree_distr.dat','w')
	print(f)
	for i in range(0,101) :
		threshold = float(i)/100
		G = get_my_threshold_matrix(filename,threshold)
		check_sum = 0
		degree_hist = {}
		for node in G :
			if G.degree(node) not in degree_hist :		
				degree_hist[G.degree(node)] = 1
			else :
				degree_hist[G.degree(node)] += 1
		keys = degree_hist.keys()
		keys.sort()
		degrees = range(0, nx.number_of_nodes(G)+1 , 1) #?
		for item in degrees :
			if item in keys :
				prob = float(degree_hist[item])/float(nx.number_of_nodes(G))
				check_sum += prob
				f.write('%d\t%f\t%d\t%f\n'%(item, threshold, degree_hist[item], prob))
			else :
				f.write('%d\t%f\t0\t0.\n' % (item, threshold))
    		f.write("\n")
    	print 'degree distr of threshold: %f, check sum: %f' % (threshold, check_sum)
	f.close()

# DEGREES OF NODES FOR DIFFERENT THRESHOLDS
def get_my_degrees(filename) :
	threshold = 0
	f = open(filename[:-4]+'_degrees.dat', 'w')
	print(f)
	for i in range(0,101) : 
		threshold = float(i)/100
		G = get_my_threshold_matrix(filename,threshold)
		for node in G :
			f.write('%d \t %f \t %d \n' %((node+1), threshold, G.degree(node)))
		f.write("\n")
	f.close()		

def get_my_average_degree(filename) :
	threshold = 0
	f = open(filename[:-4]+'_average_degree.dat','w')
	print f	
	f.write('threshold \tave_degree \n')
	for i in range(0,101):
		threshold = float(i)/100
		G = get_my_threshold_matrix(filename, threshold)
		values = []		
		for node in G :
			values.append(G.degree(node))
		ave_degree = float(sum(values))/float(nx.number_of_nodes(G))
		f.write('%f\t%f\t\n'%(threshold,ave_degree))
	f.close()

def get_my_number_of_components(filename) : #wiki: connec._comp.
	threshold = 0
	f = open(filename[:-4]+'_components.dat','w')
	print f	
	f.write('threshold \tnumber_of_connected_components \n')
	for i in range(0,101):
		threshold = float(i)/100
		G = get_my_threshold_matrix(filename, threshold)
		f.write('%f\t%d\n'%(threshold,nx.number_connected_components(G)))
	f.close()

def get_my_shortest_pathlength(filename):
	threshold = 0
	f = open(filename[:-4]+'_shortest_pathlength.dat','w')
	print f
	f.write('threshold\tave_shor_pathl\n')	
	for i in range(0,101):
		threshold = float(i)/100
		G = get_my_threshold_matrix(filename, threshold)
		components = nx.connected_component_subgraphs(G) #subgraphs in mtrx !
		values = []		
		for i in range(len(components)) :
			if nx.number_of_nodes(components[i]) >1 : # pathleng: min 2 node
				values.append(nx.average_shortest_path_length(components[i]))
		if len(values) == 0 :
			f.write("%f\t0.\n" % (threshold))
			#print 'average shortest pathlength: 0'
		else :
			f.write("%f\t%f\n" % (threshold, (sum(values)/len(values))))
			#print 'average shortest pathlength: %f ' % (sum(values)/len(values))
	f.close()	


def get_my_nodes_of_components(filename, value):
	import networkx as nx
	threshold = value
	f = open(filename[:-4]+'_nodes_components_r'+str(threshold)+'.dat','w')
	G = get_my_threshold_matrix(filename, threshold)
	print 'number of connected components:', nx.number_connected_components(G)
	comps = nx.connected_component_subgraphs(G)
	counter = 0
	f.write('threshold\tnumber_subG\tnode\n')
	for graph in comps :
		counter += 1
		liste = graph.nodes()
		for node in graph.nodes() :
			f.write('%f\t%d\t\t%d\n' % (value,counter,graph.nodes()))
	f.close()




if __name__ == '__main__':
  import sys
  usage = 'Usage: %s correlation_matrix threshold' % sys.argv[0]
  try:
    infilename_data = sys.argv[1]
    value = float(sys.argv[2])
  except:
    print usage; sys.exit(1)


network = get_my_threshold_matrix(infilename_data , value)

nx.draw(network)

get_my_characteristics(network,infilename_data)

get_my_number_of_edges(infilename_data)

get_my_cluster_coefficients(infilename_data)

get_my_average_cluster_coefficient(infilename_data)

get_my_degree_distribution(infilename_data)

get_my_degrees(infilename_data)

get_my_average_degree(infilename_data)

get_my_number_of_components(infilename_data)

get_my_shortest_pathlength(infilename_data)

get_my_nodes_of_components(infilename_data,value)

















