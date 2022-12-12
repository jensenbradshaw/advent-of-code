f = open('day1.txt')
lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        if int(lines[i]) + int(lines[j]) == 2020:
            output = int(lines[i]) * int(lines[j])

print(output)

f.close()