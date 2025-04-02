n = int(input())
binary = ''
while n > 0:
    binary = str(n % 2) + binary
    n //= 2

b = 1
result = 0
for i in range(len(binary)):
    if binary[i] == "1":
        result += b
    b *= 2
print(result)
