class node:

    xCoord = 0 #X coordinate of the node
    yCoord = 0 # Y coordinate of the node
    beneficialCoE = 0 #Beneficial Coefficient determines healthiness of the node to the virus
    visitedBool = False #Whether or not the node has been visited already
    numVisits = 0 #How many times the node has been visited

    def __init__(self,x, y, BCE):
        self.xCoord = x
        self.yCoord = y
        self.beneficialCoE = BCE

    #Get X Coordinate
    def getX(self):
        return self.xCoord
    
    #Get Y Coordinate
    def getY(self):
        return self.yCoord

    #Get Beneficial Coefficient
    def getBCE(self):
        return self.beneficialCoE


#Debug
def main():
    testNode = node(1,2,3)
    print('X:', testNode.getX(),'Y:', testNode.getY(),'BCE:',testNode.getBCE())

if __name__ == '__main__': #if running node
    main()