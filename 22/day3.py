f = open('day3.txt')
lines= f.readlines()
f.close()

priority_sum = 0

for line in lines:
    line = line.replace('\n', '')
    comp1 = line[:(len(line)//2)]
    comp2 = line[(len(line)//2):]

    for char in comp2:
        if char in comp1:
            if char.isupper():
                priority_sum += (ord(char) - 38)
            else:
                priority_sum += (ord(char) - 96)
            break

print("Solution 1:", priority_sum)