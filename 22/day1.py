f = open('day1.txt')
lines = f.readlines()

currentCalories = 0
highestCalories = 0
secondHighestCalories = 0
thirdHighestCalories = 0
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')
    if lines[i]:
        currentCalories += int(lines[i])
    else:
        if highestCalories < currentCalories:
            thirdHighestCalories = secondHighestCalories
            secondHighestCalories = highestCalories
            highestCalories = currentCalories
        elif secondHighestCalories < currentCalories:
            thirdHighestCalories = secondHighestCalories
            secondHighestCalories = currentCalories
        elif thirdHighestCalories < currentCalories:
            thirdHighestCalories = currentCalories
        currentCalories=0

print("Part 1 Solution:", highestCalories)
print("Part 2 Solution:", highestCalories + secondHighestCalories + thirdHighestCalories)