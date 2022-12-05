import re

def openFile(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    return lines

def getStacks(lines):
    stack_num = 0

    for char in lines[8]:
        if char != ' ' and char != '\n':
            stack_num += 1

    stacks = [[] for i in range(9)]

    for line in lines[:8]:
        for i in range(len(line)):
            if line[i] != ' ' and line[i] != '[' and line[i] != ']' and line[i] != '\n':
                stacks[(i-1)//4].append(line[i])

    for i in range(len(stacks)):
        stacks[i] = stacks[i][::-1]
    
    return stacks

def solution(moves, stacks, part2):
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
print("Solution 1:", solution(f[10:], getStacks(f[:9]), False))
print("Solution 2:", solution(f[10:], getStacks(f[:9]), True))