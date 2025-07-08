import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a, b, initial, goal = input().split()
    a = int(float(a) * 1000)
    b = int(float(b) * 1000)
    goal = int(float(goal) * 1000)
    min_cnt = 6

    if initial == 'A':
        current = a
        for cnt in range(6):
            if current == goal:
                if min_cnt > cnt:
                    min_cnt = cnt
                break
            current += 20
            if current > 146000:
                current = 144000

        current = a
        for cnt in range(6):
            if current == goal:
                if min_cnt > cnt:
                    min_cnt = cnt
                break
            current -= 20
            if current < 144000:
                current = 146000

        current = b
        for cnt in range(1, 6):
            if current == goal:
                if min_cnt > cnt:
                    min_cnt = cnt
                break
            current += 20
            if current > 146000:
                current = 144000

        current = b
        for cnt in range(1, 6):
            if current == goal:
                if min_cnt > cnt:
                    min_cnt = cnt
                break
            current -= 20
            if current < 144000:
                current = 146000

    else:
        current = b
        for cnt in range(6):
            if current == goal:
                if min_cnt > cnt:
                    min_cnt = cnt
                break
            current += 20
            if current > 146000:
                current = 144000

        current = b
        for cnt in range(6):
            if current == goal:
                if min_cnt > cnt:
                    min_cnt = cnt
                break
            current -= 20
            if current < 144000:
                current = 146000

        current = a
        for cnt in range(1, 6):
            if current == goal:
                if min_cnt > cnt:
                    min_cnt = cnt
                break
            current += 20
            if current > 146000:
                current = 144000

        current = a
        for cnt in range(1, 6):
            if current == goal:
                if min_cnt > cnt:
                    min_cnt = cnt
                break
            current -= 20
            if current < 144000:
                current = 146000

    print(min_cnt)