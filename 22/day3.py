f = open('day3.txt')
lines= f.readlines()
f.close()

def getPriority(char):
    if char.isupper():
        return (ord(char) - 38)
    else:
        return (ord(char) - 96)

def solution_1(lines):
    priority_sum = 0

    for line in lines:
        length = len(line)//2
        s1 = set(line[:length])
        s2 = set(line[length:])
        priority_sum += getPriority(list(s1.intersection(s2))[0])

    return priority_sum

def solution_2(lines):
    priority_sum = 0
    s1 = set()
    s2 = set()
    s3 = set()

    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '')
        if i%3 == 0:
            s1 = set(lines[i])
        elif i%3 == 1:
            s2 = set(lines[i])
        elif i%3 == 2:
            s3 = set(lines[i])
            priority_sum += getPriority(list(s1.intersection(s2).intersection(s3))[0])

    return priority_sum

print("Solution 1:", solution_1(lines))
print("Solution 2:", solution_2(lines))