from collections import deque

N, M, V = map(int, input().split())

visited = [0] * (N + 1)
lst = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    i, j = map(int, input().split())
    lst[i][j] = 1
    lst[j][i] = 1

# for i in range(N+1):
#     print(*lst[i])

def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    for i in range(1, N + 1):
        if (visited[i] == 0
                and lst[v][i] == 1):  ### [ceun] visited[v]가 아니라 visited[i] !!
            dfs(i)


def bfs(v):
    visited[v] = 1
    queue = deque()
    queue.append(v)
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, N + 1):
            if (visited[i] == 0 and lst[v][i] == 1):
                visited[i] = 1
                queue.append(i)  ### [ceun] 추가해주기!!


dfs(V)
print()
visited = [0] * (N + 1)
bfs(V)
