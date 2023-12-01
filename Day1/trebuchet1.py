# Yank input into a list
with open('input.txt') as i:
    val = i.read().splitlines()

# Reverse input to find the last integer
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


# Find the first integer
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

# Use the above functions to get lists of all first and last integers
firstNum = getDig(val)
lastNum = revVals(val)

# Combine the two lists using zip
combined = zip(firstNum,lastNum)

# Join the first and last integers for all line items in input
def joinNums(combined):
    combinedList = []
    for c in list(combined):
        y = c[0]+c[1]
        y = int(y)
        combinedList.append(y)
    return combinedList

# Create the combined list and print the total sum
combinedList = joinNums(combined)
print(sum(combinedList))