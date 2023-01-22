# 참고

import sys
input = sys.stdin.readline

def adjacent(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i: # 열 or 대각선이 같은 경우
            return False
    return True

def backtracking(x):
    global result

    if x == N:
        result += 1
    else:
        for i in range(N):
            row[x] = i
            if adjacent(x): # 열 or 대각선이 다른 경우 (잘 놓여져 있는 경우) 백트래킹 안하기
                backtracking(x+1)
    
N = int(input())
row = [0] * N
result = 0
backtracking(0)
print(result)
