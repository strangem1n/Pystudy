n, m = map(int, input().split())
arr = list(map(int, input().split()))
positive = negative = 0
pos_arr = []
neg_arr = []
for i in range(n):
    if arr[i] < 0:
        negative += 1
        neg_arr.append(-arr[i])    # 음수 방향 책의 절댓값을 미리 취하기
    elif arr[i] > 0:
        positive += 1
        pos_arr.append(arr[i])
pos_arr.sort()    # 양수, 음수 방향 각각 0에서부터의 거리를 오름차순으로 정렬
neg_arr.sort()

result = 0    # 걸음 수

# 가장 먼 지점은 왕복하지 않고 편도로 가서 끝낼 것이라, 초기값에서 가장 먼 좌표만큼 미리 뺀다.
if positive == 0 or (negative > 0 and neg_arr[-1] > pos_arr[-1]):
    result -= neg_arr[-1]
elif negative == 0 or (positive > 0 and neg_arr[-1] <= pos_arr[-1]):
    result -= pos_arr[-1]

# 거꾸로 접근해서, 0에서부터 절댓값이 가장 먼 지점부터 방문해서 책이 다 없어질 때까지 방문한다.
while positive > 0 or negative > 0:
    if positive == 0 or (negative > 0 and neg_arr[-1] > pos_arr[-1]):    # 양수 방향에 책이 없거나, 음수 방향에 더 먼 책이 있으면
        result += neg_arr[-1] * 2    # 0에서 그 지점까지 갔다가 다시 0으로 되돌아옴
        if negative >= m:    # 들고갈 수 있는 책의 개수에 따라서 그 다음으로 먼 지점들의 책까지 함께 놔두고 온다.
            negative -= m
            for _ in range(m):
                neg_arr.pop()
        else:    # 음수 방향으로 책이 m개 미만으로 남았으면, 이번 방문으로 더 이상 음수 방향 탐색은 하지 않는다.
            negative = 0
    elif negative == 0 or (positive > 0 and neg_arr[-1] <= pos_arr[-1]):    # 음수 방향에 책이 없거나, 음수 방향에 더 먼 책이 있으면
        result += pos_arr[-1] * 2    # 0에서 그 지점까지 갔다가 다시 0으로 되돌아옴
        if positive >= m:
            positive -= m
            for _ in range(m):
                pos_arr.pop()
        else:    # 양수 방향으로 책이 m개 미만으로 남았으면, 이번 방문으로 더 이상 음수 방향 탐색은 하지 않는다.
            positive = 0

print(result)
