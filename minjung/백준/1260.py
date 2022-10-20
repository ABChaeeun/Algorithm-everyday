from collections import deque


def bfs(start):
    discoverd = [start]
    queue = deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        print(node,end=' ')
        for i in range(len(visited[start])) :
            if visited[node][i] == 1 and (i  not in discoverd):
                discoverd.append(i)
                queue.append(i)

def dfs(start,discoverd_=[]):
    discoverd_.append(start)
    print(start,end=' ')
    for i in range(len(visited[start])):
        if visited[start][i] == 1 and (i not in discoverd_):
            dfs(i,discoverd_)
n, m, v = map(int,input().split())

visited = [[0] *(n+1) for _ in range(n+1)]

for _ in range(m):
    i, j = map(int,input().split())
    visited[i][j] = 1
    visited[j][i] = 1



dfs(v)
print()
bfs(v)