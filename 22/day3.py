f = open('day3.txt')
lines= f.readlines()
f.close()

priority_sum = 0

for line in lines:
    length = len(line)//2
    comp1 = line[:length]
    comp2 = line[length:]

    for char in comp2:
        if char in comp1:
            if char.isupper():
                priority_sum += (ord(char) - 38)
            else:
                priority_sum += (ord(char) - 96)
            break

print("Solution 1:", priority_sum)