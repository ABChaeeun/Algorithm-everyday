N, K = map(int, input().split())

lst = []
for i in range(N):
    lst.append(int(input()))
lst.sort(reverse = True)

cnt = 0
for dong in lst:
    
    if K == 0:
        break
        
    if K % dong != K:
        cnt += K // dong
        K = K % dong
        
print(cnt)