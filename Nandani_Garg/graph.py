from collections import defaultdict
import numpy as np

# Class to represent a graph


class Graph:

    def __init__(self, vertices):
        '''
        Args:
        vertices : No of vertices of graph		
        '''
        self.V = vertices  # No. of vertices
        self.graph = []  # default list to store graph

        #Vertex adjacency list required for DFS traversal
        self.adjList = defaultdict(list)
        self.weights = {}


    def addEdge(self, src, des, wt):
        '''
        function to add an edge to graph
        Args:
        src: source vertex
        des:	destination vertex
        wt: weight of edge
        '''
        self.graph.append([src, des, wt])


    def makeadjList(self, src, des, wt):
        '''
        function to make adjList of a graph
        Args:
        src: source vertex
        des:	destination vertex
        wt: weight of edge
        '''	
        self.adjList[src].append(des)
        self.weights[(src, des)] = wt



    def find(self, parent, i):
        '''
        function to find set of an element i
        Args: 
        parent: parent of i
        i: vertex i
        '''

        if parent[i] == i:
            return i
        return self.find(parent, parent[i])


    def union(self, parent, rank, x, y):
        '''
        A function that does union of two sets of x and y
        (uses union by rank)
        '''
        xparent = self.find(parent, x)
        yparent = self.find(parent, y)

        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[xparent] < rank[yparent]:
            parent[xparent] = yparent
        elif rank[xparent] > rank[yparent]:
            parent[yparent] = xparent

        # If ranks are same, then make one as root
        # and increment its rank by one
        else:
            parent[yparent] = xparent
            rank[xparent] += 1


    def getKruskalMST(self):
        '''
        The main function to construct MST using Kruskal's algorithm

        Returns: list of resultant MST
        '''

        result = []  # This will store the resultant MST

        # An index variable, used for sorted edges
        i = 0

        # An index variable, used for result[]
        e = 0

        # Step 1:  Sort all the edges in
        # non-decreasing order of their
        # weight.  If we are not allowed to change the
        # given graph, we can create a copy of graph
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])

        parent = []
        rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:

            # Step 2: Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge does't
            #  cause cycle, include it in result
            #  and increment the indexof result
            # for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
            # Else discard the edge

        return result

    def DFS(self, src, des, route_cost, wt, visited):
        '''
        Function to find cost of the path from src to des from a given MST
        Args:
        src : Source vertex
        des: Destination vertex
        route_cost: empty list representing cost of the path from src to des
        wt: edge wt
        visited: list containing visit status of each vertex in MST

        Returns:
        route_cost: list containing cost of the path from src to des
        '''

        visited[src] = 1
        route_cost.append(wt)

        # If current vertex is same as destination, then return route_cost
        if src==des:
            return route_cost
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.adjList[src]:
                if visited[i]==0:
                    r_cost = self.DFS(i, des, route_cost, self.weights[(src,i)], visited)
                    if r_cost:
                        return r_cost

        # Remove current cost from route_cost and mark it as unvisited
        route_cost.pop()
        visited[src] = 0