import node

class branch:

    branchLen = 0 #Length of branch between nodes
    branchConnected = False #False if branch is not connected to 2 nodes, True if it is
    branchN1 = None #First node connected
    branchN2 = None #Second node connected
    
    def __init__(self, n1, n2):
        self.branchN1 = n1
        self.branchN2 = n2
        self.branchLen = n1.getDistance(n2)
        self.branchConnected = True
    
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

    #Return if branch is fully connected
    def getConnect(self):
        return self.branchConnected

    def __str__(self):
        result = "Branch: " + str(self.branchLen)
        return result
    

#Debug
def main():
    testNode = node.node(1,2,3)
    t2 = node.node(5,5,6)
    t3 = node.node(7,8,9)
    testNode.addNode(t2)
    testNode.addNode(t3)
    #print(testNode)
    #print(testNode.getDistance(t2))

    testBranch = branch(testNode, t2)
    print(testBranch.branchLen)

if __name__ == '__main__': #if running node
    main()