f = open("day4.txt")
lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')

# PART 1

call_order = lines[0]
lines = lines[1:]
call_order = [int(i) for i in call_order.split(',')]
cards = list()
card = ''
card_lines = 0

for i in range(len(lines)):
    if i % 6 == 0:
        continue
    else:
        card += lines[i] + ' ' 
        card_lines += 1
        if card_lines == 5:
            cards.append(card)
            card = ''
            card_lines = 0

for i in range(len(cards)):
    cards[i] = [int(j) for j in cards[i].split()]

bingo = False
for i in range(len(call_order)):
    for j in range(len(cards)):
        for k in range(len(cards[0])):
            if cards[j][k] == call_order[i]:
                cards[j][k] = 'X'
                if  cards[j][0] == 'X' and cards[j][1] == 'X' and cards[j][2] == 'X' and cards[j][3] == 'X' and cards[j][4] == 'X':
                    bingo = True
                    num_sum = 0
                    for num in cards[j]:
                        if num != 'X':
                            num_sum += num
                    print('bingo!!!! answer:', str(num_sum * call_order[i]))
                    break
                elif cards[j][5] == 'X' and cards[j][6] == 'X' and cards[j][7] == 'X' and cards[j][8] == 'X' and cards[j][9] == 'X':
                    bingo = True
                    num_sum = 0
                    for num in cards[j]:
                        if num != 'X':
                            num_sum += num
                    print('bingo!!!! answer:', str(num_sum * call_order[i]))
                    break
                elif cards[j][10] == 'X' and cards[j][11] == 'X' and cards[j][12] == 'X' and cards[j][13] == 'X' and cards[j][14] == 'X':
                    bingo = True
                    num_sum = 0
                    for num in cards[j]:
                        if num != 'X':
                            num_sum += num
                    print('bingo!!!! answer:', str(num_sum * call_order[i]))
                    break
                elif cards[j][15] == 'X' and cards[j][16] == 'X' and cards[j][17] == 'X' and cards[j][18] == 'X' and cards[j][19] == 'X':
                    bingo = True
                    num_sum = 0
                    for num in cards[j]:
                        if num != 'X':
                            num_sum += num
                    print('bingo!!!! answer:', str(num_sum * call_order[i]))
                    break
                elif cards[j][20] == 'X' and cards[j][21] == 'X' and cards[j][22] == 'X' and cards[j][23] == 'X' and cards[j][24] == 'X':
                    bingo = True
                    num_sum = 0
                    for num in cards[j]:
                        if num != 'X':
                            num_sum += num
                    print('bingo!!!! answer:', str(num_sum * call_order[i]))
                    break
                elif cards[j][0] == 'X' and cards[j][5] == 'X' and cards[j][10] == 'X' and cards[j][15] == 'X' and cards[j][20] == 'X':
                    bingo = True
                    num_sum = 0
                    for num in cards[j]:
                        if num != 'X':
                            num_sum += num
                    print('bingo!!!! answer:', str(num_sum * call_order[i]))
                    break
                elif cards[j][1] == 'X' and cards[j][6] == 'X' and cards[j][11] == 'X' and cards[j][16] == 'X' and cards[j][21] == 'X':
                    bingo = True
                    num_sum = 0
                    for num in cards[j]:
                        if num != 'X':
                            num_sum += num
                    print('bingo!!!! answer:', str(num_sum * call_order[i]))
                    break
                elif cards[j][2] == 'X' and cards[j][7] == 'X' and cards[j][12] == 'X' and cards[j][17] == 'X' and cards[j][22] == 'X':
                    bingo = True
                    num_sum = 0
                    for num in cards[j]:
                        if num != 'X':
                            num_sum += num
                    print('bingo!!!! answer:', str(num_sum * call_order[i]))
                    break
                elif cards[j][3] == 'X' and cards[j][8] == 'X' and cards[j][13] == 'X' and cards[j][18] == 'X' and cards[j][23] == 'X':
                    bingo = True
                    num_sum = 0
                    for num in cards[j]:
                        if num != 'X':
                            num_sum += num
                    print('bingo!!!! answer:', str(num_sum * call_order[i]))
                    break
                elif cards[j][4] == 'X' and cards[j][9] == 'X' and cards[j][14] == 'X' and cards[j][19] == 'X' and cards[j][24] == 'X':
                    bingo = True
                    num_sum = 0
                    for num in cards[j]:
                        if num != 'X':
                            num_sum += num
                    print('bingo!!!! answer:', str(num_sum * call_order[i]))
                    break
        if bingo == True:
            break
    if bingo == True:
        break

# PART 2

