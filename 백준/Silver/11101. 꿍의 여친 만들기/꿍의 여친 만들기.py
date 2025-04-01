T = int(input())
for _ in range(T):
    raw = input().split(",")
    weight = {}
    for w in raw:
        word, cost = w.split(":")
        weight[word] = int(cost)

    raw_set = input().split("|")
    min_cost = 20000
    for s in raw_set:
        current_cost = 0
        current_set = s.split("&")
        for element in current_set:
            if current_cost < weight[element]:
                current_cost = weight[element]
        if min_cost > current_cost:
            min_cost = current_cost
            
    print(min_cost)
