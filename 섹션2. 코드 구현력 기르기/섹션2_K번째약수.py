import sys
num, k = map(int, sys.stdin.readline().split())

yak = []
for i in range(1, num+1):
    if num % i == 0:
        yak.append(i)

if len(yak) < k:
    print(-1)
else:
    print(yak[k-1])