# 백준 1012 유기농배추 실버2 그래프탐색
import sys
from collections import deque
input = sys.stdin.readline
queue = deque()

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    table = [[0] * m for _ in range(n)]
    visitied = [[False] * m for _ in range(n)]
    data = []

    for _ in range(k):
        x, y = map(int, input().split())
        table[y][x] = 1
        data.append((x, y))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for d in data:
        queue.append(d)
        while queue:
            node = queue.popleft()
            visitied[node[1]][node[0]] = True
            for i in range(4):
                x = node[0] + dx[i]
                y = node[1] + dy[i]
                if x < 0 or x >= m or y < 0 or y >= n:
                    continue
                else:
                    if (table[y][x] == 1) and (visitied[y][x] == False):
                        queue.append((x, y))
                        visitied[y][x] = True
                        table[y][x] = 0

    ans = 0
    for t in table:
        ans += sum(t)
    print(ans)