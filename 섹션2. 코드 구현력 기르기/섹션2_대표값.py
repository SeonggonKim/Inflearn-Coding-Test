import sys
input = sys.stdin.readline

n = int(input())
number = list(map(int, input().split()))
average = int(round(sum(number) / len(number), 0))
min = 2147000000

for i, j in enumerate(number):
    tmp = abs(j-average)
    if tmp < min:
        min = tmp
        score = j
        res = i + 1
    elif tmp == min:
        if j > score:
            score = j
            res = i + 1

print(average, res)