'''
Takes an undirected graph (adjacency list), and returns a minimum spanning tree (MST) 
that connects all vertices with the smallest total sum of weights of the eges. Algorithm
used is Kruskals Algorithm.

Return formatted as an adjacency list, just like the input. 
'''


def question3(graph):
    from collections import defaultdict
    def transformGraph(graph1):
        edges = []
        counter = 1
        for node in graph1:
            for edge in graph1[node]:
                counter += 1
                try:
                    temp = [node, edge[0], int(edge[1])]
                except ValueError:
                    print "Error!"
                edges.append(sorted(temp))
        hubs = graph1.items() # list of nodes and outgoing vertices

        def remove_duplicates(x):
            a = []
            for i in x:
                if i not in a:
                    a.append(i)
            return a
        import numpy as np
        tempGraph = np.asarray(remove_duplicates(edges))
        verticez = len(tempGraph) - 1
        g2 = Graph(verticez)
        import string
        di=dict(zip(string.letters,[ord(c)%32 - 1 for c in string.letters]))
        di2 = dict((v,k) for k,v in di.iteritems())
        for row in range(0,len(tempGraph)):
            g2.addEdge( di[tempGraph[row][1]] , di[tempGraph[row][2]] , int(tempGraph[row][0]) )
        return g2

    class Graph:

        def __init__(self,vertices):
            self.vertice = vertices 
            self.graph = [] 
        def addEdge(self,u,v,w):
            self.graph.append([u,v,w])
        def find(self, parent, i):
            if parent[i] == i:
                return i
            return self.find(parent, parent[i])
        def union(self, parent, rank, x, y):
            xroot = self.find(parent, x)
            yroot = self.find(parent, y)
            if rank[xroot] < rank[yroot]:
                parent[xroot] = yroot
            elif rank[xroot] > rank[yroot]:
                parent[yroot] = xroot
            else :
                parent[yroot] = xroot
                rank[xroot] += 1

        # Kruskal algorithm to make the Minimum Spanning Tree
        def KruskalMST(self):
            result =[]
            i = 0 
            e = 0 
            self.graph = sorted(self.graph,key=lambda item: item[2])
            parent = [] ; rank = []
            for node in range(self.vertice):
                parent.append(node)
                rank.append(0)
            while e < self.vertice -1:
                u,v,w= self.graph[i]
                i = i + 1
                x = self.find(parent, u)
                y = self.find(parent ,v)
                if x != y:
                    e = e + 1
                    result.append([u,v,w])
                    self.union(parent, rank, x, y)         
            adjacency_list = {}
            import string
            di=dict(zip(string.letters,[ord(c)%32 - 1 for c in string.letters]))
            di2 = dict((v,k) for k,v in di.iteritems())
            for u,v,weight in result:
                adjacency_list.setdefault(di2[u], {})[di2[v]] = weight
                adjacency_list.setdefault(di2[v], {})[di2[u]] = weight


            return adjacency_list
    try:
        g2 = transformGraph(graph)
    except:
        print "Error! Check your inputs!"
        return
        
    return g2.KruskalMST()
    
# Has 0 and float
graph1= {'A': [('B', 0), ('D', 40), ('C', 37)],
         'B': [('A', 0), ('C', 2.5)], 
         'C': [('B', 2.5), ('A', 37)],
         'D': [('A', 40)],
        }        
# Long number!
graph2= {'A': [('B', 2), ('D', 4), ('C', 40), ('H', 5)],
         'B': [('A', 2), ('C', 5)], 
         'C': [('B', 5), ('E', 2000000000), ('A', 40)],
         'D': [('A', 4), ('F', 15)],
         'E': [('C', 2000000000), ('G', 13), ('G', 1)],
         'F': [('D', 15)],
         'G': [('E', 13), ('E', 1)],
         'H': [('A', 5)]
        }   
# Missing values for distance
graph3= {'A': [('B'), ('D', 40), ('C', 37)],
         'B': [('A'), ('C', 2.5)], 
         'C': [('B', 2.5), ('A', 37)],
         'D': [('A', 40)],
        }      

print question3(graph1)
# {'a': {'b': 0}, 'c': {'b': 2}, 'b': {'a': 0, 'c': 2}}
print question3(graph2)
# {'a': {'h': 5, 'b': 2, 'd': 4}, 'c': {'b': 5, 'e': 2000000000}, 'b': {'a': 2, 'c': 5}, 'e': {'c': 2000000000, 'g': 1}, 'd': {'a': 4, 'f': 15}, 'g': {'e': 1}, 'f': {'d': 15}, 'h': {'a': 5}}
print question3(graph3)
# Error! Check your inputs!