# 로봇 청소기
# BFS

import sys
from collections import deque

input = sys.stdin.readline
d = [[-1,0],[0,1],[1,0],[0,-1]]

def bfs(x,y,direction):
    visited[x][y] = 1
    result = 1
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x,y = queue.popleft()
        flag = 0    
        for _ in range(4):
            nx = x + d[(direction+3)%4][0] #왼쪽부터 탐색
            ny = y + d[(direction+3)%4][1]

            direction = (direction+3)%4 #현재 방향 초기화

            if 0 <= nx <n and 0<=ny <m and robot[nx][ny] == 0:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    result += 1
                    queue.append((nx,ny))
                    flag = 1    #하나라도 청소하면 flag값을 변경시켜줌
                    break
        if flag == 0 :
            if robot[x-d[direction][0]][y-d[direction][1]] == 1:    # 후진 시 벽이면 결과값 출력 
                print(result)
                break
            else:
                queue.append((x-d[direction][0],y-d[direction][1])) # 벽이 없으면 후진 후 후진한 위치에서 다시 출발
                           


n,m = map(int,input().split())

start,end,direction = map(int,input().split())
robot = []
visited= [[0]*m for _ in range(n)]

for _ in range(n):
    robot.append(list(map(int,input().split())))


bfs(start,end,direction)