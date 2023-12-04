'''
1. Separate winning numbers lucky numbers to two lists
2. Search for winning numbers in lucky numbers and get a count
3. Double the count and add to a list
4. Sum the list
'''

import re

with open('input.txt') as t:
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

# 3. Double wins
def doubWins(wins):
    if wins == 0:
        pass
    elif wins == 1:
        return 1
    else:
        answer = (1*(2**wins))/2
        answer = int(answer)
        return answer


# 4. Sum the list
points = segNums(lottery)
print(sum(points))