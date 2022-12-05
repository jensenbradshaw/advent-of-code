import re

def openFile(filename):
    '''Takes in a string containing a file name,
    returns an array of the lines of the file.'''
    f = open(filename)
    lines = f.readlines()
    f.close()

    return lines

def solution(games, scores, part2):
    '''Takes in a string containing the lines of the file representing the
    games, a dictionary containing scoring and whether or not it is part2,
    returns the score.'''
    score = 0

    for game in games:
        game = re.split(' |\n', game)[0:2]
        score += scores[game[1]]

        if not part2:
            if ((game[0] == 'A' and game[1] == 'Y') or
                (game[0] == 'B' and game[1] == 'Z') or
                (game[0] == 'C' and game[1] == 'X')):
                score += 6
            elif scores[game[0]] == scores[game[1]]:
                score += 3
        else:
            if game[1] == 'X':
                move = scores[game[0]] - 1
                if move == 0:
                    move = 3
                score += move
            elif game[1] == 'Y':
                score += scores[game[0]]
            elif game[1] == 'Z':
                move = scores[game[0]] + 1
                if move == 4:
                    move = 1
                score += move

    return score

f = openFile('day2.txt')
scores_1 = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
scores_2 = {"A": 1, "B": 2, "C": 3, "X": 0, "Y": 3, "Z": 6}

print("Solution 1:", solution(f, scores_1, False))
print("Solution 2:", solution(f, scores_2, True))