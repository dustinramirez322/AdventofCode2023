'''
1. bring in input and split int a list
  2. find ascii value of first character
  3. multiply value by 17
  4. return remainder of value/256
  5. add to next ascii value of second character...
6. End total is added to list
7. Return sum of list
'''

#1. bring in input
with open('input.txt') as t:
    input = t.read().split(',')

totalVal = []

def algoHASH(input, val = 0):
    asciiVal = ord(input)
    updatedVal = asciiVal + val
    mul17Val = updatedVal * 17
    remVal = mul17Val % 256
    return remVal

test = ['H', 'A', 'S', 'H']

x = 0
def listAdder(input):
    for i in input:
        x = 0
        toHASH = ([*i])
        for t in toHASH:
            length = len(toHASH) - 1
            if x == 0:
                val = 0
                remVal = algoHASH(t)
                x += 1
            elif x == length:
                val = remVal
                remVal = algoHASH(t, val)
                totalVal.append(remVal)
                x += 1
            else:
                val = remVal
                remVal = algoHASH(t, val)
                x += 1


'''
for t in test:
    length = len(test) - 1
    if x==0:
        val = 0
        remVal = algoHASH(t)
        x += 1
    elif x == length:
        val = remVal
        remVal = algoHASH(t, val)
        totalVal.append(remVal)
        x += 1
    else:
        val = remVal
        remVal = algoHASH(t, val)
        x += 1

print(totalVal)'''

answer = listAdder(input)
print(sum(totalVal))

