f = open("day5.txt")
lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '').replace(' -> ', ',')
    lines[i] = lines[i].split(',')
    for j in range(len(lines[i])):
        lines[i][j] = int(lines[i][j])

row = [0] * 1000
field = []
for i in range(1000):
    field.append(row.copy())

for i in range(len(lines)):
    
    if lines[i][0] < lines[i][2]:
        x1 = lines[i][0]
        x2 = lines[i][2]
    else:
        x1 = lines[i][2]
        x2 = lines[i][0]
        
    if lines[i][1] < lines[i][3]:
        y1 = lines[i][1]
        y2 = lines[i][3]
    else:
        y1 = lines[i][3]
        y2 = lines[i][1]
        
    if x1 == x2:
        for j in range(y2-y1+1):
            field[y1+j][x1] += 1
    elif y1 == y2:
        for j in range(x2-x1+1):
            field[y1][x1+j] += 1

count = 0
for i in range(len(field)):
    for j in range(len(field[i])):
        if field[i][j] > 1:
            count += 1
print(count)

