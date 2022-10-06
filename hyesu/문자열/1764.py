import sys
input = sys.stdin.readline

n, m = map(int, input().split())

listens = []
sees = []

for _ in range(n):
    listens.append(input())

for _ in range(m):
    sees.append(input())

ans = list(set(listens) & set(sees))
ans.sort()
print(len(ans))
print(''.join(ans), end='')