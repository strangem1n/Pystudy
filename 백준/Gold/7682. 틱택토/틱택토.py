import sys

while True:
    tic = sys.stdin.readline().rstrip()
    if tic == 'end':
        break

    cnt_x = cnt_o = cnt_blank = 0
    for i in range(9):
        if tic[i] == 'X':
            cnt_x += 1
        elif tic[i] == 'O':
            cnt_o += 1
        else:
            cnt_blank += 1

    if cnt_o > cnt_x or cnt_x > cnt_o + 1 :
        print('invalid')
        continue

    line_x = line_o = 0
    if tic[0] == tic[1] == tic[2]:
        if tic[0] == 'X':
            line_x += 1
        elif tic[0] == 'O':
            line_o += 1
    if tic[3] == tic[4] == tic[5]:
        if tic[3] == 'X':
            line_x += 1
        elif tic[3] == 'O':
            line_o += 1
    if tic[6] == tic[7] == tic[8]:
        if tic[6] == 'X':
            line_x += 1
        elif tic[6] == 'O':
            line_o += 1


    if tic[0] == tic[3] == tic[6]:
        if tic[0] == 'X':
            line_x += 1
        elif tic[0] == 'O':
            line_o += 1
    if tic[1] == tic[4] == tic[7]:
        if tic[1] == 'X':
            line_x += 1
        elif tic[1] == 'O':
            line_o += 1
    if tic[2] == tic[5] == tic[8]:
        if tic[2] == 'X':
            line_x += 1
        elif tic[2] == 'O':
            line_o += 1


    if tic[0] == tic[4] == tic[8]:
        if tic[0] == 'X':
            line_x += 1
        elif tic[0] == 'O':
            line_o += 1
    if tic[2] == tic[4] == tic[6]:
        if tic[2] == 'X':
            line_x += 1
        elif tic[2] == 'O':
            line_o += 1

    if line_x > 0 and line_o > 0:
        print('invalid')
        continue
    elif line_x > 0:
        if cnt_x == cnt_o:
            print('invalid')
            continue
        if line_x > 1 and cnt_x == line_x * 3:
            print('invalid')
            continue
    elif line_o > 0:
        if cnt_x > cnt_o:
            print('invalid')
            continue
        if line_o > 1 and cnt_o == line_o * 3:
            print('invalid')
            continue
    else:
        if cnt_blank > 0:
            print('invalid')
            continue

    print('valid')
    continue