import sys
input = sys.stdin.readline

n = int(input())
jump = list(map(int, input().split()))

d = [10000] * n
d[0] = 0

for i in range(n):
    maxIdx = i + jump[i]
    if maxIdx >= n:
        maxIdx = n-1
    for j in range(i, maxIdx+1):
        d[j] = min(d[j], d[i] + 1)

if d[n-1] != 10000:
    print(d[n-1])
else:
    print(-1)