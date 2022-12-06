f = open("day2.txt")
lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

valid = 0
for i in range(len(lines)):
    count = -1
    if lines[i][1] == "-":
        minc = int(lines[i][0])
        if lines[i][3] == " ":
            maxc = int(lines[i][2])
            letter = lines[i][4]
        else:
            maxc = int(lines[i][2:4])
            letter = lines[i][5]
    else:
        minc = int(lines[i][0:2])
        maxc = int(lines[i][3:5])
        letter = lines[i][6]
            
    for j in range(len(lines[i])):
        if lines[i][j] == letter:
            count += 1
    if count >= minc and count <= maxc:
        valid += 1

print(valid)

valid = 0
for i in range(len(lines)):
    
    if lines[i][1] == "-":
        if lines[i][3] == " ":
            posa = int(lines[i][0]) + 6
            posb = int(lines[i][2]) + 6
            letter = lines[i][4]
        else:
            posa = int(lines[i][0]) + 7
            posb = int(lines[i][2:4]) + 7
            letter = lines[i][5]
    else:
        posa = int(lines[i][0:2]) + 8
        posb = int(lines[i][3:5]) + 8
        letter = lines[i][6]
            
    if (lines[i][posa] == letter) ^ (lines[i][posb] == letter):
        valid += 1

print(valid)