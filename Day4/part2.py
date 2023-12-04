'''
1. Separate winning numbers lucky numbers to two lists
2. Search for winning numbers in lucky numbers and get a count
3. Determine how many below cards you win
4. Create a dictionary that shows how many of each card you get
   {'Card1': ['wins': 4, 'count': 1], 'Card2': ['wins': 2, 'count': 2],...
5. Pass that multiple down to next card
5. Repeat steps 3/4
4. Sum the list + the original card amount
'''

import re

with open('testInput.txt') as t:
    lottery = t.read().splitlines()

# 1. Separate numbers into lists
def segNums(lottery):
    pointsTotal = []
    for l in lottery:
        card = l.split(':')
        nums = card[1].split('|')
        winningNums = re.findall(r'\d+', nums[0])
        luckyNums = re.findall(r'\d+', nums[1])
        game = [winningNums, luckyNums]
        points = searchNums(game)
        if points == None:
            pass
        else:
            pointsTotal.append(points)
    return pointsTotal

# 2. compare and return amount of wins
def searchNums(game):
    winningNums = game[0]
    luckyNums = game[1]
    matches = set(winningNums) & set(luckyNums)
    if matches == set():
        pass
    else:
        wins = len(matches)
        points = doubWins(wins)
        return points



# 4. Sum the list
#points = segNums(lottery)
#print(sum(points))