bingo = False
for i in range(len(call_order)):
    for j in range(len(cards)):
        for k in range(len(cards[0])):
            if cards[j][k] == call_order[i]:
                cards[j][k] = 'X'
                if  cards[j][0] == 'X' and cards[j][1] == 'X' and cards[j][2] == 'X' and cards[j][3] == 'X' and cards[j][4] == 'X':
                    bingo = True
                    num_sum = 0
                    for l in range(len(cards[j])):
                        if cards[j][l] != 'X':
                            num_sum += cards[j][l]
                        cards[j][l] = 'Y'
                    print('bingo!!!! answer:', str(num_sum * call_order[i]))
                    break
                elif cards[j][5] == 'X' and cards[j][6] == 'X' and cards[j][7] == 'X' and cards[j][8] == 'X' and cards[j][9] == 'X':
                    bingo = True
                    num_sum = 0
                    for l in range(len(cards[j])):
                        if cards[j][l] != 'X':
                            num_sum += cards[j][l]
                        cards[j][l] = 'Y'
                    print('bingo!!!! answer:', str(num_sum * call_order[i]))
                    break
                elif cards[j][10] == 'X' and cards[j][11] == 'X' and cards[j][12] == 'X' and cards[j][13] == 'X' and cards[j][14] == 'X':
                    bingo = True
                    num_sum = 0
                    for l in range(len(cards[j])):
                        if cards[j][l] != 'X':
                            num_sum += cards[j][l]
                        cards[j][l] = 'Y'
                    print('bingo!!!! answer:', str(num_sum * call_order[i]))
                    break
                elif cards[j][15] == 'X' and cards[j][16] == 'X' and cards[j][17] == 'X' and cards[j][18] == 'X' and cards[j][19] == 'X':
                    bingo = True
                    num_sum = 0
                    for l in range(len(cards[j])):
                        if cards[j][l] != 'X':
                            num_sum += cards[j][l]
                        cards[j][l] = 'Y'
                    print('bingo!!!! answer:', str(num_sum * call_order[i]))
                    break
                elif cards[j][20] == 'X' and cards[j][21] == 'X' and cards[j][22] == 'X' and cards[j][23] == 'X' and cards[j][24] == 'X':
                    bingo = True
                    num_sum = 0
                    for l in range(len(cards[j])):
                        if cards[j][l] != 'X':
                            num_sum += cards[j][l]
                        cards[j][l] = 'Y'
                    print('bingo!!!! answer:', str(num_sum * call_order[i]))
                    break
                elif cards[j][0] == 'X' and cards[j][5] == 'X' and cards[j][10] == 'X' and cards[j][15] == 'X' and cards[j][20] == 'X':
                    bingo = True
                    num_sum = 0
                    for l in range(len(cards[j])):
                        if cards[j][l] != 'X':
                            num_sum += cards[j][l]
                        cards[j][l] = 'Y'
                    print('bingo!!!! answer:', str(num_sum * call_order[i]))
                    break
                elif cards[j][1] == 'X' and cards[j][6] == 'X' and cards[j][11] == 'X' and cards[j][16] == 'X' and cards[j][21] == 'X':
                    bingo = True
                    num_sum = 0
                    for l in range(len(cards[j])):
                        if cards[j][l] != 'X':
                            num_sum += cards[j][l]
                        cards[j][l] = 'Y'
                    print('bingo!!!! answer:', str(num_sum * call_order[i]))
                    break
                elif cards[j][2] == 'X' and cards[j][7] == 'X' and cards[j][12] == 'X' and cards[j][17] == 'X' and cards[j][22] == 'X':
                    bingo = True
                    num_sum = 0
                    for l in range(len(cards[j])):
                        if cards[j][l] != 'X':
                            num_sum += cards[j][l]
                        cards[j][l] = 'Y'
                    print('bingo!!!! answer:', str(num_sum * call_order[i]))
                    break
                elif cards[j][3] == 'X' and cards[j][8] == 'X' and cards[j][13] == 'X' and cards[j][18] == 'X' and cards[j][23] == 'X':
                    bingo = True
                    num_sum = 0
                    for l in range(len(cards[j])):
                        if cards[j][l] != 'X':
                            num_sum += cards[j][l]
                        cards[j][l] = 'Y'
                    print('bingo!!!! answer:', str(num_sum * call_order[i]))
                    break
                elif cards[j][4] == 'X' and cards[j][9] == 'X' and cards[j][14] == 'X' and cards[j][19] == 'X' and cards[j][24] == 'X':
                    bingo = True
                    num_sum = 0
                    for l in range(len(cards[j])):
                        if cards[j][l] != 'X':
                            num_sum += cards[j][l]
                        cards[j][l] = 'Y'
                    print('bingo!!!! answer:', str(num_sum * call_order[i]))
                    break

f.close()
