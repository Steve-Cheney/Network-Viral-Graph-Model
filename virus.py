import node as no
import branch as br
import numpy as np
import random
from random import randrange

#Helper functions for Node naming
#Increment an uppercase character, returning 'A' if 'Z' is given
def increment_char(c):    
    return chr(ord(c) + 1) if c != 'Z' else 'A'
#Increment the string of Alpha characters; I.E. A->B, Z->AA, AZ->BA
def increment_str(s):
    lpart = s.rstrip('Z')
    num_replacements = len(s) - len(lpart)
    new_s = lpart[:-1] + increment_char(lpart[-1]) if lpart else 'A'
    new_s += 'A' * num_replacements
    return new_s

class virus:
    numNodes = None
    maxX = 0
    maxY = 0
    nodeList = []
    maxBranchDistance = 0
    startNode = None
    virusBCE = 0.2
    usedCoords = []
    
    #Init function
    def __init__(self, numNodes, maxX, maxY):
        self.numNodes = numNodes
        self.maxX = maxX
        self.maxY = maxY
       
        #Create random Nodes with function params
        #Does not repeat coords
        char = 'A' #start of Node labeling
        for i in range(numNodes):
            if len(self.usedCoords) == maxX * maxY: #if amount of nodes created == max nodes possible, break out of creating nodes
                break
            randX = randrange(maxX)
            randY = randrange(maxY)
            coordTuple = (randX,randY)
            while coordTuple in self.usedCoords:
                randX = randrange(maxX)
                randY = randrange(maxY)
                coordTuple = (randX,randY)
            self.usedCoords.append(coordTuple)
                
            randBCE = random.uniform(0,1)
            
            #Set name of Node; format Node### where # is a letter from A to Z
            name = "Node_" + char
            char = increment_str(char) #increment identifier by one letter
            node = no.node(name,randX,randY,randBCE) #create new node
            self.nodeList.append(node) #add the node to the virus system

    #Set max branch distance
    def setMaxBranchDist(self, val):
        assert(type(val) is int),"Error: value must be int"
        self.maxBranchDistance = val
    
    #Set starting node
    def setStartNode(self, n: no):
        #assert(type(n) is no),"Error: starting node must be a node object"
        self.startNode = n
    
    #Get starting node
    def getStartNode(self):
        return self.startNode

    #Get virus BCE limit
    def getBCELimit(self):
        return self.virusBCE

    #Get max branch distance
    def getmaxBranchDist(self):
        return self.maxBranchDistance

    #Get all nodes in virus
    def getNodes(self):
        return self.nodeList

    #Search for a node by name in the virus and return it
    def getNodeByName(self, name):
        for each in self.nodeList:
            if each.getNodeName() == name:
                return each
        print("Node not found")
        return None

    #Search for a node by name in the virus and return it
    def getNodeByCoords(self, x, y):
        for each in self.nodeList:
            if each.getX() == x:
                if each.getY() == y:
                    return each
        print("Node not found")
        return None

    #Check via a Node whether or not 2 nodes are connected in a virus
    def checkIfNodeConnected_Node(self,n1: no, n2: no):
        return n1.nodeConnected_Node(n2)
    
    #Check via a Node Name whether or not 2 nodes are connected in a virus
    def checkIfNodeConnected_Name(self,n1: str,n2: str):
        return n1.nodeConnected_Name(n2)

    #Return the list of nodes in the virus. Returns node Name, X, Y coordinates
    def getNodeListShort(self):
        result = ""
        for each in self.nodeList:
            result += each.strXY() + '\n'
        return result

    #Return the list of nodes in the virus. Returns node Name, X, Y coordinates, BCE, and connected nodes
    def getNodeListLong(self):
        result = ""
        for each in self.nodeList:
            result += str(each) + '\n'
        return result
    
    #Set Beneficial Coefficient Limit
    def setBCELimit(self, BCE):
        assert(type(BCE) is float),"Error: BCE must be float"
        self.virusBCE = BCE

    #Connect nodes
    #Specify a starting node
    #Specify max distance for a connection and the beneficial CoE threshhold - determines if a connection should be made if benedicial enough
    def connectNodes(self, startNode, maxDist):
        self.setStartNode(startNode)
        sn = self.getStartNode()
        self.setMaxBranchDist(maxDist)
        md = self.getmaxBranchDist()

        currNodes = self.getNodes()
        connectedNodes = []
        if sn.getNodeHealth() < 0.01:
            return

        for node in currNodes:
            if node == sn:
                continue
            if sn.nodeConnected_Node(node): #if node is already connected, skip to next node
                continue
            if node.getBCE() > self.getBCELimit(): #if node is less than the beneficial CoE limit, do not branch nodes 
                if sn.getDistance(node) <= md: #if node is more than the distance limit, do not branch nodes
                    sn.addNode(node) #Branch nodes if all params are satisfied
                    connectedNodes.append(node)
        return connectedNodes

    def runVirus(self,startNode, maxDist):
        out = self.connectNodes(startNode,maxDist)
        for each in out:
            self.runVirus(each, maxDist)

    #Print a grid of all nodes in the virus
    def printGrid(self):
        out = ""
        for col in range(self.maxX):
            for row in range(self.maxY):
                if tuple((col,row)) in self.usedCoords:
                    out += " " + self.getNodeByCoords(col, row).getNodeName().partition('_')[2] + " "
                else:
                    out += ' . '
            out += '\n'
        return out

    #Print a grid of all nodes in the virus, denoteing if a node is connected to a branch with *
    def printGridBranch(self):
        out = ""
        for col in range(self.maxX):
            for row in range(self.maxY):
                if tuple((col,row)) in self.usedCoords:
                    node = self.getNodeByCoords(col, row)
                    if node.getNodeCount() > 0:
                        out += " " + node.getNodeName().partition('_')[2] + "*"
                    else:    
                        out += " " + node.getNodeName().partition('_')[2] + " "
                else:
                    out += ' . '
            out += '\n'
        return out


#Run main 
def main():
    #do something
    testV = virus(15, 20, 20)
    print('Running Virus. . .')
    #print(testV.getNodeListShort())
    #print(testV.getNodeListLong())
    #print(testV.checkIfNodeConnected_Name(testV.getNodeByName('NodeA'),testV.getNodeByName('NodeB')))
    node1 = testV.getNodeByName('Node_A')
    #node1.addNode(testV.getNodeByName('NodeB'))
    #print(node1)
    #print(testV.checkIfNodeConnected_Node(node1,testV.getNodeByName('NodeB')))
    #print(type(node1))
    testV.runVirus(node1, 10)
    print(testV.getNodeListShort())
    print(testV.getNodeListLong())
    print(testV.printGrid())
    print(testV.printGridBranch())
if __name__ == '__main__': #if running virus
    main()