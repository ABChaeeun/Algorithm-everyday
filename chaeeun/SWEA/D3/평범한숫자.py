T = int(input())

for tc in range(1, T + 1):
    num = int(input())

    lst = list(map(int, input().split()))

    
    for i in range(1, num):
        cnt = 0
        for j in range(1, i):
            if lst[j] != max(lst[j - 1], lst[j], lst[j + 1]) and lst[j] != min(lst[j - 1], lst[j], lst[j + 1]):
                cnt += 1

    print('#{} {}'.format(tc, cnt))
