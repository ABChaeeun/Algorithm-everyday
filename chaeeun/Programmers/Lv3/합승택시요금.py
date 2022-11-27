INF = 40000000

### floyd-warshall 알고리즘
def floyd(dist, n):
    for k in range(n): # k : 거쳐가는 노드
        for i in range(n): # i : 출발 노드
            for j in range(n): # j : 도착 노드
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j] # dist[] : 모든 출발점과 도착점의 최소비용

def solution(n, s, a, b, fares):

    dist = [[INF for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0 # 자기자신으로 가는 값은 0

    for node1, node2, fee in fares:
        dist[node1-1][node2-1] = fee
        dist[node2-1][node1-1] = fee

    floyd(dist, n)

    s, a, b = s-1, a-1, b-1 # 인덱스가 0부터 시작하는걸로 맞춰주기 위해서
    answer = INF
    for k in range(n):
        answer = min(answer, dist[s][k] + dist[k][a] + dist[k][b])

    return answer
