import sys
input = sys.stdin.readline


def work(idx, block):
    t = 0

    for k in range(len(cnt)-1, idx, -1):    # 특정 높이보다 높은 땅: 블럭 제거
        current_blocks = cnt[k]
        t += current_blocks * 2 * (k-idx)    # 걸리는 시간: 2초 * (높이 차이)
        block += current_blocks * (k-idx)    # 인벤토리에 들어온 블럭 더하기

    for k in range(0, idx):    # 특정 높이보다 낮은 땅: 블럭 설치
        current_blocks = cnt[k]
        t += current_blocks * (idx-k)    # 걸리는 시간: 1초 * (높이 차이)
        block -= current_blocks * (idx-k)    # 인벤토리에서 블럭 사용하기
        if block < 0:    # 인벤토리가 음수가 될 수는 없으므로 불가능한 값 리턴
            return float('inf')

    return t    # 특정 높이로 평탄화를 마쳤을 때 걸린 시간 리턴


n, m, b = map(int, input().split())
a = ''
for _ in range(n):
    a += input()
arr = list(map(int, a.split()))    # 땅의 높이를 1차원 배열로 만들기 (좌표가 중요하지 않으므로)

max_h = max(arr)
min_h = min(arr)

cnt = [0] * ((max_h-min_h)+1)    # (최소 높이 ~ 최대 높이) 길이만큼의 리스트 생성
for num in arr:
    cnt[num-min_h] += 1    # 각 높이마다 땅이 몇 칸 존재하는지 세기


min_time = float('inf')
result_height = -1
for i in range(len(cnt)):    # 최소 높이 ~ 최대 높이 범위 내에서 특정 높이로 평탄화
    work_time = work(i, b)    # 그 때 걸리는 시간을 전부 구해본다.
    if min_time >= work_time:    # 최솟값 갱신 (단 걸리는 시간이 최솟값과 같을 경우 땅의 높이는 더 높은 값으로)
        min_time = work_time
        result_height = i+min_h    # 그 때의 땅의 높이

print(min_time, result_height)
