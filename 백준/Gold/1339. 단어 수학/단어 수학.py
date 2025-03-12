n = int(input())
arr = [input() for _ in range(n)]

max_len = 0    # 가장 긴 단어의 길이 찾기
for word in arr:
    if max_len < len(word):
        max_len = len(word)

for i in range(n):    # 짧은 단어는 앞에 "0"을 추가해서 가장 긴 쪽에 맞추기
    if max_len > len(arr[i]):
        add = max_len - len(arr[i])
        arr[i] = ("0" * add) + arr[i]

char2num = {}    # 각 알파벳에 대응되는 숫자 저장할 딕셔너리

for i in range(n):    # 먼저 알파벳이 각 자리별로 몇 번 등장하는지 확인
    for j in range(max_len):
        char = arr[i][j]
        if char == "0":
            continue
        if char2num.get(char):    # 예시) 단어가 "ABC" 이면, A => 100, B => 10, C => 1로 가중치 설정
            char2num[char] += 10 ** (max_len - (j+1))
        else:
            char2num[char] = 10 ** (max_len - (j+1))

char_list = list(char2num.items())
char_list.sort(reverse=True, key=lambda x: x[1])    # 각 알파벳의 가중치가 제일 높은 순대로 정렬

num = 9
for char in char_list:    # 가중치가 높은 순대로 9부터 내림차순으로 배정
    char2num[char[0]] = str(num)    # 딕셔너리에는 숫자를 문자로 저장해서 서로 붙일 수 있게 함
    num -= 1

for i in range(n):    # 원본 단어의 각 알파벳을 숫자로 변환
    new_word = ""    # 문자 형태의 숫자를 하나씩 이어붙인다.
    for j in range(max_len):
        if arr[i][j] == "0":    # 앞에 추가한 "0"은 무시
            continue
        else:
            new_word += char2num[arr[i][j]]
    arr[i] = int(new_word)    # 정수로 변환

print(sum(arr))    # 변환한 수의 합 출력
