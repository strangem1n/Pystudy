import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)


def find_set(x):    # 내가 속한 집합의 루트 찾기
    if rep[x] == x:    # 자기 자신을 가리키면 그곳이 루트
        return x
    else:
        rep[x] = find_set(rep[x])    # 경로 압축
        return rep[x]


def union(x, y):    # 두 집합을 합침
    rep[find_set(y)] = find_set(x)


while True:
    m, n = map(int, input().split())
    if m == n == 0:    # 입력 종료
        break

    rep = [i for i in range(m)]    # 어떤 원소의 부모 노드를 가리키는 리스트
    edges = [list(map(int, input().split())) for _ in range(n)]
    edges.sort(key=lambda x: x[2])    # 크루스칼 알고리즘 위해 길의 거리 오름차순 정렬

    cnt = 0    # MST의 간선 개수
    saving_cost = 0    # 불필요한 도로를 없애서 절약할 수 있는 비용
    all_connected = False

    for i in range(n):
        if cnt == m-1:    # MST의 간선 개수는 (전체 노드-1) 이므로 충족하면 더 이상 연결하지 않음
            all_connected = True
        house1, house2, road = edges[i]
        if not all_connected and find_set(house1) != find_set(house2):    # 서로 다른 집합일 때 연결
            union(house1, house2)
            cnt += 1
        else:    # 불필요한 도로는 제거
            saving_cost += road

    print(saving_cost)
