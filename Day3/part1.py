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
print(puncList)


### Step 1 complete

### 2. Find numbers on target
def findNums(above, target, below):
    aggValidNums = []
    x = 0
    for t in target:
        numInfo = {}
        nums = re.findall(r'\d+', t)
        if nums != []:
            for n in nums:
                numInfo['nums'] = nums
                loc = t.index(n)
                length = len(n)
                numInfo[n] = {'lineNum': x, 'location': loc, 'length': length}
#            print(nums)
            validNums = plotNums(numInfo)
            print(validNums)
            for v in validNums:
                aggValidNums.append(v)
        else:
            pass
        x += 1
    return aggValidNums


# Example numInfo
# {'467': {'lineNum': 0, 'location': 0, 'length': 3}, '114': {'lineNum': 0, 'location': 5, 'length': 3}}
def plotNums(numInfo):
    validParts = []
    for n in numInfo['nums']:
#        print(n)
#        print(numInfo[n])
        lineNum = numInfo[n]['lineNum']
        location = numInfo[n]['location']
        length = numInfo[n]['length']
        if lineNum > len(target) - 1:
            aString = above[lineNum][location - 1:location + length + 1]
            tString = target[lineNum][location - 1:location + length + 1]
            bString = below[lineNum][location - 1:location + length + 1]
        else:
            if numInfo[n]['location'] == 0:
                aString = above[lineNum][0:length + 1]
                tString = target[lineNum][length:length + 1]
                bString = below[lineNum][0:length + 1]
            else:
                aString = above[lineNum][location-1:location + length+1]
                tString = target[lineNum][location-1:location + length+1]
                bString = below[lineNum][location-1:location + length+1]
        #        print(above[lineNum])
#                print(aString)
#                print(tString)
#                print(bString)
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

aggValidNums = findNums(above, target, below)

print(sum(aggValidNums))
