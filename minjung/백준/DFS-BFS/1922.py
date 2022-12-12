import sys
input = sys.stdin.readline

#크루스칼 알고리즘
# 비용을 오름차순으로 정렬하고 사이클이 발생하면 추가하지 않고 사이클이 발생하지 않으면 추가한다.
# 특정 원소가 속한 집합을 찾기

# 루트 노드를 찾을때까지 재귀
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent, b)

    if a<b:
        parent[b] = a
    else :
        parent[a] = b

n = int(input())
m = int(input())

# 부모 테이블 초기화
parent = [0] *(n+1)

# 자기 자신의 부모를 자기로 초기화
for i in range(1,n+1):
    parent[i] = i

edges = []
result = 0

for _ in range(m):
    a,b,c = map(int,input().split())
    edges.append((a,b,c))

edges = sorted(edges,key = lambda x:x[2])

# 간선을 하나씩 확인하여 사이클이 발생하지 않는 경우에만 집합에 포함
for e in edges:
    a,b,c = e
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += c

print(result)