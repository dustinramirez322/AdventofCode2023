numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# Combine words and integers
combinedVals = numbers + digits

# Map words to their integer value
valConvert = dict.fromkeys(numbers)
for key, value in zip(valConvert.keys(), digits):
    valConvert[key] = value

# Yank input into a list
with open('input.txt') as i:
    val = i.read().splitlines()

def findRightNums(val):
    # find position of all numbers in each line of input
    lineItem = []
    for v in val:
        position = {}
        lastPosition = {}
        # find first value
        for c in combinedVals:
            num = v.find(c)
            # Ignore if value is not found (equals -1)
            if num == -1:
                pass
            # Add where the number was found to a dictionary
            else:
                position[num] = c
        startNum = min(position)
        first = position[startNum]
        #find last value
        for c in combinedVals:
            num = v.rfind(c)
            # Ignore if value is not found (equals -1)
            if num == -1:
                pass
            # Add where the number was found to a dictionary
            else:
                lastPosition[num] = c
        endNum = max(lastPosition)
        last = lastPosition[endNum]

        # Convert value if it is a word
        if len(first) > 1:
            firstConv = valConvert[first]
        else:
            firstConv = first
        if len(last) > 1:
            lastConv = valConvert[last]
        else:
            lastConv = last

        # Combine first and last numbers then convert to integers
        lineItem.append(int(firstConv + lastConv))
    return lineItem

position = findRightNums(val)
print(sum(position))