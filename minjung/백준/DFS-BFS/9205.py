# 맥주 마시면서 걸어가기
# BFS/DFS

import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append([home[0],home[1]])

    while queue:
        x,y = queue.popleft()
        if abs(x-festi[0])+abs(y-festi[1]) <=1000:  #페스티벌 까지의 거리가 1000 이하면 성공
            return print("happy")
        for i in range(convi_num):
            if not visited[i]:
                nx,ny = convi[i]
                if abs(x-nx)+abs(y-ny) <=1000:      # 새로운 좌표 값을 받았을 때 거기까지의 거리가 1000 이하면 그 지점까지는 갈 수 있음
                    queue.append([nx,ny])
                    visited[i] = 1
    return print("sad")
    


t = int(input())


for _ in range(t):
    convi = []
    convi_num = int(input())
    home = list(map(int,input().split()))
    for _ in range(convi_num):
        x,y = map(int,input().split())
        convi.append([x,y])
    festi = list(map(int,input().split()))
    visited = [0]*(convi_num+1)
    bfs()