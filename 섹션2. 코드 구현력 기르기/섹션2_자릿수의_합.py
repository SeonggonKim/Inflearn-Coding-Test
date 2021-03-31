n = int(input())
num = list(map(int, input().split()))
number = [[] for _ in range(n)]

for i in range(n):
    number[i] = list(str(num[i]))

result = [0 for _ in range(n)]

for i in range(n):
    for j in range(len(number[i])):
        result[i] += int(number[i][j])

for i in range(n):
    if result[i] == max(result):
        print(num[i])
        break