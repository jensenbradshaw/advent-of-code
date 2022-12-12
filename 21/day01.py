f = open('day1.txt')
lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

# PART 1

previous_depth = 0
increase_count = 0

for i in range(len(lines)):
    if i > 0:
        if int(lines[i]) > previous_depth:
            increase_count += 1
        previous_depth = int(lines[i])
    else:
        previous_depth = int(lines[i])

print(increase_count)

# PART 2

previous_depth_sum = 0
increase_count = 0

for i in range(len(lines)-2):
    depth_sum = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
    if i > 0:
        if depth_sum > previous_depth_sum:
            increase_count += 1
    previous_depth_sum = depth_sum

print(increase_count)

f.close()
