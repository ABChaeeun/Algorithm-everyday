import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    queue = deque()
    queue.append(N)
    while queue:
        x = queue.popleft()
        if x == K:
            return dist[x]
        for nx in (x-1,x+1,2*x):
            if 0<=nx<=MAX and not dist[nx]:
                dist[nx] = dist[x]+1
                queue.append(nx)


MAX = 100000
N, K = map(int,input().split())
dist = [0]*(MAX+1)


print(bfs())