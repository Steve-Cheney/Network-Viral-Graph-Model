# Network-Viral-Graph-Model

#### A viral model for depicting network connectivity.

This model uses a virus-like traversing algorithm that connects nodes to a starting node.

### node
##### Contains the following methods attributes:

    xCoord = 0 #X coordinate of the node
    yCoord = 0 #Y coordinate of the node
    beneficialCoE = 0 #Beneficial Coefficient determines healthiness of the node to the virus
    visitedBool = False #Whether or not the node has been visited already
    numVisits = 0 #How many times the node has been visited
    nodeList = [] #List of directly connected nodes
    nodeBranches = [] #List of all individual branches connected to a node
    nodeBranchTuples = [] #List of branches with each node name in a tuple
    nodeName = '' #Name of the node
    nodeHealth = 1.0 #Health of the node; 1.0 is fully healthy, 0.0 is destroyed
    nodeDepreciation = 1.0 #Rate at which the node should depreciate until it is destroyed
    bceDepreciation = 1.0 #Rate at which the Beneficial CoE should depreciate until it is destroy
    
    
### branch
##### Contains the following methods attributes:

    branchLen = 0 #Length of branch between nodes
    branchConnected = False #False if branch is not connected to 2 nodes, True if it is
    branchN1 = None #First node connected
    branchN2 = None #Second node connected
    branchStart = None #Starting coords in tuple form
    branchEnd = None #Ending coords in tuple form
    

### virus
##### Contains the following methods attributes:

    numNodes = None #Number of nodes in connected graph
    maxX = 0 #Max X value of the coordinate grid
    maxY = 0 #Max Y value of the coordinate grid
    nodeList = [] #List of all nodes in virus
    maxBranchDistance = 0 #Maximum distance that a node can branch to
    startNode = None #The node at which the virus model starts
    virusBCE = 0.2 #The Beneficial Coefficient limit. If the node is less than this value, it will not get connected to the graph
    usedCoords = [] #List of coords where nodes already exist
    virusBranches = [] #List of all branches in the virus (unique)
    virusBranchTuples = [] #List of tuples of all branch node name pairs (nodeNameA, nodeNameB)
