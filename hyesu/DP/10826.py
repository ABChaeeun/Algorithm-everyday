import sys
input = sys.stdin.readline

n = int(input())
d = [0] * (n+1)

for i in range(n):
    if i <= 1:
        d[i] = 1
    else:
        d[i] = d[i-1] + d[i-2]

print(d[n-1])