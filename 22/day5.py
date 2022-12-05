import re

f = open('day5.txt')
lines= f.readlines()
f.close()

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

def copy2dArray(old):
    new = []

    for i in range(0, len(old)):
        new.append([])
        for j in range(0, len(old[i])):
            new[i].append([])

    for i in range(0, len(old)):
        for j in range(0, len(old[i])):
            new[i][j] = old[i][j]

    return new

def solution_1(stacks):
    for line in lines[10:]:
        line = re.split('move | from | to |\n', line)
        amount = int(line[1])
        box1 = int(line[2]) - 1
        box2 = int(line[3]) - 1

        for i in range(amount):
            stacks[box2].append(stacks[box1].pop(-1))

    answer = ''
    for stack in stacks:
        answer += stack[-1]

    return answer

def solution_2(stacks):
    for line in lines[10:]:
        line = re.split('move | from | to |\n', line)
        amount = int(line[1])
        box1 = int(line[2]) - 1
        box2 = int(line[3]) - 1

        for i in range(amount, 0, -1):
            stacks[box2].append(stacks[box1].pop(-i))

    answer = ''
    for stack in stacks:
        answer += stack[-1]

    return answer

stacks1 = getStacks(lines)
stacks2 = copy2dArray(stacks1)

print("Solution 1:", solution_1(stacks1))
print("Solution 2:", solution_2(stacks2))