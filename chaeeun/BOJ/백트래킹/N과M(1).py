# 참고

import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
result = []
visited = [False] * (N+1)

def backtracking(lv):
    if lv == M:
        print(' '.join(map(str, result)))
        return

    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            backtracking(lv + 1)
            visited[i] = False
            result.pop()


backtracking(0)