T = int(input())

for tc in range(1, T+1):
    A, B = map(int, input().split())

    if A + B >= 24:
        result = A + B - 24
    else:
        result = A + B

    print('#{} {}'.format(tc, result))
