n = int(input())
slogan = input() + '.'
start = 0
result = 0
for i in range(n+1):
    if slogan[i] in ['.', '|', ':', '#']:
        result += int(slogan[start:i])
        start = i+1
print(result)
