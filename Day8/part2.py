'''
1. Ingest directions and input
2. Convert input into dictionary
3. Identify all startings points
4. Take first step with all starting points
5. Increment count
6. Create a list of all next/current steps of all starting points
7. Check to see if all items current step list ends in 'Z'
8. If not, wipe list and repeat until all do.
9. Return count
'''

with open('input.txt') as t:
    map = t.read().splitlines()

with open('directions.txt') as t:
    steps = t.read()
    directions = ([*steps])

def mapToDict(map):
    mapDict = {}
    for m in map:
        mapKey = m.split('=')[0].strip()
        mapVal = m.split('=')[1].strip().strip('()').split(',')
        mapDict[mapKey] = (mapVal[0], mapVal[1])
    return mapDict

def getStartPoints(map):
    startingPoints = []
    for m in map:
        if m.split('=')[0].strip().endswith('A'):
            startingPoints.append(m.split('=')[0].strip())
        else:
            pass
    return startingPoints

def getEndPoints(map):
    endPoints = []
    for m in map:
        if m.split('=')[0].strip().endswith('Z'):
            endPoints.append(m.split('=')[0].strip())
        else:
            pass
    return endPoints

startingPoints = getStartPoints(map)
endPoints = getEndPoints(map)
mapDict = mapToDict(map)

def findNextKey(mapDict, directions, startingPoint, dirCount=0):
    line = mapDict[startingPoint]
    if directions[dirCount] == 'L':
        startingPoint = line[0].strip()
    elif directions[dirCount] == 'R':
        startingPoint = line[1].strip()
    return(startingPoint)

def ghostSteps(startingPoints, directions, mapDict, dirCount=0):
    count = 0
    evalSteps = False
    while evalSteps == False:
        resetDir = len(directions)
        if dirCount == resetDir:
            dirCount = 0
        currentStep = []
        for s in startingPoints:
            nextStep = findNextKey(mapDict, directions, s, dirCount)
            currentStep.append(nextStep)
        count += 1
        dirCount += 1
        startingPoints = currentStep.copy()
        evalSteps = evalCurrentStep(currentStep)
        if evalSteps == True:
            print(currentStep)
            print(count)
            break


def evalCurrentStep(currentStep):
    count = 0
    for c in currentStep:
        if c.endswith('Z'):
            count += 1
        else:
            pass
    if count == len(startingPoints):
        return True
    else:
        return False

ghostSteps(startingPoints, directions, mapDict)