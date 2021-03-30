N, M = list(map(int,input().split()))

SUM = []

for i in range(1, N+1):
    for j in range(1, M+1):
        SUM.append(i+j)
SUM.sort()

number = [1 for _ in range(len(SUM))]

for i in range(len(number)-1):
    if SUM[i+1] == SUM[i]:
        number[i+1] = number[i] + 1

MAX = []
for i in range(len(number)):
    if number[i] == max(number):
        MAX.append(SUM[i])

for i in MAX:
    print(i, end = ' ')