'''
Created on Feb 28, 2018

@author: ema
'''
from Graph.DictGraph import DictGraph
from Graph.Node import Node


class UI:
    def __init__(self):
        self.__graph = self.readFile()
        self.__total = 0
        
    
    @staticmethod
    def printMenu():
        s = '\t\tMenu\n'
        s += '\t1 - Check if the graph is a DAG\n'
        s += '\t2 - Print the earliest and latest starting time for each activity and the total time of the project.\n'
        s += '\t3 - Print the critical activities\n'
        s += '\t0 - Exit\n'
        print(s)
    
    def readVertex(self):
        while True:
            v = input("Enter vertex ID: ")
            try:
                v  = int(v)
                if self.graph.isValidVertex(v):
                    return v
                else:
                    print("Invalid vertex ID! Try again.")
            except ValueError:
                print("The vertex ID must be an integer number. Please try again: ")
                
    def readFile(self):
        with open("../act.csv", "r") as f:
            graph = DictGraph()
            startNode = Node(0,0)
            graph.addVertex(startNode)
            last = 0
            for line in f:
                line = line.strip().split(" ")
                ID = int(line[0].strip())
                if ID > last:
                    last = ID
                d = int(line[1].strip())
                pre = line[2].strip()
                if pre == "-":
                    pre = []
                else:
                    pre = pre.split(",")
                if Node(ID,d) not in graph.getVertices():
                    y = Node(ID,d)
                    graph.addVertex(y)
                else:
                    y = graph.getVertexByID(ID)
                    y.setDuration(d)
                for p in pre:
                    x = graph.getVertexByID(int(p))
                    if x == None:
                        x = Node(int(p),-1)
                        graph.addVertex(x)
                    graph.addEdge(x,y)
                if len(pre)==0:
                    graph.addEdge(startNode, y)
            endVertex = Node(last+1,0)
            graph.addVertex(endVertex)
            for v in graph.getVertices():
                if len(graph.parseOut(v))==0 and v!=endVertex:
                    graph.addEdge(v,endVertex)
        return graph
                
    def tSorting(self):
        '''
        Input: - graph : directed graph
        Output: - sortedList : a list of vertices in topological sorting order, or null if G has cycles
        '''
        sortedList = []
        q = []
        count = {}
        for x in self.__graph.getVertices():
            count[x] = self.__graph.getInDegree(x)
            if count[x] == 0:
                q.append(x)
        while len(q)>0:
            x = q.pop(0)
            sortedList.append(x)
            for y in self.__graph.parseOut(x):
                count[y] = count[y] - 1
                if count[y] == 0:
                    q.append(y)      
        if len(sortedList) < self.__graph.getNumberOfVertices():
            sortedList = None
        return sortedList
    
    def fillTimeInfo(self):
        order = self.tSorting()
        for v in order:
            inbound = self.__graph.parseIn(v)
            start = 0
            for x in inbound:
                if x.getEEnd() > start:
                    start = x.getEEnd()
            v.setEarliest(start)        
        order.reverse()
        for x in order:
            end = order[0].getEStart()
            outbound = self.__graph.parseOut(x)
            for y in outbound:
                if y.getLStart() < end:
                    end = y.getLStart()
            x.setLatest(end)  
        self.__total = order[0].getEEnd()
            
    def findCritical(self):
        lst = []
        for v in self.__graph.getVertices():
            if v.getEStart() == v.getLStart() and v.getDuration()!= 0:
                lst.append(v)
        return lst
        
    def findLatest(self):
        order = self.tSorting()
        latest = order[0]
        for v in order:
            if v.getEEnd() > max.getEEnd():
                latest = v
        return latest

    def printEdges(self):
        for x in self.__graph.getVertices():
            for y in self.__graph.getVertices():
                if self.__graph.isEdge(x, y):
                    print("(",x.getID(),",",y.getID(),")")
    def start(self):
        lst = self.tSorting()
        if lst == None:
            print("\tThe graph is not a DAG.")
        else:
            print("\tThe graph is a DAG.")
            print("The activity list sorted in topological order: .")
            for v in lst:
                if v.getDuration() != 0:
                    print("Activity ",v.getID())
        self.fillTimeInfo()
        print("\n\tStarting times")
        for i in self.tSorting():
            if i.getDuration() != 0:
                print("\nActivity ",i.getID())
                print("Eariest start: ",i.getEStart())
                print("Latest start: ",i.getLStart())
        print("Total time: ", self.__total)
        print("\n\tCritical activities")
        for v in self.findCritical():
            print("Activity ",v.getID())
ui = UI()
ui.start()

