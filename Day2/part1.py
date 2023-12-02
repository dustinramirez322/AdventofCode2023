with open('input.txt') as t:
    vals = t.read().splitlines()

colors = ['red', 'green', 'blue']
colorsDict = {'red': 12, 'green': 13, 'blue': 14}
maxRed = 12
maxGreen = 13
maxBlue = 14

def regPoss(vals):
    possGames = []
    for v in vals:
        # Register game number so that it can be added to a list
        gameNum = int(v.split(':')[0].split('Game ')[1])
        # Split out the game number so that we can just look at the game rounds
        for game in v.split(':')[1:]:
            # split out individual rounds
            games = game.split(';')
            # Look at individual rounds
            gameResults = []
            for g in games:
                # Remove all spaces
                colorsShown = g.replace(' ', '').split(',')
                # Set l to zero so that we can iterate over our list
                l = 0
                roundResults = []
                while l < len(colors):
                    # Look at each color
                    for c in colorsShown:
                        # find a color and amount that is in our list
                        if colors[l] in c:
                            # remove the color and convert the number to an integer
                            num = int(c.split(colors[l])[0])
                            # Check to see if the integer is higher or lower than our max
                            # Add a True or False to a roundResults list
                            if num > colorsDict[colors[l]]:
                                roundResults.append(False)
                            else:
                                roundResults.append(True)
                    # Add one to iterate over the next color
                    l = l+1
                # if a round was impossible mark the game False
                if False in roundResults:
                    gameResults.append(False)
                # else if all rounds were possible mark the game True
                elif True in roundResults:
                    gameResults.append(True)
        # if a game is False skip it, otherwise add its game number to the possible games list
        if False in gameResults:
            pass
        else:
            possGames.append(gameNum)
    return possGames


possGames = regPoss(vals)

print(sum(possGames))

