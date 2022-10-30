from collections import deque
import sys
input = sys.stdin.readline

queue = deque([])

def bfs():
    d = [(0,0,1),(0,0,-1),(-1,0,0),(1,0,0),(0,1,0),(0,-1,0)]
    while queue:
        x,y,z = queue.popleft()
        for dx,dy,dz in d:
            nx, ny, nz = x+dx, y+dy, z+dz
            cnt = 1
            if (0<=nx<H) and (0<=ny<N) and (0<=nz<M) and tomato[nx][ny][nz] == 0:
                tomato[nx][ny][nz] = tomato[x][y][z]+1
                queue.append([nx,ny,nz])
M, N, H = map(int,input().split())
tomato = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)] 
res = []
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k]==1:
                queue.append([i,j,k])

answer = -1e9

bfs()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 0:
                print('-1')
                exit(0)
        answer = max(answer,max(tomato[i][j]))

print(answer - 1)