import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

d = [1] * n  # d[i] i일때 자신을 포함해서 만들 수 있는 부분 수열의 최대 크기

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            d[i] = max(d[i], d[j] + 1)

print(max(d))