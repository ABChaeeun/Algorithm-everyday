# 참고

import sys
input = sys.stdin.readline

N, S = map(int, input().split())
lst = list(map(int, input().split()))

answer = 0
def backtracking(index, sum):
    global answer

    if index >= N:
        return

    sum += lst[index]
    if sum == S:
        answer += 1

    backtracking(index+1, sum-lst[index])
    backtracking(index+1, sum)

backtracking(0,0)
print(answer)