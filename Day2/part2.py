with open('input.txt') as t:
    vals = t.read().splitlines()

colors = ['red', 'green', 'blue']
colorsDict = {'red': 12, 'green': 13, 'blue': 14}
maxRed = 12
maxGreen = 13
maxBlue = 14

def regMin(vals):
    gameProds = []
    for v in vals:
        # Split out the game number so that we can just look at the game rounds
        for game in v.split(':')[1:]:
            # split out individual rounds
            games = game.split(';')
            # Look at individual rounds
            gameResults = []
            redList = []
            greenList = []
            blueList = []
            for g in games:
                # Remove all spaces
                colorsShown = g.replace(' ', '').split(',')
                for c in colorsShown:
                    # find a color and amount that is in our list
                    # add individual color numbers to a corresponding list
                    if colors[0] in c:
                        num = int(c.split('red')[0])
                        redList.append(num)
                    if colors[1] in c:
                        num = int(c.split('green')[0])
                        greenList.append(num)
                    if colors[2] in c:
                        num = int(c.split('blue')[0])
                        blueList.append(num)
            # get the product of the highest number per color
            gameProduct = findProduct(redList,greenList, blueList)
            # append that product to the game Prods list
            gameProds.append(gameProduct)
    # Return a list of all products per game so they can be summed
    return gameProds

def findProduct(redList, greenList, blueList):
    maxRed = max(redList)
    maxGreen = max(greenList)
    maxBlue = max(blueList)
    product = maxRed * maxGreen * maxBlue
    return product

gameProds = regMin(vals)
print(gameProds)
print(sum(gameProds))