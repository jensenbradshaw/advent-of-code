import re

f = open('day4.txt')
lines= f.readlines()
f.close()

def answer(lines, solution):
    contain_sum = 0

    for line in lines:
        ranges = re.split('-|\n|,', line)[0:4]
        for i in range(len(ranges)):
            ranges[i] = int(ranges[i])
        if solution == 1 and ((ranges[0] <= ranges[2] and ranges[1] >= ranges[3]) or (ranges[2] <= ranges[0] and ranges[3] >= ranges[1])):
            contain_sum += 1    
        elif solution == 2 and ((ranges[2] <= ranges[0] <= ranges[3]) or (ranges[2] <= ranges[1] <= ranges[3]) or (ranges[0] <= ranges[2] <= ranges[1]) or (ranges[0] <= ranges[3] <= ranges[1])):
            contain_sum += 1

    return contain_sum

print("Solution 1:", answer(lines, 1))
print("Solution 2:", answer(lines, 2))