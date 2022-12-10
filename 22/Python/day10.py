def openFile(filename):
    '''Takes in a string containing a file name, returns an array of the lines
    of the file.'''
    f = open(filename)
    lines = f.readlines()
    f.close()

    return lines

def increaseClock(cycles, register_X, signal_sum, screen):
    '''Takes the cycle number, value of register X, current signal sum and
    current state of the screen, returns the increased cycle as well as updated
    signal sum and screen.'''
    cycles += 1

    if (cycles - 20) % 40 == 0:
        signal_sum += cycles * register_X

    if cycles < 41 and (register_X-1 <= cycles-1 <= register_X+1):
        screen[0][cycles-1] = '#'
    elif cycles < 81 and (register_X-1 <= cycles-41 <= register_X+1):
        screen[1][cycles-41] = '#'
    elif cycles < 121 and (register_X-1 <= cycles-81 <= register_X+1):
        screen[2][cycles-81] = '#'
    elif cycles < 161 and (register_X-1 <= cycles-121 <= register_X+1):
        screen[3][cycles-121] = '#'
    elif cycles < 201 and (register_X-1 <= cycles-161 <= register_X+1):
        screen[4][cycles-161] = '#'
    elif cycles < 241 and (register_X-1 <= cycles-201 <= register_X+1):
        screen[5][cycles-201] = '#'

    return cycles, signal_sum, screen

def solution(lines):
    '''Takes an array of CPU operations and tracks the register X value and
    clock cycle, returns the display screen and the sum of the signal every 40th
    cycle from 20 cycles.'''
    register_X = 1
    cycles = 0
    signal_sum = 0
    screen = [['.' for i in range(40)] for i in range(6)]

    for line in lines:
        try:
            instruction, amount = line.split()
        except ValueError:
            instruction = line.split()[0]

        if instruction == 'noop':
            cycles, signal_sum, screen = increaseClock(cycles, register_X, signal_sum, screen)
        elif instruction == 'addx':
            cycles, signal_sum, screen = increaseClock(cycles, register_X, signal_sum, screen)
            cycles, signal_sum, screen = increaseClock(cycles, register_X, signal_sum, screen)
            register_X += int(amount)

    for row in screen:
        output = ""
        for pixel in row:
            output += pixel
        print(output)

    return signal_sum

f = openFile('day10.txt')

print("Solution 2:")
print("Solution 1:", solution(f))