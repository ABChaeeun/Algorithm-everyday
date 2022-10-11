import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

d = [1] * n # d[i]: i까지 왔을때 부분수열의 최대 길이 저장

# 현재 수 a[i]가 이전거 보다 크면 부분수열 가능
# d에계속 max값을 저장해 나간다.

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            d[i] = max(d[i], d[j]+1) 

# 그리고 dp중 가장 큰 값을 출력한다. 
print(max(d))