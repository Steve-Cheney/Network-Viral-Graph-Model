#Author: Stephen Cheney

#node class

import branch as br
import math

class node:

    xCoord = 0 #X coordinate of the node
    yCoord = 0 # Y coordinate of the node
    beneficialCoE = 0 #Beneficial Coefficient determines healthiness of the node to the virus
    visitedBool = False #Whether or not the node has been visited already
    numVisits = 0 #How many times the node has been visited
    nodeList = [] #List of directly connected nodes
    nodeBranches = [] #List of all individual branches connected to a node
    nodeBranchTuples = [] #List of branches with each node name in a tuple
    nodeName = '' #Name of the node
    nodeHealth = 1.0 #Health of the node; 1.0 is fully healthy, 0.0 is destroyed
    nodeDepreciation = 1.0 #Rate at which the node should depreciate until it is destroyed
    bceDepreciation = 1.0 #Rate at which the Beneficial CoE should depreciate until it is destroyed

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

    #Get the list of branches in string format
    def getBranches_str(self):
        result = 'Branches:\n'
        for each in self.nodeBranches:
            result += str(each) + '\n'
        return result

    #Get the list of branches
    def getBranches(self):
        for each in self.nodeBranches:
            print("Branches: " + str(each))
        return self.nodeBranches

    #Get the health of the node
    def getNodeHealth(self):
        return self.nodeHealth
    
    #Get the depreciation value of the node
    def getNodeDepreciation(self):
        return self.nodeDepreciation

    #Get the BCE Depreciation rate of the node
    def getBCEDepreciation(self):
        return self.bceDepreciation

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
    
    #Set the depreciation value of the node
    def setNodeDepreciation(self, val):
        assert(type(val) is float),"Error: value must be float"
        self.nodeDepreciation = val

    #Set the BCE depreciation value of the node
    def setBCEDepreciation(self, val):
        assert(type(val) is float),"Error: value must be float"
        self.bceDepreciation = val

    #Depreciate the health of the Node by the Depreciation rate
    #When a node's health < 0.01 it is destroyed
    def nodeDepreciate(self):
        self.nodeHealth = self.nodeHealth * self.getNodeDepreciation()


    #Add a node to the connected node list; only immediately connected nodes
    def addNode(self, N):
        assert(type(N) is node),"Error: added object is not a node"
        self.nodeList.append(N)
        if (((self.getNodeName(), N.getNodeName())) in self.nodeBranchTuples) or (((N.getNodeName(),self.getNodeName())) in self.nodeBranchTuples):
            return
        else:
            print("Adding branch between " + N.getNodeName() + " & " + self.getNodeName())
            self.nodeBranches.append(br.branch(self,N))
            self.nodeBranchTuples.append(((self.getNodeName(), N.getNodeName())))
    
    #Check if 2 nodes are connected by a branch; checks full node
    def nodeConnected_Node(self, n2):
        if n2 in self.getNodeList():
            return True
        else:
            return False

    #Check if 2 nodes are connected by a branch; checks by node name
    def nodeConnected_Name(self, name):
        for each in self.getNodeList():
            if name == each.getNodeName():
                return True
        return False

    
    def __str__(self):
        result = "---------Node---------\n" +  self.getNodeName() + "\nX coord:"+ str(self.getX())+ "\nY coord:"+ str(self.getY())+ "\nBeneficial CoE:"+ str(self.getBCE())+ "\nConnected Nodes:  X  Y  Distance  BCE\n"
        index = 0
        for each in self.getNodeList():
            result += "          " + each.strXY() + "  " + str(each.nodeBranches[index].getLen()) + "      " + str(each.getBCE()) +"\n"
            index += 1
        return result

    def strXY(self):
        result = self.getNodeName() + ": " + str(self.getX()) + ", " + str(self.getY())# + ", " + str(self.getBCE()) 
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
    #print(testNode.getBranches())
    print(testNode.nodeBranchTuples)

if __name__ == '__main__': #if running node
    main()
    