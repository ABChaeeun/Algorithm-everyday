from collections import deque

queue = deque([])
def bfs():
    
    d = [(-1,0),(1,0),(0,1),(0,-1)]
    while queue:
        x,y = queue.popleft()
        for dx,dy in d:
            nx, ny = x+dx, y+dy
            cnt = 1
            if (0<=nx<N) and (0<=ny<M) and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y]+1
                queue.append([nx,ny])
                

    
M, N = map(int,input().split())

tomato = [list(map(int,input().split())) for _ in range(N)]
res = []
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1 :
            queue.append([i,j])
answer = -1e9

bfs()

for i in range(N):
    for j in range(M):
        if (tomato[i][j] == 0):
            print('-1')
            exit(0)
    answer = max(answer,max(tomato[i])) 

            
print(answer - 1)