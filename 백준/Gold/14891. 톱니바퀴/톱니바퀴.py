import sys
from collections import deque
input = sys.stdin.readline

def chk(k, s):
    current = k - 1
    left = current - 1
    is_spin = [0] * 4
    is_spin[current] = s

    while left > -1:
        if gear[current][6] + gear[left][2] == 1:
            is_spin[left] = is_spin[current] * (-1)
            current -= 1
            left -= 1
        else:
            break

    current = k - 1
    right = current + 1
    while right < 4:
        if gear[current][2] + gear[right][6] == 1:
            is_spin[right] = is_spin[current] * (-1)
            current += 1
            right += 1
        else:
            break

    for i in range(4):
        change(i, is_spin[i])

def change(k, s):
    selected_gear = gear[k]
    if s == 1:
        selected_gear.appendleft(selected_gear.pop())
    elif s == -1:
        selected_gear.append(selected_gear.popleft())

def score():
    point = 0
    for i in range(4):
        if gear[i][0] == 1:
            point += 2 ** i
    return point

gear1 = deque(map(int, input().rstrip()))
gear2 = deque(map(int, input().rstrip()))
gear3 = deque(map(int, input().rstrip()))
gear4 = deque(map(int, input().rstrip()))
gear = [gear1, gear2, gear3, gear4]

n = int(input())
for _ in range(n):
    start, spin = map(int, input().split())
    chk(start, spin)
print(score())
