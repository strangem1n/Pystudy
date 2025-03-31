N = int(input())

pattern = input()
left = right = ''
idx = 0
while pattern[idx] != '*':
    left += pattern[idx]
    idx += 1
left_length = idx

idx = -1
while pattern[idx] != '*':
    right = pattern[idx] + right
    idx -= 1
right_length = idx + 1

for _ in range(N):
    name = input()
    if len(name) >= (left_length-right_length) and left == name[:left_length] and right == name[right_length:]:
        print("DA")
    else:
        print("NE")
