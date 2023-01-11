# 참고
# 백준 - PyPy3로만 통과

import sys
sys.setrecursionlimit(1000)
input = sys.stdin.readline

R, C = map(int, input().split())
lst = [list(map(lambda x: ord(x) - 65, input()))
       for _ in range(R)]  ### 알파벳을 다 숫자로 바꿔서 리스트로 넣어주기
visited = [0] * 26  ### 알파벳으로 방문 체크

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(i, j, cnt):
    global max
    if max < cnt:
        max = cnt

    visited[lst[i][j]] = 1
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]

        if 0 <= nx < R and 0 <= ny < C and visited[lst[nx][ny]] == 0:
            # print('[',nx,']','[',ny,']', lst[nx][ny])
            visited[lst[nx][ny]] = 1
            dfs(nx, ny, cnt + 1)
            visited[lst[nx][ny]] = 0  ### <중요> 이거 추가!!!!!


max = 1
dfs(0, 0, max)
print(max)
