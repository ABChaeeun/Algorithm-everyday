import sys
n, k = map(int, sys.stdin.readline().split())
a = []
cnt = 0

for i in range(n):
    a.append(int(input()))

for j in range(n-1, -1, -1):
    if k ==0:
        break
    if a[j] > k:
        continue
    cnt += (k // a[j])
    k %= j
print(cnt)

