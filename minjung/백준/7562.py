
from collections import deque
import sys
input  =sys.stdin.readline

dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,-2,-1,1,2]

def bfs(x,y):
    visited[x][y]=1
    q= deque()
    q.append([x,y])
    while q:
        cur_x,cur_y = q.popleft()
        if cur_x == newn and cur_y == newm:
            return visited[newn][newm]-1
        for i in range(8):
            ny ,nx = cur_y+dy[i],cur_x+dx[i]         
            if 0 <= ny < size and 0 <= nx < size and visited[nx][ny]==0:
                visited[nx][ny] == visited[cur_x][cur_y]+1
                q.append((nx,ny))


test = int(input())
for i in range(test):
    size = int(input())
    x,y = map(int,input().split())
    newn,newm = map(int,input().split())
    visited = [[0 for _ in range(size)] for _ in range(size)]
    print(bfs(x,y))



