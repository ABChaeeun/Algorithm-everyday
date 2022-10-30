import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

data = list(set(data))
data.sort()

for d in data:
    print(d, end=' ')
print()