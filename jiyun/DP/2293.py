import sys
n, k = map(int, sys.stdin.readline().split())
coin = []

arr = [0 for _ in range(k+1)]
arr[0] = 1
for i in range(n):
    coin.append(int(sys.stdin.readline()))


for i in coin:
    for j in range(i, k+1):
        arr[j] += arr[j-i]

print(arr[k])