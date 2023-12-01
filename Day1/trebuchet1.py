with open('input.txt') as i:
    val = i.read().splitlines()

def revVals(input):
    revDigits = []
    for v in val:
        y = v[::-1]
        for x in y:
            try:
                x == int(x)
                break
            except Exception as e:
                pass
        revDigits.append(x)
    return revDigits


def getDig(input):
    digits = []
    for v in val:
        for x in v:
            try:
                x == int(x)
                break
            except Exception as e:
                pass
        digits.append(x)
    return digits

firstNum = getDig(val)
lastNum = revVals(val)


combined = zip(firstNum,lastNum)
#print(list(combined))

def joinNums(combined):
    combinedList = []
    for c in list(combined):
        y = c[0]+c[1]
        y = int(y)
        combinedList.append(y)
    return combinedList

combinedList = joinNums(combined)

print(combinedList)
print(sum(combinedList))