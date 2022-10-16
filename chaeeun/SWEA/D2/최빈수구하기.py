T = int(input())

for i in range(1, T+1):
    tc = int(input())

    scores = list(map(int, input().split()))
    # scores[] : 학생들 점수 배열
        # index : 학생 id
        # value : 점수
    
    counts = [0]*101
    # counts[] : 0점 ~ 100점 count
        # index : 점수
        # value : cnt

    # 각 점수가 출현할 때 마다 더해주기
    for num in scores:
        counts[num] += 1

    # 최빈수 구하기 (최빈수가 여러 개 일 때에는 가장 큰 점수로)
    m = max(counts)
    max_modes_idx = [ii for ii, vv in enumerate(counts) if vv == m]
    mode = max(max_modes_idx)

    print('#{} {}'.format(tc, mode))