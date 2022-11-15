T = 10
N = 100

for tc in range(T):
    tcc = int(input())
    
    # lst = []
    # for _ in range(100):
    #     lst.append(map(int, input().split()))
    lst = [list(map(int, input().split())) for _ in range(N)]
    
    sum_max = 0

    ### 가로합
    for i in range(N):
        sum = 0
        for j in range(N):
            sum += lst[i][j]
        if sum > sum_max:
            sum_max = sum

    ### 세로합
    for i in range(N):
        sum = 0
        for j in range(N):
            sum += lst[j][i]
        if sum > sum_max:                
            sum_max = sum

    ### 대각선합 (우하향)
    sum = 0
    for i in range(N):
        sum += lst[i][i]
    if sum > sum_max:
        sum_max = sum

    ### 대각선합 (좌하향)
    sum = 0
    for i in range(N):
        sum += lst[i][N-1-i] ### N-1 로 해줘야함!!!!!!!
    if sum > sum_max:
        sum_max = sum
                
    print('#{} {}'.format(tcc, sum_max))
