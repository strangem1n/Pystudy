import sys
from collections import deque
input = sys.stdin.readline

def chk():
    cnt = 0
    for dur, is_robot in belt:
        if dur == 0:
            cnt += 1
    if cnt < limit:
        return True
    else:
        return False

def robot_move():
    for idx in range(n*2-1, -1, -1):
        current_robot = belt[idx][1]
        if current_robot == 0:
            continue

        next_dur, next_robot = belt[idx+1]
        if next_dur > 0 and next_robot == 0:
            belt[idx][1] -= 1
            belt[idx+1][1] += 1
            belt[idx+1][0] -= 1

n, limit = map(int, input().split())
belt = deque(map(lambda x: [int(x), 0] , input().split()))

level = 0
while chk():    # 각 단계별로 내구도 확인. 로봇 이동할 때마다 내리는 위치도 확인
    level += 1

    # 1. 벨트 회전
    belt.rotate(1)
    belt[n-1][1] = 0

    # 2. 로봇 스스로 이동
    robot_move()
    belt[n-1][1] = 0

    # 3. 가능하면 로봇 올리기
    if belt[0][0] > 0:
        belt[0][0] -= 1
        belt[0][1] += 1

print(level)