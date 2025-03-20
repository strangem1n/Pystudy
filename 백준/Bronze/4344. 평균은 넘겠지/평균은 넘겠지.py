tc = int(input())
for _ in range(tc):
    num, *point = map(int, input().split())
    average = sum(point) / num
    over_average = 0
    for student in point:
        if student > average:
            over_average += 1
    result = over_average / num * 100
    print(f"{result:.3f}%")
