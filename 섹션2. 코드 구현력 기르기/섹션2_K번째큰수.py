import sys

N, K = map(int, sys.stdin.readline().split())
cards = list(list(map(int, sys.stdin.readline().split())))
cards.sort(reverse = True)

sum = []
for i in range(len(cards)-2):
    for j in range(i+1, len(cards)-1):
        for k in range(j+1, len(cards)):
            sum.append(cards[i] + cards[j] + cards[k])

answer = list(set(sum))
answer.sort(reverse = True)

print(answer[K-1])