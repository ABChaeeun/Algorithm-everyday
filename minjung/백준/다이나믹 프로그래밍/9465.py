import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    graph = []

    n = int(input())
    for _ in range(2):
        graph.append(list(map(int,input().split())))

    if n == 1:
        print(max(graph[0][0],graph[1][0]))
        continue

    graph[0][1] += graph[1][0]
    graph[1][1] += graph[0][0]

    for k in range(2,n):
        graph[0][k] += max(graph[1][k-1],graph[1][k-2])
        graph[1][k] += max(graph[0][k-1],graph[0][k-2])

    print(max(graph[0][n-1],graph[1][n-1]))       
