import re

f = open('day2.txt')
lines = f.readlines()
f.close()
scores_1 = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
scores_2 = {"A": 1, "B": 2, "C": 3, "X": 0, "Y": 3, "Z": 6}

def solution_1(games, moves):
    score = 0
    for game in games:
        game = re.split(' |\n', game)[0:2]
        score += moves[game[1]]
        if (game[0] == "A" and game[1] == "Y") or (game[0] == "B" and game[1] == "Z") or (game[0] == "C" and game[1] == "X"):
            score += 6
        elif moves[game[0]] == moves[game[1]]:
            score += 3
        else:
            score += 0
    return score

def solution_2(games, scores):
    score = 0
    for game in games:
        game = re.split(' |\n', game)[0:2]
        score += scores[game[1]]
        match game[1]:
            case "X":
                move = scores[game[0]] - 1
                if move == 0:
                    move = 3
                score += move
            case "Y":
                score += scores[game[0]]
            case "Z":
                move = scores[game[0]] + 1
                if move == 4:
                    move = 1
                score += move
    return score

print("Solution 1:", solution_1(lines, scores_1))
print("Solution 2:", solution_2(lines, scores_2))