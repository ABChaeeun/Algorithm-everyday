T = int(input())

for tc in range(1, T+1):
    D, H, M = map(int, input().split())
    day = (D - 11) * 24 * 60
    hour = (H - 11) * 60
    minute = (M - 11)
    mm = day + hour + minute
    if mm >= 0:
        print('#{} {}'.format(tc, mm))
    else:
        print('#{} {}'.format(tc, -1))
