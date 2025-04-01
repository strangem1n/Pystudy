n = int(input())
for _ in range(n):
    binary = input()
    result = 0
    for i in range(23, -1, -1):
        if binary[i] == "1":
            result += 2 ** (23-i)
    print(result)
