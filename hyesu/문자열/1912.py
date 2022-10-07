import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

d = [0] * n # 해당 인덱스까지의 연속합 최댓값 결과 저장

d[0] = data[0]

for idx in range(1, n):
    d[idx] = max(data[idx], d[idx-1] + data[idx])

print(max(d))
