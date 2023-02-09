# 참고

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())

Tree = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    # Tree[a] = b 이거 아님!!
    Tree[a].append(b)
    Tree[b].append(a)

def dfs(start, tree, parents):
    for i in tree[start]:
        if parents[i] == 0:
            parents[i] = start
            dfs(i, tree, parents)


Parents = [0 for _ in range(n+1)]
dfs(1, Tree, Parents)

for i in range(2, n+1):
    print(Parents[i])