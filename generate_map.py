from queue import Queue
import random
import json

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

#Global Variables
outputFile = "C:/COP4934-Group10/Everglades/config/RandomMap.json"

size = 7
nodeDensityWeight = 1.5
nodeCreatedWeight = 0.5
nodeFailedWeight = 0.5
fortressWeight = 0.3
watchtowerWeight = 0.7

directionX = [0, 1, 1, 1, 0, -1, -1, -1]
directionY = [1, 1, 0, -1, -1, -1, 0, 1]

map = [[0 for x in range(size)] for y in range(size)]

#Generate Base Map
def GenerateBaseMap():
    queue = Queue()

    startingPoint = Point()
    startingPoint.x = int(size/2)

    map[startingPoint.x][startingPoint.y] = 1

    queue.put(startingPoint)

    while not queue.empty():
        currentPoint = queue.get()
        numPossibleConnections = 8

        i = 0
        while i < 8:
           if currentPoint.x + directionX[i] < 0 or currentPoint.x + directionX[i] >= size or currentPoint.y + directionY[i] < 0 or currentPoint.y + directionY[i] >= int(size/2) or map[currentPoint.x + directionX[i]][currentPoint.y + directionY[i]] != 0:
               numPossibleConnections = numPossibleConnections - 1
           i = i + 1

        if numPossibleConnections == 0:
            continue
        
        weight = nodeDensityWeight/numPossibleConnections

        offset = int(random.uniform(0, size - 1))

        i = 0
        while i < 8:
            if currentPoint.x + directionX[(i + offset)%8] < 0 or currentPoint.x + directionX[(i + offset)%8] >= size or currentPoint.y + directionY[(i + offset)%8] < 0 or currentPoint.y + directionY[(i + offset)%8] >= int(size/2):
                a = 0
                #Do Nothing
            elif map[currentPoint.x + directionX[(i + offset)%8]][currentPoint.y + directionY[(i + offset)%8]] == 0:
                testValue = random.random()

                if testValue <= weight:
                    testValue2 = random.random()

                    if testValue2 < fortressWeight:
                        map[currentPoint.x + directionX[(i + offset)%8]][currentPoint.y + directionY[(i + offset)%8]] = 2
                    elif testValue2 > watchtowerWeight:
                        map[currentPoint.x + directionX[(i + offset)%8]][currentPoint.y + directionY[(i + offset)%8]] = 3
                    else:
                        map[currentPoint.x + directionX[(i + offset)%8]][currentPoint.y + directionY[(i + offset)%8]] = 1
                        
                    newPoint = Point()
                    newPoint.x = currentPoint.x + directionX[(i + offset)%8]
                    newPoint.y = currentPoint.y + directionY[(i + offset)%8]
                    queue.put(newPoint)
                    weight = weight - (nodeCreatedWeight/numPossibleConnections)
                    if weight < 0:
                        weight = 0
                else:
                    map[currentPoint.x + directionX[(i + offset)%8]][currentPoint.y + directionY[(i + offset)%8]] = -1

                    weight = weight + (nodeCreatedWeight/numPossibleConnections) * 2
                    if weight > 1:
                        weight = 1
            i = i + 1

    #Fill in leftover 0s as -1s
    i = 0
    while i < int(size/2):
        j = 0
        while j < size:
            if map[j][i] == 0:
                map[j][i] = -1
            j = j + 1
        i = i + 1

    #Mirror map to opposite side
    i = 0
    while i < size:
        j = 0
        while j < int(size/2):
            map[i][size - 1 - j] = map[i][j]
            j = j + 1
        i = i + 1

    GenerateCenterLine()
    return;

#Generate Center Line
def GenerateCenterLine():
    numNodes = 0
    weight = ((nodeDensityWeight + 2)/8)
    offset = int(random.uniform(0, size - 1))

    i = 0
    while i < size:
        currentPoint = Point()
        currentPoint.x = (i + offset)%size
        currentPoint.y = int(size/2)

        hasConnection = False
        j = 0
        while j < 8:
            if currentPoint.x + directionX[j] >= 0 and currentPoint.x + directionX[j] < size and currentPoint.y + directionY[j] >= 0 and currentPoint.y + directionY[j] < size and map[currentPoint.x + directionX[j]][currentPoint.y + directionY[j]] > 0:
                hasConnection = True
                break
            j = j + 1

        testValue = random.random()

        if hasConnection and testValue <= weight:
            map[(i + offset)%size][int(size/2)] = 1;
            weight = weight - nodeCreatedWeight/size
            if weight < 0:
                weight = 0
            numNodes = numNodes + 1
        else:
            map[(i + offset)%size][int(size/2)] = -1;
            weight = weight + nodeFailedWeight/size
            if weight > 1:
                weight = 1
        i = i + 1

    if numNodes < 2:
        GenerateBaseMap()
    return;

#Generate Json File
def GenerateJsonFile():
    jsonData = {}
    nodes = []

    i = 0
    while i < size:
        j = 0
        while j < size:
            if map[i][j] > 0:
                tmp_node = {}
                connections = []

                curNodeId = ((i) * size) + j + 1
                k = 0
                while k < 8:
                    if j + directionX[k] >= 0 and j + directionX[k] < size and i + directionY[k] >= 0 and i + directionY[k] < size and map[i + directionY[k]][j + directionX[k]] > 0:
                        conNodeId = ((i + directionY[k]) * size) + j + directionX[k] + 1

                        tmp_conn = {}
                        tmp_conn["ConnectedID"] = conNodeId
                        tmp_conn["Distance"] = 5
                        connections.append(tmp_conn)
                    k = k + 1
                    
                tmp_node["Connections"] = connections
                tmp_node["ControlPoints"] = 500
                tmp_node["ID"] = curNodeId
                tmp_node["Radius"] = 1

                if map[i][j] == 2:
                    tmp_node["Resource"] = "DEFENSE"
                elif map[i][j] == 3:
                    tmp_node["Resource"] = "OBSERVE"
                else:
                    tmp_node["Resource"] = ""
                
                tmp_node["StructureDefense"] = 1

                if i == int(size/2) and j == 0:
                    tmp_node["TeamStart"] = 1
                elif i == int(size/2) and j == size-1:
                    tmp_node["TeamStart"] = 2
                else:
                    tmp_node["TeamStart"] = 0
                    
                nodes.append(tmp_node)
            j = j + 1
        i = i + 1

    jsonData["__type"] = "Map:#Everglades_MapJSONDef"
    jsonData["MapName"] = "Random"
    jsonData["nodes"] = nodes

    with open(outputFile, 'w', encoding='utf-8') as f:
              json.dump(jsonData, f, ensure_ascii=False, indent=4)

#Main
GenerateBaseMap()
GenerateJsonFile()

for x in map:
    print(*x, sep=" ")
