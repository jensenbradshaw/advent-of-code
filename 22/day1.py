f = open('day1.txt')
lines = f.readlines()

current_calories = 0
highest_calories = 0
second_highest_calories = 0
third_highest_calories = 0
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')
    if lines[i]:
        current_calories += int(lines[i])
    else:
        if highest_calories < current_calories:
            third_highest_calories = second_highest_calories
            second_highest_calories = highest_calories
            highest_calories = current_calories
        elif second_highest_calories < current_calories:
            third_highest_calories = second_highest_calories
            second_highest_calories = current_calories
        elif third_highest_calories < current_calories:
            third_highest_calories = current_calories
        current_calories=0

print("Part 1 Solution:", highest_calories)
print("Part 2 Solution:", highest_calories + second_highest_calories + third_highest_calories)