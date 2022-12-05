def openFile(filename):
    '''Takes in a string containing a file name,
    returns an array of the lines of the file.'''
    f = open(filename)
    lines = f.readlines()
    f.close()

    return lines

def solution(lines, part2):
    '''Takes in a string containing the lines of the file representing the
    calories and whether or not it is part2, returns the highest or top 3
    highest calories.'''
    current = 0
    top = [0, 0, 0]

    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '')

        # Still in the same group of ints
        if lines[i]:
            current += int(lines[i])
        # Empty line representing end of the group
        else:
            if top[0] < current:
                top[2], top[1], top[0] = top[1], top[0], current
            elif top[1] < current:
                top[2], top[1] = top[1], current
            elif top[2] < current:
                top[2] = current
            current = 0

    if not part2:
        return  top[0]
    else:
        return (top[0] + top[1] + top[2])

f = openFile('day1.txt')

print("Solution 1:", solution(f, False))
print("Solution 2:", solution(f, True))