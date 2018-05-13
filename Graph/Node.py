'''
Created on May 10, 2018

@author: ema
'''

class Node:
    '''
    classdocs
    '''

    def __init__(self, ID, duration):
        '''
        Constructor
        '''
        self.__id = ID
        self.__duration = duration
        self.__eStart = -1
        self.__eEnd = -1   
        self.__lStart = -1
        self.__lEnd = -1     
        
    def __eq__(self,other):
        if not isinstance(other, Node):
            return False
        return self.__id == other.__id
    
    def __hash__(self):
        return self.__id
        
    def getID(self):
        return self.__id
    
    def setEarliest(self, eStart):
        self.__eStart = eStart
        self.__eEnd = eStart + self.__duration
        
    def setLatest(self, lEnd):
        self.__lStart = lEnd - self.__duration
        self.__lEnd = lEnd
        
    def setDuration(self, d):
        self.__duration = d
    
    def getDuration(self):
        return self.__duration
    
    def getEStart(self):
        return self.__eStart
    
    def getEEnd(self):
        return self.__eEnd
    
    def getLStart(self):
        return self.__lStart

    def getLEnd(self):
        return self.__lEnd
    
    def isCritical(self):
        return self.__eStart == self.__lStart
    
    