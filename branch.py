import node as n

class branch:

    branchLen = 0 #Length of branch between nodes
    branchConnected = False #False if branch is not connected to 2 nodes, True if it is
    branchN1 = None #First node connected
    branchN2 = None #Second node connected
    branchStart = None #Starting coords in tuple form
    branchEnd = None #Ending coords in tuple form
    
    #Init function
    #Sets branch between 2 nodes
    def __init__(self, n1, n2):
        self.branchN1 = n1
        self.branchN2 = n2
        self.branchLen = round(n1.getDistance(n2),3)
        self.branchConnected = True
        self.branchStart = ((n1.getX(),n1.getY()))
        self.branchStart = ((n2.getX(),n2.getY()))

    ### Getters ###
    #Return length of branch
    def getLen(self):
        return self.branchLen
    
    #Return node 1
    def getN1(self):
        return self.branchN1

    #Return node 2
    def getN2(self):
        return self.branchN2

    #Return start coords
    def getStart(self):
        return self.branchStart

    #Return start coords
    def getEnd(self):
        return self.branchEnd

    #Return if branch is connected
    def getConnectionStatus(self):
        return self.branchConnected
    

    def __str__(self):
        return 'Node 1: ' + self.getN1().strXY() + ' || Node 2: ' + self.getN2().strXY() + ' || Distance: ' + str(self.getLen())
        
    

#Debug
def main():
    testNode = n.node('NodeA', 1,2,3)
    t2 = n.node('NodeB', 5,5,6)
    t3 = n.node('NodeC', 7,8,9)
    testNode.addNode(t2)
    testNode.addNode(t3)
    print(testNode)
    print(testNode.getDistance(t2))

    testBranch = branch(testNode, t2)
    print(testBranch.branchLen)
    print(testBranch)

if __name__ == '__main__': #if running branch
    main()