def openFile(filename):
    '''Takes in a string containing a file name, returns an array of the lines
    of the file.'''
    f = open(filename)
    lines = f.readlines()
    f.close()

    return lines

def parseFile(lines):
    monkeys = []
    monkey = -1
    for line in lines:
        if line.index(line) % 7 == 6:
            pass
        # Monkey number
        elif lines.index(line) % 7 == 0:
            monkeys.append({})
            monkey += 1
        # Starting items
        elif lines.index(line) % 7 == 1:
            monkeys[monkey]["Items"] = []
            for item in line[17:].strip().split(', '):
                monkeys[monkey]["Items"].append(int(item))
        # Operation
        elif lines.index(line) % 7 == 2:
            monkeys[monkey]["Operation"] = line[18:].strip()
        # Test
        elif lines.index(line) % 7 == 3:
            monkeys[monkey]["Test"] = int(line.split()[3])
        # True
        elif lines.index(line) % 7 == 4:
            monkeys[monkey]["True"] = int(line.split()[5])
        # False
        elif lines.index(line) % 7 == 5:
            monkeys[monkey]["False"] = int(line.split()[5])

    return monkeys

def solution(lines, part2):
    
    monkeys = parseFile(lines)
    inspection_total = [0 for monkey in monkeys]
    var = 1
    for monkey in monkeys:
        var *= monkey["Test"]

    rounds = 10000 if part2 else 20

    for x in range(rounds):
        for monkey in monkeys:
            for i in range(len(monkey["Items"])):
                inspection_total[monkeys.index(monkey)] += 1
                old = monkey["Items"][0]
                new = eval(monkey["Operation"])
                if not part2:
                    new = new // 3
                    append_item = new
                else:
                    append_item = new % var
                if new % monkey["Test"] == 0:
                    monkeys[monkey["True"]]["Items"].append(append_item)
                else:
                    monkeys[monkey["False"]]["Items"].append(append_item)
                monkey["Items"].remove(old)

    inspection_total.sort()
    monkey_business = inspection_total[-1] * inspection_total[-2]

    return monkey_business

f = openFile('day11.txt')

print("Solution 1:", solution(f, False))
print("Solution 2:", solution(f, True))