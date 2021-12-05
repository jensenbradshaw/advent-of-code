f = open("day2.txt")
lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

# PART 1

position = 0
depth = 0

for i in range(len(lines)):
    if "down" in lines[i]:
        depth += int(lines[i][5:])
    elif "up" in lines[i]:
        depth -= int(lines[i][3:])
    else:
        position += int(lines[i][8:])
        
output = position * depth
print(output)

# PART 2

position = 0
depth = 0
aim = 0

for i in range(len(lines)):
    if "down" in lines[i]:
        aim += int(lines[i][5:])
    elif "up" in lines[i]:
        aim -= int(lines[i][3:])
    else:
        position += int(lines[i][8:])
        depth += int(lines[i][8:]) * aim
        
output = position * depth
print(output)

f.close()
