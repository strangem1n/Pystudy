import sys
input = sys.stdin.readline

tc = int(input())
for t in range(tc):
    n = int(input())
    cloth = {}
    for _ in range(n):    # 옷의 종류에 따른 개수 세기
        name, cloth_type = input().split()
        if cloth.get(cloth_type):
            cloth[cloth_type] += 1
        else:
            cloth[cloth_type] = 1

    arr = list(cloth.values())
    type_num = len(arr)

    result = 1    # 전체 조합의 개수 저장할 변수
    for i in arr:    # 각 부분집합의 원소들의 곱이 가능한 조합의 개수
        result *= i+1
    print(result-1)
