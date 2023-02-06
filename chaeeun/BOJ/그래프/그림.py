from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

visited = [[False]*m for _ in range(n)] ### [ceun] visited 배열을 꼭! 만들어줘야..

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(i, j):
    queue = deque([(i, j)])
    visited[i][j] = True
    cntt = 1
    while queue:
        i, j = queue.popleft() # [ceun] popleft()임!!
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and lst[nx][ny] == 1: # [ceun] lst[nx][ny] == 1 이것도 조건으로 추가하기!!
                queue.append((nx, ny))
                visited[nx][ny] = True
                cntt += 1
    return cntt

size = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and lst[i][j] == 1:
            size = max(size, bfs(i, j))
            cnt += 1
            
print(cnt)
print(size)