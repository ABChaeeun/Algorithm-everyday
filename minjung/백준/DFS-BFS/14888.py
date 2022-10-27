def dfs(depth,ind):
    global add, sub, mul, div, min_score, max_score
    if depth == n:
        max_score = max(max_score,ind)
        min_score = min(min_score,ind)
    else:
        if add>0:
            add-=1
            dfs(depth+1,ind+number[depth])
            add+=1
        if sub>0:
            sub-=1
            dfs(depth+1,ind-number[depth])
            sub+=1
        if mul>0:
            mul-=1
            dfs(depth+1,ind*number[depth])
            mul+=1
        if div>0:
            div-=1
            dfs(depth+1,int(ind/number[depth]))
            div+=1


n = int(input())
number = list(map(int,input().split()))
add, sub , mul, div = map(int,input().split())

min_score =1e9
max_score =-1e9

dfs(1,number[0])

print(max_score)
print(min_score)