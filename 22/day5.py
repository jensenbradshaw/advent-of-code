import re

def openFile(filename):
    '''Takes in a string containing a file name,
    returns an array of the lines of the file.'''
    f = open(filename)
    lines = f.readlines()
    f.close()

    return lines

def getStacks(lines):
    '''Takes in a string containing the lines of the file representing the
    stacks, returns a 2d array representing the stacks.'''
    stacks = [[] for i in range(9)]

    for line in lines[:8]:
        for i in range(len(line)):
            if (line[i] != ' ' and line[i] != '[' and
                line[i] != ']' and line[i] != '\n'):
                stacks[(i-1)//4].append(line[i])

    for i in range(len(stacks)):
        stacks[i] = stacks[i][::-1]
    
    return stacks

def solution(moves, stacks, part2):
    '''Takes in a string containing the lines of the file representing the
    moves, a 2d array representing the stacks and whether or not it is part2,
    returns a string containing the solution.'''
    for move in moves:
        move = re.split('move | from | to |\n', move)
        amount, box1, box2 = int(move[1]), int(move[2]) - 1, int(move[3]) - 1

        if not part2:
            for i in range(amount):
                stacks[box2].append(stacks[box1].pop(-1))
        else:
            for i in range(amount, 0, -1):
                stacks[box2].append(stacks[box1].pop(-i))

    answer = ''
    for stack in stacks:
        answer += stack[-1]

    return answer

f = openFile('day5.txt')
stacks, moves = f[:9], f[10:]

print("Solution 1:", solution(moves, getStacks(stacks), False))
print("Solution 2:", solution(moves, getStacks(stacks), True))