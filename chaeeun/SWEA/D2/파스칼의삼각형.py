T = int(input())

for tc in range(1, T+1):

    ### input ###
    num = int(input())

    # 2차원 배열 초기화
    lst = [[0]*num for i in range(num)]

    # 파스칼의 삼각형 만들기
    for i in range(num):
        for j in range(0,i+1):
            if i == j or j == 0:
                lst[i][j] = 1
            else:
                lst[i][j] = lst[i-1][j-1] + lst[i-1][j]

    ### output ###
    print('#{}'.format(tc))
    for i in range(len(lst)):
        for j in range(0,i+1):
            print(lst[i][j], end=' ')
        print()