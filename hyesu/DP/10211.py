import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    data = list(map(int, input().split()))
    d = [0] * n

    for i in range(n):
        d[i] = max(d[i-1] + data[i], data[i])
    print(max(d))