start, end = map(int, input().split())
min_button = abs(start-end)
n = int(input())
for _ in range(n):
    favorite = int(input())
    button = abs(favorite-end)+1
    if min_button > button:
        min_button = button
print(min_button)
