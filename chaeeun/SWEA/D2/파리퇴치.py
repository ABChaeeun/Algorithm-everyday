T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    lst = []
    for i in range(N):
        lst.append(list(map(int, input().split())))
    
    sums = []
    for a in range(N - M + 1):
        for b in range(N - M + 1):
            sum = 0
            for i in range(M):
                for j in range(M):
                    sum += lst[a+i][b+j]
            sums.append(sum)

    print('#{} {}'.format(tc, max(sums)))