import os
import sys
	
def getMaxPizzeriasBlock(N, pizzeria, city):
	'''
	Updates the city blocks based on the pizzeria location
	
	Args:
	N: dimension of the city in blocks
	pizzeria: location of a pizzeria with K, [X,Y,K]
	city: matrix representing city with blocks NXN
	'''
	X = pizzeria[0]-1   #python 0-indexing
	Y = pizzeria[1]-1	#python 0-indexing
	K = pizzeria[2]
	if X>=0 and Y>=0 and K>0:
		visited = [[0]*N for i in range(N)]
		dfs(X, Y, K, city, visited)
    
    
def dfs(X, Y, K, city, visited):
	'''
	Recursive function to update neighbourhood blocks given a pizzeria location
	Args:
	X:	x-coordinate of the pizzeria location
	Y:	y-coordinate of the pizzeria location
	K:	maximum distance pizzeria's delivery guy will travel to deliver pizza
	city: city with dimension NXN
	visited: matrix of size city to keep track if a block is visited or not
	'''
	if K<0:
		return
	if X<0 or Y<0 or X>=len(city) or Y>=len(city):
		return
	if visited[X][Y]==0:
		city[X][Y] +=1
		visited[X][Y] = 1
		dfs(X-1, Y, K-1, city, visited)
		dfs(X, Y-1, K-1, city, visited)
		dfs(X, Y+1, K-1, city, visited)
		dfs(X+1, Y, K-1, city, visited)   
		
def loadData(filename):
	'''
	Load the data from a txt file.
	Args:
		filename: txt file containing input data
	
	Returns:
		a tuple containing (N, M, pizzeria_loc)
		N: dimension of the city in blocks
		M: number of pizzerias in the city
		pizzeria_loc: list containing pizzerias location with each element as [X, Y, K]
	'''
	
	lines = open(filename, 'r').read().split('\n')
	N, M = lines[0].split(' ')
	N, M = int(N), int(M)
	pizzeria_loc=[]
	if N<1 or N>1000:
		raise Exception("Input dimension should be within 1 and 1000")
		
	if M<1 or M>1000:
		raise Exception("No of pizzerias should be within 1 and 1000")
	
	for i in range(1, M+1):
		X, Y, K = lines[i].split(' ')
		X, Y, K = int(X), int(Y), int(K)
		if X<1 or X>N or Y<1 or Y>N:
			raise Exception(f"Invalid coordinate ({X}, {Y})")
		if K<1 or K>N:
			raise Exception(f"Given K:{K}, K should be >=1 and <={N}")
		pizzeria_loc.append([X, Y, K])
		
	return (N, M, pizzeria_loc)
	
		
		
if __name__ == '__main__':
	#filename passed in argument
	filename = sys.argv[1]
	
	#loads data from input file
	filepath = os.path.join(os.path.dirname(__file__), filename)
	N, M, pizzeria_loc = loadData(filepath)
	city = [[0]*N for i in range(N)]
	
	for i in range(M):
		getMaxPizzeriasBlock(N, pizzeria_loc[i], city)
	#prints output that represents the number of pizzerias that deliver pizzas to the block with the greatest selection of pizzas.
	print(max(map(max, city)))
		
	
			
		
	