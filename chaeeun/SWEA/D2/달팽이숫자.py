T = int(input())

for test_num in range(1, T + 1):
    N_snail = int(input())  # 달팽이 크기(N_snail) 입력받기
    snail = [[0] * N_snail for _ in range(N_snail)]  # 2차원 배열(snail) 초기화

    # 방향 (순서: 우 하 좌 상)
    d_row = [0, 1, 0, -1]
    d_col = [1, 0, -1, 0]

    num = 1  # 달팽이 숫자에 들어갈 수
    row, col = 0, -1  # 인덱스 위한 초기화
    d_index = 0  # 방향 위한

    while num <= N_snail * N_snail:

        # 인덱스 갱신
        i = row + d_row[d_index]
        j = col + d_col[d_index]

        # snail 안의 범위인 경우
        if 0 <= i < N_snail and 0 <= j < N_snail and snail[i][j] == 0:

            # 달팽이 숫자 넣기
            snail[i][j] = num
            num += 1

            # 실제 현재의 인덱스로 바꿔주기
            row = i
            col = j

        # 방향 바꿔야하는 경우
        else:
            # 방향 전환 알려주기
            d_index = (d_index + 1) % 4

    print('#%d' % (test_num))
    for index in range(N_snail):
        print(*snail[index])
