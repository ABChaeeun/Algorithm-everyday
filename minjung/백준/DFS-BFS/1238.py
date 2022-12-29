# 파티
# 다익스트라
# 그래프에서 한 정점에서 다른 정점까지 최단 경로를 구하는 알고리즘 
import sys
import heapq
input = sys.stdin.readline

n, m, x = map(int,input().split())

INF = int(1e9)

party = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int,input().split())
    party[start].append((end,cost))

def dijkstra(start):
    distance = [INF] *(n+1)
    distance[start]= 0

    q = [] # 최단거리 테이블을 힙으로 구현 
    heapq.heappush(q,(0,start)) # 힙에 (가중치, 노드 ) 형식으로 삽입
    while q:
        dist,now = heapq.heappop(q) # 최소 힙이므로 가중치가 가장 작은 값이 pop
        if distance[now] >= dist:   # 이미 최솟값을 구했는지 확인 
            for v,val in party[now]:    # 연결된 노드들 확인
                if dist + val <distance[v]: # 가중치가 더 작은 값이면 갱신
                    distance[v] = dist + val
                    heapq.heappush(q,(dist+val,v))

    return distance

answer = dijkstra(x)
answer[0] = 0

for i in range(1,n+1):
    if i != x:
        res = dijkstra(i)
        answer[i] += res[x]

print(max(answer))

