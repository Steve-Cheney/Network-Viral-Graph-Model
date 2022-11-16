#Author: Stephen Cheney

#node class

import branch
import math

class node:

    xCoord = 0 #X coordinate of the node
    yCoord = 0 # Y coordinate of the node
    beneficialCoE = 0 #Beneficial Coefficient determines healthiness of the node to the virus
    visitedBool = False #Whether or not the node has been visited already
    numVisits = 0 #How many times the node has been visited
    nodeList = [] #List of directly connected nodes
    nodeBranches = []
    nodeName = ''

    def __init__(self, name, x, y, BCE):
        self.xCoord = x
        self.yCoord = y
        self.beneficialCoE = BCE
        self.nodeList = []
        self.nodeName = name

    ### Getters ###
    #Get node's name
    def getNodeName(self):
        return self.nodeName
    
    #Get X Coordinate
    def getX(self):
        return self.xCoord
    
    #Get Y Coordinate
    def getY(self):
        return self.yCoord

    #Get Beneficial Coefficient
    def getBCE(self):
        return self.beneficialCoE

    #Get num nodes connected
    def getNodeCount(self):
        return len(self.nodeList)

    #Get list of all nodes connected
    def getNodeList(self):
        return self.nodeList

    #Get the distance between 2 nodes
    def getDistance(self, n2):
        assert(type(self) is node),"Error: first object is not a node"
        assert(type(n2) is node),"Error: second object is not a node"
        distance = 0
        n1x = self.getX()
        n1y = self.getY()
        n2x = n2.getX()
        n2y = n2.getY()
        distance = math.sqrt((n2x-n1x)**2 + (n2y-n1y)**2)
        return distance

    def getBranches(self):
        result = 'Branches:\n'
        for each in self.nodeBranches:
            result += str(each) + '\n'
        return result

    ### Setters ###
    #Set X Coordinate
    def setX(self, x):
        assert(type(x) is int),"Error: coordinate must be int"
        self.xCoord = x
    
    #Set Y Coordinate
    def setY(self, y):
        assert(type(y) is int),"Error: coordinate must be int"
        self.yCoord = y

    #Set Beneficial Coefficient
    def setBCE(self, BCE):
        assert(type(BCE) is float),"Error: BCE must be float"
        self.beneficialCoE = BCE
    
    #Add a node to the connected node list; only immediately connected nodes
    def addNode(self, N):
        assert(type(N) is node),"Error: added object is not a node"
        self.nodeList.append(N)
        self.nodeBranches.append(branch.branch(self,N))

    
    def __str__(self):
        result = "---------Node---------\n" +  self.getNodeName() + "\nX coord:"+ str(self.getX())+ "\nY coord:"+ str(self.getY())+ "\nBeneficial CoE:"+ str(self.getBCE())+ "\nConnected Nodes: X  Y  Distance\n"
        index = 0
        for each in self.getNodeList():
            result += "          " + each.strXY() + "  " + str(each.nodeBranches[index].getLen()) +"\n"
            index += 1
        return result

    def strXY(self):
        result = self.getNodeName() + ": " + str(self.getX()) + ", " + str(self.getY())
        return result

#Debug
def main():
    testNode = node('NodeA',1,2,3)
    #print('X:', testNode.getX(),'Y:', testNode.getY(),'BCE:',testNode.getBCE())
    t2 = node('NodeB',5,5,6)
    t3 = node('NodeC',7,8,9)
    testNode.addNode(t2)
    testNode.addNode(t3)
    print(testNode)

    #print(testNode.getDistance(t2))
    print(testNode.strXY())
    print(testNode.getBranches())

if __name__ == '__main__': #if running node
    main()
    