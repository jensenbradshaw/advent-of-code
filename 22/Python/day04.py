import re

def openFile(filename):
    '''Takes in a string containing a file name,
    returns an array of the lines of the file.'''
    f = open(filename)
    lines = f.readlines()
    f.close()

    return lines

def solution(lines, part2):
    '''Takes in a string containing the lines of the file representing the
    pairs, returns the sum of which pairs contain one another.'''
    contain_sum = 0

    for line in lines:
        ranges = re.split('-|\n|,', line)[0:4]

        for i in range(len(ranges)):
            ranges[i] = int(ranges[i])

        if not part2:
            if ((ranges[0] <= ranges[2] and ranges[1] >= ranges[3]) or
                (ranges[2] <= ranges[0] and ranges[3] >= ranges[1])):
                contain_sum += 1    
        else:
            if ((ranges[2] <= ranges[0] <= ranges[3]) or
                (ranges[2] <= ranges[1] <= ranges[3]) or
                (ranges[0] <= ranges[2] <= ranges[1]) or
                (ranges[0] <= ranges[3] <= ranges[1])):
                contain_sum += 1

    return contain_sum

f = openFile('day4.txt')

print("Solution 1:", solution(f, False))
print("Solution 2:", solution(f, True))