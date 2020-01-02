from queue import Queue
import random

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

#Global Variables
size = 7
nodeDensityWeight = 1.5
nodeCreatedWeight = 0.5
nodeFailedWeight = 0.5

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
            if currentPoint.x + directionX[j] >= 0 and currentPoint.x + directionX[j] < size and currentPoint.y + directionY[j] >= 0 and currentPoint.y + directionY[j] < size and map[currentPoint.x + directionX[j]][currentPoint.y + directionY[j]] == 1:
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

#Main
GenerateBaseMap()

for x in map:
    print(*x, sep=" ")
