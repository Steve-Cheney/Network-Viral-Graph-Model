import node as no
import branch as br
import numpy as np
import random
from random import randrange
import time
import matplotlib.pyplot as plt

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
    virusBranches = []
    virusBranchTuples = []

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
    
    #Get max X
    def getMaxX(self):
        return self.maxX
    
    #Get max Y
    def getMaxY(self):
        return self.maxY

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

    #Get random node in virus
    def getRandNode(self):
        return self.getNodes()[randrange(len(self.getNodes()))]

    #Get virus' branches
    def getVirusBranches(self):
        return self.virusBranches

    #Add branch to virus' branches
    def addVirusBranch(self, branch):
        self.virusBranches.append(branch)

    #Add branch to virus' branches tuples list
    def addVirusBranchTuple(self, branch):
        self.virusBranchTuples.append(branch)

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

        currNodes = self.getNodes()
        connectedNodes = []
        #if startNode.getNodeHealth() < 0.01:
        #    return
        for node in currNodes:
            if node == startNode:
                continue
            if startNode.nodeConnected_Node(node): #if node is already connected, skip to next node
                #print(startNode.getNodeName() + " already connected to " + node.getNodeName())
                continue
            if node.getBCE() > self.getBCELimit(): #if node is less than the beneficial CoE limit, do not branch nodes 
                if startNode.getDistance(node) <= maxDist: #if node is more than the distance limit, do not branch nodes
                    #print("Adding node " + node.getNodeName() + " to " + startNode.getNodeName())
                    startNode.addNode(node) #Branch nodes if all params are satisfied
                    connectedNodes.append(node)
                    if (((startNode.getNodeName(), node.getNodeName())) in self.virusBranchTuples) or (((node.getNodeName(),startNode.getNodeName())) in self.virusBranchTuples):
                        continue
                    else:
                        self.addVirusBranch(startNode.getBranches()[-1])
                        self.addVirusBranchTuple(((startNode.getNodeName(), node.getNodeName())))
                    #print(str(connectedNodes))
        return connectedNodes

    def runVirus(self,startNode, maxDist):
        out = self.connectNodes(startNode,maxDist)
        for each in out:
            self.runVirus(each, maxDist)
    '''
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
                if tuple((row,col)) in self.usedCoords:
                    node = self.getNodeByCoords(row, col)
                    if node.getNodeCount() > 0:
                        out += " " + node.getNodeName().partition('_')[2] + "*"
                    else:    
                        out += " " + node.getNodeName().partition('_')[2] + " "
                else:
                    out += ' . '
            out += '\n'
        return out
    '''
    def plotGraph(self, wait):
        plt.title('Drawing virus . . .')
        plt.rcParams["figure.figsize"] = [30, 30]
        plt.rcParams["figure.autolayout"] = True
        plt.xlabel('X axis')
        plt.ylabel('Y axis')
        x_values = list(map(lambda x: x[0], self.usedCoords))
        y_values = list(map(lambda x: x[1], self.usedCoords))
        plt.xlim(0,self.getMaxX()-1)
        plt.ylim(0,self.getMaxY()-1)
        plt.plot(x_values, y_values, 'bo')
        for each in self.getNodes():
            #plt.text(each.getX()-0.015, each.getY()-0.5, each.getNodeName())   
            plt.text(each.getX()-0.015, each.getY()-0.5, each.getNodeName() + ' BCE: ' + str(round(each.getBCE(),3)))             
        for branch in self.getVirusBranches():
            #print("Plotting Branch: " + str(branch))
            plt.pause(wait)
            #plt.text(branch.getStart()[0]+1, branch.getStart()[1]+1, str('Dist: ' + str(round(branch.getLen()),2)))
            plt.plot([branch.getStart()[0],branch.getEnd()[0]],[branch.getStart()[1],branch.getEnd()[1]], 'ro', linestyle="--")
            #print(branch.getStart()[0])               
             
        plt.title('Done')
        plt.pause(1.5)
        plt.title('Viral Model for Beneficial Connections')
        plt.show()

#Run main 
def main():
    #do something
    testV = virus(40, 100, 100)
    testV.setBCELimit(0.5)
    print('Running Virus. . .')
    print(testV.getNodeListShort())
    testV.runVirus(testV.getRandNode(), 33)    
    testV.plotGraph(0.1)
    
if __name__ == '__main__': #if running virus
    main()