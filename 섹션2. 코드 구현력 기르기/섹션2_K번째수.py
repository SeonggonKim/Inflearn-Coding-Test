import sys
n = int(sys.stdin.readline())

OUT = []
IN = []

for i in range(n):
    OUT.append(list(map(int, sys.stdin.readline().split())))
    IN.append(list(map(int, sys.stdin.readline().split())))

cut = []
for i in range(len(OUT)):
    cut.append(IN[i][OUT[i][1]-1:OUT[i][2]])
    cut[i].sort()
    print('#{} {}'.format(i+1, cut[i][OUT[i][3]-1]))