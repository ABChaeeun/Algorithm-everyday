from collections import deque
import sys

input = sys.stdin.readline

def biteFish(x,y,sharksize):
    distance = [[0]*n for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    temp = []

    q = deque([[x,y]])
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        for dx,dy in d:
            nx,ny = x+dx,y+dy
            if 0<=nx <n and 0<= ny<n and visited[nx][ny]==0 :
                if graph[nx][ny] <= sharksize:
                    q.append([nx,ny])
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[x][y]+1
                    if graph[nx][ny] <sharksize and graph[nx][ny] != 0:
                        temp.append((nx,ny,distance[nx][ny]))
    return sorted(temp,key=lambda x:(-x[2],-x[0],-x[1]))

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

d = [(1,0),(-1,0),(0,1),(0,-1)]
x, y  = 0,0
sharksize = 2

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x = i
            y = j

cnt = 0
result = 0
while True :
    shark = biteFish(x,y,sharksize)
    if len(shark) == 0:
        break
    nx,ny,dist = shark.pop()
    result += dist
    graph[x][y], graph[nx][ny] = 0,0

    x,y = nx,ny
    cnt+=1
    if cnt == sharksize:
        sharksize+=1
        cnt=0
print(result)