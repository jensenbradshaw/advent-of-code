def openFile(filename):
    '''Takes in a string containing a file name,
    returns an array of the lines of the file.'''
    f = open(filename)
    lines = f.readlines()
    f.close()

    return lines

def getPriority(char):
    '''Takes in a character, returns the priority value.'''
    if char.isupper():
        return (ord(char) - 38)
    else:
        return (ord(char) - 96)

def solution(lines, part2):
    '''Takes in a string containing the lines of the file representing the
    rucksacks, returns the sum of common items's priority.'''
    priority_sum = 0

    if not part2:
        for line in lines:
            length = len(line)//2
            s1 = set(line[:length])
            s2 = set(line[length:])
            common = list(s1.intersection(s2))[0]
            priority_sum += getPriority(common)
    else:
        for i in range(len(lines)):
            lines[i] = lines[i].replace('\n', '')

            if i%3 == 0:
                s1 = set(lines[i])
            elif i%3 == 1:
                s2 = set(lines[i])
            elif i%3 == 2:
                s3 = set(lines[i])
                common = list(s1.intersection(s2).intersection(s3))[0]
                priority_sum += getPriority(common)

    return priority_sum

f = openFile('day3.txt')

print("Solution 1:", solution(f, False))
print("Solution 2:", solution(f, True))