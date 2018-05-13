'''
Created on Feb 28, 2018

@author: ema
'''

class DictGraph:
    '''
    A directed graph, represented as three maps,
    one from each vertex to the set of outbound neighbours,
    one from each vertex to the set of inbound neighbours, and one with the costs of each edge.
    '''    
    
    def __init__(self,n=0):
        '''
        Creates a graph with n vertices and no edges
        '''
        self.__in = {}
        self.__out = {}
        if n>0:
            for i in range(n):
                self.__in[i]=[]
                self.__out[i] = []
            
    def addVertex(self, v):
        '''
        Adds a new isolated vertex.
        Precondition: the vertex v is not already in the graph
        Input: v - the vertex (class Node)
        '''
        if v in self.__in.keys():
            return False
        self.__in[v] = []
        self.__out[v] = []
        return True
    
    
    def removeVertex(self,v):
        '''
        Removes a vertex from the graph
        Input: v - the vertex to be removed
        Precondition: v must be a vertex of the graph
        '''
        for k in self.__in.keys():
            if v in self.__in[k]:
                self.removeEdge(v,k)
        self.__in.pop(v)
        self.__out.pop(v)
        
    def addEdge(self,x,y):
        '''
        Adds an edge from x to y.
        Input: x,y - vertices
        Precondition: there is no edge from x to y
        '''
        if self.isEdge(x, y):
            return False
        self.__out[x].append(y)
        self.__in[y].append(x)
        return True
    
    def removeEdge(self,x,y):
        ''' 
        Removes the edge (x,y) from the graph
        Input: x,y - end points of the edge to be removed
        Precondition: (x,y) is an edge of the graph
        '''
        if not self.isEdge(x, y):
            return False
        self.__out[x].remove(y)
        self.__in[y].remove(x)
        return True
        
        
    def isEdge(self,x,y):
        """
        Input: x,y - vertices
        Output: - True if there is an edge from x to y
                - False otherwise
        Precondition: x,y valid vertices
        """
        return y in self.__out[x]
    
    def getInDegree(self,v):
        '''
        Returns the in degree of vertex v
        Input: v
        Output: the in degree of v
        Preconditions: v must be a valid vertex in the graph
        '''
        return len(self.__in[v])
    
    def getOutDegree(self,v):
        '''
        Returns the out degree of vertex v
        Input: v
        Output: the out degree of v
        Preconditions: v must be a valid vertex in the graph
        '''
        return len(self.__out[v])
    
    def parseOut(self,v):
        """
        Returns an iterable containing the outbound neighbours of v
        Input: v - vertex
        Output: a list of vertices
        Preconditions: v must be a valid vertex in the graph
        """
        return self.__out[v]

    def parseIn(self,v):
        """
        Returns an iterable containing the inbound neighbours of v
        Input: v - vertex
        Output: a list of vertices
        Preconditions: v must be a valid vertex in the graph
        """
        return self.__in[v]    
    
    
    def getNumberOfVertices(self):
        '''
        Returns the number of vertices in the graph
        Input: -
        Output: the number of vertices
        Preconditions: -
        '''
        return len(self.__in.keys())

    def getVertices(self):
        return self.__out.keys()

    def isValidVertex(self, v):
        '''
        Input: v - a vertex
        Output: True - if v is valid
                False otherwise
        Preconditions: - 
        '''
        return v in self.__in.keys()
    
    def getVertexByID(self,ID):
        for v in self.getVertices():
            if v.getID() == ID:
                return v
        return None
    
    def getOut(self):
        return self.__out
    
def testGraph():
    g = DictGraph(4)
    g.addEdge(1,2)
    g.addEdge(1,3)
    g.addEdge(2,3)
    g.addEdge(0,2)
    g.addEdge(0,1)
    assert g.isEdge(1, 2) == True
    
testGraph()
    