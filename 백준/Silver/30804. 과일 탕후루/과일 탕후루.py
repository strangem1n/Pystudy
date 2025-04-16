n = int(input())
arr = list(map(int, input().split()))

fruit = {}
left = right = 0
max_sum = 0
while right < n:
    if fruit.get(arr[right]):
        fruit[arr[right]] += 1
    elif len(fruit) < 2:
        fruit[arr[right]] = 1
    else:
        left = right - 1
        left_kind = arr[left]
        left_cnt = 0
        while arr[left] == left_kind and left > -1:
            left_cnt += 1
            left -= 1
        left += 1
        sub_sum = sum(fruit.values())
        max_sum = max(max_sum, sub_sum)
        fruit = {arr[left]: left_cnt, arr[right]: 1}
    right += 1
sub_sum = sum(fruit.values())
max_sum = max(max_sum, sub_sum)

print(max_sum)
