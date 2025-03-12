width, height = map(int, input().split())
cut = int(input())
width_point = [0]    # 잘려서 생길 영역의 각 지점, 첫 지점은 0
height_point = [0]
for _ in range(cut):
    chk, point = map(int, input().split())
    if chk == 0:
        height_point.append(point)
    else:
        width_point.append(point)
width_point.sort()    # 오름차순 정렬
height_point.sort()
width_point.append(width)    # 맨 마지막 지점은 원래 직사각형의 길이
height_point.append(height)

width_area = [0] * (len(width_point)-1)    # 각 영역의 가로, 세로 길이
height_area = [0] * (len(height_point)-1)
for i in range(1, len(width_point)):
    width_area[i-1] = width_point[i] - width_point[i-1]    # 오른쪽 지점에서 왼쪽 지점의 좌표를 빼서 길이 구하기
for i in range(1, len(height_point)):
    height_area[i-1] = height_point[i] - height_point[i-1]
print(max(width_area) * max(height_area))    # 잘라서 생긴 영역 중 각 길이의 최대값끼리 곱하면 최대 영역
