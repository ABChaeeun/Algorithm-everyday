#플로이드
#n 개의 도시, 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스 , 비용 존재
# 모든 도시의 쌍에 대해 A에서 B로 가는데 필요한 비용의 최솟값 

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)
bus_cost = [[INF for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
     a, b, c = map(int,input().split())
     bus_cost[a][b] = min(c,bus_cost[a][b])
    
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i!=j:
                bus_cost[i][j] = min(bus_cost[i][j],bus_cost[i][k]+bus_cost[k][j])


for row in bus_cost[1:]:
    for col in row[1:]:
        if col == INF:
            print(0,end = " ")
        else:
            print(col,end = " ")
    print()

