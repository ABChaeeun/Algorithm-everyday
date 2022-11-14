import sys
input = sys.stdin.readline

n = int(input())
data = []

for _ in range(n):
    a, b = map(int, input().split())
    data.append((a, b))

data.sort(key=lambda x: (x[1], x[0]))

for a, b in data:
    print(a, b)