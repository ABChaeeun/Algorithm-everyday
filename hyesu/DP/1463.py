import sys

input = sys.stdin.readline

n = int(input())
d = [0] * (n+1)

# d[n] => n을 만들기 위한 연산의 최솟값 


for i in range(1, n+1):
    r = []
    if i % 3 == 0:
        r.append(d[i//3] + 1)
    if i % 2 == 0:
        r.append(d[i//2] + 1)
    r.append(d[i-1] + 1)

    d[i] = min(r)

print(d[n]-1)