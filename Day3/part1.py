'''
1. Create 3 lists: above, target, below, characters
2. Find numbers on target
3. Plot start and finish of number and surrounding spaces
4. Evaluate and add or skip
5. Move to next target line
'''
import re
import string

### 1. Create 3 lists: above, target, below
# Open up input and create target list
with open('input.txt') as t:
    target = t.read().splitlines()

# determine length of list item
size = len(target[0])

# create above and below lists
above = target.copy()
above.pop()
above.insert(0, size * '.')
below = target.copy()
below.pop(0)
below.append(size * '.')

# Find what punctuation is included in the input but remove '.'
def findPuncs(target):
    puncList = []
    for t in target:
        for c in t:
            if c == '.':
                pass
            else:
                if (c in string.punctuation): puncList.append(c)
    puncList = list(set(puncList))
    return puncList

puncList = findPuncs(target)

#print(above)
#print(target)
#print(below)
#print(puncList)


### Step 1 complete

### 2. Find numbers on target
def findNums(above, target, below):
    # create blank list to dump valid numbers into
    aggValidNums = []
    x = 0
    # look at each line of the input
    for t in target:
        # create blank dictionary to store information about found numbers
        numInfo = {}
        # use regex to find all numbers in a line
        nums = re.findall(r'\d+', t)
        # if numbers are found then do the following
        if nums != []:
            # build numInfo for each specific number found
            for n in nums:
                numInfo['nums'] = nums
                # find the location of the number on the line
                # this is necessary if a number and pattern repeats itself
                realLoc = valLocation(n, t, puncList)
                # if realLoc comes back as None than the number is the string[0]
                if realLoc == None:
                    loc = t.index(n)
                # else register the location
                else:
                    loc = int(realLoc)
                length = len(n)
                # complete the numInfo dictionary
                numInfo[n] = {'lineNum': x, 'location': loc, 'length': length}
            # insert the numInfo into our plot function, valid numbers are returned
            validNums = plotNums(numInfo)
            print(validNums)
            # append valid numbers found to our aggregate valid number list
            for v in validNums:
                aggValidNums.append(v)
        else:
            pass
        # increment the line number by 1 and continue the process
        x += 1
    return aggValidNums



def plotNums(numInfo):
    # create a list to track numbers that are next to symbols and thus valid
    validParts = []
    # assign variables to make handling easier below
    for n in numInfo['nums']:
        lineNum = numInfo[n]['lineNum']
        location = numInfo[n]['location']
        length = numInfo[n]['length']
        # compare above, target, and below strings based on the placement
        # return and provide better descriptions on what is happening below...
        if lineNum > len(target) - 1:
            aString = above[lineNum][location - 1:location + length + 1]
            tString = target[lineNum][location - 1:location + length + 1]
            bString = below[lineNum][location - 1:location + length + 1]
        else:
            # if the number is the first item in the string do the following
            if numInfo[n]['location'] == 0:
                aString = above[lineNum][0:length + 1]
#                tString = target[lineNum][length:length + 1]
                tString = target[lineNum][0:length + 1]
                bString = below[lineNum][0:length + 1]
            # else consider the location
            else:
                aString = above[lineNum][location-1:location + length+1]
                tString = target[lineNum][location-1:location + length+1]
                bString = below[lineNum][location-1:location + length+1]
        #        print(above[lineNum])
                #print(aString)
                #print(tString)
                #print(bString)
        #print(puncList)
        # iterate through the above, target, and below strings
        # if punctation is found add the number to the valid parts list
        for p in puncList:
            if p in aString:
                validParts.append(int(n))
                break
            elif p in tString:
                validParts.append(int(n))
                break
            elif p in bString:
                validParts.append(int(n))
                break
    return validParts

def valLocation(n, t, puncList):
    # copy the punctuation list and add '.'
    checkPuncList = puncList.copy()
    checkPuncList.append('.')
    # use the below to ensure you are looking at the correct number in case of duplicates
    # see if you can find the punctuation + string
    for c in checkPuncList:
        tLoc = t.find(c + str(n))
        if tLoc == -1:
            pass
        elif tLoc == 0:
            return tLoc
        # if you do, see if you can find punctuation after the string as well
        else:
            for d in checkPuncList:
                endLoc = t.find(c + str(n) + d)
                if endLoc == -1:
                    pass
                else:
                    return endLoc + 1

aggValidNums = findNums(above, target, below)

print(len(aggValidNums))
print(sum(aggValidNums))
