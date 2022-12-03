
# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# Your total score is the sum of your scores for each round. 
# The score for a single round is the score for the shape you selected 
# (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round 
# (0 if you lost, 3 if the round was a draw, and 6 if you won).

'''
AX = 0 + 1 + 3 = 4
BX = 0 + 1 + 0 = 1
CX = 0 + 1 + 6 = 7
AY = 0 + 2 + 6 = 8
BY = 0 + 2 + 3 = 5
CY = 0 + 2 + 0 = 2
AZ = 0 + 3 + 0 = 3
BZ = 0 + 3 + 6 = 9
CZ = = + 3 + 3 = 6

BX = 1 = YX
CY = 2 = ZY
AZ = 3 = XZ
AX = 4 = XX
BY = 5 = YY
CZ = 6 = ZZ
CX = 7 = ZX
AY = 8 = XY
BZ = 9 = YZ

'''

def get_score():
    sum = 0
    source = {
        'BX': 1,
        'CY': 2,
        'AZ': 3,
        'AX': 4,
        'BY': 5,
        'CZ': 6,
        'CX': 7,
        'AY': 8,
        'BZ': 9
    }
    with open('input.txt', 'r') as f:
        for line in f:
            # two letters
            sum += source[line[0] + line[2]]
    print(sum)
    return sum


# "Anyway, the second column says how the round needs to end: X means you need to lose, 
# Y means you need to end the round in a draw, and Z means you need to win. Good luck!"
def get_second_score():
    sum = 0
    source = {
        'BX': 1,
        'CY': 2,
        'AZ': 3,
        'AX': 4,
        'BY': 5,
        'CZ': 6,
        'CX': 7,
        'AY': 8,
        'BZ': 9
    }
    
    with open('input.txt', 'r') as f:
        for line in f:
            # two letters
            if (line[2] == 'X'):
                for letter in ['X', 'Y', 'Z']:
                    if source[line[0] + letter] < 4:
                        sum += source[line[0] + letter]
                        
            elif (line[2] == 'Y'):
                for letter in ['X', 'Y', 'Z']:
                    if source[line[0] + letter] >= 4 and source[line[0] + letter] < 7:
                        sum += source[line[0] + letter]
                        
            elif (line[2] == 'Z'):
                for letter in ['X', 'Y', 'Z']:
                    if source[line[0] + letter] > 6:
                        sum += source[line[0] + letter]
    print(sum)
            
get_second_score()