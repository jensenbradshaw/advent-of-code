f = open("../data/day3.txt")
lines = f.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

# PART 1

gamma_rate = ""
epsilon_rate = ""

for i in range(len(lines[0])):
    zero_count = 0
    one_count = 0
    for j in range(len(lines)):
        if lines[j][i] == "0":
            zero_count += 1
        else:
            one_count += 1
    if zero_count >= one_count:
        gamma_rate += "0"
        epsilon_rate += "1"
    else:
        gamma_rate += "1"
        epsilon_rate += "0"
        
gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)
power_consumption = gamma_rate * epsilon_rate
print(power_consumption)

# PART 2

i = 0
oxygen = lines

while len(oxygen) != 1:
    zero_count = 0
    one_count = 0
    zero_list = []
    one_list = []
    for j in range(len(oxygen)):
        if oxygen[j][i] == "0":
            zero_count += 1
            zero_list.append(oxygen[j])
        else:
            one_count += 1
            one_list.append(oxygen[j])
    if zero_count > one_count:
        oxygen = zero_list
    else:
        oxygen = one_list
    i += 1
    
i = 0
co2 = lines

while len(co2) != 1:
    zero_count = 0
    one_count = 0
    zero_list = []
    one_list = []
    
    for j in range(len(co2)):
        if co2[j][i] == "0":
            zero_count += 1
            zero_list.append(co2[j])
        else:
            one_count += 1
            one_list.append(co2[j])
            
    if zero_count > one_count:
        co2 = one_list
    else:
        co2 = zero_list
    i += 1

oxygen = int(oxygen[0], 2)
co2 = int(co2[0], 2)
life_support_rating = oxygen * co2
print(life_support_rating)

f.close()
