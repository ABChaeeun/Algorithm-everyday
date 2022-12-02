import sys
from collections import deque
input = sys.stdin.readline
bus = [[] for _ in range(1001)]

def bfs(start):
    queue = deque([[start,0]])
    visited[start] = 0
    while queue:
        start, cost= queue.popleft()

        if (cost>visited[start]):
            continue        
      
        for i in range(len(bus[start])):
            next = bus[start][i][0]
            next_cost = bus[start][i][1]+ visited[start]
            # print('nextcost',next_cost)
            if next_cost<visited[next]:
                visited[next] = next_cost
                queue.append([next,next_cost])

            

n = int(input())
m = int(input())
visited = [1e9]*(n+1)

for _ in range(m):
    start, end, fee = map(int,input().split())
    bus[start].append([end,fee])

get_start , get_end = map(int,input().split())

bfs(get_start)
print(visited[get_end])
# print(visited)

