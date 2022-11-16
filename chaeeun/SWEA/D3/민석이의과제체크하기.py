T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split()) # 수강생, 제출한 사람수
    lst = list(map(int, input().split()))
    # print(*lst)

    print('#{} '.format(tc), end='')
    for i in range(1, N+1):
        if i not in lst:
            print('{} '.format(i), end='')
    print()
    