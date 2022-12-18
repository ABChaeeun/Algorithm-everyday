# 최소 스패닝 트리
# 주어진 그래프의 모든 정점을 연결하는 부분 그래프중 가중치의 합이 최소인 그래프

import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else :
        parent[a] = b

v,e = map(int,input().split())

parent =  [i for i in range(v+1)]
edges = []
result = 0
for _ in range(e):
    a,b,c = map(int,input().split())
    edges.append((a,b,c))

edges = sorted(edges,key=lambda x:x[2])

for e in edges :
    a,b,c = e
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += c
print(result)
        