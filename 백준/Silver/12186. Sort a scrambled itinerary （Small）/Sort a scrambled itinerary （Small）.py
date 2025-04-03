T = int(input())
for tc in range(1, T+1):
    N = int(input())
    flight = {}
    cnt = {}
    for i in range(N):
        start = input()
        end = input()
        flight[start] = end
        if cnt.get(start):
            cnt[start] += 1
        else:
            cnt[start] = 1
        if cnt.get(end):
            cnt[end] += 1
        else:
            cnt[end] = 1

    city_list = list(cnt.items())
    city_list.sort(key=lambda x: x[1])
    edge1, edge2 = city_list[0][0], city_list[1][0]

    if flight.get(edge1):
        source = edge1
    else:
        source = edge2

    print(f"Case #{tc}:", end=" ")
    for _ in range(N):
        print(f"{source}-{flight[source]}", end=" ")
        source = flight[source]
    print("")
