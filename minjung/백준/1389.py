from collections import deque
from os import link
import queue
import sys
input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    visited[v] = 1
    while queue:
        target = queue.popleft()

        for i in linked[target]:
            if not visited[i]:
                visited[i] = visited[target]+1
                queue.append(i)

            

n , m = map(int,input().split())

linked = [[] for _ in range(n+1)]

for _ in range(m):
    i , j = map(int,input().split())
    linked[i].append(j)
    linked[j].append(i)

res = []

for i in range(1,n+1):
    visited = [0] * (n+1)
    bfs(i)
    res.append(sum(visited))

print(res.index(min(res))+1)


