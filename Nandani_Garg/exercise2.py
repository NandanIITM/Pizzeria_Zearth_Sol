import numpy as np
from graph import Graph
import sys
import os

def calculateDistance(node1, node2):
	'''
	Calculates eucledian distance between 2 teleport nodes
	
	Args:
	node1: teleport station 1
	node2: teleport station 2
	
	Returns:
	eucledian distance between 2 teleport nodes
	'''
	arr1 = np.array(node1)
	arr2 = np.array(node2)
	temp = arr1-arr2
	dot_product = np.dot(temp.T, temp)
	return np.sqrt(dot_product)


	
def preprocess_data(teleport_coord):
	'''
	Preprocess teleport coordinates
	Args:
		teleport_coord: list containing earth coordinate, teleport coordinates, zearth coordinate
	
	Returns:
		processed_coord: processed list containing earth coordinate, teleport coordinates, zearth coordinate		
	'''
	
	processed_coord=[]
	for i in range(len(teleport_coord)):
		X, Y, Z = float(teleport_coord[i][0]), float(teleport_coord[i][1]), float(teleport_coord[i][2])
		if X<-10000.0 or X>10000.0 or Y<-10000.0 or Y>10000.0 or Z<-10000.0 or Z>10000.0:
			raise Exception(f'Invalid coordinates, X, Y, Z should be in range [-10000, 10000]')
		else:
			processed_coord.append([X, Y, Z])
	return processed_coord
	

def loadData(filename):
	'''
	Load the data from a txt file.
	Args:
		filename: txt file containing input data
	
	Returns:
		teleport_coord : list containing earth coordinate, teleport coordinates, zearth coordinate
	'''
	
	lines = open(filename, 'r').read().split('\n')
	zearth_coord = lines[0].split(' ')
	N = int(lines[1].rstrip())
	
	if N<1 or N>500:
		raise Exception('Number of teleport stations should be within 1 and 500')
	
	
	teleport_coord = []
	#earth coordinates
	earth_coord = [0.0, 0.0, 0.0]
	teleport_coord.append(earth_coord)
	for i in range(2, N+2):
		coordinate = lines[i].split(' ')
		if len(coordinate)<3:
			raise Exception('Teleport coordinates should be 3-dimension')
		teleport_coord.append(coordinate)
	
	#append zearth coordinates, earth coordinate is at location 0 and zearth coordinate is at loaction N-1
	teleport_coord.append(zearth_coord)
	teleport_coord = preprocess_data(teleport_coord)
	return teleport_coord
	
		
	
	
if __name__=='__main__':
	#filename passed in argument
	filename = sys.argv[1]
	
	#loads data from input file
	filepath = os.path.join(os.path.dirname(__file__), filename)
	teleport_coord = loadData(filepath)
	
	
	N=len(teleport_coord)
	#Step1: initialize graph and add edges to the graph, edge weight is calculated using eucledian dis between 2 nodes
	g = Graph(N)
	for i, node1 in enumerate(teleport_coord):
		for j , node2 in enumerate(teleport_coord):
			if i<j:
				edge_wt = calculateDistance(node1, node2)
				g.addEdge(i, j, edge_wt)
                
                
	#Step2: Get MST of the given graph from Kruskal algorithm
	result = g.getKruskalMST()
	
	#Step3: Make adjList from MST for DFS traversal
	for i, r in enumerate(result):
		g.makeadjList(r[0], r[1], r[2])
		g.makeadjList(r[1], r[0], r[2])
		
	#Step4:	DFS traversal on MST to find cost of the path from earth(src) to zearth(des)
	route_cost=[]
	visited= [0]*N
	route_cost= g.DFS(0, N-1, route_cost, 0, visited)

	#Step5: Given path from earth to zearth, calculate max edge weight
	max_weight=0
	for i, r in enumerate(route_cost):
		weight = r
		if weight>max_weight:
			max_weight = weight
            
	max_wt_float = "{:.2f}".format(max_weight)
	print(max_wt_float)		