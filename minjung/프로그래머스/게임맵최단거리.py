import sys
input = sys.stdin.readline
from collections import deque

def bfs(x,y,maps):
    n = len(maps)
    m = len(maps[0])
    queue = deque([[x,y]])
    visited = [[0 for _ in range(m)] for _ in range(n)] 
    visited[x][y]=1
    d = [(1,0),(-1,0),(0,1),(0,-1)]
    while queue:
        x,y = queue.popleft()
        if x == n-1 and y == m-1:
            return visited[n-1][m-1]
        for dx,dy in d:
            nx,ny = x+dx,y+dy
            if maps[x][y] == 1 and 0<=nx<n and 0<=ny<m and visited[nx][ny]== 0 :
                queue.append([nx,ny])
                visited[nx][ny] = visited[x][y]+1
    return -1

def solution(maps):
    answer = bfs(0,0,maps)
    return answer