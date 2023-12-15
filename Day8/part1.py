'''
1. Ingest directions and input
2. Convert input into dictionary
3. Start at AAA and reference directions to find next key
4. Take next step and increment counter by 1
5. Repeat
6. View count
'''
# 1. Ingest directions and input
with open('input.txt') as t:
    map = t.read().splitlines()

with open('directions.txt') as t:
    steps = t.read()
    directions = ([*steps])


# 2. Convert map input into a dictionary
def mapToDict(map):
    mapDict = {}
    for m in map:
        mapKey = m.split('=')[0].strip()
        mapVal = m.split('=')[1].strip().strip('()').split(',')
        mapDict[mapKey] = (mapVal[0], mapVal[1])
    return mapDict

# 3/4/5. Start at AAA and find next key
def findNextKey(mapDict, directions, startingPoint, count=0, dirCount=0):
    while startingPoint != 'ZZZ':
        try:
            line = mapDict[startingPoint]
            if directions[dirCount] == 'L':
                startingPoint = line[0].strip()
            elif directions[dirCount] == 'R':
                startingPoint = line[1].strip()
            count = count + 1
            dirCount = dirCount + 1
        except IndexError:
            dirCount = 0
            if directions[dirCount] == 'L':
                startingPoint = line[0].strip()
            elif directions[dirCount] == 'R':
                startingPoint = line[1].strip()
            count = count + 1
            dirCount = dirCount + 1
    print(count)


startingPoint = 'AAA'
mapDict = mapToDict(map)
findNextKey(mapDict, directions, startingPoint)
print(mapDict)
