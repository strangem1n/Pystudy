n = int(input())
people = list(map(int, input().split()))
people.sort()
timesum = 0
for count, time in enumerate(people):
    timesum += time * (len(people) - count)
print(timesum)